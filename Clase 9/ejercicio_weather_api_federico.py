#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
import pprint
import csv

key = '2e5258fc491f51e70ff8a01c8afc358e'

def obtener_tiempo(ciudad_normalizada,key):
    url = 'http://api.openweathermap.org/data/2.5/weather?q='+ciudad_normalizada+'&appid='+key+'&units=metric&lang=es'
    str_objeto = requests.get(url).text
    objeto = json.loads(str_objeto)
    return objeto

with open('sucursales_sol_360.csv','r',encoding='latin-1') as archivo:
    reader = csv.reader(archivo,delimiter = ';')
    for sucursal_geo in reader:
        ciudad = sucursal_geo[0] +',' + sucursal_geo[1] +', Argentina'
        ciudad = ciudad.replace("Ciudad de Buenos Aires","Buenos Aires")
        ciudad_cod = requests.utils.quote(ciudad)
        objeto = obtener_tiempo(ciudad_cod,key)
        try:
            print(ciudad + '-> Estado general ->' + objeto['weather'][0]['description'])
            print(ciudad + '-> Temperatura ->' + str(objeto['main']['temp']) + 'C')
        except:
            
            ciudad_cod = requests.utils.quote(sucursal_geo[0])
            provincia_cod = requests.utils.quote(sucursal_geo[1])
            url2 = 'https://apis.datos.gob.ar/georef/api/municipios?nombre='+ciudad_cod+'&provincia='+provincia_cod
            objeto_ciudad = json.loads(requests.get(url2).text)
            print("Ciudad no encontrada:", sucursal_geo[0],"-- Intentando búsqueda con normalización")
            try:
                ciudad_norm = objeto_ciudad['municipios'][0]['nombre']
                ciudad_cod = requests.utils.quote(ciudad_norm + ',Argentina')
                objeto = obtener_tiempo(ciudad_cod,key)

                
                try:
                     print(ciudad_norm + '-> Estado general ->' + objeto['weather'][0]['description'])
                     print(ciudad_norm + '-> Temperatura ->' + str(objeto['main']['temp']) + 'C')
                except:
                     print("Error de formato de coordenadas para ciudad:", sucursal_geo[0],'. Cancelando.....')
            except:
                   print("Ciudad no encontrada:", sucursal_geo[0],'. Cancelando.....')

        print(" ")

