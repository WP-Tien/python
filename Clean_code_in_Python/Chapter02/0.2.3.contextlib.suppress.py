'''
contextlib.suppress: bỏ qua exception có chủ đích

Đây là một utility context manager có sẵn

with contextlib.suppress(DataConversionException):
    parse_data(input_json_or_dict)
    
Tương đương với:
try:
    parse_data(input_json_or_dict)
except DataConversionException:
    pass
    
Nhưng tại sao suppress tốt hơn ?
- Rõ ý đồ hơn
- Code đọc vào là biết:
=> "Exception này là expected, không phải là bug"

Trong ví dụ:
- Nếu có DataConversionException
- Nghĩa là data đã đúng format
-> bỏ qua là hợp lý
'''