word = 'brontosaurus'
d = dict()
for c in word: 
    # if c not in d: 
    #     d[c] = 1 
    # else: 
    #     d[c] = d[c] + 1 

    # give the new key a new value in the dictionary, which is the character in the word.
    # The default value is 0, and each time the loop runs it adds 1 to the value
    # of the key if it is already there. If the key is not there, it returns 0, the default value
    d[c] = d.get(c, 0) + 1
print(d)