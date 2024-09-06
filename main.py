
from src.game import play_game

def main():
   
    while True:
        play_game()
        play_again = input("¿Quieres jugar de nuevo? (sí/no): ").lower()
        if play_again != 'sí':
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    main()
