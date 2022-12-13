"""This script creates a file using the current date and time
as the name of the file.
"""

# First, let's import the datetime library
import datetime

# Extract the current date and time  and store it in a variable
file_name = datetime.datetime.now()

# create a function that creates the file using the date and time as the file name
def create_file():

    # Formatting characters found at strftime.org are used to depict how the file should
    # be named using the strftime method, because the datetime.datetime.now() format
    # will not be accepted as a correct name for the file
    # %Y = Year, %m = month, %d = day, %H = Hour, %M = Minutes
    with open(file_name.strftime("%Y-%m-%d-%H-%M"), "w") as file:
        file.write("This file was created on {} at {}min(s) past {}hour(s).".format(file_name.strftime('%d-%m-%Y'),file_name.strftime('%M'),file_name.strftime('%H')))

create_file()