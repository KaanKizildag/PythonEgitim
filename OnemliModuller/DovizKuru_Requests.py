import requests
import json

# https://api.exchangeratesapi.io/latest?base=USD
base = input('baz kuru girin: ').upper()
exchange = input('Dönüştürmek istediğiniz birim: ').upper()
miktar = float(input('Kaç {base} var? '.format(base = base)))

url = 'https://api.exchangeratesapi.io/latest?base='+base
r = requests.get(url)
result = json.loads(r.content)
rate = float(result['rates'][exchange])
print(f'1 {base} = {exchange} {rate} '
      .format(base = base,
              exchange = exchange,
              rate = rate))

result = rate * miktar

print(f'{miktar} {base} = {result} {exchange}'
      .format(miktar,base,result,exchange))

