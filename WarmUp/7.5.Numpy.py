# Lặp data với repeat() và tile()
import numpy as np

data = np.array([1, 2])
print(data)

# repeat each element three times
out1 = np.repeat(data, 3)
print(out1)

# repeat data three times
out2 = np.tile(data, 3)
print(out2)