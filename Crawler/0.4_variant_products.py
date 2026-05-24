import asyncio
import random
import re
from collections import defaultdict

from playwright.async_api import async_playwright
from openpyxl import Workbook
from bs4 import BeautifulSoup


# ================== CONFIG ==================
COLLECTION_URL = "https://www.oldsailor.com.vn/collections/all"
BASE_URL = "https://www.oldsailor.com.vn"
CONCURRENT = 5
OUTPUT_FILE = "oldsailor_products.xlsx"

UA_REAL = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

# ================== UTILS ==================
def normalize_price(price):
    if not price:
        return None
    
    if isinstance(price, int):
        return price  # đã chuẩn rồi, không xử lý nữa
    
    digits = re.sub(r"\D", "", price)
    return int(digits) if digits else None

async def human_delay(a=1.2, b=2.8):
    await asyncio.sleep(random.uniform(a, b))

# ================== SCROLL COLLECTION ==================
async def scroll_to_end(page):
    prev_height = 0
    while True:
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await page.wait_for_timeout(2000)
        height = await page.evaluate("document.body.scrollHeight")
        if height == prev_height:
            break
        prev_height = height

async def get_product_links(page):
    await page.goto(COLLECTION_URL)
    await page.wait_for_timeout(3000)
    await scroll_to_end(page)

    soup = BeautifulSoup(await page.content(), "html.parser")
    links = set()

    for a in soup.select("a[href*='/products/']"):
        href = a.get("href")
        if href:
            links.add(BASE_URL + href.split("?")[0])

    print(f"🔗 Tổng link sản phẩm: {len(links)}")
    return list(links)

# ================== 🚀 Chặn ảnh + css để tăng tốc ==================
async def block_resources(route):
    # if route.request.resource_type in ["image", "stylesheet", "font"]:
    if route.request.resource_type in ["image", "font"]: # KHÔNG block document / script
        await route.abort()
    else:
        await route.continue_() 
        
# ================== Is Clickable ==================
async def is_clickable(locator):
    try:
        if await locator.count() == 0:
            return False

        if not await locator.is_visible(timeout=800):
            return False
        
        class_name = await locator.get_attribute("class") or ""                

        if "soldout" in class_name.lower():
            return False

        return True
    except:
        return False

# ================== Detect option type ==================
async def get_option_type(swatch):
    header = swatch.locator(".pro-title")
    if await header.count() == 0:
        return None

    text = (await header.inner_text()).lower()

    if "color" in text or "màu" in text:
        return "color"
    if "size" in text or "kích" in text:
        return "size"

    return None

# ================== DETECT PRODUCT TYPE ==================
async def detect_product_type(page):
    has_color = await page.locator("#variant-swatch-0.swatch.is-color").count()
    has_size = await page.locator("#variant-swatch-0.swatch").count()
    return "variant" if (has_color or has_size) else "single"

# ================== SINGLE PRODUCT ==================
async def crawl_single(page, url):
    name = await page.locator("h1:visible").first.inner_text()
    
    try:
        price = await page.locator(".pro-price").inner_text()
    except:
        price = None

    return [{
        "product": name,
        "color": "Default",
        "size": "Default",
        "price": price,
        "url": url
    }]

# ================== VARIANT PRODUCT ==================
async def crawl_variant(page, url):
    color_name = "Default"
    price = "Default"
    size_name = "Default"
    color_el = None
    size_el = None
    results = []

    name = await page.locator("h1:visible").first.inner_text()
    
    # Lấy danh sách swatch
    swatches = page.locator(".swatch.clearfix")
    count = await swatches.count()

    for i in range(count):
        swatch = swatches.nth(i)
        opt_type = await get_option_type(swatch)
                
        if opt_type == "color":
            color_el = swatch.locator(".swatch-element")
        elif opt_type == "size":
            size_el = swatch.locator(".swatch-element.n-sd") # chỉ lấy những sản phẩm click được

    if color_el:
        color_count = await color_el.count()
    else:
        color_count = 1 # không có màu
    
    print(f"Color count: {color_count}")

    for c in range(color_count):
        # Xét nếu có color thì click, không có trường hợp color bị disable
        # if await color_el.count() > 0: đang None -> count ăn bug
        if color_el:
            color = color_el.nth(c)
            label = color.locator("label")
            color_name = (await label.inner_text()).strip()

            class_name = await label.get_attribute("class") or ""                

            if not "sd" in class_name.lower():
                print( f"Clicked Color {c} {color_name}" )
                await label.click(force=True, timeout=800)
                await page.wait_for_timeout(800)

        # Sau khi click/ hoặc không click vào color
        await page.wait_for_selector(".swatch-element.n-sd")
        # size_wrap = page.locator("#variant-swatch-1")
        # size_el = size_wrap.locator(".swatch-element.n-sd")
        size_count = await size_el.count() or 1

        for s in range(size_count):

            # Xét nếu có label
            if await size_el.count() > 0:
                
                # Xét từng size
                size = size_el.nth(s)
                size_label = size.locator("label")
                size_name = (await size_label.inner_text()).strip()

                if await is_clickable(size):
                    print( f"Clicked Size: {size_name}" )
                    await size.click()
                    await page.wait_for_timeout(600)

                    # Sau khi click vào size
                    try:
                        await page.wait_for_selector(".pro-price", timeout=3000)
                        price_raw = await page.locator(".pro-price").inner_text()
                        price = normalize_price(price_raw)
                    except:
                        price = None

                    results.append({
                        "product": name,
                        "color": color_name,
                        "size": size_name,
                        "price": price,
                        "url": url
                    })

    return results

