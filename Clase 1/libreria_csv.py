import csv

with open('peliculas.csv', encoding='utf-8') as archivo_in, open('peliculas_modificado.csv', 'w', newline='') as archivo_out:
    tabla = csv.reader(archivo_in, delimiter=',')
    salida = csv.writer(archivo_out, delimiter=',')
    salida.writerow(['película','director','actores'])
    for linea in tabla:
        #print(linea[3])
        salida.writerow([linea[0], linea[2], linea[3]])
