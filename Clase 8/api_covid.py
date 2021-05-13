import json
import requests
import pprint

url = 'https://covid-api.mmediagroup.fr/v1/cases'
objeto = json.loads(requests.get(url).text)
#pprint.pprint(objeto)
paises = [pais for pais in objeto if pais != 'Global']

mi_seleccion = {}
contador = 1
while True:
   pais_deseado = input("Ingrese el país del que quiere los datos (en Inglés): ")
   if pais_deseado not in paises:
      print("Este país no es válido")
      ver = input("Quiere ver la lista de países? s/n: ").upper()
      if ver == 'S':
         for pais in paises: print(pais)
   else:
      url = 'https://covid-api.mmediagroup.fr/v1/cases?country=' + pais_deseado
      objeto = json.loads(requests.get(url).text)
      toda_la_info = objeto.get('All')
      casos_confirmados = toda_la_info['confirmed']
      fallecidos = toda_la_info['deaths']
      recuperados = toda_la_info['recovered']
      datos_pais = {'país': pais_deseado,
                    'casos_confirmados': casos_confirmados,
                    'fallecidos':fallecidos,
                    'recuperados': recuperados}
      mi_seleccion['pais' + str(contador)] = datos_pais
      contador += 1
   agregar = input("Quiere agregar otro país? s/n: ").upper()
   if agregar == 'N': break
#pprint.pprint(mi_seleccion)
with open('selec_paises.json', 'w') as casos:
    json.dump(mi_seleccion, casos, indent=3, ensure_ascii=False)
