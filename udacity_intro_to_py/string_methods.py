# What happens when you call a string method like islower() 
# on a float object? For example, 13.37.islower(). =====> An error occurs

# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# and try them out here

print("learning with udacity is fun!".capitalize())


# format() Practice
# Use the coding space below to practice using the format() string method. 
# There are no right or wrong answers here, just practice!

# Write two lines of code below, each assigning a value to a variable
val1 = "learning with udacity is {}"
val2 = "learning with udacity is also {}"

# Now write a print statement using .format() to print out a sentence and the 
#   values of both of the variables
print(val1.format("challenging!"))
print(val2.format("fun!"))


# Quiz: String Methods Coding Practice
# Below, we have a string variable that contains the first verse of the poem, 
# If by Rudyard Kipling. Remember, \n is a special sequence of characters that 
# causes a line break (a new line).
# verse = "If you can keep your head when all about you\n  Are losing theirs and 
# blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But 
# make allowance for their doubting too;\nIf you can wait and not be tired by 
# waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t 
# give way to hating,\n  And yet don’t look too good, nor talk too wise:"

# Use the code editor below to answer the following questions about verse and use 
# Test Run to check your output in the quiz at the bottom of this page.

# What is the length of the string variable verse?
# What is the index of the first occurrence of the word 'and' in verse?
# What is the index of the last occurrence of the word 'you' in verse?
# What is the count of occurrences of the word 'you' in the verse?
# You will need to refer to Python's string methods documentation.

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
print(len(verse))
print(verse.index("and"))
print(verse.rfind("you"))
print(verse.count("you"))

# Another way to do this to make it look more appealing is...

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!

final_output = "The verse has a length of {} characters.\nThe word 'and' \
occurs at the {}th index in the verse.\nThe last occurrence of the word 'you' \
was at the {}th index.\nThe word 'you' appears {} times in the verse."


verse_length = len(verse)
word_index = verse.index('and')
last_index = verse.rfind('you')
word_occur = verse.count('you')

print(final_output.format(verse_length, word_index, last_index, word_occur))
