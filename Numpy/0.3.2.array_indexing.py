import numpy as np

l = [5, 0, 3, 3, 7, 9]

x1 = np.array(l)

print(x1) # [5 0 3 3 7 9]

print(x1[0]) # 5

print(x1[4]) # 7

# To index from the end of the array, you can use negative indices:

print(x1[-1]) # 9

print(x1[-2]) # 7

l2 = [1, 2, 3, 5, 8, 1]

x2 = np.array((l, l2))

print(x2)
'''
[[5 0 3 3 7 9]
 [1 2 3 5 8 1]]
'''

print(x2[0, 0]) # 5

print(x2[1, 0]) # 1, hàng 1 cột 0

print(x2[1, -1]) # 1 hàng 1 cột cuối

# Values can also be modified using array of the above index notaion:

x2[0, 0] = 99

print( x2 )