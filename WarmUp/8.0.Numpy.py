# Đảo ngược các phần tử của các cột trong mảng hai chiều
import numpy as np

# create a 3x3 matrix
data = np.arange(9).reshape(3,3)
print(data, '\n')

# reverse each column
out = data[::-1, :]
print(out)