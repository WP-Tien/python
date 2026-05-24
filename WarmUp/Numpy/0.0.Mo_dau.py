'''
Numpy là một thư viện mã nguồn mở trong Python được sử dụng để làm việc với mảng (array)-cấu trúc dữ liệu chính của numpy và cho phép thực hiện các thao tác toán học nhanh chóng và hiệu quả.
Để bắt đầu sử dụng Numpy, chúng ta cần phải cài đặt thư viện này trong môi trường Python qua cú pháp

pip install numpy

Sau khi cài đặt xong, bạn có thể kiểm tra xem NumPy đã được cài đặt thành công hay chưa bằng cách mở Python interpreter (hoặc Jupyter Notebook) và nhập:

import numpy as np
print(np.__version__)

'''

# Các phương pháp tạo mảng
# Tạo mảng từ dữ liệu có sẵn
# np.array là một hàm trong NumPy dùng để tạo mảng (array) từ dữ liệu có sẵn như list hoặc tuple. Cú pháp
# np.array(object)
# - object: Dữ liệu đầu vào (list, tuple, hoặc các kiểu dữ liệu khác)

# Ví dụ sau sẽ tạo mảng NumPy từ một list gồm các số nguyên [1,2,3,4,5].
import numpy as np
# Tạo mảng từ list
list_data = [1,2,3,4,5]
array_from_list = np.array(list_data)
print(array_from_list)
# [1 2 3 4 5]
'''
Chúng ta có thể kiểm tra các thuộc tính cơ bản của mảng qua các phương thức sau:
- Shape: kích thước của mảng, tức là số phần tử trong mỗi chiều của chúng
- dtype: kiểu dữ liệu của các phần tử trong mảng
- size: số lượng phần tử trong mảng
- ndim: số chiều của mảng
'''

# Ví dụ chương trình dưới đây sẽ kiểm tra các thuộc tính của một mảng
arr = np.array([1,2,3,4,5])
print("arr:", arr)
print("Shape of arr:", arr.shape)
print("Size of arr:", arr.size)
print("Data type of arr:", arr.dtype)
print("Number of dimensions of arr:", arr.ndim)

'''
arr: [1 2 3 4 5]
Shape of arr: (5,)
Size of arr: 5
Data type of arr: int64
Number of dimensions of arr: 1
'''