import pytest
from unittest.mock import patch, Mock
import requests


# ------- RESOLUCIÓN -------
def enviar_post(datos):
    res = requests.post("https://httpbin.org/post", json=datos)
    return res


# ------- TESTS -------
def test_post_json():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200
    respuesta_falsa.text = '{"json": {"nombre": "Juan", "edad": 30}}'

    with patch("requests.post", return_value=respuesta_falsa) as mock_post:
        datos = {"nombre": "Juan", "edad": 30}
        res = enviar_post(datos)

    mock_post.assert_called_once_with(
        "https://httpbin.org/post",
        json={"nombre": "Juan", "edad": 30}
    )
    assert res.status_code == 200
    assert "Juan" in res.text


if __name__ == "__main__":
    pytest.main([__file__, "-v"])