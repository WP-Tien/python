# Preserving the order of keys and values
from collections import OrderedDict
fav_languages = OrderedDict()

fav_languages['jen'] = ['python', 'ruby']
fav_languages['sarah'] = ['c']
fav_languages['edward'] = ['ruby', 'go']
fav_languages['phil'] = ['python', 'haskell']

# display
for name, langs in fav_languages.items():
    print(name + ":")
    for lang in langs:
        print("- " + lang)