'''
1. Cách cơ bản: class + __enter__/__exit__
Đây là cách "chuẩn sách giáo khoa"

class DBHandler:
    def __enter__(self):
        stop_database()
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        start_database()
        
Ưu điểm:
- Rõ ràng
- Kiểm soát đầy đủ
- Có thể giữ state (trạng thái)
Nhược điểm:
- Hơi verbose (dài dòng)
- Phải tạo class dù chỉ cần logic "trước/sau"
'''

'''
2. contextlib.contextmanager: context manager bằng function
Ý tưởng chính
@contextmanager cho phép bạn viết context manager như một hàm, thay vì class.

import contextlib
def db_handler():
    stop_database()
    yield
    start_database()
    
Sử dụng:
with db_handler():
    db_backup()
    
Cách hoạt động (rất quan trọng)
Hàm này là generator function (vì có yield)
Python sẽ hiểu như sau:

Phần code               Tương đương
Trước yield             __enter__
Giá trị yield           giá trị trả về của __enter__
sau yield               __exit__

Ví dụ:
'''
import contextlib

@contextlib.contextmanager
def cm():
    print("enter")
    yield "resource"
    print("exit")
    
with cm() as r:
    print(r)
    
# => Nếu yield không trả gì -> None sẽ được gán cho biến sau as

'''
Khi nào nên dùng @contextmanager
- Khi:
Không cần tạo class
Không cần giử nhiều state
Context manager độc lập, không thuộc về object nào
Muốn refactor code cũ nhanh gọn
- Không lý tưởng khi:
Logic phức tạp
Cần nhiều trạng thái
Cần tái sử dụng theo kiểu OO
'''