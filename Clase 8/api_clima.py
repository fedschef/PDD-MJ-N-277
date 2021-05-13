import json
import requests
import pprint

key = ''
ciudad = 'San Juan, Argentina'
ciudad_cod = requests.utils.quote(ciudad)
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + ciudad_cod + '&lang=es&units=metric&appid=' + key
objeto = json.loads(requests.get(url).text)
print(ciudad, 'Clima general ->', objeto['weather'][0]['description'])
print(ciudad, 'Temperatura ->', objeto['main']['temp'], '° C')