import unittest
from src.game import initialize_game, print_results, play_game
from unittest.mock import patch

class TestGameFunctions(unittest.TestCase):
    
    def test_initialize_game(self):
        ranges = {"min": 1, "max": 100}
        
        # Establece un valor fijo para el número secreto en la prueba
        
        
        # Inicializa los valores esperados
        player_attempts = []
        computer_attempts = []
        shift = 'player'
        low = ranges['min']
        high = ranges['max']
        
        # Llama a la función con una implementación fija de get_random_number
        # que devuelve el valor que hemos definido para secret_number.
        # Puedes ajustar la implementación de `initialize_game` para 
        # permitir la inyección del valor fijo de secret_number.
        result = initialize_game(ranges)

        # Compara el resultado de la función con los valores esperados.
        self.assertEqual(type(result[0]), int,"El número secreto no es el esperado.")
        self.assertEqual(result[1], player_attempts, "Los intentos del jugador no son los esperados.")
        self.assertEqual(result[2], computer_attempts, "Los intentos del ordenador no son los esperados.")
        self.assertEqual(result[3], shift, "El turno inicial no es el esperado.")
        self.assertEqual(result[4], low, "El límite inferior no es el esperado.")
        self.assertEqual(result[5], high, "El límite superior no es el esperado.")

class TestPrintResults(unittest.TestCase):

    @patch('src.game.MAX_ATTEMPTS', 10)
    def test_max_attempts_reached(self):
        # Configuramos los valores de prueba para simular que se alcanzaron el máximo de intentos
        attempts_counter = 10
        player_attempts = [3, 5, 8, 9]
        computer_attempts = [1, 2, 4, 6]

        # Mockeamos la función print para capturar la salida
        with patch('builtins.print') as mock_print:
            print_results(attempts_counter, player_attempts, computer_attempts)

            # Verificamos que se imprime el mensaje de número máximo de intentos alcanzado
            mock_print.assert_called_once_with("Se ha alcanzado el número máximo de intentos permitidos.")

    @patch('src.game.MAX_ATTEMPTS', 10)
    def test_player_wins(self):
        # Configuramos los valores de prueba para simular que el jugador adivinó el número correcto
        attempts_counter = 9
        player_attempts = [10, 20, 30, 40, 50]
        computer_attempts = []

        # Mockeamos la función print para capturar la salida
        with patch('builtins.print') as mock_print:
            print_results(attempts_counter, player_attempts, computer_attempts)

            # Verificamos que se imprime la lista de intentos del jugador
            mock_print.assert_called_once_with(f"Intentos del jugador: {player_attempts}")
