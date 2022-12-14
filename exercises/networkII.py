import urllib.request, urllib.parse, urllib.error

file_link = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in file_link:
#     print(line.decode().strip())

count = dict()
for line in file_link:
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)
