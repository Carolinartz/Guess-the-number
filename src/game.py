from .tools import get_random_number, get_validate_number
from .players import print_information, player_guess, computer_guess

def play_game():
    """
    Ejecuta la lógica principal del juego.
    """
    print_information()
    
    ranges = {"min": 1, "max": 100}
    secret_number = get_random_number(ranges)
    player_attempts = []
    computer_attempts = []
    shift = 'player'
    low, high = ranges['min'], ranges['max']

    while True:
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
