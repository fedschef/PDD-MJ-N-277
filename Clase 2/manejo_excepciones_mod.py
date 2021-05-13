import funciones_manejo_excep as funciones

fecha = '13/Febrero/2019'
try:
    fecha_normalizada = funciones.normalizador_fechas(fecha, '%Y%d%m')
except:
    try:
        fecha_normalizada = funciones.normalizador_fechas(fecha, '%Y-%d-%m')
    except:
        try:
            fecha_normalizada = funciones.normalizador_fechas(fecha, '%d/%b/%Y')
        except:
            try:
                fecha_normalizada = funciones.normalizador_fechas(funciones.constructorFecha(fecha),'%d%m%Y')
            except:
                fecha_normalizada ='N/A'
                print(fecha_normalizada)
            
            


