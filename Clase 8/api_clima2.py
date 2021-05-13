import requests
import json
import pprint
import csv
#Declaro los keys
key_open_weather = ''
archivo = csv.reader(open('sucursales_sol_360.csv'), delimiter =';')
log_error = open('sol_360_log_error.txt','w', encoding='utf-8')
# Defino funciones
def func_objeto(url):
    ''' str-> str
     Devuelve un string con datos del objeto producto de respuesta de la API .
     '''
    return(json.loads(requests.get(url).text))
 
ciudades = [lista[0] for lista in archivo]

for ciudad in ciudades:
     url_w = 'http://api.openweathermap.org/data/2.5/weather?q='+ciudad+',Argentina&units=metric&appid='+key_open_weather+'&lang=sp'
     #print(url_w)
     objeto = func_objeto(url_w)
     #pprint.pprint(objeto)
     if objeto.get('weather') == None:
          log_error.write(ciudad+' no encontrada'+'\n')
     else:
          temperatura = objeto['main'].get('temp',' Sin Datos')
          clima = objeto['weather'][0].get('description',' Sin Datos')
          print('\nESTADO DEL CLIMA')
          print(ciudad,': ',objeto.get('weather')[0]['description'].capitalize())
          print('Temperatura: ',temperatura, ' °C')

log_error.close()

