# 1. Tạo tuple (Create)
t = (1, 2, 3)

# Không cần ngoặc:
t2 = 1, 2, 3

# Tuple 1 phần tử:
t3 = (5,)

print(t) # (1, 2, 3)
print(t2) # (1, 2, 3)
print(t3) # (5,)

# 2. Truy cập phần tử (Indexing)
t4 = (10, 20, 30, 40)

print(t4[0]) # 10
print(t4[1]) # 20
print(t4[-1]) # 40

# 3. Cắt tuple (Slicing)
t5 = (10, 20, 30, 40, 50)

print(t5[1:4]) # (20, 30, 40)
print(t5[:3]) # (10, 20, 30)
print(t5[2:]) # (30, 40, 50)
# Bước nhảy
print(t5[::2]) # (10, 30, 50)

# 4. Nối tuple (Concatenation)
t6 = (1, 2, 3)
t7 = (4, 5)

t8 = t6 + t7
print(t8) # (1, 2, 3, 4, 5)

# 5. Lặp tuple (Repetition)
t9 = (1, 2)
print(t9 * 3) # (1, 2, 1, 2, 1, 2)

# 6. Kiểm tra phần tử
t10 = (10, 20, 30)

print(20 in t10) # True
print(50 not in t10) # True

# 7. Duyệt tuple (loop)
# for loop
t11 = (10, 20, 30)

for x in t11:
    print(x) # 10 20 30
    
# Dùng index
for i in range(len(t11)):
    print(t11[i]) # 10 20 30
    
# 8. Độ dài tuple
t12 = (1, 2, 3, 4)

print(len(t12)) # 4

# 9. Đếm phần tử
t13 = (1, 2, 3, 4, 2)

print(t13.count(2)) # 2

# 10. Tìm vị trí phần tử
t14 = (10, 20, 30)

print(t14.index(20)) # 1

# 11. Unpacking tuple
t15 = (10, 20, 30)

a, b, c = t15

print(a)
print(b)
print(c)

# 12. Unpacking nâng cao
t16 = (1, 2, 3, 4, 5)

a, *b, c = t16

print(a) # 1
print(b) # 2 3 4
print(c) # 5

# 13. Tuple lồng nhau (Nested Tuple)
t17 = ((1, 2), (3, 4), (5, 6))

print(t17[0]) # (1, 2)
print(t17[1][1]) # 4