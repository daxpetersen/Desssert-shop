import unittest
from dessert import IceCream

class TestIceCream(unittest.TestCase):

    def test_calculate_cost(self):
        icecream = IceCream("Vanilla", 2, 1.50)
        self.assertEqual(icecream.calculate_cost(), 3.00)
