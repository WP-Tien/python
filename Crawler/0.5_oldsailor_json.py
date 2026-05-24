import asyncio
import aiohttp
from openpyxl import Workbook

# ================== CONFIG ==================
BASE_URL = "https://www.oldsailor.com.vn"
COLLECTION_API = f"{BASE_URL}/collections/all/products.json"
OUTPUT_FILE = "oldsailor_products.xlsx"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
}

LIMIT = 250 # max Shopify cho phép

# ================== FETCH ==================
async def fetch(session, url):
    async with session.get(url, headers=HEADERS, timeout=30) as resp:
        if resp.status != 200:
            return None
        return await resp.json()

# ================== CRAWL ALL PRODUCTS ==================
async def crawl_all_products():
    since_id = 0
    all_products = []
    
    async with aiohttp.ClientSession() as session:
        while True:
            url = f"{COLLECTION_API}?limit={LIMIT}&since_id={since_id}"
            data = await fetch(session, url)
            
            if not data or not data.get("products"):
                break
            
            products = data["products"]
            all_products.extend(products)
            
    return all_products

# ================== MAIN ==================
async def main():
    print("🚀 Start crawling Oldsailor")
    products = await crawl_all_products()
    print(f"🐷 Total products: {len(products)}")

if __name__ == "__main__":
    asyncio.run(main())