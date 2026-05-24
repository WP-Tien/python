'''
1. Vấn đề mà context manager giải quyết
Rất nhiều tính huống trong code có mẫu chung:
1. Làm một việc chuẩn bị trước (precondition)
2. Thực hiện hành động chính
3. Dọn dẹp sau khi xong (postcondition), kể cả khi có lỗi

Ví dụ quen thuộc:
. Mở file -> xử lý -> đóng file
. Mở kết nối DB -> query -> đóng kết nối
. Dừng service -> backup -> khởi động lại service

Nếu làm thủ công, bạn phải dùng try/finally:
fd = open(filename)
try:
    process_file(fd)
finally:
    fd.close()
    
Cách này đúng, nhưng:
. Dài dòng
. Dễ quên finally
. Logic chính bị trộn lẫn với logic dọn dẹp
'''

'''
2. with và context manager: cách Pythonic hơn
Python cung cấp context manager để giải quyết đúng mẫu này:
with open(filename) as fd:
    process_file(fd)
    
Ưu điểm:
- File luôn được đóng, kể cả khi process_file gây exception
- Code gọn, dễ đọc
- Tách biệt rõ "Làm việc gì" và "dọn dẹp thế nào"
'''

"""
3. Context manager hoạt động như thế nào?
Một context manager là object có 2 magic methods:
__enter__
- Được gọi khi bắt đầu with
- Giá trị return sẽ được gán cho biến sau as (nếu có)
__exit__
- Được gọi khi thoát khỏi block
- Luôn chạy, dù có exception hay không
- Nhận thông tin exception nếu có

__exit__(self, exc_type, exc_value, traceback)
Nếu không có lỗi -> cả 3 là None
"""

"""
4. Tự viết context manager: ví dụ backup database
Bài toán:
- Backup DB chỉ khi DB đang tắt
- Sau backup, phải bật DB lại, dù backup thành công hay thất bại
"""

run = print

def stop_database():
    run("systemctl stop postgresql.service")
    
def start_database():
    run("systemctl start postgresql.service")
    
class DBHandler:
    def __enter__(self):
        stop_database()
        return self
    
    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()
        
def db_backup():
    run("pg_dump database")

# Sử dụng:
with DBHandler():
    db_backup()
    
'''
Ý nghĩa:
- __enter__: dừng database
- Code trong with: chỉ lo backup
- __exit__: luôn bật lại database
'''

'''
6. Cảnh báo quan trọng về __exit__
Giá trị return của __exit__
- Nếu __exit__ trả về True
-> exception bị nuốt, không lan ra ngoài
- Nếu trả về None hoặc False
-> exception vẫn raise bình thường
=> Vì vậy:
- Đừng vô tình return True
- Chỉ swallow exception khi bạn chắc chắn đó là điều mình muốn
'''

'''
7. Khi nào nên dùng context manager?
Ngoài resource management, còn rất hợp cho:
- Logging (bắt đầu/kết thúc một tác vụ)
- Timing/profiling
- Transaction (commit/rollback)
- Lock/unlock
- Tạm thay đổi cấu hình rồi khôi phục
'''
