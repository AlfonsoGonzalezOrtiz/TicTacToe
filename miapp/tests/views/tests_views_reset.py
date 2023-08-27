from django.test import TestCase,Client
from miapp.models import Marcador,Tablero,Turno,Game
from miapp.views import reset
from unittest.mock import Mock
from miapp.constants import EMPTY_CELL

class TestReset(TestCase):

    # Tests that the 'reset' function creates a new game with a new tablero, marcador, and turno
    def test_reset_creates_new_game(self):
        tablero = Tablero(a1=EMPTY_CELL,a2=EMPTY_CELL,a3=EMPTY_CELL,b1=EMPTY_CELL,b2=EMPTY_CELL,b3=EMPTY_CELL,c1=EMPTY_CELL,c2=EMPTY_CELL,c3=EMPTY_CELL)
        marcador = Marcador(playerX=0, playerO=0, num_games=0)
        turno = Turno(turno=True)

        tablero.save()
        marcador.save()
        turno.save()

        # A game was created before reset
        game = Game.objects.create(tablero=tablero,marcador=marcador,turno=turno)
        game.save()

        client = Client()  # Create a client instance to simulate requests
        response = client.post('/reset/')

        latest_game = Game.objects.latest('id')

        # Assert that the create and save methods were called with the correct arguments
        # Check only str to not check all arguments
        self.assertEqual(latest_game.__str__(),Game(tablero=tablero,marcador=marcador,turno=turno).__str__())

        # Assert that redirects to '/tictactoe'
        self.assertEqual(response.url,'/tictactoe')
        self.assertEqual(response.status_code,302) # Redirect code

        