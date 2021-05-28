#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 20:24:41 2021

@author: fedschef
"""
# Para guardar los recursos y librerias necesarios corro
# pip freeze > requirements.txt


from flask import Flask,json
from pymongo import MongoClient
from urllib.parse import urlencode
import settings
from os import environ

# requiere pymongo[srv]
# requiere dnspython

#Defino una app que se va llamar igual que este archivo
app = Flask(__name__)
USER = environ["USER"]
PASSWORD = environ["PASSWORD"]
SERVER = environ["SERVER"]
DATABASE = environ["DATABASE"]


# Agrego dos parametros mas al connection string
# ssl: para asegurar que el mensaje este encriptado
# ssl_cert_reqs: otras opciones desables de seguridad, que ahora no incluimos
# url = "mongodb+srv://federico:"+PASSWORD+"@"+SERVER+"/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"

params = {
    'retryWrites' : 'true',
    'w' : 'majority',
    'ssl' : 'true',
    'ssl_cert_reqs' : 'CERT_NONE'
        }
url = "mongodb+srv://federico:"+PASSWORD+"@"+SERVER+"/"+DATABASE+"?" +urlencode(params)
client = MongoClient(url)


@app.route('/')
def hello_flask():
    
    return "<h>Hola desde la home de Flask :D</h>"


# Agregamos una pagina que muestre usuarios de ejemplo
#################################
@app.route('/users')
def usersTwitter():
    #El output siempre tiene que ser un string, dict o tuple
    users = [{
        'name' : 'fedschef_'
        },
        {
        'name' : 'fedschef2_'
        }]
    
    response = app.response_class(response = json.dumps(users), status = 200 , mimetype = "application/json") 
    return response


#Ahora creo un path dinamico
#################################
@app.route('/users/<path>')
def searchUsers(path):
    if path == "people":
        return "Aca va un JSON de personas......"
    elif path == "company":
        return "Aca va un JSON de empresas"
    else:
        return "Error pagina no encontrada!!!!"



@app.route("/api/tweets/<usuario>/<limit>")
def getTweets(usuario,limit):
    bigdata = client['bigdata']
    tweets = bigdata['tweets']
    a=limit
    mis_tweets = tweets.find({'in_reply_to_screen_name':usuario})
    los_tweets = []
    for tweet  in mis_tweets:
  
        los_tweets.append({
        'usuario' : tweet['id_str']
        ,
        
        'texto' : tweet['full_text']
        })
    
    response = app.response_class(response = json.dumps(los_tweets), status = 200 , mimetype = "application/json") 
    return response

app.run( port = 3000, debug = True)# , host='0.0.0.0')