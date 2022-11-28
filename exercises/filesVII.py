# Sometimes when programmers get bored or want to have a bit of fun, 
# they add a harmless Easter Egg to their program Modify the program 
# that prompts the user for the file name so that it prints a funny 
# message when the user types in the exact file name "na na boo boo". 
# The program should behave normally for all other files which exist 
# and don't exist. Here is a sample execution of the program:

# python egg.py
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt

# python egg.py
# Enter the file name: missing.tyxt
# File cannot be opened: missing.tyxt

# python egg.py
# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!

file = input('Please enter a file name with it\'s correct extension:\n')

try:
    f = open(file)
except:
    if file == 'my akh' or file == 'wagwan' or file == 'Wagwan':
        print('\nZone 2K!\nMoscow B!\nWagwan, wanna get splashed?\nDo you want me to back it out?!\n\nBAZINGA!')
        exit()
    else:
        print('The file "{}" could not be opened because it does not exist.'.format(file))
        exit()

count = 0

for line in f:
    if line.startswith('Subject:'):
        count += 1
print('There were {} subjects in the {} file.'.format(count, file))