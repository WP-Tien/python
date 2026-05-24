'''
Hàm concatenate được sử dụng để nối các mảng theo chiều cụ thể.
Ví dụ sau sẽ tạo hai mảng từ list 2D là [[1,2,3], [4,5,6]] và [[7,8,9],[10,11,12]]. Sau đó sử dụng hàm concatenate để nối theo trục ngang và trục dọc.
'''

# Numpy code
import numpy as np
# Tạo hai mảng 2D
arr_1 = np.array([[1,2,3],[4,5,6]])
arr_2 = np.array([[7,8,9],[10,11,12]])
# Nối hai mảng theo chiều dọc axis = 0
arr_3 = np.concatenate((arr_1, arr_2), axis=0)
# Nối hai mảng theo chiều ngang axis = 1
arr_4 = np.concatenate((arr_1, arr_2), axis=1)
# In kết quả
print("Array 1:\n", arr_1)
print("Array 2:\n", arr_2)
print("Nối theo chiều dọc (axis=0):\n", arr_3)
print("Nối theo chiều ngang (axis=1):\n", arr_4)

'''
Array 1:
 [[1 2 3]
 [4 5 6]]
Array 2:
 [[ 7  8  9]
 [10 11 12]]
Nối theo chiều dọc (axis=0):
 [[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
Nối theo chiều ngang (axis=1):
 [[ 1  2  3  7  8  9]
 [ 4  5  6 10 11 12]]
 
Trong chương trình trên ta sử dụng np.concatenate để nối hai mảng theo chiều dọc (axis=0) và chiều ngang (axis=1), Trong đó arr_1 và arr_2 là hai mảng 2D được bằng NumPy. Tiếp theo, arr_3 được tạo bằng cách nối arr_1 và arr_2 theo chiều đọc (axis=0), nghĩa là nối theo hàng. Cuối cùng arr_4 được tạo bằng cách nối arr_1 và arr_2 theo chiều ngang (axis=1), nghĩa là nối theo cột. Khi sử dụng concatenate các bạn cần lưu ý, đối với việc nối hai array 1D theo chiều 1 sẽ gặp lỗi, lí do là vì các array chỉ có 1 chiều là chiều 0. Chính vì vậy mà ta cần chuyển đổi chúng sang dạng 2D trước khi nối chúng lại theo chiều 1. Một lựa chọn dễ dàng hơn là sử dụng vstack.
'''