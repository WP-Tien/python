import numpy as np

x = np.array([1,2,3,4])
y = np.array([5,6,7,8])

print('data x \n', x)
print('data y \n', y)

# Hadamard product between the two vectors
print('x * y = \n', x*y)

# Division between the two vectors
print('x / y = \n', x/y)

'''
data x 
 [1 2 3 4]
data y 
 [5 6 7 8]
x * y = 
 [ 5 12 21 32]
x / y = 
 [0.2        0.33333333 0.42857143 0.5       ]
'''