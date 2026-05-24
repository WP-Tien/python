'''
Khi ta thực hiện phép toán softmax trên các số lớn, máy tính có thể không xử lý được và gặp vấn đề overlfow. Ngược lại khi ta thực hiện phép toán softmax trên các số quá nhỏ, ta lại đối mặt với vấn đề underflow.

Overflow và Underflow khi tính Softmax
Khi áp dụng Softmax cho các giá trị rất lớn hoặc rất nhỏ, ta gặp vấn để overflow hoặc underflow.
'''
import math


############ Overflow khi sử dụng softmax ############
# # Given three values
# v1 = 1001.0
# v2 = 1002.0
# v3 = 1003.0

# # Compute softmax
# total = math.exp(v1) + math.exp(v2) + math.exp(v3)

# s1 = math.exp(v1)/total
# s2 = math.exp(v2)/total
# s3 = math.exp(v3)/total

# # Print out
# print(f"{s1:.5f} {s2:.5f} {s3:.5f}") # OverflowError: math range error

############ Underflow khi sử dụng softmax ############
# Given three values
v1 = -801.0
v2 = -805.0
v3 = -800.0

# Compute softmax
total = math.exp(v1) + math.exp(v2) + math.exp(v3)

s1 = math.exp(v1)/total
s2 = math.exp(v2)/total
s3 = math.exp(v3)/total

# Print out
print(f"{s1:.5f} {s2:.5f} {s3:.5f}") # ZeroDivisionError: float division by zero