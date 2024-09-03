import unittest
from unittest.mock import patch
from src.tools import get_random_number, get_validate_number

class TestTools(unittest.TestCase):

    @patch('src.tools.random.randint', return_value=42)  # Simula el número aleatorio como 42
    def test_get_random_number(self, mock_randint):
        ranges = {"min": 1, "max": 100}
        
        # Llama a la función que se está probando
        result = get_random_number(ranges)
        
        # Verifica que el número aleatorio generado sea 42
        self.assertEqual(result, 42)
        
        # Verifica que randint() se llamó con los valores correctos
        mock_randint.assert_called_once_with(ranges["min"], ranges["max"])

    def test_get_validate_number(self):
        ranges = {"min": 1, "max": 100}
        
        # Caso 1: Número correcto
        result = get_validate_number(42, 42, ranges, "usuario")
        self.assertEqual(result, (True, "¡Felicidades, usuario! Has adivinado el número correctamente."))
        
        # Caso 2: Número demasiado bajo
        result = get_validate_number(30, 42, ranges, "jugador")
        self.assertEqual(result, (False, "El número es mayor."))
        
        # Caso 3: Número demasiado alto
        result = get_validate_number(50, 42, ranges, "jugador")
        self.assertEqual(result, (False, "El número es menor."))
        
        # Caso 4: Número fuera de rango
        result = get_validate_number(0, 42, ranges, "jugador")
        self.assertEqual(result, (False, "jugador: El número no es válido. Debe estar entre 1 y 100."))
        
        result = get_validate_number(101, 42, ranges, "jugador")
        self.assertEqual(result, (False, "jugador: El número no es válido. Debe estar entre 1 y 100."))

if __name__ == '__main__':
    unittest.main()
