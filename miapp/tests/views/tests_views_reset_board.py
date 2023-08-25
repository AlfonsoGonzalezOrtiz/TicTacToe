from django.test import TestCase
from miapp.models import Tablero
from miapp.views import reset_board
from miapp.constants import EMPTY_CELL,JUGADOR1_LETTER,JUGADOR2_LETTER

class TestResetBoard(TestCase):

    # Tests that the function resets the board when 'end' is True
    def test_reset_board_with_end_true(self):
        tablero = Tablero(  a1=JUGADOR1_LETTER,a2=JUGADOR1_LETTER,a3=JUGADOR2_LETTER,
                            b1=JUGADOR2_LETTER,b2=JUGADOR2_LETTER,b3=JUGADOR1_LETTER,
                            c1=JUGADOR1_LETTER,c2=JUGADOR2_LETTER,c3=JUGADOR1_LETTER)
        
        reset_board(True,tablero)
        self.assertEqual(tablero.a1, EMPTY_CELL)
        self.assertEqual(tablero.a2, EMPTY_CELL)
        self.assertEqual(tablero.a3, EMPTY_CELL)
        self.assertEqual(tablero.b1, EMPTY_CELL)
        self.assertEqual(tablero.b2, EMPTY_CELL)
        self.assertEqual(tablero.b3, EMPTY_CELL)
        self.assertEqual(tablero.c1, EMPTY_CELL)
        self.assertEqual(tablero.c2, EMPTY_CELL)
        self.assertEqual(tablero.c3, EMPTY_CELL)

    # Tests that the function does not reset the board when 'end' is False
    def test_reset_board_with_end_false(self):
        tablero = Tablero(  a1=JUGADOR1_LETTER,a2=JUGADOR1_LETTER,a3=JUGADOR2_LETTER,
                            b1=JUGADOR2_LETTER,b2=JUGADOR2_LETTER,b3=JUGADOR1_LETTER,
                            c1=JUGADOR1_LETTER,c2=JUGADOR2_LETTER,c3=JUGADOR1_LETTER)
        reset_board(False,tablero)
        self.assertNotEqual(tablero.a1, EMPTY_CELL)
        self.assertNotEqual(tablero.a2, EMPTY_CELL)
        self.assertNotEqual(tablero.a3, EMPTY_CELL)
        self.assertNotEqual(tablero.b1, EMPTY_CELL)
        self.assertNotEqual(tablero.b2, EMPTY_CELL)
        self.assertNotEqual(tablero.b3, EMPTY_CELL)
        self.assertNotEqual(tablero.c1, EMPTY_CELL)
        self.assertNotEqual(tablero.c2, EMPTY_CELL)
        self.assertNotEqual(tablero.c3, EMPTY_CELL)
    
    def test_reset_board_with_invalid_tablero(self):
        tablero = None
        with self.assertRaises(Exception):
            reset_board(False,tablero)

    def test_reset_board_with_invalid_end(self):
        tablero = Tablero(  a1=JUGADOR1_LETTER,a2=JUGADOR1_LETTER,a3=JUGADOR2_LETTER,
                            b1=JUGADOR2_LETTER,b2=JUGADOR2_LETTER,b3=JUGADOR1_LETTER,
                            c1=JUGADOR1_LETTER,c2=JUGADOR2_LETTER,c3=JUGADOR1_LETTER)
        with self.assertRaises(Exception):
            reset_board(None,tablero)
