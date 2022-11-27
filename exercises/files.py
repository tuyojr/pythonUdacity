# This prints a double space between each line
f = open('demo.txt')
for line in f:
    if line.startswith('From:'):
        print(line)

# This removes the double space
for lines in f:
    lines = lines.rstrip()
    if lines.startswith('From:'):
        print(lines)
