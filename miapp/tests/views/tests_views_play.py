from django.test import TestCase,Client
from miapp.views import play
from miapp.constants import EMPTY_CELL
from unittest.mock import Mock,patch
from miapp.models import Tablero,Marcador,Turno,Game

class TestPlay(TestCase):

    # Test that the view returns a 200 status code when no valid Game,Marcador, Tablero, and Turno objects exist in the database.
    def test_render_template_with_no_objects(self):
        # Create a test client
        client = Client()

        # Call the play view using the client
        response = client.get('/tictactoe/')

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the template 'miplantilla.html' is rendered
        self.assertTemplateUsed(response, 'miplantilla.html')

        # Assert that the context contains the expected values
        expected_context = {
            'tablero': [[EMPTY_CELL, EMPTY_CELL, EMPTY_CELL], [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL], [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]],
            'playerX': 0,
            'playerO': 0,
            'turn': 'O',
            'num_games': 0
        }
        self.assertEqual(response.context['tablero'], expected_context['tablero'])
        self.assertEqual(response.context['playerX'], expected_context['playerX'])
        self.assertEqual(response.context['playerO'], expected_context['playerO'])
        self.assertEqual(response.context['turn'], expected_context['turn'])
        self.assertEqual(response.context['num_games'], expected_context['num_games'])

    # Test that the view returns a 200 status code when valid Game,Marcador, Tablero, and Turno objects exist in the database.
    def test_render_template_with_valid_objects(self):

        # Create valid Marcador, Tablero, and Turno objects
        marcador = Marcador.objects.create(playerX=1, playerO=2,num_games=3)
        tablero = Tablero.objects.create(a1='X', a2='O', a3='X', b1='O', b2='X', b3='O', c1='X', c2='O', c3='X')
        turno = Turno.objects.create(turno=True)
        game = Game.objects.create(marcador=marcador,tablero=tablero,turno=turno)

        # Create a test client
        client = Client()

        # Call the play view using the client
        response = client.get('/tictactoe/')

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the template 'miplantilla.html' is rendered
        self.assertTemplateUsed(response, 'miplantilla.html')

        # Assert that the context contains the expected values
        expected_context = {
            'tablero': [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']],
            'playerX': 1,
            'playerO': 2,
            'turn': 'O',
            'num_games': 3
        }
        self.assertEqual(response.context['tablero'], expected_context['tablero'])
        self.assertEqual(response.context['playerX'], expected_context['playerX'])
        self.assertEqual(response.context['playerO'], expected_context['playerO'])
        self.assertEqual(response.context['turn'], expected_context['turn'])
        self.assertEqual(response.context['num_games'], expected_context['num_games'])