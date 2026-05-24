"""
   Bài tập 01: Viết chương trình để chuyển đổi nhiệt độ từ 30 độ C sang độ F,
   Biêt công thức chuyển đổi C sang F là: độ F = độ C nhân với 9/5, sau đó cộng với 32 
"""
# gọi thư viện math
import math

# nhập số liệu nhiệt độ (C)
t = float(input("nhập nhiệt độ (C):"))
# đỗi nhiệt độ C sang độ F
f = (t*9/5)+32
# in ra màn hình kết quả
print("Độ F tương ứng là:", float(f))