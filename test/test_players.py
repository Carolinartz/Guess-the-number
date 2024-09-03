import unittest
from unittest.mock import patch
from src.game import play_game

class TestPlayGame(unittest.TestCase):

 @patch('src.game.player_guess')
 @patch('src.game.computer_guess')
 @patch('src.game.get_random_number', return_value=50)
 @patch('src.game.get_validate_number', side_effect=[(False, "El número es mayor."),
                                                    (False, "El número es mayor."),
                                                    (False, "El número es menor."),
                                                    (True, "¡Felicidades, jugador!")])
 def test_play_game(self, mock_get_random_number, mock_get_validate_number, mock_computer_guess, mock_player_guess):
    mock_player_guess.side_effect = [25, 30, 40]  # Adivinanzas del jugador en 3 intentos
    mock_computer_guess.side_effect = [60]  # Adivinanza del computador

    play_game()

    self.assertEqual(mock_player_guess.call_count, 3)  # Verifica que se llame 3 veces
    play_game()

    self.assertEqual(mock_player_guess.call_count, 2)  # Cambia 3 por 2 si solo se llama dos veces
    mock_player_guess.assert_has_calls([patch.call(), patch.call()])
    self.assertEqual(mock_computer_guess.call_count, 1)  # Verifica que se llame 1 vez

if __name__ == "__main__":
    unittest.main()
