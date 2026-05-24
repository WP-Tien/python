import numpy as np

x2 = np.array(([12, 5, 2, 4],
               [7, 6, 8, 8],
               [1, 6, 7, 7]))

# Two rows, three columns
print( x2[:2, :3] )
# [[12  5  2]
#  [ 7  6  8]]

# all rows, every other column
print( x2[:3, ::2] )
# [[12  2]
#  [ 7  8]
#  [ 1  7]]

# finally, subarray dimension can even be reversed together
print( x2[::-1, ::-1] )
# [[ 7  7  6  1]
#  [ 8  8  6  7]
#  [ 4  2  5 12]]

# Accessing array rows and columns
# first column of x2
print( x2[:, 0] ) # [12  7  1]

# first row of x2
print( x2[0, :] ) # [12  5  2  4]

# equivalent to x2[0, :]
print( x2[0] ) # [12  5  2  4]