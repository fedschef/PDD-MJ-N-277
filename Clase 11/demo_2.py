#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 20:24:41 2021

@author: fedschef
"""
from flask import Flask,json


#Defino una app que se va llamar igual que este archivo
app = Flask(__name__)


@app.route('/')
def hello_flask():
    
    return "Hola desde la home deFlask :D"


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

app.run( port = 3000 , host='0.0.0.0')



