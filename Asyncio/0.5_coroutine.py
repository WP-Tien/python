'''
    Trong asyncio của Python, coroutine là một hàm bất đồng bộ (asynchronous function) có thể tạm dừng (suspend) và tiếp tục (resume) việc thực thi của nó, giúp chương trình xử lý nhiều tác vụ I/O hiệu quả mà không cần đa luồng.


    Coroutine là hàm được khai báo bằng từ khoá async def và phải được gọi bằng await (hoặc được chạy bởi event loop)
'''

import asyncio

async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(1)
    print("Done fetching")
    return 42

'''
    async def -> định nghĩa coroutine
    await -> tạm dừng coroutine cho đến khi tác vụ bất đồng bộ hoàn thành
    
    => Gọi fetch_data() chưa chạy ngay, mà chỉ tạo ra coroutine object
'''

coro = fetch_data()
print(coro) # <coroutine object fetch_data at 0x10c4b9900>

'''
    Event loop là "bộ điều phối" chạy các coroutine.
'''

async def main():
    result = await fetch_data()
    print(result)
    
asyncio.run(main())

'''
    Luồng hoạt động
    1. main() chạy
    2. gặp await fetch_data() -> chuyển quyền cho event loop
    3. trong lúc chờ I/O -> event loop chạy coroutine khác
    4. xong -> quay lại fetch_data
'''

