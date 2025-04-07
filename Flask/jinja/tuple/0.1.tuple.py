# Tương tự như kiểu dữ liệu List tuy nhiên lại có một sự khác biệt với kiểu List đó là các phần tử trong Tuple không thể bị thay đổi sau khi gán chính vì vậy tốc độ của Tuple luoonm luôn nhanh hơn so với List, Tuple chứa một tập các giá trị, được phân tách nhau bằng dấu phẩy, có thể chứa bất kỳ kiểu dữ liệu nào. Một tuple được tạo bởi cặp dấu () như sau:

tup = ( 2, "ABC", 7, 3, [4, 3, 7], True, 3 )

# Không thể thay đổi một phần tử của Tuple:
# tup[1] = 100

# Không thể xoá phần tử trong Tuple:
# del tup[1]

# Đếm số lần xuất hiện của một phần tử trong Tuple:
# print( tup.count(3) ) 

# Lấy ra vị trí index đầu tiên tìm được:
# print( tup.index(3) )