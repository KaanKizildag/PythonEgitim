import requests
import json
r = requests.get('https://jsonplaceholder.typicode.com/todos') # response = 200 --> Başarılı

result = r.json()
for i in result:
    print(i['title'])

print(type(result))

result = json.dumps(result,indent=4)
print(type(result))