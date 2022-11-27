while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# Code: http://www.py4e.com/code3/copytildone2.py
# Or select Download from this trinket's left-hand menu



# Look what happens when the user enters an empty line of input:
# > hello there
# hello there
# > # don't print this
# > print this!
# print this!
# >
# Traceback (most recent call last):
#   File "copytildone.py", line 3, in <module>
#     if line[0] == '#':
# IndexError: string index out of range

# The code works fine until it is presented an empty line. Then there is 
# no zero-th character, so we get a traceback. There are two solutions to 
# this to make line three "safe" even if the line is empty.