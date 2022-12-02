# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     words = line.split()
#     # print 'Debug:', words
#     if len(words) == 0 : continue
#     if words[0] != 'From' : continue
#     print(words[2])

# Rewrite the guardian code in the above example without two 
# if statements. Instead, use a compound logical expression 
# using the and logical operator with a single if statement.

f = open('demo.txt')
count = 0

for line in f:
    words = line.split()
    # if len(words) == 0:
    #     continue
    # elif words[0] != 'From':
    #     count += 1
    #     continue
    if len(words) == 0 or words[0] != 'From':
        count += 1
        continue
    else:
        print("A mail came in from {} on a {}.".format(words[1], words[2]))
print('There are {} lines that have some text in the file.'.format(count))