import json
import pprint
import requests

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/hospitales/hospitales.geojson'
contenido = requests.get(url).text
objeto = json.loads(contenido)
#pprint.pprint(objeto)
for i in range(len(objeto['features'])):
   nombre_hosp = objeto['features'][i]['properties']['NOM_MAP']
   domicilio = objeto['features'][i]['properties']['DOM_NORMA']
   especialidad = objeto['features'][i]['properties']['TIPO_ESPEC']
   web = objeto['features'][i]['properties']['WEB']
   long = objeto['features'][i]['geometry']['coordinates'][0]
   lat = objeto['features'][i]['geometry']['coordinates'][1]
   print (i+1, nombre_hosp, '-', domicilio, '-', especialidad, '-', web, '-', lat, long)
   