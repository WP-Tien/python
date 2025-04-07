# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#              * unpacking operator
#               1. positional 2. default 3. keyword 4. ARBITRARY

# def add(*args):
#     print(type(args)) # tuple
# add(1, 2, 3)

# def add(*args):
#     total = 0
#     for args in args:
#         total += args
#     return total
# print(add(1,2,3))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
# display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

def print_address(**kwargs):
    # print(type(kwargs)) # dict

    # for value in kwargs.values():
    #     print(value)

    # for key in kwargs.keys():
    #     print(key)

    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.",
                city="Detroit",
                state="MI",
                zip="54321")