# ================== AUTO CRAWL ==================
async def crawl_product(context, url, sem, variants_all):
    async with sem:
        page = await context.new_page()
        
        try:
            page.set_default_navigation_timeout(30000) # là lệnh đặt thời gian chờ tối đa cho các thao tác điều hướng (navigation) trong Playwright.
            page.set_default_timeout(30000)
            
            await page.goto(
                url,
                wait_until="commit",
                timeout=30000
            )
            await page.wait_for_timeout(2000)

            ptype = await detect_product_type(page)

            if ptype == "single":
                data = await crawl_single(page, url)
                print('Done si')
            else:
                data = await crawl_variant(page, url)
                print('Done va')
                
            variants_all.extend(data)
            print(f"✅ {ptype.upper()} | {url}")

        except Exception as e:
            print(f"❌ Lỗi {url}: {e}")
        finally:
            await page.close()
            await human_delay()


# ================== GROUP VARIANTS ==================
def group_variants(variants):
    products = {}

    for v in variants:
        key = v["url"]

        if key not in products:
            products[key] = {
                "name": v["product"],
                "url": v["url"],
                "colors": set(),
                "sizes": set(),
                "prices": [],
                "variants": []
            }

        price = normalize_price(v["price"])

        products[key]["colors"].add(v["color"])
        products[key]["sizes"].add(v["size"])
        if price:
            products[key]["prices"].append(price)

        products[key]["variants"].append({
            "color": v["color"],
            "size": v["size"],
            "price": price,
        })

    result = []
    for p in products.values():
        result.append({
            "name": p["name"],
            "url": p["url"],
            "colors": ", ".join(sorted(p["colors"])),
            "sizes": ", ".join(sorted(p["sizes"])),
            "price_min": min(p["prices"]) if p["prices"] else None,
            "price_max": max(p["prices"]) if p["prices"] else None,
            "variants": p["variants"]
        })

    return result


# ================== EXPORT EXCEL ==================
def export_excel(products):
    wb = Workbook()

    ws1 = wb.active
    ws1.title = "Products"
    ws1.append(["name", "url", "colors", "sizes", "price_min", "price_max"])

    for p in products:
        ws1.append([
            p["name"], p["url"], p["colors"],
            p["sizes"], p["price_min"], p["price_max"]
        ])

    ws2 = wb.create_sheet("Variants")
    ws2.append(["product", "color", "size", "price", "url"])

    for p in products:
        for v in p["variants"]:
            ws2.append([
                p["name"], 
                v["color"],
                v["size"], 
                v["price"],
                p["url"]
            ])

    wb.save(OUTPUT_FILE)
    print(f"📁 Xuất file: {OUTPUT_FILE}")


# ================== MAIN ==================
async def main():
    variants_all = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )

        context = await browser.new_context(
            user_agent=UA_REAL,
            locale="vi-VN",
            timezone_id="Asia/Ho_Chi_Minh",
            viewport={"width": 1920, "height": 1080}
        )

        # 🚀 chặn ảnh + css để tăng tốc
        # await page.route("**/*", block_resources)

        page = await context.new_page()
        product_links = await get_product_links(page)

        sem = asyncio.Semaphore(CONCURRENT)
        tasks = [
            crawl_product(context, url, sem, variants_all)
            for url in product_links
        ]

        await asyncio.gather(*tasks)
        await browser.close()

    products = group_variants(variants_all)
    export_excel(products)

    print("🎯 HOÀN TẤT TOÀN BỘ PIPELINE")


if __name__ == "__main__":
    asyncio.run(main())