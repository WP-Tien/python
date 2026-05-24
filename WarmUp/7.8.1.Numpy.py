import numpy as np

data1 = np.array([5,3,8,2,7])
data2 = np.array([2,7,3,1,8])

# Way 2: Using the maximum() function
out2 = np.maximum(data1, data2)
print(out2)

# Way 3: Using the where() function
out3 = np.where(data1>data2, data1, data2)
print(out3)