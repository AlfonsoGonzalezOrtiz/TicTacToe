from django.test import TestCase
from miapp.utils import check_line
class TestCheckLine(TestCase):

    # Tests that check_line returns True when all elements in the line are X's
    def test_check_line_all_X(self):
        line = ['X', 'X', 'X']
        result = check_line(line)
        self.assertTrue(result)

    # Tests that check_line returns True when all elements in the line are O's
    def test_check_line_all_O(self):
        line = ['O', 'O', 'O']
        result = check_line(line)
        self.assertTrue(result)

    # Tests that check_line returns False when the line contains a mix of X's and O's
    def test_check_line_mix_X_O(self):
        line = ['X', 'O', 'X']
        result = check_line(line)
        self.assertFalse(result)

    # Tests that check_line returns False when the line contains invalid inputs
    def test_check_line_invalid_input(self):
        line = ['{', 'F', '&']
        result = check_line(line)
        self.assertFalse(result)