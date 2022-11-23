# Working with the random module
import random

for i in range(10):
    x = random.random()
    print(x)
    
hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

def pay_computation():
    if hours <= 40:
        pay = hours * rate
    else:
        pay = ((hours - 40) * (rate * 1.5) + (40 * rate))
    return 'Your pay for this weeks is: {}'.format(pay)

print(pay_computation())

score = input('Please enter your score (between 0.0 and 1.0): ')

def grader():
    float(score)
    if float(score) >= 0.9 and float(score) <= 1.0:
        print('Perfect Score! Your grade is A.')
    elif float(score) >= 0.8 and float(score) <= 0.9:
        print('Great Score! Your grade is B.')
    elif float(score) >= 0.7 and float(score) <= 0.8:
        print('Good Score! Your grade is C.')
    elif float(score) >= 0.6 and float(score) <= 0.7:
        print('Well Done! Your grade is D.')
    elif float(score) >= 0.0 and float(score) <= 0.6:
        print('You can always do better, you got F.')
    else:
        print('Invalid Score!')

grader()

