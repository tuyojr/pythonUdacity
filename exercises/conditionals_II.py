# Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error message. 
# If the score is between 0.0 and 1.0, print a grade using 
# the following table:

# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
# < 0.6    F

score = input('Please enter you score (between 0.0 and 1.0): ')
try:
    float(score)
    if float(score) >= 0.9 and float(score) <= 1.0:
        print('Perfect Score! {} is a grade A'.format(score))
    elif float(score) >= 0.8 and float(score) <= 0.9:
        print('Great Score! {} is a grade B'.format(score))
    elif float(score) >= 0.7 and float(score) <= 0.8:
        print('Good Score! {} is a grade C'.format(score))
    elif float(score) >= 0.6 and float(score) <= 0.7:
        print('Well Done! {} is a grade D'.format(score))
    elif float(score) >= 0.0 and float(score) <= 0.6:
        print('You can do better! {}, is a grade F'.format(score))
    else:
        print('Invalid Score, please run the program again')
except:
    print('Invalid Score, please run the program again')
