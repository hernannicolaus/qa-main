import pytest
import requests

# ------- RESOLUCIÓN -------
URL = "https://rickandmortyapi.com/api/character/"


def obtener_personaje(id_personaje):
    res = requests.get(f"{URL}{id_personaje}", timeout=10)
    res.raise_for_status()
    return res.json()


def extraer_datos_personaje(personaje):
    return {
        "nombre": personaje["name"],
        "estado": personaje["status"],
        "especie": personaje["species"],
        "origen": personaje["origin"]["name"],
    }


# ------- TESTS -------

def test_personaje_status_code_es_200():
    respuesta = requests.get(f"{URL}1", timeout=10)
    assert respuesta.status_code == 200

def test_personaje_nombre_es_rick_sanchez():
    datos = obtener_personaje(1)
    assert datos["name"] == "Rick Sanchez"

def test_personaje_especie_es_Human():
    datos = obtener_personaje(1)
    assert datos["species"] == "Human"

def test_personaje_estado_es_alive():
    datos = obtener_personaje(1)
    assert datos["status"] == "Alive"

def test_extraer_datos_personaje():
    personaje = obtener_personaje(1)
    resultado = extraer_datos_personaje(personaje)
    esperado = {
        "nombre": "Rick Sanchez",
        "estado": "Alive",
        "especie": "Human",
        "origen": "Earth (C-137)",
    }
    assert resultado == esperado


if __name__ == "__main__":
    pytest.main([__file__, "-v"])