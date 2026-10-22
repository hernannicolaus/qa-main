import unittest
import numpy as np

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


class TestExpansivos(unittest.TestCase):
    def testExpand_desdeUno(self):
        np.testing.assert_array_equal(np.array([1, 1]), expand(np.array([1])))

    def testExpand_desdeOnce(self):
        np.testing.assert_array_equal(np.array([2, 1]), expand(np.array([1, 1])))

    def testExpand_desdeVeintiuno(self):
        np.testing.assert_array_equal(np.array([1, 2, 1, 1]), expand(np.array([2, 1])))

    def testExpand_desdeMilDoscientosOnce(self):
        np.testing.assert_array_equal(np.array([1, 1, 1, 2, 2, 1]), expand(np.array([1, 2, 1, 1])))

    def testList2num_once(self):
        self.assertEqual(11, list2num(np.array([1, 1])))

    def testList2num_veintiuno(self):
        self.assertEqual(21, list2num(np.array([2, 1])))

    def testList2num_milDoscientosOnce(self):
        self.assertEqual(1211, list2num(np.array([1, 2, 1, 1])))

    def testList2num_cientoOnceMilDoscientosVeintiuno(self):
        self.assertEqual(111221, list2num(np.array([1, 1, 1, 2, 2, 1])))


if __name__ == "__main__":
    unittest.main()