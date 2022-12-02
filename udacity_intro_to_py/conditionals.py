# Practice: Which Prize
# Write an if statement that lets a competitor know which of these 
# prizes they won based on the number of points they scored, which 
# is stored in the integer variable points.

# Points	Prize
# 1 - 50	wooden rabbit
# 51 - 150	no prize
# 151 - 180	wafer-thin mint
# 181 - 200	penguin
# All of the lower and upper bounds here are inclusive, and points 
# can only take on positive integer values up to 200.

# In your if statement, assign the result variable to a string holding 
# the appropriate message based on the value of points. If they've won 
# a prize, the message should state "Congratulations! You won a 
# [prize name]!" with the prize name. If there's no prize, the message 
# should state "Oh dear, no prize this time."

# Note: Feel free to test run your code with other inputs, but when you 
# submit your answer, only use the original input of points = 174. You 
# can hide your other inputs by commenting them out.

points = 174 # use this input to make your submission

# write your if statement here

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)




# Quiz: Guess My Number
# You decide you want to play a game where you are hiding a number 
# from someone. Store this number in a variable called 'answer'. 
# Another user provides a number called 'guess'. By comparing guess 
# to answer, you inform the user if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how their 
# guess compares to the answer.

answer = 16 #provide answer
guess = 8 #provide guess

if guess < answer: #provide conditional
    result = "Oops!  Your guess was too low."
elif guess > answer: #provide conditional
    result = "Oops!  Your guess was too high."
elif guess == answer: #provide conditional
    result = "Nice!  Your guess matched the answer!"

print(result)






# Quiz: Tax Purchase
# Depending on where an individual is from we need to tax them 
# appropriately. The states of CA, MN, and NY have taxes of 7.5%, 9.5%, 
# and 8.9% respectively. Use this information to take the amount of a 
# purchase and the corresponding state to assure that they are taxed 
# by the right amount.

state = 'CA' #Either CA, MN, or NY
purchase_amount = 100 #amount of purchase

if state == 'CA':#provide conditional for checking state is CA
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':#provide conditional for checking state is MN
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':#provide conditional for checking state is NY
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)

