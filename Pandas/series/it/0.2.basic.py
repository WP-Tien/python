import pandas as pd

score = {"Jane":90, "Bill":80, "Elon": 85, "Tom": 75, "Tim": 95}

names = pd.Series(score) # Convert to Series

print( names )

# Find Tim score
print( names['Tim'] )

# Filter score >= 85
print( names[names>=85] )

# Replace Tom score -> 60
names['Tom'] = 60
print( names )

# Replace all values <= 80 with 83
names[names <= 80] = 83
print( names )

# Check if Tom in names
print( 'Tom' in names.keys() )

# Check if Can in names
print( 'Can' in names.keys() )

# Scale score to range 10
print( names/10 )

# ^2 score
print( names**2 )

# Check if value is null
print( names.isnull() )

print( names[names.isnull()] )