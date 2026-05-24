'''
Tạo một bản sao nông: danh sách cha được sao chép, nhưng các phần tử bên trong vẫn tham chiếu đến cùng một đối tượng.
'''

original_list = [[1,2,3], [4,5,6]]
shallow_copy = original_list.copy()

# Thay đổi một phần tử trong danh sách con
shallow_copy[0][0] = 100

print("Original List:", original_list)
print("Shallow  Copy:", shallow_copy)

# Output
# Original List: [[100,2,3], [4,5,6]]
# Shallow Copy: [[100,2,3], [4,5,6]]