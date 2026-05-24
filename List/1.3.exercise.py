l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Truy xuất phần tử
'''
Truy xuất phần tử đầu tiên, phần tử cuối cùng, phần tử ở giữa
'''
print(l[0], l[len(l)//2], l[-1])

'''
Tạo một list rỗng và add các phần tử truy xuất ở trên vào list đó
'''

l1 = []
l1.append(l[0])
l1.append(l[len(l)//2])
l1.append(l[-1])

print(l1)


'''
Tính tổng (dùng hàm sum), trung bình (dùng hàm mean), giá trị nhỏ nhất (dùng hàm min) và lớn nhất (hàm max) của list ở trên
'''

import statistics
# import numpy as np
# np.mean()

tong = sum(l1)
tb = statistics.mean(l1)
nho = min(l1)
lon = max(l1)

print(tong, tb, nho, lon)

'''
Sort list l ban đầu theo thứ tự từ lớn đến nhỏ
'''

print(sorted(l1, reverse=True))

'''
Tạo một list gồm các giá trị sum, mean, min, max đã tính và add list này thành 1 phần tử trong list ban đầu
'''
l2 = [tong, tb, nho, lon]
l.append(l2)

print(l)


'''
Truy xuất lấy phần tử gần cuối của list l ban đầu
'''

print(l[-2])

'''
Xoá phần tử cuối cùng, sau đó in ra phần tử vừa mới xoá của list l ban đầu
'''

value = l.pop()
print(value)

'''
Cho các list:
l2 = [1, 2, 3, 4]
l_chan = l_le = []
Kiểm tra nếu tổng 2 phần tử cuối của l2 là số chẵn thì add vào l_chan, ngược lại add vào l_le
'''

l3 = [1,2,3,4]
l_chan = []
l_le = []
if sum(l3[-2:])%2==0:
    l_chan.extend(l3)
else:
    l_le.extend(l3)
    
print(l_chan)
print(l_le)

