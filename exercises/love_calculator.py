print("\nWelcome to the Love Calculator!\n")
name1 = input("What is your name? \n")
name2 = input("\nWhat is their name? \n")

combined_names = name1 + name2
lowercase_names = combined_names.lower()

t = lowercase_names.count('t')
r = lowercase_names.count('r')
u = lowercase_names.count('u')
e = lowercase_names.count('e')

true = t + r + u + e

l = lowercase_names.count('l')
o = lowercase_names.count('o')
v = lowercase_names.count('v')
e = lowercase_names.count('e')

love = l + o + v + e

love_score = int(str(love) + str(true))

if (love_score < 10) or (love_score > 90):
    print("Your score is {}, you go together like coke and mentos.".format(love_score))
elif (love_score >= 40) and (love_score <= 50):
    print("Your score is {}, you are alright together.".format(love_score))
else:
    print("Your score is {}.".format(love_score))

