name = "Vincent Nguyen"
age = 30
height = 74
weight = 79
eyes = "Brown"
teeth = "White"
hair = "Black"

print("Let's talk about %s" % name)
print("He's %d cm tall." % height)
print("He\'s %d pounds heavy." % weight)
print("He's got %s eyes and %s hair." % (eyes, hair))
print("Actually that's not too heavy")
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print('If I add %d, %d and %d I get %d.' %(age, height, weight, age + height + weight) )

# try more format characters
my_greeting = "Hello, \t"
my_first_name = 'Vincent'
my_last_name = 'Nguyen'
my_age = 29
# Print 'Hello, \t'my name is Vincent Nguyen, and I'm 29 years old.'
print("%r my name is %s %s, and I'm %d years old." % (my_greeting, my_first_name, my_last_name, my_age))

# Try to write some variables that convert the inches to centimeters and kilos
inches_per_centimeters = 2.54
pounds_per_kilo = 0.45359237

print("He's %f centimeters tall." % (height * inches_per_centimeters))
print("He's %f kilos heavy." % (weight * pounds_per_kilo))