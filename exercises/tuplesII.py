# Exercise 2: This program counts the distribution of the hour of 
# the day for each of the messages. You can pull the hour from the 
# "From" line by finding the time string and then splitting that 
# string into parts using the colon character. Once you have accumulated 
# the counts for each hour, print out the counts, one per line, 
# sorted by hour as shown below.

# Sample Execution:

# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1


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
    if len(words) < 5 or words[0] != 'From':
        continue
    
    colon = words[5].find(':')
    hour = words[5][:colon]
    
    if hour not in sender_mail:
        sender_mail[hour] = 1
    else:
        sender_mail[hour] += 1

# next we loop through our dictionary (as a list) and append the key and value as tuple elements in
# our new list above, the we sort this new list in a reverse order
for key, val in list(sender_mail.items()):
    sender_list.append((val, key))

sender_list.sort()

# lastly, we loop through the tuples in our reversed list, checking the value and the key
# we print the first element from the list which should be the one with the highest commits
for key, val in sender_list:
    print("{} time(s) at {} HRs".format(key, val))
