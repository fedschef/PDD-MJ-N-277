from datetime import datetime

def normalizador_fechas(fecha, patron_in, patron_out='%d-%m-%Y'):
    objeto_fecha = datetime.strptime(fecha, patron_in)
    fecha_normalizada = datetime.strftime(objeto_fecha, patron_out)
    print(fecha, '-->', objeto_fecha, '-->', fecha_normalizada)
def constructorFecha(fecha):
    meses = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']
    lista = fecha.split('/')
    mes = lista[1].upper()
    nro_mes = meses.index(mes) + 1
    fecha_aux = lista[0] + str(nro_mes) + lista[2]
    return fecha_aux
###Acá empieza el programa en sí mismo###
fecha = '20191302'
normalizador_fechas(fecha, '%Y%d%m')

fecha = '2019-13-02 14:23:33'
normalizador_fechas(fecha, '%Y-%d-%m %H:%M:%S', '%d-%m-%Y %H:%M:%S')

fecha = '13/Feb/2019'
normalizador_fechas(fecha, '%d/%b/%Y')

fecha = '13 days after February 2019'
normalizador_fechas(fecha, '%d days after %B %Y')

fecha = '13/Enero/2019'
normalizador_fechas(constructorFecha(fecha),'%d%m%Y')