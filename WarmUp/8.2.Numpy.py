import numpy as np

# create a 2x3 matrix (from 5 to 10)
data1 = np.random.uniform(5, 10, size=(2,3))
print(data1, '\n')

# create a 2x3 matrix (from 0 to 1)
data2 = np.random.random([2,3])
print(data2)

'''
[[8.71565412 8.45677775 6.65477799]
 [6.1928787  7.80037949 6.07568143]] 

[[0.53198875 0.45163988 0.76647571]
 [0.10734711 0.74334116 0.11629112]]
'''