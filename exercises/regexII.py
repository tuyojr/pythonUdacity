# Write a program to look for lines of the form

# `New Revision: 39772`
# and extract the number from each of the lines using a regular 
# expression and the findall() method. Compute the average of 
# the numbers and print out the average.

# Enter file:mbox.txt
# 38549.7949721

# Enter file:mbox-short.txt
# 39756.9259259

# import the regular expressions library
import re

# prompt the user to enter a file name
file_name = input('Please enter a file name with the correct extension: ')

# use the try and except block to check the file entered exists
try:
    file = open(file_name)
except FileNotFoundError:
    print("The file '{}' could not be found. Run the program again.".format(file_name))
    exit()

# create an empty list to store each number
numbers = []

# create a variable to hold the average of all the numbers
avg = 0

# loop through each line in the file
for line in file:

    # remove the new line character at the end of each line
    line = line.rstrip()

    # use the .findall method to search for the lines with the numbers we need
    num_list = re.findall('^New Revision: ([0-9.]+)', line)

    # loop through each number in the list of numbers created with .findall method
    for value in num_list:

        # convert each number from a string to a float
        value = float(value)

        # populate the global number list created with the new floats
        numbers = numbers + [value] 

# use the sum() method to add all the numbers in the number list and store them in a variable
total = sum(numbers)

# count the total number of numbers in the numbers list
count = float(len(numbers))

# check if the count exists, if it does, calculate the average of the numbers and store them in a variable
if count:
    avg = total / count

# display the result
print('The average of all New Revision is: {}'.format(avg))