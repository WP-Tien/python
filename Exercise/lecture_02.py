"""
    Bài tập 02: Viết chương trình tính diện tích tam giác có các cạnh cho trước sử dụng công thức Heron
            S = math.sqrt(p(p-a)(p-b)(p-c))
        Với p là nửa chu vi tam giác p = (a+b+c)/2
"""

#gọi thư viện math
import math

a = float(input("Nhập cạnh a:"))
b = float(input("Nhập cạnh b:"))
c = float(input("Nhập cạnh c:"))

p = (a+b+c)/2

s = math.sqrt(p*(p-a)*(p-b)*(p-c))

print(s)

print("Diện tích của tam giác là:", round(s,2))