import pytest
from unittest.mock import patch, Mock
import requests


# ------- RESOLUCIÓN -------
def obtener_get():
    res = requests.get("https://httpbin.org/get")
    return res


# ------- TESTS -------
def test_httpbin_get_ok():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200
    respuesta_falsa.url = "https://httpbin.org/get"
    respuesta_falsa.text = '{"url": "https://httpbin.org/get"}'

    with patch("requests.get", return_value=respuesta_falsa):
        res = obtener_get()

    assert res.status_code == 200
    assert res.url == "https://httpbin.org/get"
    assert "httpbin.org" in res.text


if __name__ == "__main__":
    pytest.main([__file__, "-v"])