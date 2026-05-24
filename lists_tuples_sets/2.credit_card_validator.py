'''
The algorithm we're going to use to verify card numbers is called the Luhn algorithm, or Luhn formula. 
This algorithm is actually used in real-life application to test credit or debit card numbers as well as SIM card serial numbers.

The purpose of the algorithm is to identify potentially mistyped numbers, because it can determin whether or not it's possible for a given number to be the number for a valid card.

The way we're going to use the algorithm is as follows:
1. Remove the rightmost from the card number. This number is called the checking digit, and it will excluded from most of our calculations.
2. Reverse the order of the remaining digits.
3. For this sequence of reversed digits, take the digits at each of the even indices (0, 2, 4, 6, etc) and double them. If any of the results are greater than 9, subtract 9 from those numbers.
4. Add together all of the results and add the checking digit.
5. If the result is divisible by 10, the number is a valid card number. If's not, the card number is not valid.

Let's look at this step by step for a valid number so we can see this in action. The number we're going to use is 5893804115457289, which is a valid Maestro card number, but not one which is in use.


Number	                Operation
5893804115457289	    Starting number
589380411545728X	    Remove the last digit
827545114083985X	    Reverse the remaining digits
16214585218016318810X	Double digits at even indices
725585218073981X	    Subtract 9 if over 9

Now we sum these digits and add the checking digit:
7 + 2 + 5 + 5 + 8 + 5 + 2 + 1 + 8 + 0 + 7 + 3 + 9 + 8 + 1 + 9

If we perform this series if additions, we get 80. 80 is divisible by 10, so the card number is valid.
'''
language = "Python"
numbers = [1, 2, 3, 4, 5]
letters = ("a", "b", "c", "d", "e")

language = reversed(language)
print(language)
numbers = reversed(numbers)
print(numbers)
letters = reversed(letters)
print(letters)

numbers = [1, 2, 3, 4, 5]
numbers.reverse()

print(numbers)