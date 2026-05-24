import numpy as np

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = np.concatenate([x, y])
print( z ) # [1 2 3 3 2 1]

# You can also be used for two-dimensional arrays:
z = np.array([99, 99, 99])
print( np.concatenate([x, y, z]) ) # [ 1  2  3  3  2  1 99 99 99]

# It can also used for two-dimensional arrays:
grid = np.array([[1, 2, 3], [4, 5, 6]])

# Concatenate along the first axis
print( np.concatenate([grid, grid]) )
# [[1 2 3]
#  [4 5 6]
#  [1 2 3]
#  [4 5 6]]

# Concatenate along the second axis (zero-indexed)
print( np.concatenate([grid, grid], axis=1) )
# [[1 2 3 1 2 3]
#  [4 5 6 4 5 6]]

# It can be clearer to use the np.vstack (vertical stack) and np.hstack (horizontal stack)
# vertically stack the arrays
print( np.vstack([x, grid]) )

# horizontally stack the arrays
y2 = np.array([[99], [99]])
print(np.hstack([grid, y2]))
# [[ 1  2  3 99]
#  [ 4  5  6 99]]