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