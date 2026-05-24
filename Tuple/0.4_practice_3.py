# 1. Các hàm built-in dùng với typle
# min
t = (4, 2, 8, 1)
print(min(t)) # 1

# max
print(max(t)) # 8

# sum
print(sum(t)) # 15

# sorted
t2 = (5, 2, 9, 1)
print(sorted(t2)) # [1, 2, 5, 9]

# 2. Chuyển đổi tuple
# tuple -> list
t3 = (1, 2, 3)

l = list(t3)
print(l) # [1, 2, 3]

# list -> tuple
t = tuple(l)
print(t) # (1, 2, 3)

# 3. So sánh tuple
t4 = (1, 2, 3)
t5 = (1, 2, 4)

print(t4 < t5) # True
# So sánh từng phần tử từ trái qua phải