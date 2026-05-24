import numpy as np

# create a 3x3 matrix
data = np.arange(9).reshape(3,3)

# A new matrix is constructed by the rows [1,0,2] from data
out = data[[1,0,2], :]
print(out)

'''
[[3 4 5]
 [0 1 2]
 [6 7 8]]
'''