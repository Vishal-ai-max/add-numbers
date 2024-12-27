import unittest
from calculator import add

class CalculatorTest(unittest.TestCase):
    
    def test_nothing(self):
        self.assertEqual(add(""), 0)
    
    def test_one_number(self):
        self.assertEqual(add("5"), 5)

    def test_two_numbers(self):
        self.assertEqual(add("5,9"), 14)

    def test_newline_instead_of_comma(self):
        self.assertEqual(add("1\n2,3"), 6)

if __name__ == '__main__':
    unittest.main()