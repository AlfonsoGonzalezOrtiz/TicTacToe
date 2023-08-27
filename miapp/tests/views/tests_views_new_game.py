from django.test import TestCase,Client
from miapp.models import Marcador,Tablero,Turno,Game
from miapp.views import new_game
from unittest.mock import Mock
from miapp.constants import EMPTY_CELL

class TestNewGame(TestCase):

    # Tests that a new game is created with a new tablero, marcador, and turn when win is True
    def test_new_game_win_true(self):

        tablero = Tablero.objects.create(a1=EMPTY_CELL,a2=EMPTY_CELL,a3=EMPTY_CELL,b1=EMPTY_CELL,b2=EMPTY_CELL,b3=EMPTY_CELL,c1=EMPTY_CELL,c2=EMPTY_CELL,c3=EMPTY_CELL)
        marcador = Marcador.objects.create(playerX=1, playerO=2, num_games=3)
        turno = Turno.objects.create(turno=False)

        tablero.save()
        marcador.save()
        turno.save()
        
        # Set the win with True
        win = True

        # Call the new_game function
        response = new_game(win, tablero, marcador, turno)

        # We get the game created before
        latest_game = Game.objects.latest('id')

        self.assertEqual(turno,latest_game.turno)
        self.assertEqual(tablero.__str__(),latest_game.tablero.__str__())
        self.assertEqual(marcador.__str__(),latest_game.marcador.__str__())

        # Assert that the redirect function was called with the correct URL
        self.assertEqual(response.url,'/tictactoe')
        self.assertEqual(response.status_code,302) # Redirect code


    # Tests that a new game is not created with a new tablero, marcador, and turn when win is False
    def test_new_game_win_false(self):
        tablero = Tablero.objects.create(a1=EMPTY_CELL,a2=EMPTY_CELL,a3=EMPTY_CELL,b1=EMPTY_CELL,b2=EMPTY_CELL,b3=EMPTY_CELL,c1=EMPTY_CELL,c2=EMPTY_CELL,c3=EMPTY_CELL)
        marcador = Marcador.objects.create(playerX=1, playerO=2, num_games=3)
        turno = Turno.objects.create(turno=False)

        tablero.save()
        marcador.save()
        turno.save()
        
        # Set the win with True
        win = False

        # Call the new_game function
        response = new_game(win, tablero, marcador, turno)

        # Use assertRaises to capture the Game.DoesNotExist exception
        with self.assertRaises(Game.DoesNotExist):
            latest_game = Game.objects.latest('id')

        # Assert that the redirect function was called with the correct URL
        self.assertEqual(response.url,'/tictactoe')
        self.assertEqual(response.status_code,302) # Redirect code