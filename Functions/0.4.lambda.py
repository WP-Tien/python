# add = lambda x, y: x + y
# print( add( 5, 7 ) )

# print(( lambda x, y: x + y )( 5, 7 ))

sequence = [ 1, 3, 5, 9 ]
doubled = [(lambda x: x * 2)(x) for x in sequence]
doubled = list(map(lambda x: x * 2, sequence))

print( doubled )