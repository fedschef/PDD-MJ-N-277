from datetime import datetime

def normalizador_fechas(fecha, patron_in, patron_out='%d-%m-%Y'):
    '''str, str str(op) ->str
    Devuelve la fecha normalizada de acuerdo
     al patrón ingresado y al patrón requerido'''
    objeto_fecha = datetime.strptime(fecha, patron_in)
    fecha_normalizada = datetime.strftime(objeto_fecha, patron_out)
    print(fecha, '-->', objeto_fecha, '-->', fecha_normalizada)
    return fecha_normalizada

def constructorFecha(fecha):
    '''str->str
    Devuelve una fecha que el módulo datime pueda normalizar'''
    meses = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']
    lista = fecha.split('/')
    mes = lista[1].upper()
    nro_mes = meses.index(mes) + 1
    fecha_aux = lista[0] + str(nro_mes) + lista[2]
    return fecha_aux

