import pytest
from unittest.mock import patch, Mock
import requests
import pandas as pd


URL = "https://jsonplaceholder.typicode.com/posts"


# ------- RESOLUCIÓN -------
def obtener_posts_df():
    res = requests.get(URL)
    res.raise_for_status()
    datos = res.json()
    return pd.DataFrame(datos)


def calcular_posts_por_usuario(df):
    return df.groupby("userId").size()


# ------- TESTS -------
def test_calculo_posts_por_usuario():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200
    respuesta_falsa.json.return_value = [
        {"userId": 1, "id": 1, "title": "a", "body": "..."},
        {"userId": 1, "id": 2, "title": "b", "body": "..."},
        {"userId": 2, "id": 3, "title": "c", "body": "..."},
        {"userId": 2, "id": 4, "title": "d", "body": "..."},
        {"userId": 3, "id": 5, "title": "e", "body": "..."},
    ]

    with patch("requests.get", return_value=respuesta_falsa):
        df = obtener_posts_df()

    posts_por_usuario = calcular_posts_por_usuario(df)

    assert posts_por_usuario[1] == 2
    assert posts_por_usuario[2] == 2
    assert posts_por_usuario[3] == 1
    assert posts_por_usuario.idxmax() in (1, 2)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])