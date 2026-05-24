import time
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

url = "https://www.oldsailor.com.vn/collections/ao-polo-nam"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # True nếu muốn chạy ẩn
    page = browser.new_page()
    page.goto(url, timeout=60000)

    page.wait_for_timeout(3000)

    # ===== Scroll đến khi không còn sản phẩm mới =====
    prev_height = 0
    while True:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(2000)

        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == prev_height:
            break
        prev_height = new_height

    print("✅ Đã load hết sản phẩm")

    # ===== Parse HTML =====
    soup = BeautifulSoup(page.content(), "html.parser")
    products = soup.select("div.product-loop")

    print(f"🔢 Tổng sản phẩm lấy được: {len(products)}")
    
    data = []
    
    for item in products:
         # Tên
        name = item.select_one("h3.product-name")
        name = name.get_text(strip=True) if name else None

        # Link
        link = item.select_one("a")
        link = "https://www.oldsailor.com.vn" + link["href"] if link else None

        # Giá
        price = item.select_one(".price")
        price = price.get_text(strip=True) if price else None

        # Ảnh (lazyload)
        img = item.select_one("img")
        img_url = None
        if img:
            img_url = img.get("data-src") or img.get("src")

        data.append({
            "name": name,
            "price": price,
            "link": link,
            "image": img_url
        })
        
    browser.close()
    
# ===== In thử =====
for d in data[:5]:
    print(d)

print("🎯 Hoàn tất")