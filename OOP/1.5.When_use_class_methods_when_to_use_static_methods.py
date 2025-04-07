class Item:
    @staticmethod
    def is_integer():
        '''
        This should do something that has a relationship
        with the class, but not something that must be unique
        per instance!
        
        Điều này sẽ thực hiện một điều gì đó có mối quan hệ
        với lớp, nhưng không phải là điều gì đó phải là duy nhất
        cho mỗi trường hợp!
        '''
    @classmethod
    def instantiate_from_something(cls):
        '''
        This should also do something that has a relationship
        with the class, but usually, those are used to
        manipulate different structures of data to instantiate
        objects, like we have done with CSV.
        '''

# THE ONLY DIFFERENCE BETWEEN THOSE:
# Static methods are not passing the object reference as the first argument in the background!
# Các phương thức tĩnh không truyền tham chiếu đối tượng làm đối số đầu tiên trong nền!


# NOTE: However, those could be also called from instances.

item1 = Item()
item1.is_integer()
item1.instantiate_from_something()