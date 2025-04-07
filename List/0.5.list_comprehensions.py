# Using a loop to generate a list of square numbers
# squares = []
# for x in range (1, 11):
#     square = x**2
#     squares.append(square)

# print(squares)

# Using a comprehension to generate a list of square numbers
# squares = [x**2 for x in range(1, 11)]

# print(squares)

######################

# Using a loop to convert a list of names to upper case 
names = ['kai', 'abe', 'ada', 'gus', 'zoe']

# upper_names = []
# for name in names:
#     upper_names.append(name.upper())

# print( upper_names )

# Using a comprehension to convert a list of names to upper case
upper_names = [name.upper() for name in names]

print( upper_names )
