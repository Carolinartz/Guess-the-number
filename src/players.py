from src.tools import get_validate_number

def player_guess():
    """
    Solicita al jugador ingresar un número y lo retorna.
    """
    while True:
        try:
            return int(input("Adivina el número entre 1 y 100: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")

def computer_guess(low, high):
    """
    Genera una suposición para el computador basándose en el rango actual.
    
    Args:
        low (int): Límite inferior del rango actual.
        high (int): Límite superior del rango actual.
        
    Returns:
        int: La suposición del computador.
    """
    return (low + high) // 2

def player_turn(player_attempts, secret_number, ranges):
    """
    Maneja el turno del jugador.
    
    Args:
        player_attempts (list): Lista de intentos del jugador.
        secret_number (int): El número secreto que el jugador debe adivinar.
        ranges (dict): Diccionario con los rangos mínimo y máximo.
        
    Returns:
        bool: True si el jugador adivina el número, False en caso contrario.
    """
    assumption = player_guess()
    player_attempts.append(assumption)
    correct, message = get_validate_number(assumption, secret_number, ranges, "jugador")

    print(message)
    
    return correct

def computer_turn(computer_attempts, secret_number, ranges, low, high):
    """
    Maneja el turno del computador.
    
    Args:
        computer_attempts (list): Lista de intentos del computador.
        secret_number (int): El número secreto que el computador debe adivinar.
        ranges (dict): Diccionario con los rangos mínimo y máximo.
        low (int): Límite inferior del rango actual.
        high (int): Límite superior del rango actual.
        
    Returns:
        tuple: (bool, int, int) - Si el computador adivinó correctamente, nuevo límite inferior, nuevo límite superior.
    """
    assumption = computer_guess(low, high)
    print("verificandooooo missing")
    computer_attempts.append(assumption)
    print(f"El ordenador adivina: {assumption}")
    correct, message = get_validate_number(assumption, secret_number, ranges, "computador")
    print(message)
    if message == "El número es mayor.":
        low = assumption + 1
    elif message == "El número es menor.":
        high = assumption - 1
    return correct, low, high
