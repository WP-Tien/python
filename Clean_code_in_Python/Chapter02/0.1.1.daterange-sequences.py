'''
Giả sử ta có object biểu diễn khoảng ngày (đơn giản dùng số cho dễ hiểu)
Requires:
- Truy cập bằng index: dr[0]
- Truy cập bằng slice: dr[2:5]
- Slice phải trả về DateRange mới
- Tuân theo slice semantics Python (end không bao gồm)
'''

class DateRange:
    def __init__(self, start, end):
        if start >= end:
            raise ValueError("Start must be smaller than end")
        self.start = start
        self.end = end
        
    def __len__(self):
        return self.end - self.start
    
    def __getitem__(self, item):
        # Index access
        if isinstance(item, int):
            if item < 0:
                item += len(self)
            if item < 0 or item >= len(self):
                raise IndexError("DateRange index out of range")
            return self.start + item
        
        # Slice access
        if isinstance(item, slice):
            # kiểm tra step
            start, stop, step = item.indices(len(self))
            if step != 1:
                raise ValueError("step is not supported")
            
            new_start = self.start + start
            new_end = self.start + stop
            return DateRange(new_start, new_end)
        
        raise TypeError("Invalid argument type")
    
dr = DateRange(10, 20)

print(len(dr))  # 10
print(dr[0])    # 10
print(dr[3])    # 13
print(dr[3])    # 13
print(dr[-1])   # 19

sub = dr[2:5]
print(sub.start)    # 12
print(sub.end)      # 15
print(type(sub))    # <class '__main__.DateRange'>

'''
__getitem__ = sức mạnh của []

    Custom sequence:
    Index → 1 phần tử
    Slice → object cùng kiểu
'''