"""
recursive: Đệ quy
"""

def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n-1)
        temp = temp * n
    return temp

print(recur_factorial(5)) # 120

"""
Phase: 1
-- n = 5; temp = (
    -- n = 4; temp = (
            -- n = 3; temp = (
                -- n = 2; temp = (
                    -- n = 1; return n
                ); temp = ???
            ); temp = ???
        ); temp = ???
    ); temp = ??? 

Phase: 2
-- n = 5; temp = (
    -- n = 4; temp = (
            -- n = 3; temp = (
                -- n = 2; temp = (
                    -- n = 1; return n
                ); temp = 1 * 2 # temp = 1; n = 2
            ); temp = 2 * 3 # temp = 2; n = 3
        ); temp = 6 * 4 # temp = 6; n = 4 
    ); temp = 24 * 5 # temp = 24; n = 5
"""
