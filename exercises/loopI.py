# Exercise 1: Write a while loop that starts at the last 
# character in the string and works its way backwards to 
# the first character in the string, printing each letter 
# on a separate line, except backwards.

value = 'Jermaine'
index = -1

while index < len(value):
    letter = value[index]
    print(letter)
    index -= 1