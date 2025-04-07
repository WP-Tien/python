def merging(left, right):
    C = []

    while min( len(left), len(right) ) > 0:
        if left[0] > right[0]:
            insert = right.pop(0)
            C.append(insert)
        elif left[0] <= right[0]:
            insert = left.pop(0)
            C.append(insert)

    if len(left) > 0:
        for i in left:
            C.append(i)
    if len(right) > 0:
        for i in right:
            C.append(i)

    return C
"""
    2 mảng phải sort trước => mảng cuối mới sort theo thứ tự
"""
left = [2, 5, 6, 10]
right = [3, 4, 12, 20]
print(merging(left, right))


"""
    4 > 0
        2 <= 3
        insert = 2
        C = [2]

        left = [5, 6, 10]
        right = [3, 4, 12, 20]
    3 > 0
        5 > 3
        insert = 3
        C = [2,3]

        left = [5, 6, 10]
        right = [4, 12, 20]

    3 > 0
        4 < 5
        insert = 4
        C = [2, 3, 4]

        left = [5, 6, 10]
        right = [12, 20]

    2 > 0
        5 < 12
        insert = 5
        C = [2, 3, 4, 5]

        left = [6, 10]
        right = [12, 20]

    2 > 0
        6 < 12
        insert = 6
        C = [2, 3, 4, 5, 6]

        left = [10]
        right = [12, 20]

    1 > 0
        10 < 12
        insert = 10
        C = [2, 3, 4, 5, 6, 10]

        left = []
        right = [12, 20]

    len(right) > 0
        C = [2, 3, 4, 5, 6, 10, 12, 20]
"""