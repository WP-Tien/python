# We define a list using square brackets like this:
names = ["John", "Alice", "Sarah", "George"]
# Each value is places inside the square bracket, separated by commas.
# We can split the list across multiple lines like so:
movie_titles = [
    "Eternal Sunshine of the Spotless Mind",
    "Memento",
    "Requiem for a Dream"
]
# We can mix whatever types of value we want in a list
friend_details = ["John", 27, "Web developer"] 

print(friend_details)

L = list(range(10))

print(L) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(type(L[0])) # <class 'int'>
# Or, similarly, a list of strings

L2 = [str(c) for c in L]
print(L2)
print(type(L2[0])) # <class 'str'>

L3 = [True, "2", 3.0, 4]
print( [type(item) for item in L3] ) # [<class 'bool'>, <class 'str'>, <class 'float'>, <class 'int'>]

# Fixed-Type Arrays in Python
import array
L = list(range(10))
A = array.array('i', L)
# Here 'i' is a type code indicating the contents are integers.

print(A)