import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter the web URL: ")
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))