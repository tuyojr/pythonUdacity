# Write a program that reads a file and prints the letters 
# in decreasing order of frequency. Your program should 
# convert all the input to lower case and only count the 
# letters a-z. Your program should not count spaces, digits, 
# punctuation, or anything other than the letters a-z. Find 
# text samples from several different languages and see how 
# letter frequency varies between languages. Compare your 
# results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string

word_count = 0
letters_dict = {}
letters_list = []

file_name = input("Please enter a file name with the correct extension: ")

try:
    f = open(file_name)
except FileNotFoundError:
    print('This file cannot be opened because it does not exist: ', file_name)
    exit()

for line in f:

    # removes all the digits
    line = line.translate(str.maketrans('', '', string.digits))

    # removes all the punctuations
    line = line.translate(str.maketrans('', '', string.punctuation))

    # changes the lines to lower case
    line = line.lower()

    words = line.split()

    # loop through each word in each line
    for word in words:

        # loop through each letter in each line
        for letter in word:
            counts =+ 1

            # checks if a letter is not in the dictionary and adds it to it
            # if it is, it just increases the value by 1
            letters_dict[letter] = letters_dict.get(letter, 0) + 1

# loop through the dictionary and add to the list, a tuple of the new value (value/counts) and the key
# the new value is a computation of the relative frequency of the letter
# the list(letters_dict.items()) creates a new list to be able to loop through
for key, val in list(letters_dict.items()):
    letters_list.append((val/counts, key))

# sort the list in reverse manner
letters_list.sort(reverse=True)

# loop through the list and print the tuples
for key, val in letters_list:
    print(key, val)