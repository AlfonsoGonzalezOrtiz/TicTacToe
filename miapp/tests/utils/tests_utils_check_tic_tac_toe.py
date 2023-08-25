from django.test import TestCase
from miapp.utils import check_tic_tac_toe
from miapp.constants import EMPTY_CELL

class TestCheckTicTacToe(TestCase):

    # Tests that the function correctly identifies a board with no winner
    def test_no_winner(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        result = check_tic_tac_toe(board)
        self.assertEqual(result, False)

    # Tests that the function correctly identifies a board with a horizontal winner
    def test_horizontal_winner(self):
        board = [
            ['X', 'X', 'X'],
            ['O', 'O', EMPTY_CELL],
            ['O', EMPTY_CELL, EMPTY_CELL]
        ]
        result = check_tic_tac_toe(board)
        self.assertEqual(result, True)

    # Tests that the function correctly identifies a board with a vertical winner
    def test_vertical_winner(self):
        board = [
            ['X', 'O', EMPTY_CELL],
            ['X', 'O', EMPTY_CELL],
            ['X', EMPTY_CELL, EMPTY_CELL]
        ]
        result = check_tic_tac_toe(board)
        self.assertEqual(result, True)

    # Tests that the function correctly identifies a board with a diagonal winner
    def test_diagonal1_winner(self):
        board = [
            ['X', 'O', EMPTY_CELL],
            ['O', 'X', EMPTY_CELL],
            [EMPTY_CELL, EMPTY_CELL, 'X']
        ]
        result = check_tic_tac_toe(board)
        self.assertEqual(result, True)

    # Tests that the function correctly identifies a board with a diagonal2 winner
    def test_diagonal2_winner(self):
        board = [
            [EMPTY_CELL, 'O', 'X'],
            ['O', 'X', EMPTY_CELL],
            ['X', EMPTY_CELL, 'X']
        ]
        result = check_tic_tac_toe(board)
        self.assertEqual(result, True)

    # Tests that the function correctly identifies a board that is completely filled but has no winner
    def test_board_filled_no_winner(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        result = check_tic_tac_toe(board)
        self.assertEqual(result, False)
