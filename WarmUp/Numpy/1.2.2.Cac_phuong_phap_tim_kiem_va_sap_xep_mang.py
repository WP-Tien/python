'''
Ngoài ra, chúng ta có thể tìm kiếm phần tử nhỏ nhất, lớn nhất theo từng chiều cụ thể đối với mảng nhiều chiều.
'''
import numpy as np

# Tạo mảng 2 chiều
arr2d = np.array([[1,2,3], [4,5,6]])

# Tìm giá trị lớn nhất theo từng chiều
max_value_row = np.max(arr2d, axis=1)
max_value_col = np.max(arr2d, axis=0)

print("Giá trị lớn nhất theo hàng trong mảng 2 chiều:", max_value_row)
print("Giá trị lớn nhất theo cột trong mảng 2 chiều:", max_value_col)

# Tìm giá trị nhỏ nhất theo từng chiều
min_value_row = np.max(arr2d, axis=1)
min_value_col = np.min(arr2d, axis=0)

print("Giá trị nhỏ nhất theo hàng trong mảng 2 chiều:", min_value_row)
print("Giá trị nhỏ nhất theo cột trong mảnh 2 chiều:", min_value_col)

'''
Giá trị lớn nhất theo hàng trong mảng 2 chiều: [3 6]
Giá trị lớn nhất theo cột trong mảng 2 chiều: [4 5 6]
Giá trị nhỏ nhất theo hàng trong mảng 2 chiều: [3 6]
Giá trị nhỏ nhất theo cột trong mảnh 2 chiều: [1 2 3]
'''