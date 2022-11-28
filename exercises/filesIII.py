file_name = input('Please Enter the file name with it\'s extension:\n')

try:
    f = open(file_name)
except:
    print('The file "{}" cannot be opened because it does not exist.'.format(file_name))
    exit()

count = 0

for line in f:
    # line = line.rstrip()
    if line.startswith('Subject:'):
        count += 1
        # continue
print('There are {} lines that start with "Subject:" in {}'.format(count, file_name))