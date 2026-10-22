import pytest
from unittest.mock import patch, Mock
import requests


# ------- RESOLUCIÓN -------
def obtener_status(url):
    r = requests.get(url)
    return r.status_code


# ------- TESTS -------
def test_obtener_status_ok():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200

    with patch("requests.get", return_value=respuesta_falsa):
        resultado = obtener_status("https://www.un.org")

    assert resultado == 200


def test_obtener_status_error():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 404

    with patch("requests.get", return_value=respuesta_falsa):
        resultado = obtener_status("https://www.un.org/no-existe")

    assert resultado == 404


if __name__ == "__main__":
    pytest.main([__file__, "-v"])