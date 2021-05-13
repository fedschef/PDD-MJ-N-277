#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 20:24:41 2021

@author: fedschef
"""
from flask import Flask


#Defino una app que se va llamar igual que este archivo
app = Flask(__name__)


@app.route('/2/users/1234/followers')
def hello_flask():
    
    return "Hola desde Flask :D"

# Antes de correr necesitamos definir un puerto.
# Ej todo lo que se navega por HTTPS es 443; mientras que el HTTP es 80
# Estos de arriba suelen ser puertos publicos
# Ahora elijo 3000, porque si.


app.run( port = 3000 )