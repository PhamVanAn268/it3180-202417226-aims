import unittest
from aims.discount import total_cost_with_discount


class DiscountTests(unittest.TestCase):
    def test_discount_total(self):
        self.assertEqual(total_cost_with_discount(100, 20), 80)
        self.assertEqual(total_cost_with_discount(100, 0), 100)
        self.assertEqual(total_cost_with_discount(100, 100), 0)

    def test_invalid_percent(self):
        for percent in (-1, 150):
            with self.assertRaises(ValueError):
                total_cost_with_discount(100, percent)
