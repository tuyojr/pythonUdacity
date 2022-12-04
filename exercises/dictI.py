# Exercise 1: [wordlist2]

# Write a program that reads the words in words.txt and stores 
# them as keys in a dictionary. It doesn't matter what the values 
# are. Then you can use the in operator as a fast way to check 
# whether a string is in the dictionary.


file = input('Please input a file name with the correct extension:\n')

f = open(file)

new_dict = dict()
count = 1
for word in f:
    word = word.rstrip()
    if word in new_dict:
        new_dict[word] = count + 1
    else: 
        new_dict[word] = count
print(new_dict)