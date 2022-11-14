# Quiz: list to set
# What would the output of the following code be?

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b)) # ===> 5



# Quiz: add and pop

# Consider the following code:
# After executing this code, will the number 5 be a part of the set b?
# ===> Maybe

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()

# When you pop an element from a set a random element is removed 
# (remember that sets, unlike lists, are unordered so there is no 
# "last element"). The number 5 may or may not be removed.
