# Dictionaries store connections between pieces of information. Each item in a dictionary is a key-value pair.
alien = {'color': 'green', 'points': 5}

# Accessing a value
print("The alien's color is " + alien['color'])

# Adding a new key-value pair
alien['name'] = 'ruby'

print( alien )

# Looping through all key-value pairs
fav_numbers = {'eric': 17, 'ever': 4}
for name, number in fav_numbers.items():
    print(name + ' loves ' + str(number))

# Looping through all keys
for name in fav_numbers.keys():
    print(name + ' loves a number')

# Looping through all values
for number in fav_numbers.values():
    print(str(number) + ' is a favorite')