import unittest
from dessert import Cookie

class TestCookie(unittest.TestCase):

    def test_calculate_cost(self):
        cookie = Cookie("Chocolate Chip", 12, 2.50)
        self.assertEqual(cookie.calculate_cost(), 2.50)
