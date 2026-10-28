import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class SortTests(unittest.TestCase):
    def test_sort_by_title(self):
        cart = Cart()
        self.assertTrue(hasattr(cart, 'sort_by_title'), 'sort_by_title missing')
        cart.sort_by_title()
        a, b = DigitalVideoDisc('Aladdin', cost=20), DigitalVideoDisc('Star Wars', cost=10)
        cart.items = [b, a]
        cart.sort_by_title()
        self.assertEqual(cart.items, [a, b])
        self.assertEqual(cart.total_cost(), 30)

    def test_sort_by_cost(self):
        cart = Cart()
        self.assertTrue(hasattr(cart, 'sort_by_cost'), 'sort_by_cost missing')
        cart.sort_by_cost()
        a, b, c = DigitalVideoDisc('A', cost=20), DigitalVideoDisc('B', cost=10), DigitalVideoDisc('C', cost=10)
        cart.items = [a, b, c]
        cart.sort_by_cost()
        self.assertEqual(cart.items, [b, c, a])
        self.assertEqual(cart.total_cost(), 40)
