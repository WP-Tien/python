import numpy as np

X = np.array([[1,2], [3,4]])
v = np.array([1,2])

# Dot product between a matrix & a vector
print('X.dot(v)', X.dot(v))
print('v.dot(x)', v.dot(X))

'''
X.dot(v) [ 5 11]
v.dot(x) [ 7 10]

Giải thích:
X.dot(v) [ 5 11] Matrix x Vector
# (1*1) + (2*2) = 5
# (3*1) + (4*2) = 11

v.dot(x) [ 7 10] Vector x Matrix
# (1*1) + (2*3) = 7
# (1*2) + (2*4) = 10
'''

X1 = np.array([[1,2], [3,4]])
Y1 = np.array([[2,3], [2,1]])

# Dot product between the two matrices
print('X.dot(Y) \n', X1.dot(Y1))
'''
X.dot(Y) 
 [[ 6  5]
 [14 13]]
 
Giải thích:
Hàng 1 cột 1:
1x2 + 2x2 = 6
Hàng 1 cột 2:
1x3 + 2x1 = 5
Hàng 2 cột 1:
3x2 + 4x2 = 14
hàng 2 cột 2:
3x3 + 4x1 = 13
'''
print('Y.dot(X) \n', Y1.dot(X1)) 
'''
Y.dot(X) 
 [[11 16]
 [ 5  8]]
'''