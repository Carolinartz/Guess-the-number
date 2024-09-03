MAX_ATTEMPTS = 20  # Número máximo de intentos permitidos

from .tools import get_random_number, get_validate_number
from .players import player_guess, computer_guess

def play_game():
    """
    Ejecuta la lógica principal del juego.
    """

    ranges = {"min": 1, "max": 100}
    secret_number = get_random_number(ranges)
    player_attempts = []
    computer_attempts = []
    shift = 'player'
    low, high = ranges['min'], ranges['max']

    attempts_counter = 0  # Contador de intentos

    # El bucle se ejecutará mientras el número de intentos sea menor o igual a MAX_ATTEMPTS
    while attempts_counter < MAX_ATTEMPTS:
        if shift == 'player':
            assumption = player_guess()
            player_attempts.append(assumption)
            correct, message = get_validate_number(assumption, secret_number, ranges, "jugador")
            print(message)
            if correct:
                print(f"Intentos del jugador: {player_attempts}")
                break
            shift = 'computer'
        else:
            assumption = computer_guess(ranges, low, high)
            computer_attempts.append(assumption)
            print(f"El ordenador adivina: {assumption}")
            correct, message = get_validate_number(assumption, secret_number, ranges, "computador")
            print(message)
            if correct:
                print(f"El ordenador ha adivinado el número en {len(computer_attempts)} intentos.")
                break
            elif message == "El número es mayor.":
                low = assumption + 1
            else:
                high = assumption - 1
            shift = 'player'

        attempts_counter += 1  # Incrementar el contador de intentos

    # Mensaje si se alcanzó el límite de intentos sin adivinar el número
    if attempts_counter >= MAX_ATTEMPTS:
        print("Se ha alcanzado el número máximo de intentos permitidos.")
