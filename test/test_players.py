import unittest
from unittest.mock import patch, call

from src.players import player_guess, computer_guess, player_turn, computer_turn
from src.tools import get_validate_number

class ValidateImput(unittest.TestCase):

    @patch('builtins.input', return_value='10')
    def test_player_guess(self, mock_input):
        # Simula la entrada del usuario y verifica la salida de player_guess
        self.assertEqual(player_guess(), 10)
        
    @patch('builtins.input', side_effect=['abc', '10'])
    @patch('builtins.print')
    def test_player_guess_invalid_input(self, mock_print, mock_input):
        # Ejecutar la función que queremos probar
        player_guess()
        
        # Verificar que `print` fue llamado con el mensaje de error adecuado
        self

class ComputerGuessTest(unittest.TestCase):
    def test_computer_guess(self):
        # Pruebas con diferentes valores de low y high
        self.assertEqual(computer_guess(1, 100), 50)
        self.assertEqual(computer_guess(10, 20), 15)
        self.assertEqual(computer_guess(5, 9), 7)
        self.assertEqual(computer_guess(0, 1), 0)
        self.assertEqual(computer_guess(7, 8), 7)
        self.assertEqual(computer_guess(50, 50), 50)  # caso donde low y high son igualesclass TestPlayerTurn(TestCase):
   
   
class TestPlayerTurn(unittest.TestCase):
    @patch('src.players.player_guess', return_value=50)
    def test_player_turn_adds_guess_to_list(self, mock_player_guess):
        # Configurar los mocks
        player_attempts = []
        ranges = {"min": 1, "max": 100}
        secret_number = 70  # Número secreto que no es relevante en este caso

        # Ejecutar la función player_turn
        player_turn(player_attempts, secret_number, ranges)

        # Verificar que el número ingresado se añadió a la lista
        self.assertIn(50, player_attempts, "El número ingresado por el jugador no se añadió a la lista.")

        # Verificar que player_guess fue llamado
        mock_player_guess.assert_called_once()
        
if __name__ == '__main__':
    unittest.main()
