import unittest
from unittest.mock import patch
from src.game import play_game

MAX_TRY = 10

class TestPlayGame(unittest.TestCase):

    @patch('src.game.get_random_number', return_value=42)
    @patch('src.game.player_guess', return_value=42)
    @patch('src.game.computer_guess', side_effect=[30, 40, 41, 42])
    @patch('src.game.get_validate_number',side_effect=[(True, "¡Felicidades, usuario! Has adivinado el número correctamente.")])
    @patch('builtins.print')
    def test_play_game(self, mock_print, mock_validate, mock_computer_guess, mock_player_guess, mock_get_random_number):
        # Mock the behavior of get_validate_number
        def mock_validate_number(number, secret_number, ranges, entity):
            if number == secret_number:
                return True, "¡Felicidades, jugador! Has adivinado el número correctamente."
            elif number < secret_number:
                return False, "El número es mayor."
            else:
                return False, "El número es menor."

        mock_validate.side_effect = mock_validate_number

        # Call play_game
        play_game()

        # Assertions
        # Ensure get_random_number was called once
        mock_get_random_number.assert_called_once()

        # Ensure player_guess was called once
        mock_player_guess.assert_called_once()

        # Ensure computer_guess was called multiple times (in this case 4 times)
        self.assertEqual(mock_computer_guess.call_count, 4)

        # Check that the print function was called to output the results
        mock_print.assert_any_call("¡Felicidades, jugador! Has adivinado el número correctamente.")
        mock_print.assert_any_call("El ordenador adivina: 30")
        mock_print.assert_any_call("El ordenador adivina: 40")
        mock_print.assert_any_call("El ordenador adivina: 41")
        mock_print.assert_any_call("El ordenador adivina: 42")
        mock_print.assert_any_call("El ordenador ha adivinado el número en 4 intentos.")
