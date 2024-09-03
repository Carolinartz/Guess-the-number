import unittest
from unittest.mock import patch
from src.game import play_game, MAX_ATTEMPTS

class TestPlayGame(unittest.TestCase):

    @patch('src.game.get_random_number', return_value=50)
    @patch('src.game.print')
    @patch('src.game.get_validate_number', side_effect=[
        (False, "El número es mayor."),  # Primer intento del jugador (fallo)
        (False, "El número es menor."),  # Primer intento de la computadora (fallo)
        (True, "¡Felicidades, usuario! Has adivinado el número correctamente.")  # Segundo intento del jugador (acierto)
    ])
    @patch('src.game.player_guess', side_effect=[60, 50])
    @patch('src.game.computer_guess', return_value=40)
    def test_player_wins(self, mock_computer_guess, mock_player_guess, mock_validate, mock_print, mock_random_number):
        play_game()
        mock_print.assert_any_call("¡Felicidades, usuario! Has adivinado el número correctamente.")
        mock_print.assert_any_call("Intentos del jugador: [60, 50]")

    @patch('src.game.get_random_number', return_value=50)
    @patch('src.game.print')
    @patch('src.game.get_validate_number', side_effect=[
        (False, "El número es mayor."),  # Primer intento del jugador (fallo)
        (False, "El número es menor."),  # Primer intento de la computadora (fallo)
        (False, "El número es mayor."),  # Segundo intento del jugador (fallo)
        (True, "El ordenador ha adivinado el número en 2 intentos.")  # Segundo intento de la computadora (acierto)
    ])
    @patch('src.game.player_guess', side_effect=[60, 40])
    @patch('src.game.computer_guess', return_value=50)
    def test_computer_wins(self, mock_computer_guess, mock_player_guess, mock_validate, mock_print, mock_random_number):
        play_game()
        mock_print.assert_any_call("El ordenador ha adivinado el número en 2 intentos.")

    @patch('src.game.get_random_number', return_value=50)
    @patch('src.game.print')
    @patch('src.game.get_validate_number', side_effect=[
        (False, "El número es mayor.") for _ in range(MAX_ATTEMPTS * 2)
    ])
    @patch('src.game.player_guess', return_value=60)
    @patch('src.game.computer_guess', return_value=40)
    def test_max_attempts_reached(self, mock_computer_guess, mock_player_guess, mock_validate, mock_print, mock_random_number):
        play_game()
        mock_print.assert_any_call("Se ha alcanzado el número máximo de intentos permitidos.")
    
if __name__ == '__main__':
    unittest.main()
