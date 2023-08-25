from django.test import TestCase
from miapp.utils import lock_configuration
from miapp.constants import EMPTY_CELL

class TestLockConfiguration(TestCase):

    # Tests that the function correctly identifies a board with no winner
    def test_no_winner(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        result = lock_configuration(board)
        self.assertEqual(result, True)

    # Tests that the function correctly identifies a board with a winner
    def test_horizontal_winner(self):
        board = [
            ['X', 'X', 'X'],
            ['O', 'O', EMPTY_CELL],
            ['O', EMPTY_CELL, EMPTY_CELL]
        ]
        result = lock_configuration(board)
        self.assertEqual(result, False)