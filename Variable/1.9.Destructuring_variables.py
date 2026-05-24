t = 5, 11
x, y = t

print(x, y)

person = ("Bob", 42, "Mechanic")
# if you dont care age
name, _, profession = person

print(name, profession) # Bob Mechanic

head, *tail = [1, 2, 3, 4, 5]
print(head) # 1
print(tail) # [2, 3, 4, 5]