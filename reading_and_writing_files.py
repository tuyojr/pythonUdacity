f = open('file.txt', 'r')
file_data = f.read()
f.close()

print(file_data)



writing = open('file', 'w')
writing.write('This is just a sample file.')
writing.close()
writing = open('file')
files = writing.read()
writing.close()

print(files)