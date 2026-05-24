import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()
        
async def main():
    urls = [
        "https://pokeapi.co/api/v2/pokemon/ditto",
        "https://pokeapi.co/api/v2/pokemon-species/aegislash"
    ]
    
    results = await asyncio.gather(*(fetch(u) for u in urls))
    print(results)
    
asyncio.run(main())