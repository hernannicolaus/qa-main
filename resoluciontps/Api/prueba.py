import requests

url = "https://rickandmortyapi.com/api/character/"

respuesta = requests.get(url)
datos = respuesta.json()

especies = set()

for personaje in datos["results"]:
    especies.add(personaje["species"])

print(especies)