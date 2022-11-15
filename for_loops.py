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

