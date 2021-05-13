from openpyxl import Workbook
wb = Workbook()
sheet = wb.active
#Ingreso un dato en esa celda
sheet['E5'] = 42
#Agregar un fila entera de datos
sheet.append([1, "Valor", 250])
#Ingresar el timestamp
from datetime import datetime
sheet['A3'] = datetime.now()
#Ingresar un valor con otro método
sheet.cell(6, 4, "Alternativo")
wb.save('ejemplo.xlsx')