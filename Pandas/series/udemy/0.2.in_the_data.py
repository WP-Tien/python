import pandas as pd

books_list = ['Fooled by Randomness', 'Sapiens', 'Lenin on the Train']
list_s = pd.Series(books_list)

books_dict = { 0: 'Fooled by Randomness', 1: 'Sapiens', 2: 'Lenin on the Train' }
dict_s = pd.Series(books_dict)

print( list_s.equals(dict_s) )