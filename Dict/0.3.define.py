# Defining a dictionary

# Making a dictionary
alien_0 = {'color': 'green', 'points': 5}

# Getting the value associated with a key
print(alien_0['color'])
print(alien_0['points'])

# Getting the value with get()
alien_0 = {'color': 'green'}

alien_color = alien_0.get('color')
alien_points = alien_0.get('points', 0)

print(alien_color)
print(alien_points)