# Khác với 3 kiểu dữ liệu ở trên Dict lưu trữ các phần tử theo dạng {key: value}, các key phải có giá trị khác nhau và Python chỉ chấp nhận các key có các kiểu dữ liệu như (string, number, tuple): Một Dict được tạo bởi cặp dấu {} và mỗi phàn tử là một cặp key:value như sau:

# Dictionaries store connections between pieces of information. Each item in a dictionary is a key-value pair.
# Dictionary = a collection of {key:value} pairs
#               ordered and changeable. No duplicates 

# customer = {
#     "name": "Vincent Nguyen",
#     "age": 29,
#     "is_verified": True
# }

# print(customer["name"])

dict_a = {
    1: "MySQL", 
    2: "SQLServer", 
    3: "SQLite"
}

dict_b = {
    "a": "MySQL", 
    "b": "SQLServer", 
    (2, 3, 7): "SQLite"
}

# Các thao tác cơ bản với Dict:
# Lấy các keys của Dict:
print( dict_a.keys() )

# Lấy các values của Dict:
print( dict_a.values() )

# Lấy các items của Dict
print( dict_a.items() )

# Truy cập bằng key
print( dict_a[2] )

# Thêm một phần tử vào Dict:
dict_a[100] = "MongoDB"

# Xoá một phần tử:
dict_a.pop(3)
print( dict_a )