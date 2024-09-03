from src.tools import get_validate_number

def player_guess():
    """
    Solicita al jugador ingresar un número y lo retorna.
    
    Returns:
        int: El número ingresado por el jugador.
    """
    while True:
        try:
            return int(input("Adivina el número entre 1 y 100: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")

def computer_guess(low, high):
    """
    Calcula la suposición del computador usando búsqueda binaria.
    
    Args:
        low (int): El límite inferior para la búsqueda.
        high (int): El límite superior para la búsqueda.
    
    Returns:
        int: El número que el computador adivina.
    """
    return (low + high) // 2

def player_turn(player_attempts, secret_number, ranges):
    """
    Ejecuta la lógica del turno del jugador.
    """
    assumption = player_guess()
    player_attempts.append(assumption) 
    correct, message = get_validate_number(assumption, secret_number, ranges, "jugador")
    print(message)
    return correct

def computer_turn(computer_attempts, secret_number, ranges, low, high):
    """
    Ejecuta la lógica del turno de la computadora.
    """
    assumption = computer_guess(low, high)
    computer_attempts.append(assumption)
    print(f"El ordenador adivina: {assumption}")
    correct, message = get_validate_number(assumption, secret_number, ranges, "computador")
    print(message)
    if message == "El número es mayor.":
        low = assumption + 1
    else:
        high = assumption - 1
    return correct, low, high
