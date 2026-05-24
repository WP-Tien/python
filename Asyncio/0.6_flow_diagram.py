'''
Dưới đây là flow diagram (sơ đồ luồng) minh hoạ cách coroutine hoạt động trong asyncio 👇
(Mình dùng ASCII để bạn dễ đọc ngay trong chat)

+------------------+
|  Event Loop     |
+------------------+
        |
        v
+------------------+
|  Coroutine A    |---- await ----+
+------------------+              |
        |                          |
        |        (đang chờ I/O)    |
        |                          v
        |                 +------------------+
        |                 |  Coroutine B    |
        |                 +------------------+
        |                          |
        |                     await sleep
        |                          |
        +------------ resume <----+
        
Ý tưởng chính
Coroutine A gặp await → tạm dừng
Event loop chuyển sang coroutine B
Khi I/O xong → coroutine A resume







Code example:
async def fetch_data():
    print("Start")
    await asyncio.sleep(1)
    print("End")

fetch_data()
     |
     v
+------------------+
|  Start 실행      |
+------------------+
     |
     v
+------------------------------+
| await asyncio.sleep(1)       |
|  -> tạm dừng coroutine       |
|  -> trả quyền cho event loop |
+------------------------------+
     |
     |   (sau 1 giây)
     v
+------------------+
|  Resume coroutine|
+------------------+
     |
     v
+------------------+
|  End 실행        |
+------------------+




Nhiều coroutine chạy “song song”
Code:
async def task(name, delay):
    await asyncio.sleep(delay)
    print(name)

async def main():
    await asyncio.gather(
        task("A", 1),
        task("B", 2),
        task("C", 3)
    )
    

Time →
------------------------------------------------>

Task A: |---sleep 1s---| print A | done
Task B: |------sleep 2s------| print B | done
Task C: |----------sleep 3s----------| print C | done

Event Loop:
   chạy A → pause
   chạy B → pause
   chạy C → pause
   resume A
   resume B
   resume C
   
Tổng thời gian = 3 giây (task lâu nhất)













Một câu chốt dễ nhớ 🧠

Coroutine không chạy song song thật, mà luân phiên cực nhanh khi gặp await.
'''