import requests
from bs4 import BeautifulSoup as bs
import csv

url = "https://www.ambito.com"
html = requests.get(url).text
dom = bs(html, features='html.parser')

titulos_articulos = [etiqueta.a.get('title', "N/A") for etiqueta in dom.find_all(class_='article-kicker')]
link_articulos = [etiqueta.a.get('href', "N/A") for etiqueta in dom.find_all(class_='article-kicker')]

# etiquetas = dom.find_all(class_="title")
# for etiqueta in etiquetas:
#    etiqueta_target = etiqueta.a
#    titulo = etiqueta_target.text
#    link = etiqueta_target.get('href', "N/A")
#    print(titulo, ':', link)

with open('noticias_principales.csv', 'w', newline='') as noticias:
    salida = csv.writer(noticias, delimiter=';')
    salida.writerow(['title', 'link'])
    
    for i in range(len(titulos_articulos)):
        salida.writerow([titulos_articulos[i], link_articulos[i]])
