from django.test import TestCase,Client
from miapp.models import Marcador,Tablero,Turno,Game
from miapp.views import turn
from miapp.constants import EMPTY_CELL
from miapp.constants import JUGADOR1_LETTER,TOKEN_KEY,TOKEN_VALUE
from unittest.mock import Mock
import pdb

class TestTurn(TestCase):

    # Tests that the function handles a valid POST request correctly
    def test_valid_post_request(self):
        tablero = Tablero(a1=EMPTY_CELL,a2=EMPTY_CELL,a3=EMPTY_CELL,b1=EMPTY_CELL,b2=EMPTY_CELL,b3=EMPTY_CELL,c1=EMPTY_CELL,c2=EMPTY_CELL,c3=EMPTY_CELL)
        marcador = Marcador(playerX=0, playerO=0, num_games=0)
        turno = Turno(turno=True)

        tablero.save()
        marcador.save()
        turno.save()

        # A game was created before reset
        game = Game.objects.create(tablero=tablero,marcador=marcador,turno=turno)
        game.save()

        data = {TOKEN_KEY: TOKEN_VALUE, 'cell_1_1': JUGADOR1_LETTER}

        client = Client()  # Create a client instance to simulate requests
        response = client.post('/turn/',data)

        latest_game = Game.objects.latest('id')

        # Assert that the create and save methods were called with the correct arguments
        self.assertEqual(latest_game.tablero.a1,JUGADOR1_LETTER)

        # Assert that redirects to '/tictactoe'
        self.assertEqual(response.url,'/tictactoe')
        self.assertEqual(response.status_code,302) # Redirect code

    # Tests that the function handles the case when there is no latest game in the database
    def test_no_latest_game(self):

        data = {TOKEN_KEY: TOKEN_VALUE, 'cell_1_1': JUGADOR1_LETTER}
        client = Client()  # Create a client instance to simulate requests
        with self.assertRaises(ValueError):
            client.post('/turn/',data)

    # Tests that the function handles the case when an invalid cell name is found in the request
    def test_invalid_cell_name(self):
        tablero = Tablero(a1=EMPTY_CELL,a2=EMPTY_CELL,a3=EMPTY_CELL,b1=EMPTY_CELL,b2=EMPTY_CELL,b3=EMPTY_CELL,c1=EMPTY_CELL,c2=EMPTY_CELL,c3=EMPTY_CELL)
        marcador = Marcador(playerX=0, playerO=0, num_games=0)
        turno = Turno(turno=True)

        tablero.save()
        marcador.save()
        turno.save()

        # A game was created before reset
        game = Game.objects.create(tablero=tablero,marcador=marcador,turno=turno)
        game.save()

        data = {TOKEN_KEY: TOKEN_VALUE, 'invalid_cell': 'invalid_cell'}

        client = Client()  # Create a client instance to simulate requests
        response = client.post('/turn/',data)

        latest_game = Game.objects.latest('id')

        # Assert that the create and save methods were called with the correct arguments
        self.assertEqual(latest_game.tablero,tablero)

        # Assert that redirects to '/tictactoe'
        self.assertEqual(response.url,'/tictactoe')
        self.assertEqual(response.status_code,302) # Redirect code
