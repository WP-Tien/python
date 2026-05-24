'''
Chúng ta sẽ tạo một mảng 2 chiều và lấy ra một phần của mảng này từ hàng thứ 2 đến hàng thứ 3 và từ cột thứ 2 đến cột cuối cùng
'''
import numpy as np

# Tạo mảng 2 chiều
arr2d = np.array([[1,2,3], [4,5,6], [7,8,9]])

# Lấy ra một phần của arr2d từ hàng thứ 2 đến hàng thứ 3 và từ cột thứ 2 đến cột cuối cùng
slice_arr2d = arr2d[1:3, 1:]
print("arr2d: \n", arr2d)
print("Slicing arr2d từ hàng 2 đến 3 và cột 2 đến cuối cùng: \n", slice_arr2d)

'''
[[5 6]
[8 9]]
'''