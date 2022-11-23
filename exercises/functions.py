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
