from pprint import pprint

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different way in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the 
    metaclass because it is best suited for this purpose
    Lớp Singleton có thể được triển khai theo nhiều cách khác nhau trong Python.
    Một số phương pháp có thể bao gồm: lớp cơ sở, decorator, metaclass. 
    Chúng ta sẽ sử dụng  metaclass vì nó phù hợp nhất cho mục đích này.

    Decorator: là một abstract class dùng để duy trì một tham chiếu của đối tượng Component và đồng thời cài đặt các phương thức của Component interface.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes(có thể thay đổi) to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance
        """
        # ...

class withoutSingleton:
    def some_business_logic(self):
        pass

if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()
    s3 = withoutSingleton()
    s4 = withoutSingleton()

pprint(__name__)
pprint(s1)
pprint(s2)
pprint(s3)
pprint(s4)