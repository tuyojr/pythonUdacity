# Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

pay = hours * rate

print("You are to pay {}".format(pay))