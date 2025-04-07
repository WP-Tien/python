import pandas as pd

books_list = [ 'Fooled by Randomness', 'Sapiens', 'Lenin on the Train' ]

# print( pd.Series(data=books_list, index=['funny', 'serious and amusing', 'kinda interesting']) )
print( pd.Series( books_list, ['funny', 'serious and amusing', 'kinda interesting'] ) )
print( pd.Series( books_list, ['funny', 'serious and amusing', 'kinda interesting'], dtype='object' ) )

list_s = pd.Series( books_list, ['funny', 'serious and amusing', 'kinda interesting'], dtype='object' )

print( pd.__version__ )

print( list_s.index )
print( type( list_s.index ) )
print( list( pd.RangeIndex(start=1, stop=7, step=1) ) )
print( list( pd.RangeIndex(start=10, stop=-11, step=-1) ) )