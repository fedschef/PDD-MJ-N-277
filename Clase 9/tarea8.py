import pprint
import csv
import funciones_tarea8 as funciones

with open('sucursales_sol_360.csv') as sucursales:
    tabla = csv.reader(sucursales, delimiter=';')
    for linea in tabla:
        cities_lat_long = funciones.get_lat_long(linea)
        dict_sucursales = funciones.get_attr(cities_lat_long, linea)
    pprint.pprint(dict_sucursales)
        