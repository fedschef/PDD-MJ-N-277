import requests

url = 'https://eant.tech/cursos/recursos/frutas.txt'

respuesta = requests.get(url)

print("Código de respuesta:", respuesta.status_code)
print("URL:", respuesta.url)
print("Contenido del mensaje: ", respuesta.content)
print("Decodificación: ", respuesta.encoding)
respuesta.encoding='utf-8'
print("Contenido como texto: ", respuesta.text)
