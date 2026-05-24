# 1. Tạo dictionary

# Cách 1
student = {
    "name": "An",
    "age": 20,
    "score": 8.5
}
print(student)

# Cách 2
student = dict(name="An", age=20, score=8.5)
print(student)

# 2. Truy cập giá trị
print(student["name"]) # An
print(student.get("age")) # 20

# get() an toàn hơn vì không gây lỗi nếu key không tồn tại:
print(student.get("height", "không có")) # in ra không có

# 3. Thêm và cập nhật phần tử
student["gender"] = "Male" # thêm mới
student["age"] = 21 # cập nhật
print(student)

# 4. Xoá phần tử
# student.pop("score") # xoá theo key
# del student["gender"] # xoá theo key
# student.clear() # xoá toàn bộ
# print(student)

# 5. Duyệt Dictionary
# Duyệt key
for key in student:
    print(key)
    
# Duyệt value
for value in student.values():
    print(value)
    
# Duyệt cả key và value
for key, value in student.items():
    print(key, value)
    
# 6. Một số phương thức hay dùng
student.keys() # danh sách key
student.values() # danh sách value
student.items() # danh sách (key, value)
student.update({"age": 22, "city": "Hanoi"})

print(student)

# 7. Ví dụ thực tế
scores = {
    "math": 9,
    "english": 8,
    "physics": 7
}

avg = sum(scores.values()) / len(scores)
print(avg)