'''
List conprehension là cách tạo list ngắn gọn trong một dòng, thay thế cho vòng lặp for truyền thống
'''

# General form:
# new_list = [expression for item ibn iterable if condition]

# expression: Biểu thức áp dụng lên từng phần tử
# item: Phần tử từ iterable (list, tuple, range, v.v...)
# condition: Chỉ thêm phần tử khi điều kiện đúng (tuỳ chọn)

# Ví dụ:
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)