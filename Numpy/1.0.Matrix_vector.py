import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])

print(x)
print(y)

# Inner product of vectors; both produce(kết quả) 219
# note: echo $((120 + 99))
# (9 * 11) + (10 * 12)
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]
# (1 * 9) + (2 * 10)
# (3 * 9) + (4 * 10)
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22] 
# [43 50]]
# Giải thích:
# Phần tử (0, 0) - hàng 1 cột 1
# 1x5 + 2x7 = 19
# Phần tử (0, 1) - hàng 1 cột 2
# 1x6 + 2x8 = 22
# Phần tử (1, 0) - hàng 2 cột 1
# 3x5 + 4x7 = 43
# Phần tử (1,1) - hàng 2 cột 2
# 3x6 + 4x8 = 50
print(x.dot(y))
print(np.dot(x, y))