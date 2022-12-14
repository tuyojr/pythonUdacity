import urllib.request, urllib.parse, urllib.error

page = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

for line in page:
    print(line.decode().strip())