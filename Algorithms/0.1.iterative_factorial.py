"""
iterative: Lặp lại
factorial: Giai thừa
fact: Việc
"""

def iterative_factorial(n):
    fact = 1

    for i in range(2, n + 1): # It mean 2, 3, 4, 5
        fact *= i
    return fact

print(iterative_factorial(5)) # 120

"""
fact = 1; i = 2; => fact = 2;
fact = 2; i = 3; => fact = 6;
fact = 6; i = 4; => fact = 24;
fact = 24; i = 5; => fact = 120;
"""