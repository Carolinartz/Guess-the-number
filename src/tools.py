
import random

def get_random_number(ranges):
    """"
    Genera un número aleatorio.
    
    Args:
        ranges (dict): Diccionario con los valores mínimo y máximo.
        
    Returns:
        int: El número aleatorio generado.
    """
    min_range = ranges["min"]
    max_range = ranges["max"]
    number_random = random.randint(min_range, max_range)
    print(number_random)
    return number_random


def get_validate_number(number, number_random, ranges, entity=""):
    """
    Valida si el número ingresado es correcto, demasiado bajo o demasiado alto.
    
    Args:
        number (int): El número a validar.
        number_random (int): El número aleatorio con el cual comparar.
        ranges (dict): Diccionario con el rango de valores mínimo y máximo.
        entity (str): Descripción de quién está adivinando ("usuario" o "computador").
    
    Returns:
        bool: True si el número es correcto, False en caso contrario.
        str: Mensaje indicando pistas o resultados.
    """
    if not (ranges['min'] <= number <= ranges['max']):
        return False, f"{entity}: El número no es válido. Debe estar entre {ranges['min']} y {ranges['max']}."
    elif number == number_random:
        return True, f"¡Felicidades, {entity}! Has adivinado el número correctamente."
    elif number < number_random:
        return False, "El número es mayor."
    else:
        return False, "El número es menor."
