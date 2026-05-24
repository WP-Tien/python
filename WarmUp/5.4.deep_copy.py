'''
Tạo một bản sao sâu: trong đó toàn bộ danh sách và các phần tử bên trong đều được sao chép thành các đối tượng độc lập
'''

import copy

original_list = [[1,2,3], [4,5,6]]
deep_copy = copy.deepcopy(original_list)

deep_copy[0][0] = 100

print("Original List:", original_list)
print("Deep Copy:", deep_copy)

'''
Original List: [[1, 2, 3], [4, 5, 6]]
Deep Copy: [[100, 2, 3], [4, 5, 6]]
'''