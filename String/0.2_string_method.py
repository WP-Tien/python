# String methods
'''
Đếm số phần tử
Kiểm tra membership
Concatenate
Xoá phần tử
Sắp xếp các phần tử
'''

# Khởi tạo một string
s = "Python is Fun."
print(s) # Python is Fun.

print(s.upper()) # PYTHON IS FUN.
print(s.lower()) # python is fun.
print(s.capitalize()) # Python is fun.
print(s.title()) # Python Is Fun.
print(s.swapcase()) # pYTHON IS fUN.

# Kiểm tra có phải các ký tự đều là lowercase
# tương tự cho upper, title, capitalize
print("hello".islower()) # True
print("Hello".islower()) # False

# Kiểm tra substring
print(s.startswith("Py")) # True
print(s.startswith("py")) # False

print(s.endswith("Un.")) # False
print(s.endswith("fUn")) # False

print("ython" in s) # True
print("PYTHON" in s) # False

# Tìm kiếm trong string
# - Dùng method .find() hoặc .rfind() Nếu không tìm thấy, return -1
# - Ngoài ra có thể dùng .index() hoặc .rindex() . Hai hàm này tương tự .find / .rfind(), khác ở điểm nếu không tìm thấy sẽ raise ValueError thay vì return -1

# Tìm index của substring đầu tiên (từ trái qua phải)
print(s.find("n")) # 5
print(s.find("X")) # -1

# Tìm index của substring đầu tiên (từ phải qua trái)
print(s.rfind("n")) # 12
print(s.find("l")) # -1
print(s.rfind("l")) # -1

# Phương thức với khoảng trắng
s = """
\t\t
    \t
"""

print(s)
print(s.isspace())

# Bỏ khoảng trắng thừa
s = "   Hello World    "
print(s)
print(len(s))

s1 = s.lstrip()
print(s1)
print(len(s1))

s1 = s.rstrip()
print(s1)
print(len(s1))

s1 = s.strip()
print(s1)
print(len(s1))