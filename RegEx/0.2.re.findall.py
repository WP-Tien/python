import re

"""
    Tìm "ai" trong chuỗi txt, tất cả các lần tìm thấy sẽ lưu vào biến x
    Trong trường hợp này sẽ là: ['ai', 'ai']
"""

txt = "The rain in pain"
x = re.findall("ai", txt)

if x:
    print("Da tim thay chuoi!")
    print(x)
else:
    print("KHONG tim thay!")
    print(x)
    
    
txt2 = '1.1.1.1 10.11.222.3 12/30-04:09:41.070967'

regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' # Định dạng IPv4
# regex = r"[a-fA-F0-9]{4}\.[a-fA-F0-9]{4}\.[a-fA-F0-9]{4}" # Định dạng địa chỉ MAC

'''
Hoặc
'''
# regex = r'\d{1,3}(?:\.\d{1,3}){3}'

IPs = re.findall(regex, txt2)
print( IPs )