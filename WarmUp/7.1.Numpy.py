# Import gói Numpy và in ra phiên bản của nó
# Python code
import numpy as np
print(np.version.version)


# Tạo mảng một chiều từ 4 đến 9
data = np.arange(4, 10)
print(data)

'''
Trong NumPy (Python), np.ones là hàm dùng để tạo một mảng (array) với tất cả các phần tử đều bằng 1.

np.ones(shape, dtype=None)

shape: kích thước mảng
- Số nguyên -> mảng 1 chiều
- Tuple -> mảng nhiều chiều
dtype (tuỳ chọn): kiểu dữ liệu (mặc định là float)
'''

# Tạo một mảng boolean 3x3 với tất cả giá trị là True
# way 1
data1 = np.ones((3,3)) > 0
print(f"{data1} \n ------------------------------")

# way 2
data2 = np.ones((3,3), dtype=bool)
print(f"{data2} \n ------------------------------")

# way 3
data3 = np.full((3, 3), True, dtype=bool)
print(f"{data3} \n ------------------------------")