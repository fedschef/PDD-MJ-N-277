import pprint
#Diccionario
perro = {'nombre': 'Rocco',
         'tipo_mascota': 'perro',
         'raza': 'labrador'}

#Variable
edad = 4

#Lista
le_gusta = ['comer', 'correr a las palomas', 'ladrar sin parar']

#Combinación
perro.update({'edad': edad})
perro.update({'le_gusta': le_gusta})

#pprint.pprint(perro)

amo = {'nombre': 'Raúl',
       'tipo': 'humano',
       'le_gusta': ['leer libros', 'los fichines', 'conversar'],
       'edad': 40,
       'mascota': perro   
   }
pprint.pprint(amo)
