# Exercise 1: Write a program which repeatedly reads numbers 
# until the user enters "done". Once "done" is entered, print 
# out the total, count, and average of the numbers. If the user 
# enters anything other than a number, detect their mistake using 
# try and except and print an error message and skip to the next number.

count = 0
total = 0
avg = 0

while True:
  line = input ('Enter a number \n>')
  try:
     line = float(line)
     count = count + 1 
     total = total + line
     avg = total / count
  except:
    if line == 'Done' or line == 'done':
      break
    else:
      print('Invalid Input')
      continue

print('You entered a total of {} numbers, the sum total of those numbers equals {}, and the average of these numbers is {}.'.format(count, total, avg))
    




# Exercise 2: Write another program that prompts for a list 
# of numbers as above and at the end prints out both the maximum 
# and minimum of the numbers instead of the average.

user_list = []
num_count = 0
value = True

# Use a while loop that executes a try block to update the user's list
# Also we want to keep track of the numbers added to the list by updating the 
# num_count variable
while value:
  try:
    user_input = input('Enter a number you want to add to the list:\n>')
    user_input = float(user_input)
    user_list.append(user_input)
    num_count = num_count + 1
  except:
    if user_input == 'Done' or user_input == 'done':
      break
    else:
      print('Invalid user input.')
      continue

smallest_num = min(user_list)
largest_num = max(user_list)

print('The smallest number in your list is {}, and the largest number is {}.'.format(smallest_num, largest_num))