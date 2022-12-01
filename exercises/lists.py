# Exercise 1:

# Write a function called chop that takes a list and modifies it, 
# removing the first and last elements, and returns None.


def chop(a_list):
    # delete the first element
    del a_list[0]

    # delete the last element
    del a_list[-1]

    return None

print("Your inputs will be turned into a list. Type 'done' to exit and see your list.")

# An empty list to hold all our users elements
user_list = []

# A while loop the continues to run if true
while True:

    # Prompt the user for input
    elements = input("Please input what you want in your list: ")

    # An if condition that breaks from the loop
    if elements == 'done':
        break

    # Add the values the user input into the empty list
    else:
        user_list.append(elements)

# call the chop function on the user's newly created list
chop(user_list)

# display the user's newly created list after chopping
print(user_list)