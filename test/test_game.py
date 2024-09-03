import unittest
from unittest.mock import patch
from src.game import play_game, MAX_ATTEMPTS

class TestPlayGame(unittest.TestCase):

    @patch('src.game.get_random_number', return_value=50)
    @patch('src.game.player_guess')
    @patch('src.game.computer_guess')
    @patch('src.game.get_validate_number')
    @patch('builtins.print')
    def test_player_wins(self, mock_print, mock_get_validate_number, mock_computer_guess, mock_player_guess,mock_get_random_number):
        """Prueba que el jugador gana el juego cuando adivina el número."""
        # Configuración de los mocks
        mock_player_guess.side_effect = [25, 30, 50]  # El jugador adivina correctamente en el tercer intento
        mock_get_validate_number.side_effect = [
            (False, "El número es mayor."), 
            (False, "El número es mayor."),
            (True, "¡Felicidades, jugador!")]
   #comprobar el numero de veces que llama a computer guees si son tres intentos
        # Ejecutar la función a probar
        play_game()

        # Verificaciones
        self.assertEqual(mock_player_guess.call_count, 2)  # Verifica que el jugador haya adivinado 3 veces
       # mock_computer_guess.assert_not_called()  # El computador no debería adivinar

    @patch('src.game.get_random_number', return_value=50)
    @patch('src.game.player_guess', return_value=25)
    @patch('src.game.computer_guess', side_effect=[75, 50])  # Simular adivinanzas del computador
    @patch('src.game.get_validate_number')
    @patch('builtins.print')
    def test_computer_wins(self, mock_print, mock_get_validate_number, mock_computer_guess, mock_player_guess, mock_get_random_number):
        """Prueba que el computador gana el juego cuando adivina el número."""
        # Configuración de los mocks
        mock_get_validate_number.side_effect = [  #posiblidad de no mockear esta función 
            (False, "El número es menor."),
            (True, "¡Felicidades, computador!")]

        # Ejecutar la función a probar
        play_game()

        # Verificaciones
        self.assertEqual(mock_computer_guess.call_count, 2)  # Verifica que el computador haya adivinado 2 veces
        mock_player_guess.assert_called_once()  # El jugador debería haber adivinado una vez

    @patch('src.game.get_random_number', return_value=50)
    @patch('src.game.player_guess')
    @patch('src.game.computer_guess')
    @patch('src.game.get_validate_number')
    @patch('builtins.print')
    def test_max_attempts_reached(self, mock_get_validate_number, mock_computer_guess, mock_player_guess):
        """Prueba que el juego termina cuando se alcanzan el número máximo de intentos."""
        # Configuración de los mocks
        mock_player_guess.side_effect = [25] * MAX_ATTEMPTS  # El jugador hace 20 intentos fallidos
        mock_get_validate_number.side_effect = [(False, "El número es mayor.")] * MAX_ATTEMPTS

        # Ejecutar la función a probar
        play_game()

        # Verificaciones
        self.assertEqual(mock_player_guess.call_count, MAX_ATTEMPTS)  # Verifica que el jugador haya adivinado MAX_ATTEMPTS veces
        mock_computer_guess.assert_not_called()  # El computador no debería adivinar

    @patch('src.game.get_random_number', return_value=50)
    @patch('src.game.player_guess', return_value=25)
    @patch('src.game.computer_guess', side_effect=[50, 75])  # Simular adivinanzas del computador
    @patch('src.game.get_validate_number')
    @patch('builtins.print')
    def test_player_and_computer_interaction(self, mock_print, mock_get_validate_number, mock_computer_guess, mock_player_guess):
        """Prueba la interacción entre jugador y computador en el juego."""
        # Configuración de los mocks
        mock_get_validate_number.side_effect = [
            (False, "El número es mayor."),  # Respuesta para el jugador
            (True, "¡Felicidades, computador!")]  # Respuesta para el computador

        # Ejecutar la función a probar
        play_game()

        # Verificaciones
        self.assertEqual(mock_player_guess.call_count, 1)  # Verifica que el jugador haya adivinado 1 vez
        self.assertEqual(mock_computer_guess.call_count, 1)  # Verifica que el computador haya adivinado 2 veces

if __name__ == '__main__':
    unittest.main()

