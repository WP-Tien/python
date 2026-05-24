# d: dimension
# Chuyển định dạng (shape) của một ndarray. Chuyển mảng một chiều thành mảng hai chiều
import numpy as np

# create a 1D ndarray from 0 to 9
data = np.arange(10)
print(data)

# reshape data to 2 rows and 5 columns
data_2d = data.reshape(2, 5)
print(data_2d)

# Xếp chồng 2 mảng theo chiều dọc
# 👉 -1 giúp khỏi cần tính số cột/dòng
data1 = np.arange(10).reshape(2, -1)
print(data1)

data2 = np.arange(7, 10).reshape(2, -1)
print(data2)

# Way 1:
out1 = np.concatenate([data1, data2], axis=0)
print(out1)

# Way 2:
out2 = np.vstack([data1, data2])
print(out2)

# Way 3:
out3 = np.r_[data1, data2]
print(out3)