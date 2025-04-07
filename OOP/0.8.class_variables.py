# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:
    class_year = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)

print(student2.name);
print(student2.age);
print(student2.class_year);