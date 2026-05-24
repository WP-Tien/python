'''
contextlib.ContextDecorator: context manager + decorator
Đây là level tiếp theo
Vấn đề nó giải quyết
Thay vì:
with DBHandler():
    backup()
    
Ta muốn:
backup()
... nhưng tự động chạy trong context manager.

Cách dùng
import contextlib

class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()
        
    def __exit__(self, exc_type, exc_value, traceback):
        start_database()
    
Áp dụng như decorator:
@dbhandler_decorator()
def offline_backup():
    run("pg_dump database")

Gọi:
offline_backup()
=> Không cần with nữa!
Điều gì đang xảy ra?
- ContextDecorator tự động:
    - Wrap function
    - Chạy function bên trong context manager
- Bạn chỉ cần lo __enter__/__exit__

Hạn chế của cách này
Không dùng được:

with offline_backup() as X:
    ...

Vì:
Decorator không trao đổi object với function
Function và context manager độc lập hoàn toàn
-> Nếu bạn cần giá trị từ __enter__, thì:
Dùng with
Hoặc @contextmanager

Khi nào nên dùng ContextDecorator
✔ Khi:
Logic trước/sau giống nhau cho nhiều function
Muốn viết một lần, tái sử dụng nhiều nơi
Không cần state từ context manager
'''