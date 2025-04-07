# Truy cập 1 nhóm các phần tử 1 lúc (luôn trả về 1 list)
# Cú pháp l[start:stop] hoặc l[start:stop:step]

# start: index phần tử đầu tiên (included)
# stop: index phần tử cuối cùng (excluded)
# step: bước nhảy, mặc định là 1

# Khởi tạo lại list
l = [1,2,3,4,5]
print(l)

# Slice từ đầu đến phần tử thứ 3
# print(l[0:3])
print(l[:3])

# Slice từ phần tử thứ 3 đến cuối
print(l[2:])

# Slice từ phần tử thứ 2 đến thứ 4
print(l[1:4])

# Slice từ đầu đến cuối (trả về 1 shallow copy)
print(l[:])

# Slice từ đầu đến cuối, nhảy 2 bước
print(l[::2])

# Slice đảo ngược lại list
print(l[::-1])

# Slice phần tử 2 đến 4, và thay nó bằng [99, 100]
l[1:3] = [99, 100]
print(l)

# Slice lấy n phần tử cuối cùng
print(l[-1::])
