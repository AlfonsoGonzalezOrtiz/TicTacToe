from django.test import TestCase,Client,override_settings
from django.template import TemplateDoesNotExist
from miapp.views import games
from miapp.constants import EMPTY_CELL
from unittest.mock import Mock,patch
from miapp.models import Tablero,Marcador,Turno,Game
from unittest.mock import Mock


class TestGames(TestCase):

    # Tests that the function retrieves the 10 most recent games from the database and renders them in the 'games.html' template.
    def test_retrieve_10_most_recent_games(self):

        # Create 11 games in the database
        for i in range(11):
            tablero = Tablero.objects.create(a1=EMPTY_CELL,a2=EMPTY_CELL,a3=EMPTY_CELL,b1=EMPTY_CELL,b2=EMPTY_CELL,b3=EMPTY_CELL,c1=EMPTY_CELL,c2=EMPTY_CELL,c3=EMPTY_CELL)
            tablero.save()
            marcador = Marcador.objects.create(playerX=0, playerO=0, num_games=0)
            marcador.save()
            turno = Turno.objects.create(turno=True)
            turno.save()
            game = Game.objects.create(tablero=tablero,marcador=marcador,turno=turno)
            game.save()

        client = Client()  # Create a client instance to simulate requests
        response = client.get('/games/')

        # Assert that the response contains the 10 most recent games
        self.assertEqual(len(response.context['games']), 10)
        self.assertEqual(response.status_code, 200)

    # Tests that the function retrieves all games from the database and renders them in the 'games.html' template when there are less than 10 games in the database.
    def test_retrieve_all_games_when_less_than_10_games_in_database(self):
        # Create 5 games in the database
        for i in range(5):
            tablero = Tablero.objects.create(a1=EMPTY_CELL,a2=EMPTY_CELL,a3=EMPTY_CELL,b1=EMPTY_CELL,b2=EMPTY_CELL,b3=EMPTY_CELL,c1=EMPTY_CELL,c2=EMPTY_CELL,c3=EMPTY_CELL)
            tablero.save()
            marcador = Marcador.objects.create(playerX=0, playerO=0, num_games=0)
            marcador.save()
            turno = Turno.objects.create(turno=True)
            turno.save()
            game = Game.objects.create(tablero=tablero,marcador=marcador,turno=turno)
            game.save()

        client = Client()  # Create a client instance to simulate requests
        response = client.get('/games/') 

        # Assert that the response contains all the games
        self.assertEqual(len(response.context['games']), 5)
        self.assertEqual(response.status_code, 200)

    # Tests that the function renders an empty 'games.html' template when there are no games in the database.
    def test_render_empty_template_when_no_games_in_database(self):
        client = Client()  # Create a client instance to simulate requests
        response = client.get('/games/')

        # Assert that the response contains an empty list of games
        self.assertEqual(len(response.context['games']), 0)
        self.assertEqual(response.status_code, 200)
        
    # Tests that the function raises a 'TemplateDoesNotExist' exception when the 'games.html' template fails to render.
    @override_settings(TEMPLATES=[{'BACKEND': 'django.template.backends.django.DjangoTemplates', 'DIRS': ['/nonexistent'] }])
    def test_render_empty_template_when_template_fails_to_render(self):
        # Call the 'games' function
        with self.assertRaises(TemplateDoesNotExist):
            client = Client()  # Create a client instance to simulate requests
            response = client.get('/games/')

    # Tests that the function retrieves only the 10 most recent games from the database and renders them in the 'games.html' template when there are more than 10 games in the database.
    def test_retrieve_10_most_recent_games_when_more_than_10_games_in_database(self):
        # Create 15 games in the database
        for i in range(15):
            tablero = Tablero.objects.create(a1=EMPTY_CELL,a2=EMPTY_CELL,a3=EMPTY_CELL,b1=EMPTY_CELL,b2=EMPTY_CELL,b3=EMPTY_CELL,c1=EMPTY_CELL,c2=EMPTY_CELL,c3=EMPTY_CELL)
            tablero.save()
            marcador = Marcador.objects.create(playerX=0, playerO=0, num_games=0)
            marcador.save()
            turno = Turno.objects.create(turno=True)
            turno.save()
            game = Game.objects.create(tablero=tablero,marcador=marcador,turno=turno)
            game.save()

        client = Client()  # Create a client instance to simulate requests
        response = client.get('/games/')

        # Assert that the response contains the 10 most recent games
        self.assertEqual(len(response.context['games']), 10)
        self.assertEqual(response.status_code, 200)