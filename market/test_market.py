import unittest
from market_utils import *

class TestMarketFunctions(unittest.TestCase):

    def setUp(self):
        self.catalog = [
            Fruit(1, "Pomme", 100, 1.22),
            Fruit(2, "Poire", 50, 2.30),
            Fruit(3, "Ananas", 30, 2.90),
        ]

    def test_add_fruit_to_catalog(self):
        fraise = Fruit(4, "Fraise", 30, 7.00)
        updated_catalog = add_fruit_to_catalog(self.catalog, fraise)
        self.assertIn(fraise, updated_catalog)

    def test_remove_fruit_from_catalog(self):
        updated_catalog = remove_fruit_from_catalog(self.catalog, 1)
        self.assertNotIn(self.catalog[0], updated_catalog)

    def test_calculate_stock_value(self):
        stock_value = calculate_stock_value(self.catalog)
        self.assertAlmostEqual(stock_value, 100 * 1.22 + 50 * 2.30 + 30 * 2.90)

    def test_sell_fruit(self):
        result = sell_fruit(self.catalog, 1, 10)
        self.assertEqual(result["quantity_sold"], 10)
        self.assertEqual(result["total_amount"], 10 * 1.22)

        result = sell_fruit(self.catalog, 1, 500)
        self.assertIn("error", result)

        result = sell_fruit(self.catalog, 999, 10)
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()
