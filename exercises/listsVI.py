# Exercise 6: Rewrite the program that prompts the user for 
# a list of numbers and prints out the maximum and minimum 
# of the numbers at the end when the user enters "done". 
# Write the program to store the numbers the user enters 
# in a list and use the max() and min() functions to compute 
# the maximum and minimum numbers after the loop completes.

# Enter a number: 6
# Enter a number: 2
# Enter a number: 9
# Enter a number: 3
# Enter a number: 5
# Enter a number: done
# Maximum: 9.0
# Minimum: 2.0

print("Your inputs will be turned into a list. Type 'done' to exit and see your list.")

# An empty list to hold all our users elements
user_list = []

# A while loop the continues to run if true
while True:

    # Prompt the user for input
    elements = input("Please input numbers you want in your list: ")

    # An if condition that breaks from the loop
    if elements == 'done':
        break

    # Add the values the user input into the empty list
    else:
        user_list.append(int(elements))
        
maximum = max(user_list)
minimum = min(user_list)

# display the user's newly created list
print(user_list)
print('Maximum: {}'.format(float(maximum)))
print('Minimum: {}'.format(float(minimum)))