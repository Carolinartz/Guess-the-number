import unittest
from src.game import initialize_game

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

if __name__ == '__main__':
    unittest.main()
