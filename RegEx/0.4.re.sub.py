import re

txt = "The rain is pain"
x = re.sub("\s", "9", txt)

print(x)

'''
    Tìm khoảng trắng trong chuỗi txt nếu:
    - Tìm thấy thì thay thế khoảng trắng bằng số 9
    - và chỉ thay thế HAI(2) lần

    => KÊT QUẢ: "the9rain9in pain"
    Trong chuỗi hiện tại có 3 dấu khoảng trắng nhưng CHỈ THAY 2 khoảng trắng đầu tìm được
    
'''

text = "The rain in pain"
x = re.sub("\s", "9", txt, 2)

if x:
    print("Chuoi da THAY THE")
    print(x)
else:
    print("KHONG tim thay!")
    print(x)
