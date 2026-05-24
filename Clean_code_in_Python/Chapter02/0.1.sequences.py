"""
Creating your own sequences

__getitem__ là gì?
value = myobject[key]
Khi bạn viết như trên, Python ngầm gọi:
myobject.__getitem__(key)
- key có thể là :
    - số nguyên (obj[0])
    - slice (obj[1:5])
    - hoặc key bất kỳ (với dict-like object)

Thế nào được coi là sequence, một bobject được coi là sequence nếu nó có:
    __getitem__
    __len__
-> Khi có 2 method này:
- Có thể truy cập bằng index
- Có thể lặp (iterate) bằng for
Ví dụ sequence có sẵn:
- list
- typle
- str

> Squences
"""

class Items:
    def __init__(self, *values):
        self._values = list(values)
        
    def __len__(self):
        return len(self._values)
    
    def __getitem__(self, item):
        return self._values.__getitem__(item)