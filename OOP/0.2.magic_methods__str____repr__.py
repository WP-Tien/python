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

"""
__str__(self): This method returns a user-friendly, informal string representation of an object. It is called by the str() function and implicitly by the print() function. The goal of __str__ is to be readable and informative for end users.

__repr__(self): This method returns a more detailed, unambiguous string representation of an object, often used for debugging and logging. It is called by the repr() function and in the interactive interpreter. Ideally, the string returned by __repr__ should be a valid Python expression that can be used to recreate the object.
"""

