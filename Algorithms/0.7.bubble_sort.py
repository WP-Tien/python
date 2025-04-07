# def swap (A, i, j):
#     temp = A[i]
#     A[i] = A[j]
#     A[j] = temp

# def bubble_sort_un_op(A):
#     iterations = 0

#     for i in A:
#         for j in range(len(A)-1):
#             iterations += 1
#             if A[j] > A[j+1]:
#                 swap(A, j, j + 1)

#     return A, iterations

# A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(bubble_sort_un_op(A))


def bubble_optimized(A):
    iterations = 0
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            iterations += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j] # Using Temporary Variable

    return A, iterations

A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bubble_optimized(A))

"""
    A|length = 8
    - i = 0 
        j = 0; 8-0-1 = 7
        j = 0
            A[0] = 9
            A[1] = 8
            9 > 8
            [8] [9] [7] [6] [5] [4] [3] [2] [1]

        j = 1
            A[1] = 9
            A[2] = 7
            9 > 7
            [8] [7] [9] [6] [5] [4] [3] [2] [1]

        j = 2
            A[2] = 9
            A[3] = 6
            9 > 6
            [8] [7] [6] [9] [5] [4] [3] [2] [1]
        ... 
            [8] [7] [6] [5] [4] [3] [2] [1] [9]
    - i = 1
        j = 0; 8-1-1 = 6
        j = 0
            A[0] = 8
            A[1] = 7
            8 > 7
            [7] [8] [6] [5] [4] [3] [2] [1] [9]
        ...
            [7] [6] [5] [4] [3] [2] [1] [8] [9]
    ...
    - i = 7
        j = 0; 8-7-1 = 0

        [1] [2] [3] [4] [5] [6] [7] [8] [9]
"""