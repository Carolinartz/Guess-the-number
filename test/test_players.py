import unittest
from unittest.mock import patch
from src.tools import get_validate_number
from src.players import player_guess, computer_guess, player_turn, computer_turn

class TestGameFunctions(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['50', 'abc', '70'])
    def test_player_guess(self, mock_input):
        # Simulando una entrada incorrecta primero, luego correcta
        self.assertEqual(player_guess(), 50)
        self.assertEqual(player_guess(), 70)
    
    def test_computer_guess(self):
        # Verificando si la suposición del ordenador es correcta
        self.assertEqual(computer_guess(1, 100), 50)
        self.assertEqual(computer_guess(51, 100), 75)
        self.assertEqual(computer_guess(1, 50), 25)

    @patch('src.tools.get_validate_number')
    @patch('builtins.input', side_effect=['50', '30'])
    def test_player_turn(self, mock_input, mock_get_validate_number):
        # Simular diferentes respuestas de la función get_validate_number
        mock_get_validate_number.return_value = (False, "El número es menor.")
        player_attempts = []
        ranges = {"min": 1, "max": 100}
        secret_number = 70

        # Primer intento incorrecto
        result = player_turn(player_attempts, secret_number, ranges)
        self.assertFalse(result)
        self.assertIn(50, player_attempts)
        mock_get_validate_number.assert_called_with(50, secret_number, ranges, "jugador")

if __name__ == '__main__':
    unittest.main()

