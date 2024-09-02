import unittest
from unittest.mock import patch
from src.tools import get_random_number, get_validate_number
from src.players import player_guess, computer_guess
from src.game import play_game

class TestTools(unittest.TestCase):
    def test_get_random_number(self):
        ranges = {"min": 1, "max": 100}
        number = get_random_number(ranges)
        self.assertTrue(ranges["min"] <= number <= ranges["max"])
    
    def test_get_validate_number(self):
        ranges = {"min": 1, "max": 100}
        secret_number = 50
        
        correct, message = get_validate_number(50, secret_number, ranges, "jugador")
        self.assertTrue(correct)
        self.assertIn("¡Felicidades", message)
        
        correct, message = get_validate_number(25, secret_number, ranges, "jugador")
        self.assertFalse(correct)
        self.assertEqual(message, "El número es mayor.")
        
        correct, message = get_validate_number(75, secret_number, ranges, "jugador")
        self.assertFalse(correct)
        self.assertEqual(message, "El número es menor.")
        
class TestPlayers(unittest.TestCase):
    @patch('builtins.input', return_value='42')
    def test_player_guess(self, mock_input):
        guess = player_guess()
        self.assertEqual(guess, 42)
    
    def test_computer_guess(self):
        ranges = {"min": 1, "max": 100}
        guess = computer_guess(ranges, 1, 100)
        self.assertTrue(1 <= guess <= 100)

class TestGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['42', '42', 'no'])
    @patch('src.players.player_guess', return_value=42)
    @patch('src.tools.get_random_number', return_value=42)
    def test_play_game(self, mock_random, mock_guess, mock_input):
        play_game()



