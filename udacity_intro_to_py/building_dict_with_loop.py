# Let's start with a list containing the words in a series of book titles:
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

# Create an empty dictionary.
word_counter = {}

# Iterate through each element in the list. If an element is already 
# included in the dictionary, add 1 to its value. If not, add the 
# element to the dictionary and set its value to 1.
for word in book_title:
    # the if statement checks if word is in the word_counter dictionary.
    # Since it doesn't yet, the statement word_counter[word] = 1 adds 
    # great as a key to the dictionary with a value of 1.Then, it leaves 
    # the if else statement and moves on to the next iteration of the for 
    # loop. word now takes the value expectations and repeats the process.
    # When the if condition is not met, it is because that word already 
    # exists in the word_counter dictionary, and the statement 
    # word_counter[word] = word_counter[word] + 1 increases the count of 
    # that word by 1.
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

print(word_counter)

# Using the get() method

word_counter1 = {}

# The for loop iterates through the list as we saw earlier. The for loop 
# feeds 'great' to the next statement in the body of the for loop.In this 
# line: word_counter[word] = word_counter.get(word,0) + 1, since the key 
# 'great' doesn't yet exist in the dictionary, get() will return the value 
# 0 and word_counter[word] will be set to 1.Once it encounters a word that 
# already exists in word_counter (e.g. the second appearance of 'the'), 
# the value for that key is incremented by 1. On the second appearance of 
# 'the', the key's value would add 1 again, resulting in 2. Once the for 
# loop finishes iterating through the list, the for loop is complete.

for word in book_title:
    word_counter1[word] = word_counter1.get(word, 0) + 1
print(word_counter1)




