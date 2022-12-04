# But, soft! what light through yonder window breaks?
# It is the east, and Juliet is the sun.
# Arise, fair sun, and kill the envious moon,
# Who is already sick and pale with grief,

# Since the Python split function looks for spaces and treats words 
# as tokens separated by spaces, we would treat the words "soft!" 
# and "soft" as different words and create a separate dictionary 
# entry for each word.

# Also since the file has capitalization, we would treat "who" and "Who" 
# as different words with different counts.

# We can solve both these problems by using the string methods lower, 
# punctuation, and translate. The translate is the most subtle of the 
# methods. Here is the documentation for translate:

# line.translate(str.maketrans(fromstr, tostr, deletestr))

# Replace the characters in fromstr with the character in the same position 
# in tostr and delete all characters that are in deletestr. The fromstr and 
# tostr can be empty strings and the deletestr parameter can be omitted.

# We will not specify the table but we will use the deletechars parameter 
# to delete all of the punctuation. We will even let Python tell us the 
# list of characters that it considers "punctuation":

import string

file_name = input('Enter the file name: ')
try:
    f = open(file_name)
except:
    print('File cannot be opened: {}'.format(file_name))
    exit()

word_count = dict()
for line in f:
    line = line.rstrip()

    # we want to delete all the punctuations in the text
    line = line.translate(line.maketrans('', '', string.punctuation))

    # also convert all the text to lower case
    line = line.lower()

    # create a list of words
    words = line.split()

    for word in words:
        # if word not in word_count:
        #     word_count[word] = 1
        # else:
        #     word_count[word] += 1
        word_count[word] = word_count.get(word, 0) + 1

print(word_count)