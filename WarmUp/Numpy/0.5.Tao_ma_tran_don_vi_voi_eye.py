'''
np.eye là một hàm dùng để tạo một ma trận đơn vị, trong đó các phần tử trên đường chéo chính là 1 và các phần tử còn lại là 0. Cú pháp:

- N: số hàng và số cột của ma trận (ma trận vuông)

Ví dụ sau sẽ tạo một ma trận đơn vị 3x3, với các phần tử trên đường chéo chính là 1 và các phần tử còn lại là 0
'''
import numpy as np

# Tạo ma trận đơn vị 3x3
eye_matrix = np.eye(3)
print(eye_matrix)

'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''