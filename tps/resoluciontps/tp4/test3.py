import pytest
from unittest.mock import patch, Mock
import requests


# ------- RESOLUCIÓN -------
def buscar_con_params(nombre, edad):
    params = {"nombre": nombre, "edad": edad}
    res = requests.get("https://httpbin.org/get", params=params)
    return res


# ------- TESTS -------
def test_params_se_envian():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200
    respuesta_falsa.url = "https://httpbin.org/get?nombre=Juan&edad=30"
    respuesta_falsa.text = '{"args": {"nombre": "Juan", "edad": "30"}}'

    with patch("requests.get", return_value=respuesta_falsa) as mock_get:
        res = buscar_con_params("Juan", 30)

    mock_get.assert_called_once_with(
        "https://httpbin.org/get",
        params={"nombre": "Juan", "edad": 30}
    )
    assert "nombre=Juan" in res.url
    assert "edad=30" in res.url


if __name__ == "__main__":
    pytest.main([__file__, "-v"])