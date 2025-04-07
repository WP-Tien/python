'''
    df = df.query(<Điều kiện trích chọn>)

    1. Từ ví dụ trên, hãy hiển thị ra danh sách sinh viên ở Hà Nội
    2. Từ ví dụ trên, hãy hiển thị ra danh sách những sinh viên thộc lớp A1 hoặc A2
'''

import pandas as pd

df = pd.read_csv("sinhvien.txt", sep=",", header=None, names=["Ma", "Ten", "Lop", "QueQuan"])

# df1 = df.query( 'QueQuan == " Ha Noi" and Lop == " A1"' )
# df1 = df.query( 'QueQuan == " Thai Nguyen" or QueQuan == " Nam Dinh"' )

qq = [ " Thai Nguyen", " Nam Dinh" ]

df1 = df.query( 'QueQuan in @qq' )

print( df1 )