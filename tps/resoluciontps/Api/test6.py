import pytest
from unittest.mock import patch, Mock
import requests


# ------- RESOLUCIÓN -------
def descargar_imagen(url, destino):
    res = requests.get(url)
    if res.status_code == 200:
        with open(destino, "wb") as archivo:
            archivo.write(res.content)
        return True
    return False


# ------- TESTS -------
def test_descargar_imagen(tmp_path):
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200
    respuesta_falsa.content = b"datos_falsos_de_imagen"

    archivo_destino = tmp_path / "imagen.png"

    with patch("requests.get", return_value=respuesta_falsa):
        resultado = descargar_imagen("https://httpbin.org/image/png", archivo_destino)

    assert resultado is True
    assert archivo_destino.exists()
    assert archivo_destino.read_bytes() == b"datos_falsos_de_imagen"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])