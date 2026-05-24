'''
Slicing trong NumPy cho phép ta trích xuất một phần của mảng bằng cách chỉ định khoảng chỉ mục.
Để hiểu rõ hơn về cách sử dụng slicing, chúng ta sẽ thực hiện các ví dụ sau đây.
Ví dụ 1: Chúng ta sẽ tạo một mảng 1 chiều và lấy ra một phần của mảng này bao gồm các phần tử từ chỉ số thứ nhất đến chỉ số thứ 3.
'''
import numpy as np

# Tạo mảng 1 chiều
arr1d = np.array([1,2,3,4,5])

# Lấy ra một phần của arr1d từ chỉ số thứ nhất đến chỉ số thứ 3
slice_arr1d = arr1d[1:4]
print("arr1d:", arr1d)
print("Slicing arr1d từ chỉ số 1 đến 3:", slice_arr1d)