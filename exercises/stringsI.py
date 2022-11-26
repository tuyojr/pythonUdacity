# Exercise 3:
# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)
# Encapsulate this code in a function named count, and 
# generalize it so that it accepts the string and the 
# letter as arguments.

def count(word, abc):
    count = 0
    for letter in word:
        if letter == abc:
            count += 1
    return count

print(count('banana', 'a'))
        