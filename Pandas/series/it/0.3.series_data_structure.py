import pandas as pd

games = pd.read_csv("supermarket_sales_nan.xlsx - Sheet1.csv")

# print( games )

# Print top 3 rows
print( games.head(3) )

# Check data type of each column
print( games.dtypes )

# Quick view City column (descriptive statistics)
print('\n')
print( games['City'].describe() )
'''
count       1000
unique         3
top       Yangon
freq         340
Name: City, dtype: object
'''

# Count frequence of each value in column
print('\n')
print( games['City'].value_counts() )
'''
City
Yangon       340
Mandalay     332
Naypyitaw    328
Name: count, dtype: int64
'''

# Normalize column City in value count
print('\n')
print( games['City'].value_counts(normalize=True) )
'''
City
Yangon       0.340
Mandalay     0.332
Naypyitaw    0.328
Name: proportion, dtype: float64
'''

# 
print('\n')
print( type(games['City'].value_counts()) )
'''
<class 'pandas.core.series.Series'>
'''

# Value count top 2
print( games['City'].value_counts().head(2) )
'''
City
Yangon      340
Mandalay    332
Name: count, dtype: int64
'''

# Value count bottom 2
print( games['City'].value_counts().tail(2) )
'''
City
Mandalay     332
Naypyitaw    328
Name: count, dtype: int64
'''

# View unique values of City column
print('\n')
print( games['City'].unique() )
'''
['Yangon' 'Naypyitaw' 'Mandalay']
'''

# Count unique values of City column
print('\n')
print( games['City'].nunique() )
# 3

# Crosstab City vs Unit price
print('\n')
print( pd.crosstab( games['City'], games['Unit price'] ) )