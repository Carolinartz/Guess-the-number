import unittest
from unittest.mock import patch, call
from src.tools import get_validate_number
from src.players import player_guess, computer_guess, player_turn, computer_turn

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



if __name__ == '__main__':
    unittest.main()
