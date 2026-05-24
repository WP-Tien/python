import numpy as np

grid = np.arange(1, 10).reshape((3, 3))
print(grid)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

x = np.array([1, 2, 3])

# row vector via reshape
x.reshape((1, 3)) # 1 Row, 3 columns
print(x) # [1 2 3]

# row vector via newaxis (thêm chiều)
print( x[np.newaxis, :] ) # [[1 2 3]]
print( x[:, np.newaxis] )
# [[1]
#  [2]
#  [3]]

# column vector via reshape
print( x.reshape((3, 1)) ) # 3 Rows, 1 column
# [[1]
#  [2]
#  [3]]

