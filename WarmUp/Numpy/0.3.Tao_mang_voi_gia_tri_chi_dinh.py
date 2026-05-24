'''
np.full là hàm dùng để tạo một mảng với tất cả các phần tử đều có cùng một giá trị xác định. Cú pháp:

np.full(shape, fill_value)

- shape: Kích thước của mảng (có thể là một số nguyên hoặc một tuple)
- fill_value: Giá trị sẽ được gán cho tất cả các phần tử của mảng

Ví dụ sau sẽ tạo một mảng NumPy 2 chiều, kích thước 2x3 với tất cả các phần tử đều có giá trị là 7
'''
import numpy as np

# Tạo mảng 2 chiều 2x3 với tất cả các phần tử đều có giá trị là 7
full_array = np.full((2,3), 7)
print(full_array)

'''
[[7 7 7]
 [7 7 7]]
'''