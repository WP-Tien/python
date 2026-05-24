import numpy as np

x = np.arange(10)

print(x) # [0 1 2 3 4 5 6 7 8 9]

# first five elements
print(x[:5]) # [0 1 2 3 4]

# elements after index 5
print(x[5:]) # [5 6 7 8 9]

# middle sub-array
print(x[4:7]) # [4 5 6]

# every other element
print(x[::2]) # [0 2 4 6 8]

# every other element, starting at index 1
print(x[1::2]) # [1 3 5 7 9]

# all elements, reversed
print(x[::-1]) # [9 8 7 6 5 4 3 2 1 0]

# reversed every other from index 5
print(x[5::-2]) # [5 3 1]
