# keyword arguments = an argument preceded by an identifier
#                       helps with readability
#                       order of arguments doesn't matter
#                       1.Positional 2.default 3.Keyword 4.arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello( "Hello", title="Mr.", last="John", first="James" )

for x in range(1, 11):
    print(x, end=" ")

print("1", "2", "3", "4", "5", "6", sep="-")