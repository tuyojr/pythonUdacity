# As your file processing programs get more complicated, 
# you may want to structure your search loops using continue. 
# The basic idea of the search loop is that you are looking for 
# "interesting" lines and effectively skipping "uninteresting" 
# lines. And then when we find an interesting line, we do 
# something with that line.

f = open('demo.txt')
for line in f:

    # Removes whitespaces at the end of each line
    line = line.rstrip()

    # If the line does not start with 'From:', continue the loop until you find one
    if not line.startswith('From:'):
        continue
    print(line)