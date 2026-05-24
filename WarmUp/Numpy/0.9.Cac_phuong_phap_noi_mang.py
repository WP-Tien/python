'''
Trong thư viện Numpy các hàm hstack, vstack, và concatenate đươc sử dụng để nối các mảng với nhau theo hướng khác nhau. Trong bài tập này, chúng ta sẽ tìm hiểu cách sử dụng ba hàm trên.

# hstack
Hàm hstack được sử dụng để nối các mảng theo chiều ngang, tức là nối chúng thành một cấu trúc dữ liệu lớn hơn theo chiều thứ hai. Quá trình này giúp kết hợp dữ liệu từ các nguồn khác nhau hoặc mở rộng kích thước của cấu trúc dữ liệu hiện có.

Ví dụ sau sử dụng hstack để nối các mảng theo chiều ngang.
'''
# Numpy code
import numpy as np

# Tạo hai mảng
arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])

# Nối hai mảng theo trục ngang (axis=0)
arr_3 = np.hstack((arr_1, arr_2))

# In kết quả
print("Mảng 1:\n", arr_1)
print("Mảng 2:\n", arr_2)
print("Mảng sau khi nối theo trục ngang:\n", arr_3)

'''
Mảng 1:
 [1 2 3]
Mảng 2:
 [4 5 6]
Mảng sau khi nối theo trục ngang:
 [1 2 3 4 5 6]

Lưu ý khi sử dụng hstack là các mảng cần phải có cùng độ dài trong chiều dọc(cùng số hàng). 
Nếu các mảng không có cùng độ dài trong chiều dọc sẽ gây ra lỗi khi thực thi chương trình.
'''