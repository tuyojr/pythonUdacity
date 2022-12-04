# Exercise 1: [wordlist2]

# Write a program that reads the words in words.txt and stores 
# them as keys in a dictionary. It doesn't matter what the values 
# are. Then you can use the in operator as a fast way to check 
# whether a string is in the dictionary.

# Prompt user to enter a file name
file = input('Please input a file name with the correct extension:\n')

# Open the user's file
f = open(file)

# Create a new dictionary that will contain our output
new_dict = dict()

# A count variable to keep track of the words in the new dictionary
count = 1

# loop through each line in the file
for word in f:

    # remove the new line character at the end of each line
    word = word.rstrip()

    # check if the word is already in our dictionary
    # if it is, just increase the count of the word
    # else, just set the value to the value of count
    if word in new_dict:
        new_dict[word] = count + 1
    else: 
        new_dict[word] = count
print(new_dict)