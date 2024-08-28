import unittest
from unittest.mock import patch

# Suponiendo que el juego está en un archivo llamado guess_the_number.py
from game import guess_the_number

class TestGuessTheNumber(unittest.TestCase):

    @patch('builtins.input', side_effect=['50', '70', '60', 'no'])
    @patch('random.randint', return_value=60)
    def test_player_wins(self, mock_randint, mock_input):
        with patch('builtins.print') as mock_print:
            guess_the_number()
            
            # Verifica que la jugadora adivine correctamente
            mock_print.assert_any_call("¡Felicidades! Has adivinado el número 60 en 3 intentos.")
    
    @patch('builtins.input', side_effect=['40', 'sí', '30', 'sí', '60', 'no'])
    @patch('random.randint', side_effect=[60, 90])
    def test_multiple_rounds(self, mock_randint, mock_input):
        with patch('builtins.print') as mock_print:
            guess_the_number()
            
            # Verifica que se juega más de una ronda
            self.assertTrue(mock_randint.called)
            self.assertTrue(mock_input.called)
    
    @patch('builtins.input', side_effect=['60', 'no'])
    @patch('random.randint', return_value=60)
    def test_computer_wins(self, mock_randint, mock_input):
        with patch('builtins.print') as mock_print:
            guess_the_number()
            
            # Verifica que la computadora adivine correctamente
            mock_print.assert_any_call("El ordenador ha adivinado el número 60 en 1 intentos.")

if __name__ == '__main__':
    unittest.main()
