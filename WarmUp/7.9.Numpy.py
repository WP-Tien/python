# Hoán đổi các cột trong mảng 2 chiều
import numpy as np

# create a 3x3 matrix
data = np.arange(9).reshape(3,3)
print(data, '\n')

# A new matrix is constructed by the columns [1,0,2] from data
out = data[:, [1,0,2]]
print(out)


'''
[[0 1 2]
 [3 4 5]
 [6 7 8]] 

[[1 0 2]
 [4 3 5]
 [7 6 8]]
'''