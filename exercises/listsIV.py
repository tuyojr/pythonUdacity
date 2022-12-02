# Download a copy of the file from www.py4e.com/code3/romeo.txt
# Write a program to open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split 
# function.
# For each word, check to see if the word is already in a list. If 
# the word is not in the list, add it to the list.
# When the program completes, sort and print the resulting words in 
# alphabetical order.

# Enter file: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
# 'and', 'breaks', 'east', 'envious', 'fair', 'grief',
# 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
# 'sun', 'the', 'through', 'what', 'window',
# 'with', 'yonder']

# Create a function that accepts a file name as user input
def file(user_file):

    # Open the file in read mode
    open_file = open(user_file)

    # Create an empty list to store words from the file
    new_list = list()

    # loop through each line in the file
    for line in open_file:

        # split each line into words
        words = line.split()

        # loop through each word in each line
        for word in words:

            # if a word in the file is not in the empty list above, add it to it and sort the new_list
            if word not in new_list:
                new_list.append(word)
                new_list.sort()
    # return the value of the new_list
    return new_list

# Just a prompt to show the user what to do and how to use the program
print('You can input a file you want to open, with the correct extension.\nIf you wish to terminate the program without any interaction\njust type "done".\n')

# create a variable that stores the user input
file_name = input('Enter a file name: ')

# Not necessary, counts each time the loop runs
count = 0

# Simple while loop that runs if the user wants to continue or not with the program
while True:
    if file_name == 'done':
        print('Thank you for using this program.')
        break
    else:
        count += 1
        print(file(file_name))
        exit()

