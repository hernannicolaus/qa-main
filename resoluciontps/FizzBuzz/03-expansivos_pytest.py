import numpy as np
import pytest


def expand(arreglo: np.ndarray) -> np.ndarray:
    # esta funcion cuenta cuantas veces se repite cada numero seguido
    resultado = []
    cifraActual = arreglo[0]
    contador = 1
    for i in range(1, len(arreglo)):
        if arreglo[i] == cifraActual:
            # es el mismo numero que el anterior, sigo contando
            contador += 1
        else:
            # cambio el numero, guardo lo que iba contando y arranco de nuevo
            resultado.append(contador)
            resultado.append(cifraActual)
            cifraActual = arreglo[i]
            contador = 1
    # el ultimo grupo no se guarda en el for, asi que lo agrego aca
    resultado.append(contador)
    resultado.append(cifraActual)
    return np.array(resultado)


def list2num(arreglo: np.ndarray) -> int:
    # Convierte un array de digitos en el numero entero que representan.
    numero = 0
    for cifra in arreglo:
        numero = numero * 10 + cifra
    return numero


@pytest.mark.parametrize(
    "entrada, esperado",
    [
        (np.array([1]), np.array([1, 1])),
        (np.array([1, 1]), np.array([2, 1])),
        (np.array([2, 1]), np.array([1, 2, 1, 1])),
        (np.array([1, 2, 1, 1]), np.array([1, 1, 1, 2, 2, 1])),
    ],
)
def test_expand(entrada, esperado):
    np.testing.assert_array_equal(esperado, expand(entrada))


@pytest.mark.parametrize(
    "entrada, esperado",
    [
        (np.array([1, 1]), 11),
        (np.array([2, 1]), 21),
        (np.array([1, 2, 1, 1]), 1211),
        (np.array([1, 1, 1, 2, 2, 1]), 111221),
    ],
)
def test_list2num(entrada, esperado):
    assert esperado == list2num(entrada)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
