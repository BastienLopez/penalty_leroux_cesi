import unittest
from pasta_utils import *

class TestPastaUtils(unittest.TestCase):

    def setUp(self):
        self.tree = {
            "name": "Pasta",
            "children": [
                {"name": "Spaghetti"},
                {"name": "Macaroni"},
                {
                    "name": "Autres pâtes",
                    "children": [
                        {"name": "Gnocchi"},
                        {"name": "Ravioli"},
                    ]
                }
            ]
        }

    def test_find_in_tree(self):
        result = find_in_tree(self.tree, "Gnocchi")
        self.assertEqual(result["name"], "Gnocchi")

    def test_upper_case_and_surround_with_emoji(self):
        result = upper_case_and_surround_with_emoji("Spaghetti")
        self.assertEqual(result, "SPAGHETTI DE LA MAMA")

    def test_get_all_values(self):
        values = get_all_values(self.tree)
        self.assertIn("Spaghetti", values)
        self.assertIn("Ravioli", values)

    def test_find_node_and_path(self):
        path = find_node_and_path([self.tree], "Gnocchi")
        self.assertEqual(path, ["Pasta", "Autres pâtes", "Gnocchi"])

    def test_count_nodes(self):
        count = count_nodes(self.tree)
        self.assertEqual(count, 5)

if __name__ == "__main__":
    unittest.main()
