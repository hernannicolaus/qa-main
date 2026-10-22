import pytest
from unittest.mock import patch, Mock
import requests


# ------- RESOLUCIÓN -------
def leer_stream(url):
    res = requests.get(url, stream=True)
    res.raise_for_status()
    lineas = []
    for linea in res.iter_lines():
        if linea:
            lineas.append(linea.decode("utf-8"))
    return lineas


# ------- TESTS -------
def test_iter_lines():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200
    respuesta_falsa.iter_lines.return_value = [
        b'{"id": 0}',
        b'{"id": 1}',
        b'{"id": 2}',
    ]

    with patch("requests.get", return_value=respuesta_falsa) as mock_get:
        lineas = leer_stream("https://httpbin.org/stream/5")

    mock_get.assert_called_once_with(
        "https://httpbin.org/stream/5",
        stream=True
    )
    assert len(lineas) == 3
    assert '{"id": 0}' in lineas
    assert '{"id": 2}' in lineas


if __name__ == "__main__":
    pytest.main([__file__, "-v"])