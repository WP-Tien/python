''' 
Tương tự như 2 kiểu dữ liệu chúng ta đã tìm hiểu ở trên tuy nhiên Set lại chứa các phần tử là DUY NHẤT có nghĩa là các phần tử không bị lặp lại trong một tập hợp Set, Set chứa một tập các giá trị, được phân tách nhau bằng dấu phẩy, có thể sử dụng được các phép toán trên tập hợp, các phần tử trong Set không có thứ tự. Một tập hợp Set được tạo bởi cặp dấu {} như sau:
'''
# Set = {} unordered and immutable (không thể thay đổi), but Add/Remove OK. No duplicates

st_a = { 2, 7, 3, 2, 5 }
st_b = { 2, 3, 5, 99 }

print( st_a )
print( type(st_a) )

# Các thao tác cơ bản với Set:
# Thêm một phần tử vào Set:
st_a.add(100)
print( st_a )

# Xoá một phần tử bằng pop:
st_a.pop()
print( st_a )

# Phép &h lấy giao của A và B
print( st_a & st_b )

# Phép | lấy hợp của A và B
print( st_a | st_b )

# Phép - lấy các giá trị chỉ có ở A không có ở B
print( st_a - st_b )

# Phép ^ bù của A và B chỉ lấy những phần tử có ở A và B nhưng không phải phần tử chung của hai tập hợp này
print( st_a ^ st_b )