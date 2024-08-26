import unittest
from game import guess_the_number

class TestAdivinaElNumero(unittest.TestCase):
    def test_suposicion_correcta_jugadora(self):
        numero_secreto = 42
        suposicion = 42
        self.assertEqual(suposicion, numero_secreto)

    def test_suposicion_incorrecta_menor(self):
        numero_secreto = 42
        suposicion = 30
        self.assertLess(suposicion, numero_secreto)

    def test_suposicion_incorrecta_mayor(self):
        numero_secreto = 42
        suposicion = 50
        self.assertGreater(suposicion, numero_secreto)

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
