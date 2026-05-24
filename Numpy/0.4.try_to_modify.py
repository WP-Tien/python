import numpy as np

# Try to modify an array's size (Error)

a = np.arange(9)
print(a)

del a[0]

#ValueError: cannot delete array elements