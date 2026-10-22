import pytest
from unittest.mock import patch, Mock
import requests


# ------- RESOLUCIÓN -------
def obtener_con_redirect():
    res = requests.get("https://httpbin.org/redirect/3")
    return res


# ------- TESTS -------
def test_redirecciones():
    redir1 = Mock(status_code=302, url="https://httpbin.org/redirect/3")
    redir2 = Mock(status_code=302, url="https://httpbin.org/relative-redirect/2")
    redir3 = Mock(status_code=302, url="https://httpbin.org/relative-redirect/1")

    respuesta_final = Mock()
    respuesta_final.status_code = 200
    respuesta_final.url = "https://httpbin.org/get"
    respuesta_final.history = [redir1, redir2, redir3]

    with patch("requests.get", return_value=respuesta_final):
        res = obtener_con_redirect()

    assert res.url == "https://httpbin.org/get"
    assert len(res.history) == 3
    assert res.history[0].status_code == 302
    assert res.history[1].status_code == 302
    assert res.history[2].status_code == 302


if __name__ == "__main__":
    pytest.main([__file__, "-v"])