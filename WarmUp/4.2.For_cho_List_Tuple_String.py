'''
    Đồi với các iterables như List, Tuple hay String, ta đều tuân theo cùng một quy tắc là vòng lặp sẽ bắt đầu với phần tử đầu của iterable và lập tức kết thúc ngay ở phần tử cưới của iterable đó, đảm bảo iterable sẽ trả về toàn bộ phần tử có trong nó
'''

# Tạo một danh sách điểm của học sinh và trả về từng điểm một
danh_sach_diem = [5,6,7]
print("Ứng dụng của For trong danh sách điểm:")

for diem in danh_sach_diem:
    print(f"Giá trị điểm hiện tại là: {diem}")
    
print("----------------------------------------------")
# Tạo một bộ các nguyên liệu cần thiết cho món bánh kem và liệt kê từng món một
nguyen_lieu_banh_kem = ("Bột mì", "Trứng gà", "Bơ lạt", "Sữa tươi")
print("Ứng dụng của For trong bộ nguyên liệu:")

for nguyen_lieu in nguyen_lieu_banh_kem:
    print(f"Nguyên liệu hiện tại là :{nguyen_lieu}")

print("----------------------------------------------")
# Đếm số lần chữ 'a' xuất hiện trong chuỗi "Hello AIVietNam"
chuoi = "AIVietNam"
print("Đếm số lần chữ 'a' xuất hiện trong chuỗi 'AIVietNam'")

dem=0
for ky_tu in chuoi:
    print(f"Ký tự hiện tại: {ky_tu}")
    if ky_tu.lower() == 'a':
        dem = dem + 1
        
print(f"Số lần chữ 'a' xuất hiện trong chuỗi là: {dem}")