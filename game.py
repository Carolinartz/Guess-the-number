import random

def guess_the_number():
    while True:  # Bucle principal para permitir jugar de nuevo
        secret_number = random.randint(0, 100)
        player = []
        computer = []
        shift = 'player'
        
        while True:  # Bucle para el juego en sí
            if shift == 'player':
                # Obtener la suposición de la jugadora
                assumption = int(input("Adivina el número entre 1 y 100: "))
                player.append(assumption)
                
                # Comprobar si la suposición es correcta
                if assumption == secret_number:
                    print(f"¡Felicidades! Has adivinado el número {secret_number} en {len(player)} intentos.")
                    print("Intentos de la jugadora: ", player)
                    break
                elif assumption < secret_number:
                    print("El número secreto es mayor.")
                else:
                    print("El número secreto es menor.")
                shift = 'computer'
                
            else:
                # El ordenador hace una suposición aleatoria
                assumption = random.randint(0, 100)
                computer.append(assumption)
                print(f"El ordenador adivina: {assumption}")
                
                if assumption == secret_number:
                    print(f"El ordenador ha adivinado el número {secret_number} en {len(computer)} intentos.")
                    break
                elif assumption < secret_number:
                    print("El número secreto es mayor.")
                else:
                    print("El número secreto es menor.")
                shift = 'player'
        
        # Preguntar si la jugadora quiere jugar de nuevo
        play_again = input("¿Quieres jugar de nuevo? (sí/no): ").lower()
        if play_again != 'sí':
            print("¡Gracias por jugar!")
            break

# Ejecutar el juego
guess_the_number()
