# Write a program to read through a file and print the 
# contents of the file (line by line) all in upper case.

file = input('Please enter a file name with it\'s correct extension:\n')
f = open(file)

for line in f:
    line = line.rstrip()
    print(line.upper())