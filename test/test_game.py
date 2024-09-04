import unittest
from unittest.mock import patch
from src.game import initialize_game, print_results, play_game
from src.players import player_turn, computer_turn
from src.number import get_random_number, get_validate_number

class TestGameFunctions(unittest.TestCase):

    def setUp(self):
        # Establecemos un rango fijo para las pruebas
        self.ranges = {"min": 1, "max": 100}
        self.secret_number = 50  # Número secreto predeterminado

    @patch('src.tools.get_random_number')
    def test_initialize_game(self, mock_get_random_number):
        # Configuramos el valor de retorno del mock
        mock_get_random_number.return_value = self.secret_number

        secret_number, player_attempts, computer_attempts, shift, low, high = initialize_game(self.ranges)

        # Verificamos que los valores sean los esperados
        self.assertEqual(secret_number, self.secret_number)
        self.assertEqual(player_attempts, [])
        self.assertEqual(computer_attempts, [])
        self.assertEqual(shift, 'player')
        self.assertEqual(low, self.ranges['min'])
        self.assertEqual(high, self.ranges['max'])

    @patch('builtins.print')
    def test_print_results(self, mock_print):
        # Prueba con menos de MAX_ATTEMPTS
        player_attempts = [10, 20]
        computer_attempts = [30]
        print_results(5, player_attempts, computer_attempts)
        mock_print.assert_called_with(f"Intentos del jugador: {player_attempts}")

        # Prueba cuando se alcanzan los MAX_ATTEMPTS
        print_results(20, player_attempts, computer_attempts)
        mock_print.assert_called_with("Se ha alcanzado el número máximo de intentos permitidos.")

    @patch('src.players.player_turn')
    @patch('src.players.computer_turn')
    @patch('src.tools.get_validate_number')
    @patch('src.tools.get_random_number')
    @patch('builtins.print')
    def test_play_game(self, mock_print, mock_get_random_number, mock_get_validate_number, mock_computer_turn, mock_player_turn):
        # Configuramos los mocks
        mock_get_random_number.return_value = self.secret_number
        mock_player_turn.side_effect = [False, True]  # Jugador adivina en el segundo intento
        mock_computer_turn.return_value = (False, self.ranges['min'], self.ranges['max'])
        mock_get_validate_number.return_value = (True, "¡Correcto!")  # Validación exitosa para el jugador

        with patch('src.game.initialize_game') as mock_initialize_game:
            mock_initialize_game.return_value = (self.secret_number, [], [], 'player', self.ranges['min'], self.ranges['max'])
            play_game()

        # Verificamos las llamadas y resultados esperados
        mock_initialize_game.assert_called_once_with(self.ranges)
        mock_player_turn.assert_called()
        mock_computer_turn.assert_called()
        mock_print.assert_called_with(f"Intentos del jugador: {[10, 20]}")

if __name__ == '__main__':
    unittest.main()
