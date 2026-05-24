'''
    https://viblo.asia/p/gioi-thieu-ve-numpy-mot-thu-vien-chu-yeu-phuc-vu-cho-khoa-hoc-may-tinh-cua-python-maGK7kz9Kj2

    Một mảng numpy là một lưới các giá trị, và tất cả các giá trị có dùng kiểu giá trị, và được lập chỉ mục bởi một số nguyên không âm, số chiều được gọi là rank của mảng Numpy, và shape là một tuple các số nguyên đưa ra kích thước của mảng theo mỗi chiều.
'''
import numpy as np

a = np.array([1,2,3]) # Tạo một numpy array với rank = 1

print(type(a))
print(a.shape)
print(a[0], a[1], a[2])
a[0] = 5
print(a)

b = np.array([[1,2,3], [4,5,6]]) # Tạo một numpy array với rank = 2
print(b.shape)

'''
    Vài loại thao tác mảng dưới đây:
    . Atrribute of arrays: Determining(xác định) the size, shape, memory consumption(tiêu thụ), and data types of arrays
    . Indexing of arrays: Getting and setting the value of individual( riêng lẻ ) array elements
    . Slicing of arrays: Getting and setting smaller subarrays within a larger array
    . Reshaping of arrays: Changing the shape of a given array
    . Joining and Splitting of arrays: Combining multiple arrays into one, and splitting one array into many
'''