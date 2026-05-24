'''
Aliasing (tham chiếu cùng một danh sách)
Gán một list cho biến khác chỉ tạo tham chiếu, không tạo bản sao 
'''

list1 = [1,2,3]
list2 = list1 # list2 tham chiếu đến list1
list2[0] = 10 # list1 cũng thay đổi: [10, 2, 3]