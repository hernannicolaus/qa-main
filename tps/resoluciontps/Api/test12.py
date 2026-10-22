import pytest
from unittest.mock import patch, Mock
import requests


URL = "https://api.github.com/search/repositories"


# ------- RESOLUCIÓN -------
def buscar_repos(query):
    params = {"q": query, "sort": "stars", "order": "desc"}
    res = requests.get(URL, params=params)
    res.raise_for_status()
    return res.json()


# ------- TESTS -------
def test_buscar_repos_python():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200
    respuesta_falsa.json.return_value = {
        "total_count": 2,
        "items": [
            {
                "full_name": "usuario/repo1",
                "description": "Un repo",
                "stargazers_count": 100,
                "html_url": "https://github.com/usuario/repo1"
            },
            {
                "full_name": "usuario/repo2",
                "description": "Otro repo",
                "stargazers_count": 50,
                "html_url": "https://github.com/usuario/repo2"
            }
        ]
    }

    with patch("requests.get", return_value=respuesta_falsa) as mock_get:
        datos = buscar_repos("python")

    mock_get.assert_called_once_with(
        URL,
        params={"q": "python", "sort": "stars", "order": "desc"}
    )
    assert datos["total_count"] == 2
    assert datos["items"][0]["full_name"] == "usuario/repo1"
    assert datos["items"][0]["stargazers_count"] == 100


if __name__ == "__main__":
    pytest.main([__file__, "-v"])