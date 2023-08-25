from django.test import TestCase
from miapp.utils import string_to_matrix

class TestStringToMatrix(TestCase):

    # Tests that input string with length 9 returns a 3x3 matrix
    def test_happy_path_length_9(self):
        input_string = "123456789"
        expected_matrix = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(string_to_matrix(input_string), expected_matrix)

    # Tests that input string with valid characters returns a 3x3 matrix
    def test_happy_path_valid_characters(self):
        input_string = "abc123xyz"
        expected_matrix = [['a', 'b', 'c'], ['1', '2', '3'], ['x', 'y', 'z']]
        self.assertEqual(string_to_matrix(input_string), expected_matrix)

    # Tests that input string with length less than 9 raises a ValueError
    def test_edge_case_length_less_than_9(self):
        input_string = "12345678"
        with self.assertRaises(ValueError):
            string_to_matrix(input_string)

    # Tests that input string with length greater than 9 raises a ValueError
    def test_edge_case_length_greater_than_9(self):
        input_string = "1234567890"
        with self.assertRaises(ValueError):
            string_to_matrix(input_string)

    # Tests that input string with all same characters returns a 3x3 matrix with all elements the same
    def test_all_same_characters(self):
        input_string = "111111111"
        expected_matrix = [['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']]
        self.assertEqual(string_to_matrix(input_string), expected_matrix)