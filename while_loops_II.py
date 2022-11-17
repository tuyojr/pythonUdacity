# Quiz: Count By
# Suppose you want to count from some number start_num by 
# another number count_by until you hit a final number end_num. 
# Use break_num as the variable that you'll change each time 
# through the loop. For simplicity, assume that end_num is always 
# larger than start_num and count_by is always positive.

# Before the loop, what do you want to set break_num equal to? How 
# do you want to change break_num each time through the loop? What 
# condition will you use to see when it's time to stop looping?

# After the loop is done, print out break_num, showing the value that 
# indicated it was time to stop looping. It is the case that break_num 
# should be a number that is the first number larger than end_num.

start_num = 0 #provide some start number
end_num = 10 #provide some end number that you stop when you hit
count_by = 2 #provide some number to count by 

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
break_num = start_num

while break_num < end_num:
    break_num += count_by

print(break_num)





# Quiz: Count By Check
# Suppose you want to count from some number start_num by another number 
# count_by until you hit a final number end_num, and calculate break_num 
# the way you did in the last quiz.

# Now in addition, address what would happen if someone gives a start_num 
# that is greater than end_num. If this is the case, set result to "Oops! 
# Looks like your start value is greater than the end value. Please try 
# again." Otherwise, set result to the value of break_num.

start_num = 0 #provide some start number
end_num = 10 #provide some end number that you stop when you hit
count_by = 2 #provide some number to count by 

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
break_num = start_num

if end_num > start_num:
    while break_num < end_num:
        break_num += count_by
        result = break_num
else:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."


print(result)




# Quiz: Nearest Square
# Write a while loop that finds the largest square number less than an 
# integer limit and stores it in a variable nearest_square. A square 
# number is the product of an integer multiplied by itself, for example 
# 36 is a square number because it equals 6*6.

# For example, if limit is 40, your code should set the nearest_square to 36.

limit = 40

# write your while loop here
num = 0

# first, while the squared value of num is less than the limit, increase the value of num
# set the value of the nearest_sqaure less than the limit to the value of num squared 
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2


print(nearest_square)




# You need to make sure the while loop has: 
# 1) a condition expression that will be assessed and when met, will allow you to exit the loop 
# 2) make sure the loop is advancing 
# 3) the value of the condition variables is changing with each iteration of the loop.




# Your code should add up the odd numbers in the list, but only up to the first 
# 5 odd numbers together. If there are more than 5 odd numbers, you should stop 
# at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.

# Would you use a while or a for loop to write this code?

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 
            87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

# A variable to hold the number of odd numbers in the list
odd_num_count = 0

# A variable to hold the sum of the odd numbers in the list
odd_sum = 0

# A variable to keep track of where we are in the list
list_index = 0

# A variable to hold the length of the list
len_num_list = len(num_list)

# We want to keep checking while the number of odd numbers is less than 5 (required numbers we want),
# and the index where we are is less than the length of the list. If the value at the index where we
# are in the list does not have a remainder = 0, we want to add the value at that index to the odd_sum
# variable and than increase our odd number count by 1. The condition keeps executing until our list_index
# is not more than 5

while (odd_num_count < 5) and (list_index < len_num_list): 
    if num_list[list_index] % 2 != 0:
        odd_sum += num_list[list_index]
        odd_num_count += 1
    list_index += 1

print ("The numbers of odd numbers added are: {}".format(odd_num_count))
print ("The sum of the odd numbers added is: {}".format(odd_sum))