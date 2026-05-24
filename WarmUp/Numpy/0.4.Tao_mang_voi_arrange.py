'''
np.arange là một hàm dùng để tạo một mảng chứa các số nguyên liên tiếp trong một khoảng xác định.
Cú pháp:

np.arange(start,stop,step)

- start: Giá trị bắt đầu của dãy số(giá trị này bao gồm trong mảng được tạo)
- stop: Giá trị kết thúc của dãy số(giá trị này không bao gồm trong mảng được tạo)
- step: Khoảng cách giữa các giá trị trong dãy số (mặc định là 1)

Ví dụ dưới đây sẽ tạo một mảng chứa các số nguyên từ 0 đến 9
'''
import numpy as np

# Tạo mảng chứa các số nguyên từ 0 đến 9
arange_array = np.arange(0, 10)
print(arange_array) # [0 1 2 3 4 5 6 7 8 9]