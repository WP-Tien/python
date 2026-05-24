import asyncio
import random
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from openpyxl import Workbook


# COLLECTION_URL = "https://www.oldsailor.com.vn/collections/all" # Link tất cả sản phẩm
COLLECTION_URL = "https://www.oldsailor.com.vn/collections/nhom-iron-deep-black" # Iron deep black
BASE_URL = "https://www.oldsailor.com.vn"

# ===== Scroll lazy-load =====
async def scroll_to_end(page):
    prev_height = 0
    while True:
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        '''
        page.evaluate(...)
        Thực thi JavaScript trực tiếp trong ngữ cảnh của trình duyệt

        window.scrollTo(x, y)
        x = 0 → không cuộn ngang
        y = document.body.scrollHeight → chiều cao toàn bộ nội dung trang
        '''
        await page.wait_for_timeout(2000)
        
        new_height = await page.evaluate("document.body.scrollHeight")
        if new_height == prev_height:
            break
        prev_height = new_height

# ===== Lấy link sản phẩm =====
async def get_product_links(page):
    await asyncio.sleep(random.uniform(1.5, 3.5))
    await page.goto(COLLECTION_URL, timeout=60000)
    await page.wait_for_timeout(3000)
    await scroll_to_end(page)
    
    soup = BeautifulSoup(await page.content(), "html.parser")
    links = set()
    
    for a in soup.select("div.product-loop a[href]"):
        href = a["href"]
        if "/products/" in href:
            links.add(BASE_URL + href)
            
    print(f"🔗 Tổng link sản phẩm: {len(links)}")
    return list(links)

# ===== Crawl chi tiết sản phẩm =====
async def crawl_product(context, url):
    page = await context.new_page()
    
    try:
        # Làm như người thật:
        await asyncio.sleep(random.uniform(1.5, 3.5))
        await page.goto(url, timeout=60000)
        await page.wait_for_timeout(2000)

        soup = BeautifulSoup(await page.content(), "html.parser")

        name = soup.select_one("h1")
        name = name.get_text(strip=True) if name else None

        price = soup.select_one(".pro-price")
        # price = price.get_text(strip=True) if price else None
        price = price.get_text(strip=True).replace("₫", "").replace(",", "") if price else None

        desc = soup.select_one(".desc-content-js")
        desc = desc.get_text("\n", strip=True) if desc else None

        # Ảnh
        imgs = []
        # for img in soup.select("img"):
        for img in soup.select(".product-gallery img, .product-image img"):
            src = img.get("data-src") or img.get("src")
            if src and "cdn.hstatic.net" in src:
                imgs.append(src)

        # Size / variant
        sizes = []
        for s in soup.select(".swatch-element label"):
            sizes.append(s.get_text(strip=True))

        return {
            "url": url,
            "name": name,
            "price": price,
            "sizes": ", ".join(set(sizes)),
            "images": ", ".join(set(imgs)),
            "description": desc
        }
        
    except Exception as e:
        print(f"❌ Lỗi {url}: {e}")
        return None
    finally:
        await page.close()
        
# 🚀 chặn ảnh + css để tăng tốc
async def block_resources(route):
    if route.request.resource_type in ["image", "stylesheet", "font"]:
        await route.abort()
    else:
        await route.continue_() 
        
# ===== MAIN =====
async def main():
    async with async_playwright() as p:
        # Tắt dấu hiệu automation
        browser = await p.chromium.launch(
            headless=False, # đổi True nếu chạy ẩn
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        )
        
        # User-Agent giống người thật
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            locale="vi-VN",
            timezone_id="Asia/Ho_Chi_Minh"
        )
        
        page = await context.new_page()
        
        # 🚀 chặn ảnh + css để tăng tốc
        # await page.route("**/*", block_resources)
        
        product_links = await get_product_links(page)
        
        results = []
        sem = asyncio.Semaphore(3)  # giới hạn song song 3-5 là an toàn
        
        async def sem_task(url):
                async with sem:
                    data = await crawl_product(context, url)
                    if data:
                        results.append(data)
                        
        await asyncio.gather(*[sem_task(url) for url in product_links])
        await browser.close()

        # ===== GHI EXCEL =====
        wb = Workbook()
        ws = wb.active
        ws.title = "Products"

        headers = [
            "url", "name", "price", "sizes", "images", "description"
        ]
        ws.append(headers)

        for item in results:
            ws.append([item.get(h) for h in headers])

        wb.save("oldsailor_products.xlsx")

        print("🎯 Xuất file oldsailor_products.xlsx thành công")

    
if __name__ == "__main__":
    asyncio.run(main())