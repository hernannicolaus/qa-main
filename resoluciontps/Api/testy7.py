import pytest
from unittest.mock import patch, Mock
import requests


# ------- RESOLUCIÓN -------
def enviar_cookie(nombre, valor):
    cookies = {nombre: valor}
    res = requests.get("https://httpbin.org/cookies", cookies=cookies)
    return res


# ------- TESTS -------
def test_enviar_cookie():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200
    respuesta_falsa.text = '{"cookies": {"usuario": "Juan"}}'

    with patch("requests.get", return_value=respuesta_falsa) as mock_get:
        res = enviar_cookie("usuario", "Juan")

    mock_get.assert_called_once_with(
        "https://httpbin.org/cookies",
        cookies={"usuario": "Juan"}
    )
    assert "Juan" in res.text


if __name__ == "__main__":
    pytest.main([__file__, "-v"])