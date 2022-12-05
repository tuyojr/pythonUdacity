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

days = {}
days_list = []
file_name = input('Enter the file name with a correct extension: ')

with open(file_name) as f:
    for line in f:
        days_list = line.split()
        if len(days_list) > 3 and line.startswith('From'):
            day = days_list[2]
        if day not in days:
            days[day] = 1
        else:
            days[day] += 1
    print (days)