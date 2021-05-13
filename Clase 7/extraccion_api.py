import requests
import json
import pprint

direccion = "Rivadavia y Loria"
localidad = 'caba'
#print(direccion + ',' + localidad)
direccion_formato = requests.utils.quote(direccion + ', ' + localidad)
#print(direccion_formato)
url = 'http://servicios.usig.buenosaires.gob.ar/normalizar/?direccion=' + direccion_formato
print(url)
respuesta = requests.get(url).text
dire_normalizada = json.loads(respuesta)
pprint.pprint(dire_normalizada)
