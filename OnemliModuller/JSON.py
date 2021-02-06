import json

person = {'name':'Kaan', 'languages': ['Python','Java']}
personString = '{"name":"Hüseyin", "languages": ["C#","Angular"]}'
# çift tırnak olmalı !!
result = json.loads(personString)
# print(type(personString)) # burda neden str dönüyi?
# result = person['name']
# result = person['languages'][0]

# with open("Person.json",'r') as file:
#     result = file.read()
#     #print(result)
#     result = json.loads(result)
# 
# print(type(result)) # burda da list döniy?


# DICT TO JSON
person_dict = {
    'name' : 'Ali',
    'languages':['python','c#']
}
with open('Person_dict_to_json.json','w') as file:
    json.dump(person_dict, file)


result = json.dumps(person_dict,indent= 4)
print(result)