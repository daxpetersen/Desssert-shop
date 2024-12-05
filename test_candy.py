
import unittest
from dessert import Candy

class TestCandy(unittest.TestCase):

    def test_calculate_cost(self):
        candy = Candy("Candy Corn", 1.5, 0.50)
        self.assertEqual(candy.calculate_cost(), 0.75)
