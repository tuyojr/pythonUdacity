# This prints a double space after each line
f = open('demo.txt')
for line in f:
    if line.startswith('From:'):
        print(line)

# This removes the double space after each line
for lines in f:
    lines = lines.rstrip()
    if lines.startswith('From:'):
        print(lines)
