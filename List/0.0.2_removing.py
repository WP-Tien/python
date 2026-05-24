# For example, if we have a list like this:
names = ["John", "Sarah", "Alice", "John"]

# We can remove the first "John" by calling remove:
names.remove("John")

print(names) # ['Sarah', 'Alice', 'John']

# Using del keyword
del names[0]

print(names) # ['Alice', 'John']

# Using the pop method
names.pop()

print(names) # ['Alice']

# `Clear` it’s just going to remove everything inside a given list
names.clear()

print(names) # []