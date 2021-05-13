from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

#Insertar un valor
#alumno  = dict(apellido="Herman", nombre="Alma", dni=36123486)
#cliente.universidad.alumnos.insert_one(alumno)

bd = cliente['universidod']
coleccion = bd['alumnos']

#Insertar varios valores
estudiantes = [{'apellido': 'Hoffmann', 'nombre': 'Aldana'},
               {'apellido': 'Sian', 'nombre': 'Pablo', 'dni': 25456321},
               {'apellido': 'Surten', 'nombre': 'Jorge',
                'hijos': [{'nombre': 'Román', 'edad': 12},
                          {'nombre': 'Juana', 'edad': 10}]}]

coleccion.insert_many(estudiantes)
print("Datos subidos")