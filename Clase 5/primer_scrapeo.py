from bs4 import BeautifulSoup as BS

archivo_html = open('web_ejemplo.html', encoding='utf-8')
dom = BS(archivo_html, features= 'html.parser')
#print(dom.prettify())
#Captura por etiquetas

#primer_link = dom.a
primer_link = dom.find('a')
print(primer_link.text)

todos_los_links = dom.find_all('a')
print(todos_los_links[2].text)

for etiqueta in todos_los_links:
   print(etiqueta.text)
   
#Capturar valores por los atributos
print(primer_link['class'])
print(primer_link['href'])
print(primer_link['id'])

#Método de diccionario get
print(primer_link.get('data-minumero', "No existe"))
#Búsqueda más específica
parrafo_buscado = dom.find(id='otros-integrantes')
#clase_historia = dom.find_all(class_='historia')

clase_historia = dom.find_all(attrs={'class':'historia'})
historia = dom.find(attrs={'data-minumero':'124124'})

parrafo_historia = dom.find_all('p', class_='historia')

