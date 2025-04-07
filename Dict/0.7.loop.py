# Looping through all key-valye pairs
# Store people's favorite languages.

fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# Show each person's favorite language.
for name, language in fav_languages.items():
    print( name + ": " + language )

# Looping through all the keys
for name in fav_languages.keys():
    print(name)

# Looping through all the values
for language in fav_languages.values():
    print(language)

# Looping through all the keys in order
for name in sorted(fav_languages.keys()):
    print(name + ": " + language)