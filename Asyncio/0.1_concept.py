'''
asyncio là thư viện chuẩn của Python (từ Python 3.4+) dùng để lập trình bất đồng bộ (asynchronous programming) dựa trên event loop. Nó giúp chương trình xử lý nhiều tác vụ I/O-bound (network, file, API, sleep…) mà không cần tạo nhiều thread.

1️⃣ Khi nào nên dùng asyncio?

Dùng khi chương trình của bạn:

Gọi API / HTTP request nhiều
Xử lý socket, websocket
Chờ I/O (database, file, network)
Cần xử lý hàng nghìn task đồng thời nhưng không CPU nặng

❌ Không phù hợp cho:

Tính toán nặng (CPU-bound) → dùng multiprocessing
'''


'''
async/await
- async def: khai báo coroutine (hàm bất đồng bộ)
- await: chờ kết quả của coroutine khác
'''

import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")
    
asyncio.run(hello())

'''
Event Loop

Vòng lặp trung tâm quản lý và phân phối task
Bạn thường không cần thao tác trực tiếp
'''