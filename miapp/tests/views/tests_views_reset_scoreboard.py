from django.test import TestCase
from miapp.models import Marcador
from miapp.views import reset_scoreboard

class TestResetScoreboard(TestCase):

    # Tests that the function updates the 'playerO' and 'playerX' fields of the 'marcador' object to 0.
    def test_happy_path_reset_scoreboard(self):
        marcador = Marcador(playerO=5, playerX=3)
        reset_scoreboard(marcador)
        self.assertEqual(marcador.playerO, 0)
        self.assertEqual(marcador.playerX, 0)

    # Tests that the function does not throw an exception if the 'marcador' object is None.
    def test_edge_case_marcador_none(self):
        marcador = None
        reset_scoreboard(marcador)
        self.assertIsNone(marcador)

    # Tests that the function updates the 'playerO' and 'playerX' fields of the 'marcador' object to 0.
    def test_happy_path_reset_scoreboard_with_invalid_inputs(self):
        marcador = Marcador(playerO='sd', playerX=-23)
        reset_scoreboard(marcador)
        self.assertEqual(marcador.playerO, 0)
        self.assertEqual(marcador.playerX, 0)