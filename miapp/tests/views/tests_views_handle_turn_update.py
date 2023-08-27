from django.test import TestCase
from miapp.views import handle_turn_update
from miapp.models import Turno
class TestHandleTurnUpdate(TestCase):

    # Tests that when 'updated' is True and neither 'win' nor 'bloqueo' are True, the 'turno' object is updated to the opposite boolean value and saved.
    def test_updated_true_no_win_no_bloqueo(self):
        turno = Turno(turno=True)
        updated = True
        win = False
        bloqueo = False

        handle_turn_update(turno, updated, win, bloqueo)

        self.assertEqual(turno.turno, False)

    # Tests that when 'updated' is False, the 'turno' object is not updated and saved.
    def test_updated_false(self):
        turno = Turno(turno=True)
        updated = False
        win = False
        bloqueo = False

        handle_turn_update(turno, updated, win, bloqueo)

        self.assertEqual(turno.turno, True)

    # Tests that when 'win' is True, the 'turno' object is not updated and saved.
    def test_win_true(self):
        turno = Turno(turno=True)
        updated = True
        win = True
        bloqueo = False

        handle_turn_update(turno, updated, win, bloqueo)

        self.assertEqual(turno.turno, True)

    # Tests that when 'bloqueo' is True, the 'turno' object is not updated and saved.
    def test_bloqueo_true(self):
        turno = Turno(turno=True)
        updated = True
        win = False
        bloqueo = True

        handle_turn_update(turno.turno, updated, win, bloqueo)

        self.assertEqual(turno.turno, True)

    # Tests that when 'updated' is True and 'win' is True, the 'turno' object is not updated and saved.
    def test_updated_true_win_true(self):
        turno = Turno(turno=True)
        updated = True
        win = True
        bloqueo = False

        handle_turn_update(turno, updated, win, bloqueo)

        self.assertEqual(turno.turno, True)