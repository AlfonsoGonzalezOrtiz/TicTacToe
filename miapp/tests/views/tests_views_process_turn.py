from miapp.models import Tablero
from django.test import TestCase
from miapp.views import process_turn
from miapp.utils import update_cell
from miapp.constants import EMPTY_CELL,JUGADOR1_LETTER,JUGADOR2_LETTER
class TestProcessTurn(TestCase):

    def test_valid_input_updates_tablero(self):
        # Create a Tablero
        tablero = Tablero(  a1=EMPTY_CELL,a2=EMPTY_CELL,a3=EMPTY_CELL,
                            b1=EMPTY_CELL,b2=EMPTY_CELL,b3=EMPTY_CELL,
                            c1=EMPTY_CELL,c2=EMPTY_CELL,c3=EMPTY_CELL)
        # Create a cell_name
        cell_name = 'cell_1_1'
        # Create a player_letter
        player_letter = JUGADOR1_LETTER

        # Call the process_turn function
        win, updated = process_turn(tablero, cell_name, player_letter)

        # Assert that the return values are correct
        self.assertTrue(updated)
        self.assertFalse(win)
        

    def test_cannot_update_a_non_empty_cell(self):
        # Create a Tablero
        tablero = Tablero(  a1=JUGADOR1_LETTER,a2=EMPTY_CELL,a3=EMPTY_CELL,
                            b1=EMPTY_CELL,b2=EMPTY_CELL,b3=EMPTY_CELL,
                            c1=EMPTY_CELL,c2=EMPTY_CELL,c3=EMPTY_CELL)
        # Create a cell_name
        cell_name = 'cell_1_1'
        # Create a player_letter
        player_letter = JUGADOR2_LETTER

        # Call the process_turn function
        win, updated = process_turn(tablero, cell_name, player_letter)

        # Assert that the return values are incorrect
        self.assertFalse(updated)
        self.assertFalse(win)
        

    def test_update_a_empty_cell_and_finnish_with_a_winning_game(self):
        # Create a Tablero
        tablero = Tablero(  a1=JUGADOR1_LETTER,a2=JUGADOR1_LETTER,a3=EMPTY_CELL,
                            b1=JUGADOR2_LETTER,b2=JUGADOR2_LETTER,b3=EMPTY_CELL,
                            c1=EMPTY_CELL,c2=EMPTY_CELL,c3=EMPTY_CELL)
        # Create a cell_name
        cell_name = 'cell_1_3'
        # Create a player_letter
        player_letter = JUGADOR1_LETTER

        # Call the process_turn function
        win, updated = process_turn(tablero, cell_name, player_letter)

        # Assert that the return values are correct
        self.assertTrue(updated)
        self.assertTrue(win)

    def test_not_update_a_empty_cell_and_finnish_with_a_winning_game(self):
        # Create a Tablero
        tablero = Tablero(  a1=JUGADOR1_LETTER,a2=JUGADOR1_LETTER,a3=JUGADOR2_LETTER,
                            b1=JUGADOR2_LETTER,b2=JUGADOR2_LETTER,b3=JUGADOR1_LETTER,
                            c1=JUGADOR1_LETTER,c2=JUGADOR2_LETTER,c3=JUGADOR1_LETTER)
        # Create a cell_name
        cell_name = 'cell_1_3'
        # Create a player_letter
        player_letter = JUGADOR1_LETTER

        # Call the process_turn function
        win, updated = process_turn(tablero, cell_name, player_letter)

        # Assert that the return values are correct
        self.assertFalse(updated)
        self.assertFalse(win)
