class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")

# ClassTest.class_method() # Called class_method of <class '__main__.ClassTest'>
ClassTest.static_method() # Called static_method