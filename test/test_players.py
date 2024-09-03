import unittest
from unittest.mock import patch
from src.players import player_guess, computer_guess

class TestGameFunctions(unittest.TestCase):

    @patch('builtins.input', return_value='50')
    def test_player_guess_valid(self, mock_input):
        """Prueba que player_guess devuelve el número ingresado por el jugador."""
        result = player_guess()
        self.assertEqual(result, 50)

    @patch('builtins.input', side_effect=['abc', '25'])
    def test_player_guess_invalid(self, mock_input):
        """Prueba que player_guess maneja entradas no válidas y solicita un número válido."""
        with patch('builtins.print') as mock_print:
            result = player_guess()
            self.assertEqual(result, 25)
            # Verifica que se haya llamado a print para la entrada no válida
            mock_print.assert_called_with("Por favor, ingrese un número válido.")
    
    def test_computer_guess(self):
        """Prueba que computer_guess usa búsqueda binaria para adivinar el número."""

        low = 1
        high = 100
        # La suposición debería ser el promedio de low y high
        result = computer_guess(low, high)
        expected = (low + high) // 2
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
