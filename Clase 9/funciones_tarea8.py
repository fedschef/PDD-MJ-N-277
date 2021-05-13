import json
import requests


def get_lat_long(linea):
    city_code = (linea[0] + ', ' + linea[1] + ", Argentina")
    city = "https://nominatim.openstreetmap.org/search?q=" + city_code +"&format=json"
    cities = json.loads(requests.get(city).text)
    return cities

dict_sucursales = {}
def get_attr(cities, linea):
    key="8a534d2c8bef29412cb6914b4ae67f99"
    url = "http://api.openweathermap.org/data/2.5/weather?units=metric&lang=es&lat="+ cities[0]['lat'] + "&lon=" + cities[0]['lon'] + "&appid=" + key
    objeto = json.loads(requests.get(url).text)
    try:
        dict_sucursales[linea[1]] = {
                                    'celsius': objeto['main']['temp'],
                                    'descripcion': objeto['weather'][0]['description']
                                    }
    except:
        print("La provincia "+linea[1]+" dio error")
    return dict_sucursales