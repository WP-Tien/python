# Lấy tất cả vị trí nơi giá trị các phần tử 2 mảng giống nhau
import numpy as np

# create data1 v data2
data1 = np.array([1,2,3,4,5,6])
data2 = np.array([1,1,1,6,6,6])

# compare the two array
comp = data1==data2

# get indices whose elements are not zero
indices = comp.nonzero()
print(indices)





# Lấy tất cả các giá trị trong một phạm vi cho trước
data3 = np.array([1,8,3,9,7,6])
print(data3)

# Way 1
# indices : chỉ số
indices = np.where(data3>=7)
out1 = data3[indices]
print(out1)

# Way 2
out2 = data3[data3>=7]
print(out2)