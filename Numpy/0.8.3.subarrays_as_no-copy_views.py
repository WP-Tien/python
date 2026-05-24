import numpy as np

# Creating a np array
x = np.array(([12, 5, 2, 4],
              [7, 6, 8, 8],
              [1, 6, 7, 7]))

# Extract a 2x2 subarray
x_sub = x[:2, :2]
print(x_sub)
# [[12  5]
#  [ 7  6]]

# Modify this subarray
x_sub[0, 0] = 99
print(x_sub)
# [[99  5]
#  [ 7  6]]

# then check againt x
print(x)
# [[99  5  2  4]
#  [ 7  6  8  8]
#  [ 1  6  7  7]]

# Creating copies of arrays
x_sub_copy = x[:2, :2].copy()
print(x_sub_copy)
# [[99  5]
#  [ 7  6]]

# Assign the value to x_sub_copy
x_sub_copy[0, 0] = 42
print(x_sub_copy)
# [[42  5]
#  [ 7  6]]

# Check array x, 1 more time
print(x)
# [[99  5  2  4]
#  [ 7  6  8  8]
#  [ 1  6  7  7]]