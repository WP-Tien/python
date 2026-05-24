# Ví dụ ❌ tuần tự (chậm)
import asyncio

async def task(n):
    await asyncio.sleep(1) # KHÁC time.sleep() → sẽ block toàn bộ event loop
    print(n)
    
# async def main():
#     await task(1)
#     await task(2)
#     await task(3)
    
# asyncio.run(main())

# Ví dụ song song
# async def main():
#     await asyncio.gather(
#         task(1),
#         task(2),
#         task(3),
#     )
    
# asyncio.run(main())

# Tạo task chạy nền
async def main():
    t1 = asyncio.create_task(task(1))
    t2 = asyncio.create_task(task(2))
    
    await t1
    await t2
    
asyncio.run(main())