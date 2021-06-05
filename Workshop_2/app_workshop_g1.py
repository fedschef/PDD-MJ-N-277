#https://127.0.0.1:3030/api/BARRIO/INMUEBLE/TIPO


from flask import Flask,json
from pymongo import MongoClient
from urllib.parse import urlencode
#import settings
from os import environ

# requiere pymongo[srv]
# requiere dnspython

#Defino una app que se va llamar igual que este archivo
app = Flask(__name__)
USER = "federico" #environ["USER"]
PASSWORD = "1234" #environ["PASSWORD"]
SERVER = "clusterpdd.esivo.mongodb.net" #environ["SERVER"]
DATABASE = "bigdata" #environ["DATABASE"]
PORT = 3300


params = {
    'retryWrites' : 'true',
    'w' : 'majority',
    'ssl' : 'true',
    'ssl_cert_reqs' : 'CERT_NONE'
        }
url = "mongodb+srv://"+ USER+":"+PASSWORD+"@"+SERVER+"/"+DATABASE+"?" +urlencode(params)
client = MongoClient(url)



@app.route('/')
def hello_flask():
    
    return "<h>Compará precio de Alquileres! :D</h>"



@app.route("/api/<path>/<value>")
#def searchPropiedades(path,value):
#    if path == 'inmobiliarias':
#        return 'Acá va el json de personas'
#    elif path == 'ubicacion':
#        return 'Acá va un json de empresas'
#    else:
#        return 'No puedo mostrar lo que estás buscando'
    
def getPropiedades(path,value):
    bigdata = client['bigdata']
    propiedades = bigdata['propiedades']
    
   # diccionario = {"barrio" : "ubicacion",
   #                "inmobiliaria" : "inmobiliaria"}
    
    if path == "barrio":
        path = "ubicacion"
        
    mis_propiedades = propiedades.find({path:value})

    las_propiedades = []
    for propiedad  in mis_propiedades:
  
        las_propiedades.append({
        #'usuario' : tweet['id_str'],
          'ubicacion' : propiedad['ubicacion'],
          'moneda' : propiedad['precio'][0]['precio_moneda'],
          'valor' : propiedad['precio'][0]['precio_valor'],
          'ambientes' : propiedad['data'][0]['ambientes'],
          'metros2' : propiedad['data'][0]['m2'],
          'baños' :  propiedad['data'][0]['banhos'],
          'inmobiliaria' : propiedad['inmobiliaria']        
        
        })
#    return las_propiedades 

    response = app.response_class(response = json.dumps(las_propiedades), status = 200 , mimetype = "application/json") 
    return response


app.run(port=3000)
