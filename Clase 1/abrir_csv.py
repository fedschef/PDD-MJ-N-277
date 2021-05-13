archivo = open('subtes.csv', 'r', encoding='utf-8')

for linea in archivo:
    linea = linea.replace('\n', '')
    linea = linea.split(',')
    print(linea[2])
