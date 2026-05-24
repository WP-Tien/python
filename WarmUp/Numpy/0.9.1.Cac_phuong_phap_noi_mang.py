'''
Hàm vstack trong NumPy được sử dụng để nối các mảng theo chiều dọc, tức là nối chúng thành một cấu trúc dữ liệu lớn hơn theo chiều thứ nhất.

Ví dụ dưới đây sử dụng vstack để nối các mảng theo chiều dọc.
'''
import numpy as np
# Tạo hai array
arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])

# Nối hai mảng theo chiều dọc
arr_3 = np.vstack((arr_1, arr_2))
# In kết quả
print("Array 1:\n", arr_1)
print("Array 2:\n", arr_2)
print("Array sau khi nối theo chiều dọc:\n", arr_3)

'''
Lưu ý khi sử dụng vstack là các mảng phải có cùng số cột. Nếu các mảng không có cùng số cột sẽ gây ra lỗi khi thực thi chương trình.
'''