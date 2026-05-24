'''
Chúng ta sẽ tạo một mảng 2 chiều và truy cập vào một phần tử cụ thể ở hàng thứ nhất và cột thứ hai của mảng
'''
import numpy as np

# Tạo mảng 2 chiều
arr2d = np.array([[1,2,3], [4,5,6]])
print(arr2d)

# Truy cập vào phần tử ở hàng thứ nhất và cột thứ hai của arr2d
element_1_2 = arr2d[0, 1]
print("Phần tử ở hàng thứ nhất và cột thứ hai của arr2d:", element_1_2) # 2