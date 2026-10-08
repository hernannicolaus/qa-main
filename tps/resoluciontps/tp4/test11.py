import pytest
from unittest.mock import patch, Mock
import requests


URL = "https://jsonplaceholder.typicode.com/posts"


# ------- RESOLUCIÓN -------
def obtener_posts():
    res = requests.get(URL)
    res.raise_for_status()
    return res.json()


def crear_post(titulo, contenido, usuario_id):
    datos = {"title": titulo, "body": contenido, "userId": usuario_id}
    res = requests.post(URL, json=datos)
    res.raise_for_status()
    return res.json()


# ------- TESTS -------
def test_obtener_posts():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200
    respuesta_falsa.json.return_value = [
        {"id": 1, "title": "Post 1", "body": "...", "userId": 1},
        {"id": 2, "title": "Post 2", "body": "...", "userId": 1},
    ]

    with patch("requests.get", return_value=respuesta_falsa) as mock_get:
        posts = obtener_posts()

    mock_get.assert_called_once_with(URL)
    assert len(posts) == 2
    assert posts[0]["title"] == "Post 1"


def test_crear_post():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 201
    respuesta_falsa.json.return_value = {
        "title": "Mi nuevo post",
        "body": "Contenido",
        "userId": 1,
        "id": 101
    }

    with patch("requests.post", return_value=respuesta_falsa):
        post = crear_post("Mi nuevo post", "Contenido", 1)

    assert post["id"] == 101
    assert post["title"] == "Mi nuevo post"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])