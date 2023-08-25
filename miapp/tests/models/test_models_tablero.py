from django.test import TestCase
from miapp.models import Tablero
from miapp.constants import EMPTY_CELL

class TestTablero(TestCase):

    # Tests that a new instance of Tablero has all fields as empty strings
    def test_empty_fields(self):
        tablero = Tablero()
        self.assertEqual(tablero.a1, EMPTY_CELL)
        self.assertEqual(tablero.a2, EMPTY_CELL)
        self.assertEqual(tablero.a3, EMPTY_CELL)
        self.assertEqual(tablero.b1, EMPTY_CELL)
        self.assertEqual(tablero.b2, EMPTY_CELL)
        self.assertEqual(tablero.b3, EMPTY_CELL)
        self.assertEqual(tablero.c1, EMPTY_CELL)
        self.assertEqual(tablero.c2, EMPTY_CELL)
        self.assertEqual(tablero.c3, EMPTY_CELL)

    # Tests that the __str__ method returns the expected string when all fields have values
    def test_str_method_all_fields(self):
        tablero = Tablero(a1="X", a2="O", a3="X", b1="O", b2="X", b3="O", c1="X", c2="O", c3="X")
        expected_string = "XOXOXOXOX"
        self.assertEqual(str(tablero), expected_string)

    # Tests that the __str__ method returns the expected string when some fields have values and the remaining fields are empty strings
    def test_str_method_some_fields(self):
        tablero = Tablero(a1="X", a2="O", b2="X", c3="O")
        expected_string = "XO  X   O"
        self.assertEqual(str(tablero), expected_string)

    # Tests that a validation error is raised when setting a value for a field that exceeds the maximum length
    def test_max_length_validation(self):
        with self.assertRaises(Exception):
            Tablero(a1="XX")

    # Tests that a validation error is raised when setting a value for a field that is not a single character
    def test_single_character_validation(self):
        with self.assertRaises(Exception):
            Tablero(a1="XX")

    # Tests that all fields have the expected values after saving and retrieving an instance from the database
    def test_save_and_retrieve_instance(self):
        tablero = Tablero(a1="X", a2="O", a3="X", b1="O", b2="X", b3="O", c1="X", c2="O", c3="X")
        tablero.save()
        retrieved_tablero = Tablero.objects.get(id=tablero.id)
        self.assertEqual(retrieved_tablero.a1, "X")
        self.assertEqual(retrieved_tablero.a2, "O")
        self.assertEqual(retrieved_tablero.a3, "X")
        self.assertEqual(retrieved_tablero.b1, "O")
        self.assertEqual(retrieved_tablero.b2, "X")
        self.assertEqual(retrieved_tablero.b3, "O")
        self.assertEqual(retrieved_tablero.c1, "X")
        self.assertEqual(retrieved_tablero.c2, "O")
        self.assertEqual(retrieved_tablero.c3, "X")
