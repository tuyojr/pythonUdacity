# Exercise 4: Add code to the above program to figure out who has the 
# most messages in the file.

# After all the data has been read and the dictionary has been created, 
# look through the dictionary using a maximum loop (see Section [maximumloop]) 
# to find who has the most messages and print how many messages the person has.

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195

sender = {}
sender_list = []

file_name = input('Enter the file name with a correct extension: ')
count = None

with open(file_name) as f:
    for line in f:
        sender_list = line.split()
        if len(sender_list) > 3 and line.startswith('From'):
            senders = sender_list[1]
        elif senders not in sender:
            sender[senders] = 1
        else:
            sender[senders] += 1
    print('\nSenders Dictionary: ', sender)

for email in sender:
    top_sender = sender[email]
    if count == None or top_sender > count:
        count = top_sender
        sender_email = email
print('\n{} sent the most mails with a total of {} mails'.format(sender_email, count))