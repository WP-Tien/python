# Khởi tạo list
l = [1, 2, 3, 4, 5]
print(l)

# Đếm số lượng phần tử
print( len(l) )

# Kiểm tra xem một giá trị nào đó có trong list hay không
print(l)
print(1 in l)
print(99 in l)

# Nối 2 list thành 1 list
l2 = [1, -3, 8]

print(l + l2)

# Tạo một list mới bằng cách replicate phần tử của list có sẵn
l = [1, 2]
l2 = l * 3

print(l)
print(l2)

# Sắp xếp 1 list (nếu được)
print(l2)
print(sorted(l2))
print(sorted(l2, reverse=True))

# Unpack list
l = [2020, 1, 25]
y, m, d = l

print(y)
print(d)
print(m)

# Unpack list (3)
l = [2020, 1, 25]
y, *_ = l

print(y)
print(_)

# Tìm phần tử nhỏ nhất
l = [10, 11, 14, 6, 8]
print( sorted(l)[0] )