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
    