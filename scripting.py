# Question: Create a function that opens the flowers.txt, 
# reads every line in it, and saves it as a dictionary. 
# The main (separate) function should take user input 
# (user's first name and last name) and parse the user 
# input to identify the first letter of the first name. 
# It should then use it to print the flower name with the 
# same first letter (from dictionary created in the first function).

# Sample Output:

# >>> Enter your First [space] Last name only: Bill Newman
# >>> Unique flower name with the first letter: Bellflower

# Write your code here

# HINT: create a dictionary from flowers.txt

# A function that accepts the filename as an argument
def create_dict(file):

    # A dictionary to store the files from the input filename
    flower_dict = {}

    # First open the file to read it
    with open('flowers.txt', 'r') as f:

        # Loop through each line
        for line in f:

            # For each item at the 0 index, put it in a variable which will be set 
            # as the key (it is separated by a colon), also change it to lower case
            letter = line.split(": ")[0].lower()
            
            # For each flower name which is at the index 1, remove the : before it 
            # and put it in a variable flower 
            flower = line.split(": ")[1].strip()
            
            # Next set each letter in the dictionary to it's respective flower and 
            # return the created dictionary's value
            flower_dict[letter] = flower

    return flower_dict
            

# HINT: create a function to ask for user's first and last name

# Create a main function that uses the previous function
def main(): 

    # Create a variable the stores the created dictionary for the required file
    flower_d = create_dict('flowers.txt')

    # Create a variable that stores the user's full name in the required format
    full_name = input("Enter your First [space] Last name only: ")

    # Create a variable that stores the users first name in lower case
    first_name = full_name[0].lower()

    # Create a variable that stores the first letter of the user's first name
    first_letter = first_name[0]

# print the desired output

    # Print an output that makes use of the first letter of the user as a reference to the created dictionary
    print("Unique flower name with the first letter {}".format(flower_d[first_letter]))


# Call the main function
main()