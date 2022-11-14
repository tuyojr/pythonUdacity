# Quiz: Define a Dictionary

# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {
    'Shanghai': 17.8,
    'Istanbul': 13.3,
    'Karachi': 13.0,
    'Mumbai': 12.5
}

print(population)
print('Karachi' in population)
print(population['Mumbai'])
print(population.get('Istanbul'))
print(population.get('Lagos'))
print(population.get('Lagos') is None)
print(population.get('Lagos') is not None)



# Which of these could be used as the key for a dictionary? 
# (Choose all that apply.) Hint: Dictionary keys must be immutable, 
# that is, they must be of a type that is not modifiable.

#  ===> str, int, float



# What happens if we look up a value that isn't in the dictionary? 
# Create a test dictionary and use the square brackets to look up a 
# value that you haven't defined. What happens?
# ===> A KeyError occurs.



# Checking for Equality vs. Identity: == vs. is
# What will the output of the following code be? 
# (Treat the commas in the multiple choice answers as newlines.)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b) # True
print(a is b) # True
print(a == c) # True
print(a is c) # True

# List a and list b are equal and identical. List c is equal to a 
# (and b for that matter) since they have the same contents. 
# But a and c (and b for that matter, again) point to two different objects, 
# i.e., they aren't identical objects. That is the difference between checking f
# or equality vs. identity.



# Use the dictionary below to answer ALL of the questions regarding 
# dictionaries. Consider you have a dictionary named animals that looks like this:

animals = {
    'dogs': [20, 10, 15, 8, 32, 15], 
    'cats': [3,4,2,8,2,4], 
    'rabbits': [2, 3, 3], 
    'fish': [0.3, 0.5, 0.8, 0.3, 1]
}

# The data type of the keys in the dictionary. ===> String
# The data type of the values in the dictionary. ===> List
# The result of animals['dogs']. ===> [20, 10, 15, 8, 32, 15]
# The result of animals['dogs'][3]. ===> 8
# The result of animals[3] ===> Key Error
# The result of animals['fish'] ===> [0.3, 0.5, 0.8, 0.3, 1]

