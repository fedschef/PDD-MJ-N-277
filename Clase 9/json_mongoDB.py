from pymongo import MongoClient
import requests
import json
url = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/vicejefatura-de-gobierno/estaciones-saludables/estaciones-saludables.geojson"
response = requests.get(url).text
objeto = json.loads(response)
client = MongoClient('mongodb://localhost:27017')
bd = client['estaciones_saludables']
collection = bd['estaciones']
collection.insert_many(objeto['features'])