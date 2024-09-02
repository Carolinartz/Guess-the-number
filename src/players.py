
def player_guess():
    """
    Solicita al jugador ingresar un número y lo retorna.
    
    Returns:
        int: El número ingresado por el jugador.
    """
    return int(input("Adivina el número entre 1 y 100: "))

def computer_guess(ranges, low, high):
    """
    Calcula la suposición del computador usando búsqueda binaria.
    
    Args:
        ranges (dict): Diccionario con los valores mínimo y máximo.
        low (int): El límite inferior para la búsqueda.
        high (int): El límite superior para la búsqueda.
    
    Returns:
        int: El número que el computador adivina.
    """
    return (low + high) // 2
