import unittest
from unittest.mock import patch
from src.players import player_turn, computer_turn, player_guess, computer_guess
from src.tools import get_validate_number

class TestGameFunctions(unittest.TestCase):

    def setUp(self):
        # Establecemos un número secreto predeterminado y un rango fijo para todas las pruebas
        self.secret_number = 50
        self.ranges = {"min": 1, "max": 100}
        self.low = 1
        self.high = 100

    @patch('src.players.player_guess')
    @patch('src.tools.get_validate_number')
    def test_player_turn_correct_guess(self, mock_validate_number, mock_player_guess):
        # Configuramos los valores para las funciones mock
        mock_player_guess.return_value = 50
        mock_validate_number.return_value = (True, "¡Correcto!")

        player_attempts = []
        result = player_turn(player_attempts, self.secret_number, self.ranges)

        # Verificamos el resultado
        self.assertTrue(result)
        self.assertEqual(player_attempts, [50])
        mock_player_guess.assert_called_once()
        mock_validate_number.assert_called_once_with(50, self.secret_number, self.ranges, "jugador")

    @patch('src.players.player_guess')
    @patch('src.tools.get_validate_number')
    def test_player_turn_incorrect_guess(self, mock_validate_number, mock_player_guess):
        mock_player_guess.return_value = 30
        mock_validate_number.return_value = (False, "El número es menor.")

        player_attempts = []
        result = player_turn(player_attempts, self.secret_number, self.ranges)

        # Verificamos el resultado
        self.assertFalse(result)
        self.assertEqual(player_attempts, [30])
        mock_player_guess.assert_called_once()
        mock_validate_number.assert_called_once_with(30, self.secret_number, self.ranges, "jugador")

    @patch('src.players.computer_guess')
    @patch('src.tools.get_validate_number')
    def test_computer_turn_correct_guess(self, mock_validate_number, mock_computer_guess):
        mock_computer_guess.return_value = 50
        mock_validate_number.return_value = (True, "¡Correcto!")

        computer_attempts = []
        result, new_low, new_high = computer_turn(computer_attempts, self.secret_number, self.ranges, self.low, self.high)

        # Verificamos el resultado
        self.assertTrue(result)
        self.assertEqual(computer_attempts, [50])
        self.assertEqual(new_low, self.low)
        self.assertEqual(new_high, self.high)
        mock_computer_guess.assert_called_once()
        mock_validate_number.assert_called_once_with(50, self.secret_number, self.ranges, "computador")

    @patch('src.players.computer_guess')
    @patch('src.tools.get_validate_number')
    def test_computer_turn_incorrect_guess_higher(self, mock_validate_number, mock_computer_guess):
        mock_computer_guess.return_value = 50
        mock_validate_number.return_value = (False, "El número es mayor.")

        computer_attempts = []
        result, new_low, new_high = computer_turn(computer_attempts, self.secret_number, self.ranges, self.low, self.high)

        # Verificamos el resultado
        self.assertFalse(result)
        self.assertEqual(computer_attempts, [50])
        self.assertEqual(new_low, 51)
        self.assertEqual(new_high, self.high)
        mock_computer_guess.assert_called_once()
        mock_validate_number.assert_called_once_with(50, self.secret_number, self.ranges, "computador")

    @patch('src.players.computer_guess')
    @patch('src.tools.get_validate_number')
    def test_computer_turn_incorrect_guess_lower(self, mock_validate_number, mock_computer_guess):
        mock_computer_guess.return_value = 50
        mock_validate_number.return_value = (False, "El número es menor.")

        computer_attempts = []
        result, new_low, new_high = computer_turn(computer_attempts, self.secret_number, self.ranges, self.low, self.high)

        # Verificamos el resultado
        self.assertFalse(result)
        self.assertEqual(computer_attempts, [50])
        self.assertEqual(new_low, self.low)
        self.assertEqual(new_high, 49)
        mock_computer_guess.assert_called_once()
        mock_validate_number.assert_called_once_with(50, self.secret_number, self.ranges, "computador")

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import patch
from src.players import player_turn, computer_turn

class TestGameFunctions(unittest.TestCase):

    @patch('src.players.player_guess')
    @patch('src.tools.get_validate_number')
    def test_player_turn_correct_guess(self, mock_validate_number, mock_player_guess):
        # Configurar los valores de retorno para las funciones mock
        mock_player_guess.return_value = 50
        mock_validate_number.return_value = (True, "¡Correcto!")

        player_attempts = []
        secret_number = 50
        ranges = {"min": 1, "max": 100}

        result = player_turn(player_attempts, secret_number, ranges)

        # Verificar que la función devuelva True cuando la suposición es correcta
        self.assertTrue(result)
        self.assertEqual(player_attempts, [50])
        mock_player_guess.assert_called_once()
        mock_validate_number.assert_called_once_with(50, secret_number, ranges, "jugador")

    @patch('src.players.player_guess')
    @patch('src.tools.get_validate_number')
    def test_player_turn_incorrect_guess(self, mock_validate_number, mock_player_guess):
        mock_player_guess.return_value = 30
        mock_validate_number.return_value = (False, "El número es menor.")

        player_attempts = []
        secret_number = 50
        ranges = {"min": 1, "max": 100}

        result = player_turn(player_attempts, secret_number, ranges)

        self.assertFalse(result)
        self.assertEqual(player_attempts, [30])
        mock_player_guess.assert_called_once()
        mock_validate_number.assert_called_once_with(30, secret_number, ranges, "jugador")

    @patch('src.tools.get_validate_number')
    def test_computer_turn_correct_guess(self, mock_validate_number):
        mock_validate_number.return_value = (True, "¡Correcto!")

        computer_attempts = []
        secret_number = 50
        ranges = {"min": 1, "max": 100}
        low, high = 1, 100

        result, new_low, new_high = computer_turn(computer_attempts, secret_number, ranges, low, high)

        self.assertTrue(result)
        self.assertEqual(computer_attempts, [50])
        self.assertEqual(new_low, low)
        self.assertEqual(new_high, high)
        mock_validate_number.assert_called_once_with(50, secret_number, ranges, "computador")

    @patch('src.tools.get_validate_number')
    def test_computer_turn_incorrect_guess_higher(self, mock_validate_number):
        mock_validate_number.return_value = (False, "El número es mayor.")

        computer_attempts = []
        secret_number = 75
        ranges = {"min": 1, "max": 100}
        low, high = 1, 100

        result, new_low, new_high = computer_turn(computer_attempts, secret_number, ranges, low, high)

        self.assertFalse(result)
        self.assertEqual(computer_attempts, [50])
        self.assertEqual(new_low, 51)
        self.assertEqual(new_high, high)
        mock_validate_number.assert_called_once_with(50, secret_number, ranges, "computador")

    @patch('src.tools.get_validate_number')
    def test_computer_turn_incorrect_guess_lower(self, mock_validate_number):
        mock_validate_number.return_value = (False, "El número es menor.")

        computer_attempts = []
        secret_number = 25
        ranges = {"min": 1, "max": 100}
        low, high = 1, 100

        result, new_low, new_high = computer_turn(computer_attempts, secret_number, ranges, low, high)

        self.assertFalse(result)
        self.assertEqual(computer_attempts, [50])
        self.assertEqual(new_low, low)
        self.assertEqual(new_high, 49)
        mock_validate_number.assert_called_once_with(50, secret_number, ranges, "computador")

if __name__ == '__main__':
    unittest.main()
