from datetime import datetime

fecha = '13/2/2019'
objeto_fecha = datetime.strptime(fecha, "%d/%m/%Y")
fecha_normalizada = datetime.strftime(objeto_fecha, "%d-%m-%Y")
print(fecha, '-->', objeto_fecha, '-->', fecha_normalizada)

