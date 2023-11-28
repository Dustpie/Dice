import unittest
from src.Roll import Roll


class test_Roll(unittest.TestCase):
    roll = Roll()
    
    def test_roll_dice(self):
        self.assertIn(self.roll.roll_dice(),range(7) )