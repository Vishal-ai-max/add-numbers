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

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_negative_number(self):
        with self.assertRaises(ValueError) as context:
            add("-9,6")
        self.assertEqual(str(context.exception), f"negative numbers not allowed: -9")

    def test_negative_number_1(self):
        with self.assertRaises(ValueError) as context:
            add("-9,6\n-8")
        self.assertEqual(str(context.exception), f"negative numbers not allowed: -9, -8")

    def test_negative_number_2(self):
        with self.assertRaises(ValueError) as context:
            add("///\n-9/6\n-8")
        self.assertEqual(str(context.exception), f"negative numbers not allowed: -9, -8")

    def test_custom_delimiter_multidigit(self):
        self.assertEqual(add("//;\n1;2;15"), 18)
    

if __name__ == '__main__':
    unittest.main()