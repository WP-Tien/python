'''
    Swap first and last element of a list
'''

test = [3, 10, 6, 5, 20]

print(test)

test[0], test[-1] = test[-1],test[0]

print(test)


'''
    Swap elememts at given positions (user input)
'''

test2 = [3, 10, 6, 5, 20]

i = int(input("Nhập index:"))

n = int(input("Nhập giá trị mới:"))

test[i] = n

print(test)