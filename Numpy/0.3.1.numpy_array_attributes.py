import numpy as np

np.random.seed(0) # seed for reproducibility

x1 = np.random.randint(10, size=6) # One-dimensional array
x2 = np.random.randint(10, size=(3, 4)) # Two=dimensional array
x3 = np.random.randint(10, size=(3, 4, 5)) # Three-dimensional array

print( x1 ) 
'''
[5 0 3 3 7 9]
'''
print( x2 )
'''
[[3 5 2 4]
 [7 6 8 8]
 [1 6 7 7]]
'''
print( x3 )
'''
[[[8 1 5 9 8]
  [9 4 3 0 3]
  [5 0 2 3 8]
  [1 3 3 3 7]]

 [[0 1 9 9 0]
  [4 7 3 2 7]
  [2 0 0 4 5]
  [5 6 8 4 1]]

 [[4 9 8 1 1]
  [7 9 9 3 6]
  [7 2 0 3 5]
  [9 4 4 6 4]]]
'''

# Each array has attribute ndim (the number of dimension), shape (the size of each dimension), and size (the total size of the array):
print("x3 ndim: ", x3.ndim) # x3 ndim:  3
print("x3 shape: ", x3.shape) # x3 shape:  (3, 4, 5)
print("x3 size: ", x3.size) # x3 size:  60

# Another useful attribute is the dtype, the data type if the array
print("dtype:", x3.dtype) # dtype: int64

# Other attributes include itemsize, which lists the size (in bytes) of each array element, and nbytes, which lists the total size(in bytes) of the array:
print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")
# itemsize: 8 bytes
# nbytes: 480 bytes