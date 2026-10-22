import pytest
from unittest.mock import patch, Mock
import requests


URL = "https://swapi.dev/api/people/"


# ------- RESOLUCIÓN -------
def obtener_pagina_personajes(url=URL):
    res = requests.get(url, timeout=10)
    res.raise_for_status()
    return res.json()


def buscar_personaje(nombre):
    res = requests.get(URL, params={"search": nombre}, timeout=10)
    res.raise_for_status()
    return res.json()


# ------- TESTS -------
def test_obtener_primera_pagina():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200
    respuesta_falsa.json.return_value = {
        "results": [
            {"name": "Luke Skywalker", "height": "172", "mass": "77"},
            {"name": "C-3PO", "height": "167", "mass": "75"},
        ],
        "next": None
    }

    with patch("requests.get", return_value=respuesta_falsa):
        datos = obtener_pagina_personajes()

    assert len(datos["results"]) == 2
    assert datos["results"][0]["name"] == "Luke Skywalker"
    assert datos["next"] is None


def test_buscar_personaje_encontrado():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200
    respuesta_falsa.json.return_value = {
        "results": [
            {
                "name": "Luke Skywalker",
                "height": "172",
                "mass": "77",
                "hair_color": "blond",
                "skin_color": "fair",
                "eye_color": "blue",
                "birth_year": "19BBY",
                "gender": "male"
            }
        ]
    }

    with patch("requests.get", return_value=respuesta_falsa) as mock_get:
        datos = buscar_personaje("Luke")

    mock_get.assert_called_once_with(
        URL,
        params={"search": "Luke"},
        timeout=10
    )
    assert len(datos["results"]) == 1
    assert datos["results"][0]["name"] == "Luke Skywalker"


def test_buscar_personaje_no_encontrado():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200
    respuesta_falsa.json.return_value = {"results": []}

    with patch("requests.get", return_value=respuesta_falsa):
        datos = buscar_personaje("NoExiste")

    assert len(datos["results"]) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])