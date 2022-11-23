# the tuple in the dictionary contains age, room number, email
dict_users = {
    'Messi': (35, 10, 'lionelmessi@thegoat.com'),
    'Ronaldo': (37, 7, 'cristianoronaldo@agoat.com'),
    'Bukayo': (19, 77, 'bukayousaka@arsenal.com'),
    'Jude':(19, 22, 'judebellingham@dortmund.com'),
    'Pedri': (19, 8, 'pedrigonzalez@barcelona.com'),
    'Kevin':(31, 17, 'kevindebruyne@city.com')
}

# simple algorithm to sort dictionary keys in alphabetical order, First sort the keys using sorted
sorted_names = dict(sorted(dict_users.items(), key=lambda dict_key:dict_key))

# for each key name retrieve the values from the dict
for key, value in sorted_names.items():
    print('PLAYER: {},\nAGE: {},\nROOM No.: {},\nEMAIL: {} \n'.format(key, value[0], value[1], value[2]))
