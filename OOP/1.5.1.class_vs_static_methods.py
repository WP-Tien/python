class Foo:
    def instance_bar(self, x):
        print("Executing instance_bar(%s, %s)" % (self, x))

    @classmethod
    def class_bar(cls, x):
        print("Executing class_bar(%s, %s)" % (cls, x))

    @staticmethod
    def static_bar(x):
        print("Executing static_bar(%s)" % x)

foo = Foo()
# Dưới đây là cách đơn giản nhất để thực thi một phương thức:
foo.instance_bar('args')
"""
Đây là một instance method, là phương thức phổ biến nhất. Một đối tượng (instance của class) được ngầm truyền thành tham số thứ nhất (self) của phương thức này.
"""

"""
Class method là phương thức thuộc về cả class. Khi thực thi, nó không dùng đến bất cứ một instance nào của class đó. Thay vào đó, cả class sẽ được truyền thành tham số thứ nhất (cls) của phương thức này:
"""
Foo.class_bar('args')

"""
Một điều thú vị là class method cũng có thể gọi từ instance mà không gặp trở ngại gì (nhiều ngôn ngữ vẫn cho làm điều này kèm theo vài warning).
"""
foo.class_bar('args')

"""
Static method là một phương thức đặc biệt, nó không sử dụng bất cứ thứ gì liên quan đến class hay instance của class đó. Cả self hay cls đều không xuất hiện trong tham số của loại phương thức này. Và static method hoạt động không khác gì một hàm thông thường.
"""
foo.static_bar('args')
Foo.static_bar('args')