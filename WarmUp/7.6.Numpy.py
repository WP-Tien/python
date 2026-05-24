# Lấy phần tử chung của 2 mảng
import numpy as np

data1 = np.array([1,2,3,2])
data2 = np.array([7,2,1,8])
print(data1)
print(data2)

out = np.intersect1d(data1, data2)
print(out)


# Xoá phần tử từ một mảng mà tồn tại trong một mảng khác
data3 = np.array([1,2,3,4,5])
data4 = np.array([1,5,9])

out2 = np.setdiff1d(data3, data4)
print(out2)