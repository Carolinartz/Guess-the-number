import unittest
from unittest.mock import patch
from src.game import initialize_game, print_results, play_game

class TestGameFunctions(unittest.TestCase):
    
    def test_initialize_game(self):
        ranges = {"min": 1, "max": 100}
        player_attempts = []
        computer_attempts = []
        shift = 'player'
        low = ranges['min']
        high = ranges['max']
        
        result = initialize_game(ranges)

        self.assertEqual(type(result[0]), int, "El número secreto no es el esperado.")
        self.assertEqual(result[1], player_attempts, "Los intentos del jugador no son los esperados.")
        self.assertEqual(result[2], computer_attempts, "Los intentos del ordenador no son los esperados.")
        self.assertEqual(result[3], shift, "El turno inicial no es el esperado.")
        self.assertEqual(result[4], low, "El límite inferior no es el esperado.")
        self.assertEqual(result[5], high, "El límite superior no es el esperado.")

class TestPrintResults(unittest.TestCase):

    @patch('src.game.MAX_ATTEMPTS', 10)
    def test_max_attempts_reached(self):
        attempts_counter = 10
        player_attempts = [3, 5, 8, 9]
        computer_attempts = [1, 2, 4, 6]

        with patch('builtins.print') as mock_print:
            print_results(attempts_counter, player_attempts, computer_attempts)
            mock_print.assert_called_once_with("Se ha alcanzado el número máximo de intentos permitidos.")

    @patch('src.game.MAX_ATTEMPTS', 10)
    def test_player_wins(self):
        attempts_counter = 9
        player_attempts = [10, 20, 30, 40, 50]
        computer_attempts = []

        with patch('builtins.print') as mock_print:
            print_results(attempts_counter, player_attempts, computer_attempts)
            mock_print.assert_called_once_with(f"Intentos del jugador: {player_attempts}")

class TestPlayGame(unittest.TestCase):

    @patch('src.game.initialize_game')
    @patch('src.game.player_turn')
    @patch('src.game.computer_turn')
    @patch('src.game.print_results')
    def test_play_game(self, mock_print_results, mock_computer_turn, mock_player_turn, mock_initialize_game):
        mock_initialize_game.return_value = (50, [], [], 'player', 1, 100)
        mock_player_turn.return_value = False
        mock_computer_turn.return_value = (False, 1, 100)

        play_game()

        mock_initialize_game.assert_called_once_with({"min": 1, "max": 100})
        mock_player_turn.assert_called()
        mock_computer_turn.assert_called()
        mock_print_results.assert_called()

# Ejecutar los tests si este archivo es el principal
if __name__ == '__main__':
    unittest.main()
