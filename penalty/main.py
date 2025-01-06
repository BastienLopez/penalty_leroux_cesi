import random
from utils import simulate_shootout, display_history

def main():
    print("Début des tirs au but")
    
    # Simule les tirs et récupère historique & winner
    history, winner = simulate_shootout()
    
    # Affiche historique & résultat 
    display_history(history, winner)

if __name__ == "__main__":
    main()
