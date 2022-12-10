# Write a simple program to simulate the operation of the grep command 
# on Unix. Ask the user to enter a regular expression and count the 
# number of lines that matched the regular expression:

# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author

# $ python grep.py
# Enter a regular expression: ^X-
# mbox.txt had 14368 lines that matched ^X-

# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4218 lines that matched java$

# first import the library for regular expressions
import re

# prompt the user to input their regular expression
regex = input('Please enter a regular expression: ')

# convert the user input to a string
exp = str(regex)

# open the file that we want to search through for the user's regular expression
file = open('demo_short.txt')

# a variable to keep track of the user's search
count = 0

# loop through the file
for line in file:

    # remove the new line character at the end of each line
    line = line.rstrip()

    # use the findall method to search for the user's expression
    x = re.findall(exp, line)

    # if the list created from finding the user's expression is not empty, increase the count
    if x != []:
        count += 1

# print the user's result
print("The 'demo_short.txt' file had {} lines that matched '{}'.".format(count, regex))
