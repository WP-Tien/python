import numpy as np

# 1-D array
# a = np.arange(12)
# print(a)

# # 1st ele
# print(a[0])

# # last ele
# print(a[-1])

# # 1st to 3rd
# print(a[:3])

# # 3rd to last
# print(a[2:])

# a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# print(a)
# print(a[:2, 1:3])

# n-D array
# Note: Try with order = F
a = np.arange(9).reshape((3, 3))
print(a)

# Ele at 0
print(a[0,0])

# 1st row
print(a[0])
print(a[0, :])

# last row
print(a[-1])
print("")

# 1st col
print(a[:, 0])

# last col
print(a[:, -1])

# first and last col
print(a[:, [0, -1]])

# everything
print(a[:, :])