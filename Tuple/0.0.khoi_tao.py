'''
    Trong python, tuple là một kiểu dữ liệu dùng để lưu nhiều giá trị trong một biến,
    giống như list nhưng không thể thay đổi (immutable) sau khi tạo.
'''

# 1. Khởi tạo
my_tuple = (1,2,3,4)
print(my_tuple)

# 2. Tuple với nhiều kiểu dữ liệu
info = ("An", 25, 1.75, True)
print(info)

# 3. Tuple một phần tử
# Phải có dấu ,
single = (5,)
print(single)
# Nếu viết
single2 = (5)
print(single2) # 5
# Thì đó chỉ là int, không phải tuple

# 4. Tạo tuple không cần ngoặc
# Python vẫn hiểu
numbers = 1, 2, 3, 4
print(numbers)

# 5. Tạo tuple bằng tuple()
# Chuyển từ list hoặc iterable:
numbers = tuple([1, 2, 3])
print(numbers) # (1, 2, 3)

# 6. Truy cập phần tử tuple
t = (10, 20, 30)
print(t[0]) # 10