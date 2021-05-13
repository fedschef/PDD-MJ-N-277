import pprint
perro = {'nombre': 'Rocco',
         'tipo_mascota': 'perro',
         'raza': 'Labrador'}
edad = 4
gustos = ['comer', 'correr a las palomas', 'ladrar sin parar']
perro.update({'edad': edad})
perro.update({'gustos': gustos})
gato = {'nombre': 'Michi',
         'tipo_mascota': 'gato',
         'raza': 'N/A',
         'edad': 8,
         'gustos': ['rasguñar', 'comer', 'maullar']}
hamster = {'nombre': 'Milo',
         'tipo_mascota': 'hanster',
         'raza': 'N/A',
         'edad': 1,
         'gustos': ['comer', 'dormir', 'jugar con la rueda']}
amo = {'nombre':'Raul',
       'tipo':'humano',
       'gustos':['leer', 'musica', 'conversar'],
       'edad': 40,
       'email': 'raul@nada.com',
       'mascotas': [perro, gato, hamster]
       }
pprint.pprint(amo)
