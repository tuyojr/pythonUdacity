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

def file(user_file):
    open_file = open(user_file)
    new_list = list()
    for line in open_file:
        words = line.split()
        for word in words:
            if word not in new_list:
                new_list.append(word)
                new_list.sort()
    return new_list


print('You can input a file you want to open, with the correct extension.\nIf you wish to terminate the program without any interaction\njust type "done".\n')

file_name = input('Enter a file name: ')
count = 0

while True:
    if file_name == 'done':
        print('Thank you for using this program.')
        break
    else:
        count += 1
        print(file(file_name))
        exit()

