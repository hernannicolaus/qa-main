import unittest

def esFizz(numero: int) -> str:
    salida = numero
    if numero % 3 == 0 and numero % 5 == 0:
        salida = "FizzBuzz"
    elif numero % 3 == 0:
        salida = "Fizz"
    elif numero % 5 == 0:
        salida = "Buzz"
    return str(salida)

def get_lista(numero: int) -> list:
    lista = []
    for i in range(1, numero + 1):
        lista.append(esFizz(i))
    return lista

class testFizz(unittest.TestCase):
    def testEsFizz_fizzbuzz(self):
        ## self.assertEqual(esperado,actual)
        self.assertEqual(esFizz(15), "FizzBuzz")

    def testEsFizz_fizz(self):
        self.assertEqual(esFizz(3), "Fizz")

    def testEsFizz_buzz(self):
        self.assertEqual(esFizz(5), "Buzz")

    def testEsFizz_ninguno(self):
        self.assertEqual(esFizz(7), "7")

    def testGetLista_longitud(self):
        resultados = get_lista(15)
        self.assertEqual(len(resultados), 15)

    def testGetLista_fizz(self):
        resultados = get_lista(15)
        self.assertEqual(resultados[2], "Fizz")

    def testGetLista_buzz(self):
        resultados = get_lista(15)
        self.assertEqual(resultados[4], "Buzz")

    def testGetLista_fizzbuzz(self):
        resultados = get_lista(15)
        self.assertEqual(resultados[14], "FizzBuzz")

    def testGetLista_numero(self):
        resultados = get_lista(15)
        self.assertEqual(resultados[0], "1")

    def testGetLista_soloNumeros(self):
        resultados = get_lista(2)
        self.assertEqual(resultados, ["1", "2"])


if __name__ == "__main__":
    for resultado in get_lista(100):
        print(resultado)
    unittest.main()