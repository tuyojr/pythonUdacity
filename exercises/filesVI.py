# Write a program to prompt for a file name, and then read 
# through the file and look for lines of the form:

# X-DSPAM-Confidence: 0.8475

# When you encounter a line that starts with "X-DSPAM-Confidence:" 
# pull apart the line to extract the floating-point number on the 
# line. Count these lines and then compute the total of the spam 
# confidence values from these lines. When you reach the end of 
# the file, print out the average spam confidence.

file = input("Please enter a file name with it\'s correct extension:\n")

try:
    f = open(file)
except:
    print("Could not open '{}' file because it does not exist. Please run the program again".format(file))
    exit()

count = 0
total_sum = 0

for line in f:
    if line.startswith('X-DSPAM-Confidence: '):
        count += 1

        # We get the idex because we know the number comes after the text
        num = float(line[20:26])
        total_sum += num
        result = total_sum/count
# print(count)
print('The total of the SPAM confidence is {}, and the average is {}.'.format(total_sum, result))