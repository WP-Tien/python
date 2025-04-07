# A list stores a series of items in a particular order. You accesss items using an index, or withing a loop. 
# List = [] ordered and changeable. Duplicates OK

names = [
    'Join',
    'Bob', 
    'Vincent',
    'Mosh',
    'Sarah'
];

print( names )
print( names[1] )
print( names[-1] )
print( names[2:] ) # ['Vincent', 'Mosh', 'Sarah']
print( names[2:4] ) # ['Vincent', 'Mosh']
print( names.index("Bob") )
print( names.count("Vincent") )

# Loop throught a list
for name in names:
    print(name)

# Adding items to a list
bikes = []
bikes.append('trek')
bikes.append('redline')
bikes.append('giant')

bikes.remove('redline')

bikes.insert(1, "redline1")

bikes.reverse()

bikes.clear()

print( bikes )

# Making numerical list
squares = []
for x in range(1, 11):
    squares.append(x**2) # 1 * 1, 2 * 2, 3 * 3

print(squares)

# list comprehensions
squares_2 = [x**2 for x in range(1, 11)]

print(squares_2)

# slice a list
finishers = ['sam', 'bob', 'ada', 'bea']

first_two = finishers[:2]

print(first_two)

# copy a list
copy_of_bike = bikes[:]

print(copy_of_bike)
