import json
import pprint
import requests

url= 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/vicejefatura-de-gobierno/estaciones-saludables/estaciones-saludables.geojson'

contenido =requests.get(url).text
objeto =json.loads(contenido) # este es loads en lugar de load pq contenido es un strin. si fuera un jason seria solo load
pprint.pprint(objeto)

archivo= open('estacsalud.csv', 'w', encoding= 'utf-8')
archivo.write('latitude;longitude;name;label\n')

for i in range(len(objeto['features'])):
    name= objeto['features'][i]['properties']["nombre"]
    label= objeto['features'][i]['properties']["direccion_"]
    longitude = objeto['features'][i]['geometry']['coordinates'][0]
    latitude = objeto['features'][i]['geometry']['coordinates'][1]
    print (i+1,'-', name, '-', label, '-', longitude, '-', latitude)
    archivo.write(str(latitude) + ';' + str(longitude) + ';' + label + ';' + name + '\n')

archivo.close()