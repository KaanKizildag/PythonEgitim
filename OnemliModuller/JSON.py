import json

person = {'name':'Kaan', 'languages': ['Python','Java']}
personString = '{"name":"Hüseyin", "languages": ["C#","Angular"]}'
# çift tırnak olmalı !!
print(personString)
# result = person['name']
# result = person['languages'][0]

result = json.loads(personString)

#print(result)