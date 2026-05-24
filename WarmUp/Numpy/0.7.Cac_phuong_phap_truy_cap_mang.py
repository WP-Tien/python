'''
Indexing trong NumPy cho phép ta truy cập vào từng phần tử của mảng bằng cách sử dụng chỉ số của nó. Để hiểu rõ hơn về cách sử dụng indexing, chúng ta sẽ thực hiện các ví dụ sau đây.

Ví dụ 1: Chúng ta sẽ tạo một mảng 1 chiều và truy cập vào phần tử đầu tiên và phần tử cuối cùng của mảng này.
'''
import numpy as np

# Tạo mảng 1 chiều
arr1d = np.array([1,2,3,4,5])

# Truy cập vào phần tử đầu tiên của arr1d
first_element = arr1d[0]
print("Phần tử đầu tiên của arr1d:", first_element)

# Truy cập vào phần tử cuối cùng của arr1d
last_element = arr1d[-1]
print("Phần tử cuối cùng của arr1d:", last_element)

'''
Phần tử đầu tiên của arr1d: 1
Phần tử cuối cùng của arr1d: 5
'''