'''
Hàm np.argmax và np.argmin được sử dụng để tìm chỉ số của giá trị lớn nhất và nhỏ nhất trong mảng.
Cú pháp:

np.argmax(array, axis)
np.argmin(array, axis)

- array: mảng đầu vào
- axis: Chiều thực hiện tìm kiếm

Để hiểu rõ hơn về cách sử dụng np.argmax và np.argmin, chúng ta sẽ tạo một mảng và tìm chỉ số của giá trị lớn nhất và nhỏ nhất trong mảng đó và tìm kiếm theo các chiều khác nhau.
'''
import numpy as np

# Tạo mảng 2 chiều
arr2d = np.array([1,2,3], [4,5,6])

# Tìm chỉ số của giá trị lớn nhất trong toàn bộ mảng
index_max2d = np.argmax(arr2d)
print("Chỉ số của giá trị lớn nhất trong mảng 2 chiều:", index_max2d)

# Tìm chỉ số của giá trị nhỏ nhất trong toàn bộ mảng
index_min2d = np.argmin(arr2d)
print("Chỉ số của giá trị nhỏ nhất trong mảng 2 chiều:", index_min2d)

# Tìm chỉ số 