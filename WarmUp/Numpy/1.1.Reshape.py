'''
reshape là một hàm sử dụng để thay đổi hình dạng của một mảng mà không làm thay đổi dữ liệu bên trong nó. Kích thước mảng mới được chỉ định thông qua tham số của hàm reshape.
Cú pháp sử dụng reshape:

np.reshape(input, newshape)

Trong đó:
- input: là mảng đầu vào
- newshape là hình dạng mới ta muốn chuyển đổi.

Trong ví dụ sau, ta sẽ sử dụng reshape để giảm chiều array:
'''
import numpy as np

# Tạo một mảng 2D
arr_2D = np.array([[1,2,3], [4,5,6]])
# (2,3)->(3,2)
new_arr_2D = np.reshape(arr_2D, (3,2))

# Chuyển từ 2D -> 1D
arr_1D = np.reshape(arr_2D, newshape=(6, ))

print("array 2D:\n", arr_2D, arr_2D.shape)
print("new array 2D :\n", new_arr_2D, new_arr_2D.shape)
print("array 1D:\n", arr_1D, arr_1D.shape)

'''
array 2D:
 [[1 2 3]
 [4 5 6]] (2, 3)
new array 2D :
 [[1 2]
 [3 4]
 [5 6]] (3, 2)
array 1D:
 [1 2 3 4 5 6] (6,)
 
Trong ví dụ trên, ta tạo một mảng 2D có 2 hàng và 3 cột. Sử dụng np.reshape để thay đổi hình dạng của mảng từ 2D thành 1D với hình dạng mới là (6,), nghĩa là một mảng có 6 phần tử. Ở đây 6=2x3, bằng với số phần tử của cũ, ta cần lưu ý khi thay đổi shape thì cần đảm bảo số lượng phần tử không được thay đổi khi reshape.
'''