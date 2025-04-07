# ITERATIVE BINARY SEARCH
# // is (discard remainder)

def binary_itr(arr, start, end, target):
    while start <= end:

        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid

    return start

arr = [2, 5, 8, 10, 16, 22, 25] 
target = 10

result = binary_itr(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Element is present at index %d" % result) # 3
else:
    print("Element is not present in array")

"""
    target = 10
    star = 0
    end = 5

    while 0 < 5
        mid  = ( 0 + 5 ) // 2 = 2
        arr[2] = 8 < 10 => start = 2 + 1 = 3
        end = 5

    while 3 < 5
        mid = ( 3 + 5 ) // 2 = 4
        start = 3
        arr[4] = 16 > 10 => end = 4 - 1 = 3
    
    while 3 <= 3
        mid = ( 3 + 3 ) // 2 = 3
        
        arr[3] = 10
        => 10
"""