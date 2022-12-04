# a Python program to read through the lines of a shortened and 
# simplified version of romeo text with no punctuation, break each 
# line into a list of words, and then loop through each of the 
# words in the line and count each word using a dictionary.


file_name = input('Enter the file name: ')
try:
    f = open(file_name)
except:
    print('File cannot be opened: "{}"'.format(file_name))
    exit()

word_count = dict()
for line in f:
    words = line.split()
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

print(word_count)