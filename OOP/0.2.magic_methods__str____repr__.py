class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # def __str__(self): # return to string instance
    #     return f"Person {self.name}, {self.age} years old."

    def __repr__(self): # should return a printable representation of the object
        return f"<Person('{self.name}', '{self.age}')>"

bob = Person("Bob", 35)
print(bob)