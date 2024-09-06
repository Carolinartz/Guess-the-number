MAX_ATTEMPTS = 10 # Número máximo de intentos permitidos

from src.tools import get_random_number
from src.players import player_turn, computer_turn

def initialize_game(ranges): #teste que genere que el 1 al 100 en random
    """
    Inicializa los valores iniciales del juego.
    """


    secret_number = get_random_number(ranges)
    player_attempts = []
    computer_attempts = []
    shift = 'player'
    low, high = ranges['min'], ranges['max']
    return secret_number, player_attempts, computer_attempts, shift, low, high

def print_results(attempts_counter, player_attempts, computer_attempts):
    """
    Imprime los resultados del juego.
    """
    if attempts_counter < MAX_ATTEMPTS:
        print(f"Intentos del jugador: {player_attempts} Intentos del ordenador : {computer_attempts}" if len(player_attempts) > 0 else f"El ordenador ha adivinado el número en {len(computer_attempts)} intentos.")
    else:
        print("Se ha alcanzado el número máximo de intentos permitidos.")

def play_game():
    """
    Ejecuta la lógica principal del juego.
    """
    ranges = {"min": 1, "max": 100}
    secret_number, player_attempts, computer_attempts, shift, low, high = initialize_game(ranges)
    
    attempts_counter = 0  # Contador de intentos

    # El bucle se ejecutará mientras el número de intentos sea menor o igual a MAX_ATTEMPTS
    while attempts_counter < MAX_ATTEMPTS:
        if shift == 'player':
            correct = player_turn(player_attempts, secret_number, ranges)
            if correct:
                break
            shift = 'computer'
        else:
            correct, low, high = computer_turn(computer_attempts, secret_number, ranges, low, high)
            if correct:
                break
            shift = 'player'

        attempts_counter += 1  # Incrementar el contador de intentos

    print_results(attempts_counter, player_attempts, computer_attempts)

if __name__ == "__main__":
    play_game()
