'''
    Cho list giá trị đơn hàng trong ngày: [100, 150, 80, 160, 250]
    Sử dụng vòng lặp for phân loại list trên thành 3 list: <100, 100-200, >=200
'''

l = [100, 150, 80, 160, 250]
l1 = []
l2 = []
l3 = []

for i in l:
    if i < 100:
        l1.append(i)
    elif i >= 200:
        l2.append(i)
    else:
        l3.append(i)
        
print(l1) # [80]
print(l2) # [250]
print(l3) # [100, 150, 160]


'''
    Cho dict tên khách hàng ứng với số điện thoại: {'Ngọc': 0707768350, 'Tiến': 123456789, 'Tài': 987654321}
    Dùng comprehension tạo một list gồm 6 số cuối sđt các khách hàng
'''
test_dict = {'Ngọc': 707768350, 'Tiến': 123456789, 'Tài': 987654321}
res = [str(k)[-6:] for k in test_dict.values()]
print(res) # ['768350', '456789', '654321']

'''
    Thiết kế hàm tính lợi nhuận của đơn hàng
    Đầu vào là dict: {'G12': 500, 'M15': 200, 'C20': 10000000}
    Kết quả trả ra là dict: {'G12': ____, 'M15': ____, 'C20': ____}
    Biết chi phí ứng với từng dòng sản phẩm như sau: G -> 20%, M -> 30%, C -> 35%
'''

d1 = {'G12': 500, 'M15': 200, 'C20': 200000}
d2 = {}

for key, value in d1.items():
    if str(key).startswith('G'):
        d3 = {'G12': int(value)*.8}
    elif str(key).startswith('M'):
        d4 = {'M15': int(value)*.7}
    else:
        d5 = {'C20': int(value)*.35}
        
d2.update(d3)
d2.update(d4)
d2.update(d5)

print(d2)
'''
{'G12': 400.0, 'M15': 140.0, 'C20': 70000.0}
'''
