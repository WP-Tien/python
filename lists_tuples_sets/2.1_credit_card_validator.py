card_number = list(input("Please enter a card number: ").strip())

# Remove the last digit from the card number
check_digit = card_number.pop()

# Reverse the order of the remaining numbers
card_number.reverse()

index = 0

for digit in card_number:
    if index % 2 == 0:
        print(f"Even index {digit}")
    else:
        print(f"Odd index {digit}")

    # Increment the index counter for each iteration
    index = index + 1