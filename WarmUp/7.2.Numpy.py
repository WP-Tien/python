# Lấy những phần tử mà thoả mãn một điều kiện cho trước của mảng một chiều
import numpy as np

# create an ndarray from 0 to 9
data = np.arange(0, 10)
print(data)

# Find odd numbers
data_odd = data[data%2 == 1]
print(data_odd)

# Thay thế phần tử thoả mãn điều kiện cho trước bằng một giá khác
data[data%2 == 1] = -1
print(data)

# replace odd numbers by -1
'''
Cú pháp
np.where(condition, x, y)

👉 Nếu condition đúng → lấy x, sai → lấy y
'''
data2 = np.arange(0, 10)
out = np.where(data2%2 == 1, -1, data2)
print(out)