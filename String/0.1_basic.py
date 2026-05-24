# Khởi tạo
s = 'Hello'

print(s)
print(type(s))

'''
Hello
<class 'str'>
'''

# Các thao tác với str
# - Các thao tác với str cũng tương tự như với tuple, ngoại trừ việc indexing tương đồng với slicing 1 phần tử.
# VD1: Imdex, slice. concate, replicate

s = "Hello World!"

# Index thứ tự đầu và cuối
print(s[0]) # H
print(s[-1]) # !

# Slice 4 ký tự đầu và 4 ký tự cuối
print(s[:3]) # Hel
print(s[-4:]) # rld!

# Slice đảo ngược string
s = "Hello"
print(s[::-1]) # olleH

# Nối 2 string
s1 = "Hello"
s2 = " World"

print( s1 + s2 )

# Replicate một string
s = "Hello"
print( s * 3 )

# Đếm số ký tự
print(len(s)) # 5

# Đếm số lần xuất hiện của ký tự
print(s.count('l')) # 2

# Sắp xếp
print(sorted(s)) # ['H', 'e', 'l', 'l', 'o']
