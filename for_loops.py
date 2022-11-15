# Practice: Quick Brown Fox
# Use a for loop to take a list and print each element of the 
# list in its own line.

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Output:
# the
# quick
# brown
# fox
# jumped
# over
# the
# lazy
# dog

for word in range(len(sentence)):
    print(sentence[word])

# OR

for word in sentence:
    print(word)

# Practice: Multiples of 5
# Write a for loop below that will print out every whole 
# number that is a multiple of 5 and less than or equal to 30.
# This should output:
# 5
# 10
# 15
# 20
# 25
# 30

# Write a for loop using range() to print out multiples of 5 up to 30 inclusive

for multiple in range(5, 35, 5):
    print(multiple)





# Quiz: Create Usernames
# Write a for loop that iterates over the names list to create a usernames list. 
# To create a username for each name, make everything lowercase and replace spaces 
# with underscores. Running your for loop over the list:

# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# should create the list:

# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

# HINT: Use the .replace() method to replace the spaces with underscores. 
# Check out how to use this method here 
# https://stackoverflow.com/questions/12723751/replacing-instances-of-a-character-in-a-string/12723785#12723785

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append(name.lower().replace(' ', '_'))

print(usernames)



# Let's say instead of creating a new list, we want to modify the 
# names list itself with the changes and write the following code. 
# What would this do?

# for name in names:
#     name = name.lower().replace(" ", "_")

# print(names)

# Answer
# The printed output for the names list will look exactly like it did 
# in the first line. During each iteration, the name variable is set 
# to a string taken from the list. Then the assignment statement 
# creates a new string (name.lower().replace(" ", "_")) and changes 
# the name variable to that string. It doesn't modify the contents 
# of the names list at all. To modify the list you must operate on 
# the list itself, using range, as you saw earlier.



# Quiz: Modify Usernames with Range
# Write a for loop that uses range() to iterate over the positions in usernames 
# to modify the list. Like you did in the previous quiz, change each name to be 
# lowercase and replace spaces with underscores. After running your loop, this list

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for friend in range(len(usernames)):
    usernames[friend] = usernames[friend].lower().replace(' ', '_')
    print(usernames)




# Quiz: Tag Counter
# Write a for loop that iterates over a list of strings, tokens, and counts how many 
# of them are XML tags. XML is a data language similar to HTML. You can tell if a 
# string is an XML tag if it begins with a left angle bracket "<" and ends with a 
# right angle bracket ">". Keep track of the number of tags using the variable count.

# You can assume that the list of strings will not contain empty strings.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1
    

print(count)





# Quiz: Create an HTML List
# Write some code, including a for loop, that iterates over a list of 
# strings and creates a single string, html_str, which is an HTML list. 
# For example, if the list is items = ['first string', 'second string'], 
# printing html_str should output:

# <ul>
# <li>first string</li>
# <li>second string</li>
# </ul>
# That is, the string's first line should be the opening tag <ul>. 
# Following that is one line per element in the source list, surrounded 
# by <li> and </li> tags. The final line of the string should be the 
# closing tag </ul>.


items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li>{}</li>\n".format(item)
    
html_str += "</ul>"

print(html_str)




# Practice with range
# For each below, match the input code to the appropriate output.

print(list(range(4))) # ===> [0, 1, 2, 3]
print(list(range(4,8))) # ===> [4, 5, 6, 7]
print(list(range(4,10,2))) # ===> [4, 6, 8]
print(list(range(0,-5)))  # ===> []
