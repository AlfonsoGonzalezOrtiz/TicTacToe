from django.test import TestCase
from miapp.models import Marcador


class MarcadorTestCase(TestCase):
        
    # Tests that a new instance of 'Marcador' can be created with valid integer values for both 'playerX' and 'playerO'.
    def test_create_instance_with_valid_values(self):
        marcador = Marcador(playerX=5, playerO=3,num_games=0)
        self.assertEqual(marcador.playerX, 5)
        self.assertEqual(marcador.playerO, 3)

    # Tests that a new instance of 'Marcador' can be saved to the database.
    def test_save_instance_to_database(self):
        marcador = Marcador(playerX=5, playerO=3,num_games=0)
        marcador.save()
        self.assertTrue(Marcador.objects.filter(playerX=5, playerO=3,num_games=0).exists())

    # Tests that an existing instance of 'Marcador' can be retrieved from the database.
    def test_retrieve_instance_from_database(self):
        marcador = Marcador(playerX=5, playerO=3,num_games=0)
        marcador.save()
        retrieved_marcador = Marcador.objects.get(playerX=5, playerO=3,num_games=0)
        self.assertEqual(retrieved_marcador.playerX, 5)
        self.assertEqual(retrieved_marcador.playerO, 3)
        self.assertEqual(retrieved_marcador.num_games, 0)

    # Tests that the 'playerX' and 'playerO' values of an existing instance of 'Marcador' can be updated.
    def test_update_instance_values(self):
        marcador = Marcador(playerX=5, playerO=3,num_games=0)
        marcador.save()
        marcador.playerX = 10
        marcador.playerO = 7
        marcador.num_games = 2
        marcador.save()
        retrieved_marcador = Marcador.objects.get(playerX=10, playerO=7,num_games=2)
        self.assertEqual(retrieved_marcador.playerX, 10)
        self.assertEqual(retrieved_marcador.playerO, 7)
        self.assertEqual(retrieved_marcador.num_games, 2)

    