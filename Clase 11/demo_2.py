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

app.run( port = 3000 , host='0.0.0.0')