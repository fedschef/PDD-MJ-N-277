#https://127.0.0.1:3030/api/BARRIO/INMUEBLE/TIPO

# Scrapeo
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

url = "https://www.properati.com.ar/s/palermo/departamento/alquiler?page=1"

response = requests.get(url)
response.encoding = "utf-8"
html = response.text

dom = BeautifulSoup(html, features = "html.parser")

# ¿hay una lista de 'anuncios'?
lista_propiedades = []

if dom.find( attrs = { 'class' : 'StyledListingWrapper-sc-1te1fm4-1 eniVyf' } ) != None:

    anuncios = dom.findAll( attrs = { 'class' : 'StyledCard-n9541a-1 ixiyWf' } )
    for anuncio in anuncios:
        
        try:
            titulo = anuncio.find(class_="StyledTitle-n9541a-4 bwJAej").text
        except:
            titulo = "No Disponible"
        try:    
            precio_moneda = anuncio.find(class_="StyledPrice-sc-1wixp9h-0 bZCCaW").text.split(" ")[0]
            precio_valor = anuncio.find(class_="StyledPrice-sc-1wixp9h-0 bZCCaW").text.split(" ")[1]
        except:
            precio_moneda = "Consultar"
            precio_valor = "Consultar"
        try:
            expensas = (anuncio.find(class_="StyledMaintenanceFees-n9541a-6 cRsmn").text)[2:-9]
        except:
            expensas = "Sin Datos"
        try:
            ubicacion = anuncio.find(class_="StyledLocation-n9541a-7 fqaBNm").text
        except:
            ubicacion = "No Disponible"
        try: 
            inmobiliaria = anuncio.find(class_="StyledInfoSeller-n9541a-10 jHsNmu").span.text
        except:
        
            inmobiliria = "Sin Datos"
        ambientes = "Sin Datos"
        banhos = "Sin Datos"
        for texto in anuncio.find(class_="StyledInfoIcons-n9541a-9 fgcFIO"):
            if "año" in texto.text:
                banhos = texto.text
            elif "mbiente" in texto.text:
                ambientes = texto.text    
            else:
                m2 = texto.text        
#        try:
#            for texto in anuncio.find(class_="StyledInfoIcons-n9541a-9 fgcFIO"):
#                m2 = texto.text
#        except: 
#            m2 = "Sin Datos"
        
        
    
        propiedad = { 
            "titulo" : titulo,
            "precio":[{            
                    "precio_moneda" : precio_moneda,
                    "precio_valor" : precio_valor,
                    }],
            "data":[{
                    "expensas" : expensas,
                    "m2" : m2,
                    "ambientes" : ambientes,
                    "banhos" : banhos,                    
                    }],
            "ubicacion" : ubicacion,
            "inmobiliaria" : inmobiliaria,
            }
        
        lista_propiedades.append(propiedad)

propiedades = tuple(lista_propiedades)

    



#%%

# Carga de datos
user = "federico"
password = "1234"
server = "clusterpdd.esivo.mongodb.net"
databse = "bigdata"


url = "mongodb+srv://"+user+":"+password+"@"+server+"/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)


bd = client['bigdata']
coleccion = bd['propiedades']
coleccion.insert_many(lista_propiedades)
              