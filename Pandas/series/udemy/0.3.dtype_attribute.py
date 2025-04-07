import pandas as pd

ages = [27, 49, 37]

print( pd.Series( ages ) )

print( pd.Series( ages, dtype="float" ) )

students = [
    'Andrew',
    'Brie', 
    'Kanika'
]

names_series = pd.Series(students)

print( names_series )
print( names_series.dtype )