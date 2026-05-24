import numpy as np

data1 = np.arange(10).reshape(2, -1)
print(data1)

data2 = np.repeat(7, 10).reshape(2, -1)
print(data2)

# Way 1
out1 = np.concatenate([data1, data2], axis=1)
print(out1)

# Way 2
out2 = np.hstack([data1, data2])
print(out2)

# Way 3
out3 = np.c_[data1, data2]
print(out3)