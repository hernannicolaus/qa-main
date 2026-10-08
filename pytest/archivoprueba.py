import pytest

@pytest.mark.parametrize("numero1, numero2, esperado", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])

def test_suma(numero1: int, numero2: int, esperado: int) -> bool:
    assert esperado == numero1 + numero2


if __name__ == "__main__":
    # __file__ limita la ejecucion a este archivo (evita recolectar todo el repo); -v muestra el detalle de cada test
    pytest.main([__file__, "-v"])

