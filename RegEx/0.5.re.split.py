import re

txt = "The pain in rain"
x = re.split("\s", txt)
print(x) # ['The', 'pain', 'in', 'rain'] # list

'''
    Tìm khoảng trắng trong chuỗi txt nếu
    - Tìm thấy thì TÁCH chuỗi
    - và chỉ tách HAI(2) lần
    
    => KẾT QUẢ: ['The', 'pain', 'in rain'].
    Trong chuỗi hiện tại có 3 đấu khoảng trắng nhưng TÁCH 2 khoảng trắng đầu tiên tìm được
'''

x2 = re.split("\s", txt, 2)

if x2:
    print("Chuoi da TACH!")
    print(x2)
else:
    print("Khong tim thay!")
    print(x2)