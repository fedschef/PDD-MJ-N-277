from pymongo import MongoClient
import pprint

cliente = MongoClient('mongodb://localhost:27017')

bd = cliente['universidad']
coleccion = bd['alumnos']

# alumnos = coleccion.find()

# for alumno in alumnos:
#    print(alumno.get('dni', "No hay dato de DNI"))

# alumno_seleccion = coleccion.find({'hijos.nombre': 'Juana'})

# for info in alumno_seleccion:
#    pprint.pprint(info['hijos'][1])

