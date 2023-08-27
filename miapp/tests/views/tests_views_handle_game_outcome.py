from django.test import TestCase
from miapp.views import handle_game_outcome
from miapp.models import Turno,Tablero,Marcador,Game
from miapp.constants import JUGADOR1_LETTER,JUGADOR2_LETTER,EMPTY_CELL

class TestHandleGameOutcome(TestCase):

    # Tests that when win is True, player's one score is incremented and the number of games played is incremented
    def test_win_increment_player1_score(self):
        # Win configuration for player1
        tablero = Tablero.objects.create(
            a1=JUGADOR1_LETTER, a2=JUGADOR1_LETTER, a3=JUGADOR1_LETTER,
            b1=JUGADOR2_LETTER, b2=JUGADOR2_LETTER, b3=EMPTY_CELL,
            c1=EMPTY_CELL, c2=EMPTY_CELL, c3=EMPTY_CELL
        )
        tablero.save()
        marcador = Marcador.objects.create(playerX=0, playerO=0, num_games=0)
        marcador.save()
        turno = Turno.objects.create(turno=True)
        turno.save()
        game = Game.objects.create(tablero=tablero,marcador=marcador,turno=turno)
        game.save()
        
        win = True
        block = False

        # Call the handle_game_outcome function with win=True
        handle_game_outcome(tablero, JUGADOR1_LETTER, marcador, turno, win, block)
    
        # Assert that the appropriate player's score is incremented
        self.assertEqual(marcador.playerO, 1)
        self.assertEqual(marcador.playerX, 0)

        # Assert that the number of games played is incremented
        self.assertEqual(marcador.num_games, 1)
    
        # Assert that a new game is created and saved
        self.assertEqual(Game.objects.count(), 2) # We created one game before so we get two games

# Tests that when win is True, player's one score is incremented and the number of games played is incremented
    def test_win_increment_player2_score(self):
        # Win configuration for player2
        tablero = Tablero.objects.create(
            a1=JUGADOR1_LETTER, a2=JUGADOR1_LETTER, a3=EMPTY_CELL,
            b1=JUGADOR2_LETTER, b2=JUGADOR2_LETTER, b3=JUGADOR2_LETTER,
            c1=JUGADOR1_LETTER, c2=EMPTY_CELL, c3=EMPTY_CELL
        )
        tablero.save()
        marcador = Marcador.objects.create(playerX=0, playerO=0, num_games=0)
        marcador.save()
        turno = Turno.objects.create(turno=False)
        turno.save()
        game = Game.objects.create(tablero=tablero,marcador=marcador,turno=turno)
        game.save()
        
        win = True
        block = False

        # Call the handle_game_outcome function with win=True
        handle_game_outcome(tablero, JUGADOR2_LETTER, marcador, turno, win, block)
    
        # Assert that the appropriate player's score is incremented
        self.assertEqual(marcador.playerO, 0)
        self.assertEqual(marcador.playerX, 1)

        # Assert that the number of games played is incremented
        self.assertEqual(marcador.num_games, 1)
    
        # Assert that a new game is created and saved
        self.assertEqual(Game.objects.count(), 2) # We created one game before so we get two games


    # Tests that when win is False and block is True, the number of games played is incremented
    def test_block_increment_num_games(self):
        # Block configuration
        tablero = Tablero.objects.create(
            a1=JUGADOR1_LETTER, a2=JUGADOR1_LETTER, a3=JUGADOR2_LETTER,
            b1=JUGADOR2_LETTER, b2=JUGADOR2_LETTER, b3=JUGADOR1_LETTER,
            c1=JUGADOR1_LETTER, c2=JUGADOR2_LETTER, c3=JUGADOR1_LETTER
        )
        tablero.save()
        marcador = Marcador.objects.create(playerX=0, playerO=0, num_games=0)
        marcador.save()
        turno = Turno.objects.create(turno=True)
        turno.save()
        game = Game.objects.create(tablero=tablero,marcador=marcador,turno=turno)
        game.save()
        
        win = False
        block = True

        # Call the handle_game_outcome function with block=True
        handle_game_outcome(tablero, JUGADOR1_LETTER, marcador, turno, win, block)
    
        # Assert that the appropriate player's score is not incremented
        self.assertEqual(marcador.playerO, 0)
        self.assertEqual(marcador.playerX, 0)

        # Assert that the number of games played is incremented
        self.assertEqual(marcador.num_games, 1)
    
        # Assert that a new game is created and saved
        self.assertEqual(Game.objects.count(), 2) # We created one game before so we get two games