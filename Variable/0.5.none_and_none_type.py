# user_selected: None = None
# user_selected: None = 'vincent321'

# Case 1:
# if user_selected:
#     print( user_selected )
# else:
#     print( 'Please select a user!' )

# Case 2:
# print( user_selected is None )
# print( user_selected is not None )

# Case 3:
# def say_hello(name: str) -> None:
#     print(f'Hello, {name}')

# value = say_hello('Vincent Nguyen')
# print(value)

## None Type ##
# print( type( None ) )

from types import NoneType
user_selected: str | None = None
print(type(user_selected))
print(type(user_selected) is NoneType)

