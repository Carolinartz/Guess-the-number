import random
#genera un unmero aleatorio con la fucnion randit o random 
def guess_the_number():
    secret_number=random.randint(0,100)
    print(secret_number)
    player = []
    computer= []
    shift= 'jugadora'
##incrementar un bucle para solicitar adivine el numero la jugadora 
    while True:
        if shift == 'jugadora':
           
##obtener el ingereso de la jugadora 
            assumption = int(input("Adivina el número entre 1 y 100: "))
            player.append(assumption)
##compara lo ingresado por la jugadora con el secreto 
            if assumption == secret_number:
##si a es correcto se termina el juego 
                print(f"¡Felicidades! Has adivinado el número {secret_number} en {len(player)} intentos.")

##si es falso dar pista de si es mayor o menor
                print("Intentos de la jugadora: ", player)
                break
            elif assumption < secret_number:
                print("El número secreto es mayor.")
            else:
                print("El número secreto es menor.")
            turno = 'computer'
      
#el ordenador hace una suposicion aleatoria 
        else:
            assumption=random.randint(0,100)
            computer.append(assumption)
            print(f"El ordenador adivina: {assumption}")
            if assumption == secret_number:
                print(f"El ordenador ha adivinado el número {secret_number} en {len(computer)} intentos.")
                break
            elif assumption < secret_number:
                print("El número secreto es mayor.")
            else:
                print("El número secreto es menor.")
            turno = 'jugadora'

## test con unites