'''
# Tìm kiếm phần tử với điều kiện - where()

Hàm np.where được sử dụng để tìm vị trí của các phần tử trong mảng thoả mãn một điều kiện nhất định. Cú pháp:

np.where(condition)

- condition: Là một mảng boolean hoặc biểu thức trả về mảng boolean.

Để hiểu rõ hơn về cách sử dụng np.where, chúng ta sẽ tạo mảng và tìm các vị trí của phần tử lớn hơn 2 và in ra giá trị các phần tử đó.
'''
import numpy as np

# Tạo mảng
arr = np.array([1,2,3,4,5])

# Tìm vị trí của các phần tử lớn hơn 2
result = np.where(arr > 2)
print("Vị trí của các phần tử lớn hơn 2:", result)
print("Giá trị các phần tử tại vị trí tìm được:", arr[result])

'''
Vị trí của các phần tử lớn hơn 2: (array([2, 3, 4]),)
Giá trị các phần tử tại vị trí tìm được: [3 4 5]
'''