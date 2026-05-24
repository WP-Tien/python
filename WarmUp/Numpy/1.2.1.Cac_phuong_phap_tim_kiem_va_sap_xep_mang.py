'''
# Tìm giá trị lớn nhất và nhỏ nhất

Hàm np.max và np.min được sử dụng để tìm giá trị lớn nhất và nhỏ nhất trong mảng. Cú pháp:

np.max(array, axis)
np.min(array, axis)

Để hiểu rõ hơn về cách sử dụng np.max và np.min, chúng ta sẽ tạo mảng và tìm giá trị lớn nhất và nhỏ nhất trong mảng đó.
'''
import numpy as np

# Tạo mảng
arr = np.array([1,2,3,4,5])

# Tìm giá trị lớn nhất
max_value = np.max(arr)
print("Giá trị lớn nhất trong mảng:", max_value)

# Tìm giá trị nhỏ nhất
min_value = np.min(arr)
print("Giá trị nhỏ nhất trong mảng:", min_value)
