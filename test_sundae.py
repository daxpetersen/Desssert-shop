import unittest
from dessert import Sundae

class TestSundae(unittest.TestCase):

    def test_calculate_cost(self):
        sundae = Sundae("Chocolate", 2, 2.00, "Hot Fudge", 1.00)
        self.assertEqual(sundae.calculate_cost(), 5.00)
