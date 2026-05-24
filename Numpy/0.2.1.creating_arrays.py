import numpy as np

# Create a length-10 integer array filled with zeros
print( np.zeros(10, dtype=int) )
# [0 0 0 0 0 0 0 0 0 0]

# Create a 3x5 floating-point array filled with ones
print( np.ones((3, 5), dtype=float) )
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

# Create a 3x5 array filled with 3.14
print( np.full((3, 5), 3.14) )
# [[3.14 3.14 3.14 3.14 3.14]
#  [3.14 3.14 3.14 3.14 3.14]
#  [3.14 3.14 3.14 3.14 3.14]]

# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)
print( np.arange(0, 20, 2) )
# [ 0  2  4  6  8 10 12 14 16 18]

# Create an array of five values evenly spaced between 0 and 1
print( np.linspace(0, 1, 5) )
# [0.   0.25 0.5  0.75 1.  ]

# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
print( np.random.random((3, 3)) )
# [[0.48875261 0.64800978 0.5737449 ]
#  [0.63467357 0.0523844  0.86369289]
#  [0.78164747 0.91367994 0.33542108]]

# Create a 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
print( np.random.normal(0, 1, (3, 3)) )
# [[-0.96662849 -1.87427427  1.07784814]
#  [-2.14214626 -0.00357497  2.12838117]
#  [-0.53364134  0.78000148 -0.24624531]]

# Create a 3x3 array of random integers in the interval [0,10)
print( np.random.randint(0, 10, (3, 3)) )
# [[3 3 7]
#  [2 4 9]
#  [7 9 2]]

# Create a 3x3 identity matrix
print( np.eye(3) )
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# Create an uninitialized array of three integers
# The values will be whatever happens to already exist at that memory location
print( np.empty(3) )
# [1. 1. 1.]