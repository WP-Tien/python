import numpy as np

'''
    Create a 1D array of numbers from 0 to 9
'''

import numpy as np

ar = np.arange(10)

print( ar )

'''
    Extract all odd number from arr
    Replace all odd numbers in arr with -1
'''

print( ar[ar % 2 != 0] )

ar[ar % 2 != 0 ] = -1
print( ar )

'''
    Convert a 1D array to a 2D array with 2 rows
'''
print( ar.reshape((2, 5)) )


'''
    Get the common items between a nad b using intersect1d
    a = np.array([1,2,3,2,3,4,5,6])
    b = np.array([7,2,10,2,3,4,9,8])
'''
a = np.array([1,2,3,2,3,4,5,6])
b = np.array([7,2,10,2,3,4,9,8])

print( np.intersect1d(a, b) )

'''
    From array a remove all items present in array b using setdiff1d
    a = np.array([1,2,3,4,5])
    b = np.array([5,6,7,8,9])
'''
a1 = np.array([1,2,3,4,5])
b1 = np.array([5,6,7,8,9])

print( np.setdiff1d(a1, b1) )

'''
    Get all items betwween 5 and 10 from a
    a = np.array([2, 6, 1, 9,10, 3, 27])
'''
a2 = np.array([2, 6, 1, 9,10, 3, 27])
print( a2[(a2>=5)&(a2<=10)] )

'''
    Swap columns 1 and 2 in the array arr
    arr = np.arange(9).reshape(3,3)
'''
arr = np.arange(9).reshape(3,3)
print( arr )
print( arr[:, [1,0,2]] )

'''
    Reverse the rows of a 2D array above
'''
print( arr[::-1] )

'''
    Compute the maximum for each row in the given array.
    a = np.random.randint(1, 10, [5,3])
'''
a = np.random.randint(1, 10, [5,3])

print( a )
print( np.max(a, axis=1) )