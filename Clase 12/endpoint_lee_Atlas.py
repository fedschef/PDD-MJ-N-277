#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 20:24:41 2021

@author: fedschef
"""
from flask import Flask,json
from pymongo import MongoClient


#Defino una app que se va llamar igual que este archivo
app = Flask(__name__)
user = "federico"
password = "1234"
server = "clusterpdd.esivo.mongodb.net"
databse = "bigdata"


url = "mongodb+srv://federico:"+password+"@"+server+"/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)


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



@app.route("/api/tweets/<usuario>/<limit>")
def getTweets(usuario,limit):
    bigdata = client['bigdata']
    tweets = bigdata['tweets']
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