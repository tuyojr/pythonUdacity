# Exercise 5: This program records the domain name (instead of the address) 
# where the message was sent from instead of who the mail came from (i.e., 
# the whole email address). At the end of the program, print out the contents 
# of your dictionary.

# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

file_name = input('Enter the file name with a correct extension: ')
email_domain = {}
file_list = []

with open(file_name) as f:
    for line in f:
        file_list = line.split()
        if line.startswith('From'):
            mail = file_list[1]
            # print(mail)
            domain = mail.split('@')[1]
            if domain not in email_domain:
                email_domain[domain] = 1
            else:
                email_domain[domain] += 1
    print(email_domain)
