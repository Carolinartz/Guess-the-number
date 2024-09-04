from src.number import get_validate_number

def player_guess():
 
    while True:
        try:
            return int(input("Adivina el número entre 1 y 100: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")

def computer_guess(low, high):
    return (low + high) // 2

def player_turn(player_attempts, secret_number, ranges):
    assumption = player_guess()
    player_attempts.append(assumption) 
    correct, message = get_validate_number(assumption, secret_number, ranges, "jugador")
    print(message)
    return correct

def computer_turn(computer_attempts, secret_number, ranges, low, high):
   
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
