'''
    Trong Python, tuple có nhiều thao tác cơ bản để làm việc dữ liệu.
'''

# 1. Truy cập phần tử (Indexing)
t = (10, 20, 30, 40)

print(t[0]) # 10
print(t[2]) # 30
print(t[-1]) # 40 (Phần tử cuối)

# 2. Cắt tuple (Slicing)
t1 = (10, 20, 30, 40, 50)

print(t1[1:4]) # (20, 30, 40)
print(t1[:3]) # (10, 20, 30)
print(t1[2:]) # (30, 40, 50)

# 3. Nối tuple (Concatenation)
# Dùng toán tử +.
tt1 = (1, 2, 3)
tt2 = (4, 5)

tt3 = tt1 + tt2
print(tt3) # (1, 2, 3, 4, 5)

# 4. Lặp tuple (Repetition)
# Dùng toán tử *.
ttt = (1, 2)

print(ttt * 3) # (1, 2, 1, 2, 1, 2)

# 5. Kiểm tra phần tử (in/ not in)
t5 = (10, 20, 30)

print( 20 in t5 ) # True
print( 40 not in t5 ) # True

# 6. Duyệt tuple (Loop)
t6 = (10, 20, 30)

for i in t6:
    print(i)
'''
10 20 30
'''

# 7. Đếm phần tử (count)
t7 = (1, 2, 2, 3, 2)

print(t7.count(2)) # 3

# 8. Tìm vị trí (index)
t = (10, 20, 30)

print(t.index(20)) # 1

# 9. Unpacking tuple
# Tách tuple ra nhiều biến.
t9 = (10, 20, 30)

a, b, c = t9

print(a) # 10
print(b) # 20
print(c) # 30

# Tuple không thể thay đổi nên các thao tác như:
# t9[0] = 100 
# Sẽ bị lỗi