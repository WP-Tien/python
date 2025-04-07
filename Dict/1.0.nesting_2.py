users = [
    {
        'last': 'fermi',
        'first': 'enrico',
        'username': 'efermi'
    },
    {
        'last': 'curie',
        'first': 'marie',
        'username': 'mcurie'
    }
]

# Show all information about each user.
for user_dict in users:
    for k, v in user_dict.items():
        print(k + ": " + v)
    print("\n")