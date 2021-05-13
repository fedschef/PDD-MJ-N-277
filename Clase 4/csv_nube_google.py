import requests
import csv
from io import StringIO

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT651r_njGaU1HoLcQJKHKO3-eUftz7TxK5s4a4llLj73uwu6MKK5a3MdOI_xGCapJDrSFs9TiPEagN/pub?gid=34778314&single=true&output=csv'
respuesta = requests.get(url)
contenido = respuesta.text
archivo = StringIO(contenido)
tabla = csv.reader(archivo)

with open('peliculas2.csv', 'w') as pelis:
   for linea in tabla:
      pelis.write(linea[1] + ',' + linea[0] + ',' + linea[2] + '\n')
