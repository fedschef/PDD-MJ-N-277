import csv
hospitales = csv.reader(open('hospitales.csv', encoding='utf-8'))
salida = open('hospitales_mod.csv', 'w')
next(hospitales)
salida.write('latitude;longitude;name;label\n')
for hospital in hospitales:
    coordenadas = hospital[0][7:-1].split()
    unidos = ';'.join([coordenadas[1], coordenadas[0], hospital[8], hospital[3]])
    salida.write(unidos + '\n')    
 
salida.close()