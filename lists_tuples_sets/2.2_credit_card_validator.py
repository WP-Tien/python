card_number = list(input("Please enter a card number: ").strip())

# Remove the last digit from the card number
check_digit = card_number.pop()

# Reverse the order of the remaining numbers
card_number.reverse()

processed_digits = []

for index, digit in enumerate(card_number):
    if index % 2 == 0:
        doubled_digit = int(digit) * 2 # Convert the digit to an integer and double the value
        
        # Substract 9 from any results that are greater than 9
        if doubled_digit > 9:
            doubled_digit = doubled_digit - 9
            
        processed_digits.append(doubled_digit)
    else: 
        processed_digits.append(int(digit))   
