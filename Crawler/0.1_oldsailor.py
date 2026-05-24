import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://www.oldsailor.com.vn"

# Danh sách đường dẫn danh mục bạn muốn cào
categories = [
    "/collections/ao-nam",
    "/collections/ao-polo-nam",
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

all_products = []

for cat in categories:
    url = BASE_URL + cat
    print(f"Đang cào: {url}")
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Không tải được {url}")
        continue
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Tìm tất cả phần tử sản phẩm
    items = soup.select("div.product-loop") # lớp tùy theo HTML; kiểm tra lại nếu khác
    
    for item in items:
        title_el = item.select_one("proloop-title a")
                
        price_el = item.select_one(".proloop-price .price")
        img_el = item.select_one("div.lazy-img.lazy-img__prod.first-image img")
        
        title = title_el.text.strip() if title_el else ""
        link = BASE_URL + title_el.get("href") if title_el else ""
        price = price_el.text.strip() if price_el else ""
        image = img_el["data-src"] if img_el and img_el.has_attr("data-src") else (img_el["src"] if img_el else "")
        
        all_products.append({
            "category": cat.split("/")[-1],
            "title": title,
            "price": price,
            "link": link,
            "image": image
        })
    
    time.sleep(1) # nghỉ để tránh bị block
    
# Lưu vào CSV
df = pd.DataFrame(all_products)
df.to_csv("oldsailor_products.csv", index=False)
print("Hoàn tất cào dữ liệu!")