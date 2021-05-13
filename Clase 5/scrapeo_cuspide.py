from bs4 import BeautifulSoup as BS
import requests

url = 'https://www.cuspide.com/cienmasvendidos'
html = requests.get(url)
html.encoding = 'utf-8'
html = html.text

dom = BS(html, features='html.parser')
etiqueta = dom.find(id='ctl00_ContentPlaceHolder1_top100UC_rptMasVendidos_ctl04_img_tapa')

articulos = dom.find_all('article')

print(articulos[0].figure.div.a['href'])

#%%
titulo_unico = etiqueta['title']

libros = dom.find_all(class_='lazy')
for i in range(len(libros)):
   print(i+1, libros[i]['title'])