# Exercise 3: Write a program to read through a mail log, build a 
# histogram using a dictionary to count how many messages have 
# come from each email address, and print the dictionary.

# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

sender = dict()
sender_list = list()

file_name = input('Enter the file name with a correct extension: ')

with open(file_name) as f:
    for line in f:
        sender_list = line.split()

        if len(sender_list) > 3 and line.startswith("From"):
            senders = sender_list[1]
        elif senders not in sender:
            sender[senders] = 1
        else:
            sender[senders] += 1
    print(sender)