# Quiz: Write a Docstring
# Write a docstring for the readable_timedelta function you defined earlier! 
# Remember the way you write your docstrings is pretty flexible! Look through 
# Python's docstring conventions https://peps.python.org/pep-0257/ and check out this Stack Overflow page
# https://stackoverflow.com/questions/3898572/what-are-the-most-common-python-docstring-formats 
# for some inspiration!


def readable_timedelta(days):
    # insert your docstring here
    """Calculating the number of weeks and days
    INPUT: 'days', this function takes one parameter which accounts for the number
    of days, the number of days is then broken down by week in the 'weeks' variables
    the // allows the output to be only whole numbers. The next variable 'remainder'
    adds the remaining integer when dividing the 'days' argument by the available number
    of days in a week (7).
    OUTPUT: We want to return a string that displays the number of weeks and the 
    number of days, when the a number is passed into the 'readable_timedelta' function.
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)