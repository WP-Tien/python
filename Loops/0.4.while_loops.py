# A while loops repeats a block of code as long as a certain condition is true.

# A simple while loop
current_value = 1
while current_value <= 5:
    print(current_value)
    current_value += 1

# Letting the user choose when to quit
msg = ''
while msg != 'quit':
    msg = input("What's your message? ")
    print(msg)