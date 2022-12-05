# Exercise 2: Write a program that categorizes each mail message by 
# which day of the week the commit was done. To do this look for lines 
# that start with "From", then look for the third word and keep a 
# running count of each of the days of the week. At the end of the 
# program print out the contents of your dictionary (order does not matter).

# Sample Line:
#     From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Sample Execution:
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

# create an empty dictionary to hold the days of the week messages were sent
days = {}

# create an empty list to hold the recurring days
days_list = []

# Prompt the user to enter the file name
file_name = input('Enter the file name with a correct extension: ')

# use the with method to open the file and close it when done
with open(file_name) as f:

    # loop through each line of the file
    for line in f:

        # set the value of the empty list above to each line in the file 
        days_list = line.split()

        # check if the line in the list is more than 3 words and starts with the keyword we want.
        # if it is, set the value of a new variable that stores the 3rd index which is where what
        # we need is.
        # next, check if the value is not in our dictionary and set it with a value of 1
        # if the value is already there, we just increase the value, indicating how many times it occurs.
        # lastly we print our new value to the screen
        if len(days_list) > 3 and line.startswith('From'):
            day = days_list[2]
        elif day not in days:
            days[day] = 1
        else:
            days[day] += 1
    print (days)