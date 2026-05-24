'''
Overflow and Underflow

Trong lập trình học máy và học sâu, ta thường xuyên phải xử lý các số thực có phạm vi rộng, từ rất lớn đến rất nhỏ. Điều này gây ra nhiều khó khăn, điển hình là vấn đề overflow và underflow.

- Overflow là hiện tượng xảy ra khi một số vượt qua giới hạn trên của kiểu dữ liệu mà nó được lưu trữ.
- Underflow là hiện tượng xảy ra

Ví dụ, trong Python, nếu một số thực vượt quá giới hạn trên của kiểu dữ liêu float, nó sẽ được chuyển đổi thành số vô cùng lớn, và ngược lại, một số quá nhỏ sẽ được chuyển thành giá trị 0. Điều này có thể dẫn đến các lỗi tính toán, hoặc thậm chí làm chương trình dừng hoạt động
'''

# Ví dụ của một số quá nhỏ sẽ chuyễn về 0 (overflow)
# 0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
result = 1e-100
print(result)

# 0.0
result = 1e-1000
print(result)

# Ví dụ của một số quá lớn sẽ chuyển thành vô cực (underflow)
result = 1e100
print(result)

result = 1e1000
print(result)