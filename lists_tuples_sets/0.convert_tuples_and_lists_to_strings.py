l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

numbers = [1, 2, 3, 4, 5]
numbers = str(numbers)

print( type(numbers) ) # <class 'str'>

numbers2 = "[1, 2, 3, 4, 5]"
print( numbers2 )
### ???
### The solution to ou problem is to the join method

project_authors = ["Mike", "Sofia", "Helen"]
project_authors = ", ". join(project_authors)
print(f"The people who worked on this project are: {project_authors}.")

# We could achieve the same thing by putting the join call right inside the curly braces of the f-string:
project_authors2 = ["Mike", "Sofia", "Helen"]
print(f"The people who worked in this project are: {', '. join(project_authors2)}." )

# Using for loop, we iterate over the numbers list. We convert each number to a string and append it to stringied_numbers.
# Finally, we use join with stringifed_numbers.
numbers = [1, 2, 3, 4]

stringified_numbers = []

for number in numbers:
    stringified_numbers.append(str(number))
    
print(', '. join(stringified_numbers)) # 1, 2, 3, 4