from django.test import TestCase,Client
from miapp.models import Marcador,Tablero,Turno,Game
from miapp.views import turn
from miapp.constants import EMPTY_CELL
from django.db import transaction
from miapp.constants import JUGADOR1_LETTER
'''
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

        client = Client()  # Create a client instance to simulate requests
        response = client.post('/turn/')

        latest_game = Game.objects.latest('id')

        # Assert that the create and save methods were called with the correct arguments
        # Check only str to not check all arguments
        self.assertEqual(latest_game.tablero.a1,JUGADOR1_LETTER)

        # Assert that redirects to '/tictactoe'
        self.assertEqual(response.url,'/tictactoe')
        self.assertEqual(response.status_code,302) # Redirect code

    # Tests that the function handles the case when there is no latest game in the database
    def test_no_latest_game(self):
        request = MagicMock()
        request.method = 'POST'
        request.POST = {'cell_1_1': 'X'}
    
        Game.objects.latest.side_effect = Exception
    
        turn(request)
    
        redirect.assert_called_once_with('/tictactoe')

    # Tests that the function handles the case when an invalid cell name is found in the request
    def test_invalid_cell_name(self):
        request = MagicMock()
        request.method = 'POST'
        request.POST = {'invalid_cell': 'X'}
    
        game = MagicMock()
        game.marcador.playerX = 0
        game.marcador.playerO = 0
        game.marcador.num_games = 0
        game.tablero.__str__.return_value = 'X' + ' ' * 8
        game.turno.turno = True
    
        Game.objects.latest.return_value = game
        get_object_or_404.side_effect = [game.marcador, game.tablero, game.turno]
    
        turn(request)
    
        game.tablero.__str__.assert_called_once()
        update_cell.assert_not_called()
        check_tic_tac_toe.assert_not_called()
        handle_game_outcome.assert_not_called()
        handle_turn_update.assert_not_called()
        redirect.assert_called_once_with('/tictactoe')

    # Tests that the function handles the case when an invalid player letter is determined based on the Turno object
    def test_invalid_player_letter(self):
        request = MagicMock()
        request.method = 'POST'
        request.POST = {'cell_1_1': 'X'}
    
        game = MagicMock()
        game.marcador.playerX = 0
        game.marcador.playerO = 0
        game.marcador.num_games = 0
        game.tablero.__str__.return_value = 'X' + ' ' * 8
        game.turno.turno = None
    
        Game.objects.latest.return_value = game
        get_object_or_404.side_effect = [game.marcador, game.tablero, game.turno]
    
        turn(request)
    
        game.tablero.__str__.assert_called_once()
        update_cell.assert_not_called()
        check_tic_tac_toe.assert_not_called()
        handle_game_outcome.assert_not_called()
        handle_turn_update.assert_not_called()
        redirect.assert_called_once_with('/tictactoe')
'''