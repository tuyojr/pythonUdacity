f = open('file.txt', 'r')
file_data = f.read()
f.close()

print(file_data)



writing = open('file', 'w')
writing.write('This is just a sample file.')
writing.close()
writing = open('file')
files = writing.read()
writing.close()

print(files)




# Quiz: Flying Circus Cast List
# You're going to create a list of the actors who appeared in the 
# television programme Monty Python's Flying Circus.

# Write a function called create_cast_list that takes a filename as 
# input and returns a list of actors' names. It will be run on the 
# file flying_circus_cast.txt (this information was collected from imdb.com). 
# Each line of that file consists of an actor's name, a comma, and 
# then some (messy) information about roles they played in the programme. 
# You'll need to extract only the name and add it to a list. You might 
# use the .split() method to process each line.



