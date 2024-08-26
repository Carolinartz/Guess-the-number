import random
#genera un unmero aleatorio con la fucnion randit o random 
def guess_the_number():
    secret_number=random.randint(0,100)
    print(secret_number)
    player = []
    computer= []
    shift= 'jugadora'
##incrementar un bucle para solicitar adivine el numero la jugadora 
##obtener el ingereso de la jugadora 
##compara lo ingresado por la jugadora con el secreto 
##si a es correcto se termina el juego 
##si es falso dar pista de si es mayor o menos 
##logica para el turno de la jugadora 
#el ordenador hace una suposicion aleatoria 
## test con unites