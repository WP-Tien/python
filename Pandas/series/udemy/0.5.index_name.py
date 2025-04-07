import pandas as pd

books_list = ['Fooled by Randomness', 'Sapiens', 'Lenin on the Train']
list_s = pd.Series(books_list)

books_series = list_s

print( books_series.size )