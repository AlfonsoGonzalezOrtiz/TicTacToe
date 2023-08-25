from miapp.constants import JUGADOR1_LETTER, JUGADOR2_LETTER
from django.test import TestCase
from miapp.views import get_player_letter
class TestGetPlayerLetter(TestCase):

    # Tests that get_player_letter returns JUGADOR1_LETTER when turn is True
    def test_happy_path_turn_true_JUGADOR1(self):
        turn = True
        result = get_player_letter(turn)
        self.assertEqual(result, JUGADOR1_LETTER)   

    # Tests that get_player_letter returns JUGADOR2_LETTER when turn is False
    def test_happy_path_turn_true_JUGADOR2(self):
        turn = False
        result = get_player_letter(turn)
        self.assertEqual(result, JUGADOR2_LETTER)

    # Tests that get_player_letter returns JUGADOR1_LETTER when turn is None
    def test_edge_case_turn_none(self):
        turn = None
        with self.assertRaises(ValueError):
            get_player_letter(turn)

    # Tests that get_player_letter returns JUGADOR1_LETTER when turn is 0
    def test_edge_case_turn_zero(self):
        turn = 0
        with self.assertRaises(ValueError):
            get_player_letter(turn)

    # Tests that get_player_letter returns JUGADOR1_LETTER when turn is a string
    def test_other_case_turn_falsey(self):
        turn = ''
        with self.assertRaises(ValueError):
            get_player_letter(turn)