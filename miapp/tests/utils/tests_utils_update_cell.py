from django.test import TestCase
from miapp.models import Tablero
from miapp.utils import update_cell, EMPTY_CELL

class TestUpdateCell(TestCase):

    def setUp(self):
        self.tablero_db = Tablero()

    # Tests that update_cell successfully updates cell with valid input
    def test_update_cell_valid_input(self):
        self.tablero_db.a1 = EMPTY_CELL
        result = update_cell(self.tablero_db, 'cell_1_1', 'X', False)
        self.assertTrue(result)
        self.assertEqual(self.tablero_db.a1, 'X')
    
    # Tests that update_cell successfully updates cell with win is set to True
    def test_update_cell_false_fin(self):
        self.tablero_db.a1 = EMPTY_CELL
        result = update_cell(self.tablero_db, 'cell_1_1', 'X', True)
        self.assertTrue(result)
        self.assertEqual(self.tablero_db.a1, 'X') 

    # Tests that update_cell returns False when cell is already occupied
    def test_update_cell_cell_occupied(self):
        self.tablero_db.a1 = 'X'
        result = update_cell(self.tablero_db, 'cell_1_1', 'O', False)
        self.assertFalse(result)
        self.assertEqual(self.tablero_db.a1, 'X')

    # Tests that update_cell returns False when cell_name is not in switch_cases
    def test_update_cell_invalid_cell_name(self):
        result = update_cell(self.tablero_db, 'cell_4_4', 'X', False)
        self.assertFalse(result)

    # Tests that update_cell returns False when tablero_db is None
    def test_update_cell_tablero_db_none(self):
        result = update_cell(None, 'cell_1_1', 'X', False)
        self.assertFalse(result)

    # Tests that update_cell returns False when turn is not a string
    def test_update_cell_invalid_turn(self):
        result = update_cell(self.tablero_db, 'cell_1_1', 1, False)
        self.assertFalse(result)

    # Tests that update_cell returns False when win is not a boolean
    def test_update_cell_invalid_fin(self):
        result = update_cell(self.tablero_db, 'cell_1_1', 'X', 1)
        self.assertFalse(result)
    