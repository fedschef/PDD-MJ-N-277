archivo = open('frutas.txt', 'r', encoding='utf-8')

for linea in archivo:
    linea = linea.rstrip('\n')
    print(linea)