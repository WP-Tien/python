numbers = [ 2, 2, 4, 6, 7, 8, 4 ]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)