import unittest
from utils import simulate_shootout

class TestPenaltyShootout(unittest.TestCase):

    def test_simulate_shootout(self):
        """
        Teste que :
        - L'historique contient au moins 5 tirs
        - Le vainqueur est soit "Équipe A", "Équipe B" ou "Égalité"
        """
        history, winner = simulate_shootout()
        self.assertGreaterEqual(len(history), 5)  # Vérifie qu'il y a au moins 5 tirs
        self.assertIn(winner, ["Équipe A", "Équipe B", "Égalité"])  # Vérifie le vainqueur

if __name__ == "__main__":
    unittest.main()
