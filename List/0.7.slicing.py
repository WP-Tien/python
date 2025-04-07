List = [1,2,3,4,5,6,7,8,9]

print(List[3:9:2])
print(List[::2])
print(List[::])
print(List[::-1])
print(List[::-3])
print(List[:1:-2])

# in 3 phần tử cưới theo thứ tự giảm dần
print(List[-3:][::-1])

# Gán 2 phần tử cuối thành [1,2]
List[-2:] = [1,2]

print(List)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Truy xuất phần tử đầu tiên, phần tử cuối cùng, phần tử ở giữa
print( l[0], l[len(l)//2], l[-1] )