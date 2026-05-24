user_numbers = input("Please enter 5 numbers separated by commas: ") # 1, 2, 3, 4, 5
numbers_list = user_numbers.split(",")
print(numbers_list) # ['1', ' 2', ' 3', ' 4', ' 5']

# We get back from split is a list, by we can always create another type of collection by passing the result to tuple, for example:

user_numbers2 = input("Please enter 5 numbers separated by commas: ") # 1,2,3,4,5
numbers_tuple = tuple(user_numbers2.split(","))

print(numbers_tuple) # => typle here

# Something this isn't really an issue, but sometimes you may need to go throught the collection with a for loop and clear things up using strip.
user_numbers3 = input("Please enter 5 numbers separated by commas: ") # 1, 2, 3, 4, 5

user_numbers3 = user_numbers3.split(",")

list_example = []

for i in user_numbers3:
    list_example.append(i.strip())
    
print( list_example )

# Finally, if we just want to put every character as a different item in a list or tuple:
sample_string = "WhereTheWindsMeetAndDota2"

print(list(sample_string))
print(tuple(sample_string))