# The sort function works the same way as when comparing tuples. 
# It sorts primarily by first element, but in the case of a tie, 
# it sorts by second element, and so on.

# This feature lends itself to a pattern called DSU for

# Decorate
# a sequence by building a list of tuples with one or more sort 
# keys preceding the elements from the sequence, e.g. 3 is the key in [(3, 'but')]

# Sort
# the list of tuples using the Python built-in sort, and

# Undecorate
# by extracting the sorted elements of the sequence. 'but' is the element in [(3, 'but')]

# [DSU]

# For example, suppose you have a list of words and you want to sort them from longest to shortest:

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
print(t)

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

print(res)