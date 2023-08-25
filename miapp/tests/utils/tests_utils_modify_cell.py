from miapp.models import Tablero
from miapp.constants import EMPTY_CELL
from miapp.utils import modify_cell
from django.test import TestCase

class TestModifyCell(TestCase):
    
    # Tests that modifying an empty cell with a non-empty value and fin=False modifies the cell and returns True
    def test_modify_empty_cell_with_non_empty_value_and_fin_false(self):
        tablero_db = Tablero()
        tablero_db.a1 = EMPTY_CELL
        attribute = 'a1'
        value = 'X'
        win = False

        result = modify_cell(tablero_db, attribute, value, win)

        self.assertTrue(result)
        self.assertEqual(tablero_db.a1, value)

    # Tests that modifying an empty cell with an empty value and fin=False modifies the cell and returns True
    def test_modify_empty_cell_with_empty_value_and_fin_false(self):
        tablero_db = Tablero()
        tablero_db.a1 = EMPTY_CELL
        attribute = 'a1'
        value = EMPTY_CELL
        win = False

        result = modify_cell(tablero_db, attribute, value, win)

        self.assertTrue(result)
        self.assertEqual(tablero_db.a1, value)
    