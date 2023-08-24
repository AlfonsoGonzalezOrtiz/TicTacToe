from django.test import TestCase
from miapp.models import Turno

class TestTurno(TestCase):

    # Tests that creating a Turno object with turno=True returns 'O'
    def test_turno_true(self):
        turno = Turno(turno=True)
        self.assertEqual(str(turno), 'O')

    # Tests that creating a Turno object with turno=False returns 'X'
    def test_turno_false(self):
        turno = Turno(turno=False)
        self.assertEqual(str(turno), 'X')

    # Tests that creating a Turno object with turno=None returns ''
    def test_turno_none(self):
        turno = Turno(turno=None)
        self.assertEqual(str(turno), ' ')

    # Tests that creating a Turno object with turno='True' returns 'O'
    def test_turno_true_string(self):
        turno = Turno(turno='True')
        self.assertEqual(str(turno), 'O')

    # Tests that creating a Turno object with turno=True sets turno to True
    def test_turno_true_value(self):
        turno = Turno(turno=True)
        self.assertTrue(turno.turno)

    # Tests that creating a Turno object with turno=False sets turno to False
    def test_turno_false_value(self):
        turno = Turno(turno=False)
        self.assertFalse(turno.turno)