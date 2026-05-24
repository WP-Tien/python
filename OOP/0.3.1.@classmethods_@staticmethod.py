
class Pizza:
    def __init__(self, radius):
        self.radius = radius
        
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2) # Tạo object từ class đó.
    
    @staticmethod
    def area(radius):
        return 3.14 * radius * radius
    
p = Pizza.from_diameter(10) # p = Pizza(10 / 2) => radius = 5
print(p.radius) # 5
print(Pizza.area(5))