import unittest
from Dessert import Candy, Cookie, IceCream, Sundae

class TestDesserts(unittest.TestCase):

    def test_candy(self):
        candy = Candy("Candy Corn", 2, 1.5)
        self.assertAlmostEqual(candy.calculate_cost(), 3.0)
        self.assertAlmostEqual(candy.calculate_tax(), 0.22)

    def test_cookie(self):
        cookie = Cookie("Chocolate Chip", 24, 4.5)
        self.assertAlmostEqual(cookie.calculate_cost(), 9.0)
        self.assertAlmostEqual(cookie.calculate_tax(), 0.65)

    def test_ice_cream(self):
        ice_cream = IceCream("Vanilla", 3, 2.0)
        self.assertAlmostEqual(ice_cream.calculate_cost(), 6.0)
        self.assertAlmostEqual(ice_cream.calculate_tax(), 0.44)

    def test_sundae(self):
        sundae = Sundae("Strawberry", 2, 2.0, "Sprinkles", 1.5)
        self.assertAlmostEqual(sundae.calculate_cost(), 5.5)
        self.assertAlmostEqual(sundae.calculate_tax(), 0.4)

