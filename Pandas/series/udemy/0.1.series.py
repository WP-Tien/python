import pandas as pd

students = ['Andrew', 'Brie', 'Kanika']
print( type(students) )
print( pd.Series(students) )

ages = [27, 49, 37]
print( pd.Series(ages) )

heights = [167.4, 173.2, 190.0]
print( pd.Series(heights) )