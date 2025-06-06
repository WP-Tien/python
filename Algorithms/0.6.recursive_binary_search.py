# RECURSIVE BINARY SEARCH

def binary_recur(arr, start, end, target):
    if end >= start:

        mid = start + end - 1 // 2

        if arr[mid] < target:
            binary_recur(arr, mid + 1, end, target)

        elif arr[mid] > target:
            return binary_recur(arr, start, mid - 1, target)

        else: 
            return mid

    else:
        return -1

arr = [2, 5, 8, 10, 16, 22, 25]
target = 10
result = binary_recur(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Element is present at index", str(result)) # Element is present at index 3
else: 
    print("Element is not present in array")

"""
    start = 0
    end = 5
    target = 10

    - 5 > 0
        mid = 0 + 5 - 1 // 2 = 2

        - 8 < 10

            mid = 2 + 1 = 3
            end = 5
            target = 10

            - 10 = target
                => 3
"""