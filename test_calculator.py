import unittest
from calculator import add

class CalculatorTest(unittest.TestCase):
    
    def test_nothing(self):
        self.assertEqual(add(""), 0)
    
    def test_one_number(self):
        self.assertEqual(add("5"), 5)

    def test_two_numbers(self):
        self.assertEqual(add("5,9"), 14)

if __name__ == '__main__':
    unittest.main()