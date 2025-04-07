import random

# random_integer = random.randint( 1, 10 )
# print( random_integer )

# random_number_0_to_1 = random.random() * 10
# print( random_number_0_to_1 )

# random_float = random.uniform( 1, 10 )
# print( random_float )

# options = ("rock", "paper", "scissor")
# option = random.choice(options)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

random.shuffle(cards)

print(cards)