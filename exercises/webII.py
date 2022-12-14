import json

json_person = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''

info = json.loads(json_person)
print('User count:', len(info))
print('')

for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('Attribute:', item['x'])
    print('')

# Code: http://www.py4e.com/code3/json2.py
# Or select Download from this trinket's left-hand menu