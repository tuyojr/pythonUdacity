# import the XML (eXtensible Markup Language) parser
import xml.etree.ElementTree as ET

# create a docstring to hold the XML document
input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

# Create a variable that parses the XML input
stuff = ET.fromstring(input)

# use the findall method to find what you need from the parsed string
lst = stuff.findall('users/user')

# We want to display the amount of what we found above
print('User count:', len(lst))
print('')

# loop through each item in the elements we found above
for item in lst:

    # Find a tag we need and extract the text in it
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)

    # Find the attribute we need and extract it's value
    print('Attribute:', item.get("x"))
    print('')

# Code: http://www.py4e.com/code3/xml2.py
# Or select Download from this trinket's left-hand menu