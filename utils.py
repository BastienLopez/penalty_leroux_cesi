import random
from typing import List, Tuple, Dict

def simulate_shootout() -> Tuple[List[Dict[str, int]], str]:
    """
    Simule une séance de tirs au but et retourne :
    - L'historique des scores
    - Le vainqueur
    """
    # Initialise a 0
    score_a, score_b = 0, 0
    
    # stock historique
    history = []
    
    # numéro de tours
    turn = 1

    # simule les tir
    while True:
        # Tir équipe A : random 0 & 1 = but
        team_a_result = random.choice([0, 1])
        score_a += team_a_result

        # Tir équipe A : random 0 & 1 = but
        team_b_result = random.choice([0, 1])
        score_b += team_b_result

        # up historique selon tirs
        history.append({
            "turn": turn,        # Numéro du tir
            "score_a": score_a,  # Score équipe A
            "score_b": score_b,  # Score équipe B
            "team_a": team_a_result,  # Résultat équipe A
            "team_b": team_b_result   # Résultat équipe B
        })

        # apres 5tirs l"equipe qui a le plus de point win
        if turn >= 5 and abs(score_a - score_b) >= 1 and score_a != score_b:
            winner = "Équipe A" if score_a > score_b else "Équipe B"
            return history, winner

        # egalité
        elif turn >= 5 and turn % 2 == 0 and score_a == score_b:
            winner = "Égalité"
            return history, winner

        # tour suivant
        turn += 1

# aff historique de tirs et winner
def display_history(history: List[Dict[str, int]], winner: str) -> None:
    """
    Affiche :
    - L'historique des tirs au but
    - Le résultat final
    """
    print("\nHistorique de la du match :")
    
    # affiche les scores apres chaque tir
    for entry in history:
        print(
            f"Tir {entry['turn']}: Score: {entry['score_a']}/{entry['score_b']} "
            f"(Équipe A : +{entry['team_a']} | Équipe B : +{entry['team_b']})"
        )
    
    # Affiche le résultat final
    print(f"\nRésultat final : {winner}")
