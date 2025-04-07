# object = A "bundle" of related attribute (variables) and methods (functions)
#           Ex. phone, cup, book
#           You need a "class" to create many object

# class = (blue print) used to design the structure and layout of an object

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student( "Rolf", (90, 90, 75, 90))
# print(student.name)
# print(student.grades)
print(student.average())