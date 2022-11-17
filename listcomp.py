# Quiz: Extract First Names
# Use a list comprehension to create a new list first_names 
# containing just the first names in names in lowercase.

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names] # write your list comprehension here
print(first_names)


# Quiz: Multiples of Three
# Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.

multiples_3 = [x*3 for x in range(1, 21)] # write your list comprehension here
print(multiples_3)