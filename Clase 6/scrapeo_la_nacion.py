from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS
driver = webdriver.Chrome('C:/Users\gonza\Documents\Trabajo\EANT\Python\Proyecto Sábados\chromedriver.exe')

#instruccion_js = "alert('Hola Mundo')"
#driver.execute_script(instruccion_js)

url = 'https://www.lanacion.com.ar/'
driver.get(url)
sleep(2)

js_dar_posicion = '''
   fin_de_pantalla = document.body.scrollHeight
   window.scrollTo(0, fin_de_pantalla)
   return fin_de_pantalla
'''
pos_actual = 0
pos_siguiente = driver.execute_script(js_dar_posicion)
sleep(3)
while pos_actual != pos_siguiente:
   pos_siguiente = pos_actual
   pos_actual = driver.execute_script(js_dar_posicion)
   sleep(3)
   print(pos_actual)
print("Llegamos al final de la página")
html = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()
dom = BS(html, features='html.parser')
titulos = dom.find_all(class_="com-title")
fallados = []
for titulo in titulos:
   try:
      titular =  titulo.a.get('title', 'N/A')
      link = titulo.a['href']
      print(titular, '-', link)
   except:
      fallados.append(titulo)