import requests
import csv
from io import StringIO

url = 'https://eant.tech/cursos/recursos/peliculas.csv'
respuesta = requests.get(url)
contenido = respuesta.text
archivo = StringIO(contenido)
tabla = csv.reader(archivo)

with open('peliculas.csv', 'w') as pelis:
   for linea in tabla:
      pelis.write(linea[1] + ',' + linea[0] + ',' + linea[2] + '\n')
