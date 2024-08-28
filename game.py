import random

def guess_the_number():
    while True:  # Bucle principal para permitir jugar de nuevo
        secret_number = random.randint(1, 100)
        player_attempts = []
        computer_attempts = []
        shift = 'player'
        
        low, high = 1, 100  # Rango inicial para la búsqueda binaria
        
        while True:  # Bucle para el juego en sí
            if shift == 'player':
                # Obtener la suposición de la jugadora
                assumption = int(input("Adivina el número entre 1 y 100: "))
                player_attempts.append(assumption)
                
                # Comprobar si la suposición es correcta
                if assumption == secret_number:
                    print(f"¡Felicidades! Has adivinado el número {secret_number} en {len(player_attempts)} intentos.")
                    print("Intentos de la jugadora: ", player_attempts)
                    break
                elif assumption < secret_number:
                    print("El número secreto es mayor.")
                else:
                    print("El número secreto es menor.")
                shift = 'computer'
                
            else:
                # La computadora usa búsqueda binaria en lugar de adivinar al azar
                assumption = (low + high) // 2
                computer_attempts.append(assumption)
                print(f"El ordenador adivina: {assumption}")
                
                if assumption == secret_number:
                    print(f"El ordenador ha adivinado el número {secret_number} en {len(computer_attempts)} intentos.")
                    break
                elif assumption < secret_number:
                    print("El número secreto es mayor.")
                    low = assumption + 1  # Ajusta el límite inferior
                else:
                    print("El número secreto es menor.")
                    high = assumption - 1  # Ajusta el límite superior
                shift = 'player'
        
        # Preguntar si la jugadora quiere jugar de nuevo
        play_again = input("¿Quieres jugar de nuevo? (sí/no): ").lower()
        if play_again != 'sí':
            print("¡Gracias por jugar!")
            break

# Ejecutar el juego
guess_the_number()
