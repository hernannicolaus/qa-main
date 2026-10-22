import pytest
from unittest.mock import patch, Mock
import requests


# ------- RESOLUCIÓN -------
def consultar_url(url):
    res = requests.get(url)
    res.raise_for_status()
    return res


# ------- TESTS -------
def test_raise_for_status_404():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 404
    respuesta_falsa.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "404 Client Error: NOT FOUND"
    )

    with patch("requests.get", return_value=respuesta_falsa):
        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            consultar_url("https://httpbin.org/esta-url-no-existe")

    assert "404" in str(exc_info.value)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])