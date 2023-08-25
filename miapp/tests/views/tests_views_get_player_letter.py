from miapp.constants import JUGADOR1_LETTER, JUGADOR2_LETTER
from django.test import TestCase
from miapp.views import get_player_letter
class TestGetPlayerLetter(TestCase):

    # Tests that get_player_letter returns JUGADOR1_LETTER when turno is True
    def test_happy_path_turno_true_JUGADOR1(self):
        turno = True
        result = get_player_letter(turno)
        self.assertEqual(result, JUGADOR1_LETTER)   

    # Tests that get_player_letter returns JUGADOR2_LETTER when turno is False
    def test_happy_path_turno_true_JUGADOR2(self):
        turno = False
        result = get_player_letter(turno)
        self.assertEqual(result, JUGADOR2_LETTER)

    # Tests that get_player_letter returns JUGADOR1_LETTER when turno is None
    def test_edge_case_turno_none(self):
        turno = None
        with self.assertRaises(ValueError):
            get_player_letter(turno)

    # Tests that get_player_letter returns JUGADOR1_LETTER when turno is 0
    def test_edge_case_turno_zero(self):
        turno = 0
        with self.assertRaises(ValueError):
            get_player_letter(turno)

    # Tests that get_player_letter returns JUGADOR1_LETTER when turno is a string
    def test_other_case_turno_falsey(self):
        turno = ''
        with self.assertRaises(ValueError):
            get_player_letter(turno)