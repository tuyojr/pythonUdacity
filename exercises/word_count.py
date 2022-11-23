# This simple application takes a file and returns the word with the largest occurrence in it.

file = input('Enter a filename with the correct extension: ')
handler = open(file)

# This creates a dictionary with all of the words in the file as the 'key' and the number of times
# the word occurs as the 'value'
count_dict = dict()

# loop through each line in the file
for line in handler:

    # create a list containing each word
    words = line.split()

    # loop through each word in the list
    for word in words:

        # every time a word is found, set it as a key and the times it occurs as the value, increase
        # this value every time it occurs
        count_dict[word] = count_dict.get(word, 0) + 1


num_count = None
word_counted = None

# loop through the key and value from the dictionary
for key, value in count_dict.items():

    # check if the value of the key in the dictionary is larger than the value of the count variable 
    # declared above, set the new value from the dictionary as the value of the count variable
    # and its corresponding key as the word_counted variable 
    if num_count is None or value > num_count:
        num_count = value
        word_counted = key

print('The most occurring word in the file is "{}" and it appeared {} times.'.format(word_counted, num_count))


