import unittest
from calculator import add

class CalculatorTest(unittest.TestCase):
    
    def test_nothing(self):
        self.assertEqual(add(""), 0)

if __name__ == '__main__':
    unittest.main()