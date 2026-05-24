'''
Trong Python, lambda là cách viết hàm ẩn danh (anonymous function) — ngắn gọn, 
dùng khi hàm đơn giản và chỉ cần dùng một lần.

Cú pháp đơn giản

lamdba arguments: expression

- Không có tên hàm
- Chỉ có 1 biểu thức
- Tự động return kết quả
'''


# Ví dụ đơn giản
add = lambda a, b: a + b
print(add(2, 3)) # 5

# Tương đương với
def add1(a, b):
    return a + b

# Dùng với map
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums ))
print(squared) # 1, 4, 9, 16

# Dùng với filter
nums2 = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums2))
print(even) # [2, 4, 6]

# Dùng với sorted
students = [("An", 20), ("Binh", 18), ("Cuong", 22)]
sorted_students = sorted(students, key = lambda x:x[1])
print(sorted_students)