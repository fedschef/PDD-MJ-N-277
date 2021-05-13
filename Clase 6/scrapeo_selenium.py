from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS
driver = webdriver.Chrome('C:/Users\gonza\Documents\Trabajo\EANT\Python\Proyecto Sábados\chromedriver.exe')

#instruccion_js = "alert('Hola Mundo')"
#driver.execute_script(instruccion_js)

url = 'https://www.olx.com.ar/items/q-aspiradora'
driver.get(url)

js_capturar_boton = """
   boton = document.querySelector('[data-aut-id="btnLoadMore"]')
   if (boton){
       boton.click()     
    }
   else{
      return "No existe"
   }
"""
sleep(3)

while driver.execute_script(js_capturar_boton) != "No existe": sleep(3)
sleep(2)
html = driver.execute_script("return document.documentElement.outerHTML")
#Acá empieza el scrapeo en sí mismo
dom = BS(html, features='html.parser')
productos = dom.find_all(class_="IKo3_")
for producto in productos:
   precio = producto.find(class_="_89yzn").text
   titulo = producto.find(class_="_2tW1I").text
   print(titulo, ':', precio)

driver.quit()