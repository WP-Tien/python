import re

'''
    Định nghĩa chuỗi mẫu có:
    - chiều dài là 5
    - ký tự đầu tiên là a
    - 3 ký tự giữa là: các ký tự bất kỳ
    - ký tự cuối cùng là z
'''

pattern = '^a.*z$'

test_in = 'anh oi xyz'
result = re.match(pattern, test_in)

if result:
    print("Da tim thay chuoi.")
    print(result)
else:
    print("Chuoi nhap vao khong co trong chuoi.")
    
