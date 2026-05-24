'''
Tượng tự với zeros, hàm ones tạo mảng chứa toàn số 1 với đầu vào là kích thước do người dùng chỉ định. Cú pháp:

np.ones(shape)

- shape: Kích thước của mảng (có thể là một số nguyên hoặc một tuple)

Ví dụ sau sẽ tạo một mảng 2 chiều có kích thước 3x3 với tất cả các phần tử đều là 1
'''
import numpy as np

# Tạo mảng 2 chiều 3x3 với tất cả các phần tử đều là 1
ones_array = np.ones((3,3))
print(ones_array)

'''
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
'''