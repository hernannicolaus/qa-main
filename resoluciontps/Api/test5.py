import pytest
from unittest.mock import patch, Mock
import requests


# ------- RESOLUCIÓN -------
def obtener_headers(headers):
    res = requests.get("https://httpbin.org/headers", headers=headers)
    return res


# ------- TESTS -------
def test_header_user_agent():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200
    respuesta_falsa.text = '{"headers": {"User-Agent": "MiProgramaPython/1.0"}}'

    with patch("requests.get", return_value=respuesta_falsa) as mock_get:
        headers = {"User-Agent": "MiProgramaPython/1.0"}
        res = obtener_headers(headers)

    mock_get.assert_called_once_with(
        "https://httpbin.org/headers",
        headers={"User-Agent": "MiProgramaPython/1.0"}
    )
    assert "MiProgramaPython/1.0" in res.text


if __name__ == "__main__":
    pytest.main([__file__, "-v"])