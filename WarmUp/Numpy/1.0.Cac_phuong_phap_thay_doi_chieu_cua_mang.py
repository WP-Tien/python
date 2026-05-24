'''
# Slicing, expand_dims
Khi thực hiện tính toán với array chúng ta sẽ thường xuyên phải điều chỉnh số chiều của chúng. 
Để thêm một chiều mới, chúng ta sử dụng newaxis hoặc expand_dims.

Ví dụ sau đây thực hiện thêm một chiều mới vào mảng sử dụng newaxis:
'''
# Numpy code
import numpy as np

# Tạo một array 1D
arr_1 = np.array([1,2,3])

# 1D -> 2D
arr_2 = arr_1[np.newaxis, :]

# 2D -> 5D
arr_3 = arr_2[np.newaxis, :, np.newaxis, :, np.newaxis]

print("array1: ", arr_1, arr_1.shape)
print("array2: ", arr_2, arr_2.shape)
print("array3: ", arr_3, arr_3.shape)
'''
array1:  [1 2 3] (3,)
array2:  [[1 2 3]] (1, 3)
array3:  [[[[[1]
    [2]
    [3]]]]] (1, 1, 1, 3, 1)
'''

'''
Trong ví dụ trên, ta tạo một mảng 1D có giá trị [1,2,3]. Tiếp theo ta sử dụng np.newaxis để thêm một chiều mới ở vị trí 0, chuyển từ mảng 1D thành mảng 2D. Cuối cùng ta dùng np.newaxis để thêm chiều mới, chuyển từ mảng 2D thành mảng 5D. Các chiều mới được thêm vào ở vị trí 0, 2, và 4.
Ở đây, dấu ":" Thể hiện chiều của mảng cũ, dấu hai chấm đầu tiên là chiều thứ nhất, dấu hai chấm thứ hai là chiều thứ 2 của mảng cũ. Ta có thể đặt dấu hai chấm này ở các vị trí khác nhau, tuỳ thuộc vào mục đích tạo mảng mới. "np.newaxis" là chiều mới ta muốn tạo, có thể đặt ở các vị trí khác nhau, ta cũng có thể thay thế nó bằng "None" hoặc "..."
Ngoài ra ta cũng có thể sử dụng cách thứ hai, np.expand_dims để thêm chiều mới cho array.
'''

# Tạo một mảng 1D
arr_1_1 = np.array([1,2,3])

# Thêm chiều mới, chuyển từ 1D -> 2D
arr_2_2 = np.expand_dims(arr_1_1, axis=0)

# Thêm nhiều chiều mới, chuyển từ 2D -> 5D
arr_3_3 = np.expand_dims(arr_2_2, axis=(0, 2, 4))

# In ra kết quả
print("array 1:", arr_1_1, arr_1_1.shape)
print("array 2:", arr_2_2, arr_3_3.shape)
print("array 3:", arr_3_3, arr_3_3.shape)
'''
array 1: [1 2 3] (3,)
array 2: [[1 2 3]] (1, 1, 1, 3, 1)
array 3: [[[[[1]
    [2]
    [3]]]]] (1, 1, 1, 3, 1)
'''