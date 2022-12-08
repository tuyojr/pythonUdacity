# Exercise 1: Revise a previous program as follows: Read and parse 
# the "From" lines and pull out the addresses from the line. Count 
# the number of messages from each person using a dictionary.

# After all the data has been read, print the person with the most 
# commits by creating a list of (count, email) tuples from the 
# dictionary. Then sort the list in reverse order and print out the 
# person who has the most commits.

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195

file_name = input("Please enter a file name with the correct extension: ")

# An empty dictionary to store our senders and amount of commits
sender_mail = {}

# An empty list to hold a tuple of our senders and their commits
sender_list = []

# A try and except block to catch a file not found error
try:
    f = open(file_name)
except FileNotFoundError:
    print('This file cannot be opened because it does not exist: ', file_name)
    exit()

# Loop through each line in the file and store them in a words list
for line in f:
    words = line.split()

    # if the length of the line's list is less than 2 or the first index of the line's list
    # does not start with the keyword 'From', we continue going through the loop
    # else, we check if the element at index 1 is in our dictionary, if it is not, we set the 
    # key of our dictionary to the element at index 1 and give it a value of 1, if it is already
    # there, we just increment it by 1
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in sender_mail:
            sender_mail[words[1]] = 1
        else:
            sender_mail[words[1]] += 1

# next we loop through our dictionary (as a list) and append the key and value as tuple elements in
# our new list above, the we sort this new list in a reverse order
for key, val in list(sender_mail.items()):
    sender_list.append((val, key))

sender_list.sort(reverse=True)

# lastly, we loop through the tuples in our reversed list, checking the value and the key
# we print the first element from the list which should be the one with the highest commits
for count, email in sender_list[:1]:
    print(email, count)

