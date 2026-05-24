'''
np.random là một module trong NumPy cung cấp các hàm để tạo mảng với các gía trị ngẫu nhiên.
Trong phần này, các ví dụ về random sẽ sử dụng seed=2024 để đảm bảo kết quả đầu ra có thể tái tạo lại.

a) random.rand()
np.random.rand tạo một mảng với các giá trị ngẫu nhiên nằm trong khoảng từ 0 đến 1. Cú pháp:
np.random.rand(d0, d1, ..., dn)

- d0,d1, ..., dn: Kích thước mảng.

Ví dụ sau sẽ tạo một mảng NumPy 2x3 với các giá trị ngẫu nhiên từ 0 đến 1.
'''
import numpy as np

np.random.seed(2024) # Đặt seed = 2024 cho random generator

# Tạo mảng ngẫu nhiên từ 0 đến 1
rand_array = np.random.rand(2,3)
print(rand_array)

'''
[[0.58801452 0.69910875 0.18815196]
 [0.04380856 0.20501895 0.10606287]]
'''

'''
b) random.randint()
np.random.randint tạo một mảng với các giá trị ngẫu nhiên là số nguyên trong một khoảng xác định.
Cú pháp:
np.random.randint(low, high, size)

- low: Giá trị nhỏ nhất (bao gồm trong mảng đầu ra)
- high: Giá trị lớn nhất (không bao gồm trong mảng đầu ra)
- size: Kích thước của mảng

Ví dụ sau sẽ tạo một mảng 3x3 với các số nguyên ngẫu nhiên từ 1 đến 9
'''

randint_array = np.random.randint(1, 10, (3,3))
print(randint_array)

# Chạy lại nhiều lần → vẫn ra đúng mảng này
'''
[[4 3 1]
 [6 2 8]
 [8 7 3]]
'''