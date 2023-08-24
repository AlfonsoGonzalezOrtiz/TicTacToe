from django.test import TestCase
from miapp.models import Marcador


class MarcadorTestCase(TestCase):
        
    # Tests that a new instance of 'Marcador' can be created with valid integer values for both 'jugadorX' and 'jugadorO'.
    def test_create_instance_with_valid_values(self):
        marcador = Marcador(jugadorX=5, jugadorO=3)
        self.assertEqual(marcador.jugadorX, 5)
        self.assertEqual(marcador.jugadorO, 3)

    # Tests that a new instance of 'Marcador' can be saved to the database.
    def test_save_instance_to_database(self):
        marcador = Marcador(jugadorX=5, jugadorO=3)
        marcador.save()
        self.assertTrue(Marcador.objects.filter(jugadorX=5, jugadorO=3).exists())

    # Tests that an existing instance of 'Marcador' can be retrieved from the database.
    def test_retrieve_instance_from_database(self):
        marcador = Marcador(jugadorX=5, jugadorO=3)
        marcador.save()
        retrieved_marcador = Marcador.objects.get(jugadorX=5, jugadorO=3)
        self.assertEqual(retrieved_marcador.jugadorX, 5)
        self.assertEqual(retrieved_marcador.jugadorO, 3)

    # Tests that the 'jugadorX' and 'jugadorO' values of an existing instance of 'Marcador' can be updated.
    def test_update_instance_values(self):
        marcador = Marcador(jugadorX=5, jugadorO=3)
        marcador.save()
        marcador.jugadorX = 10
        marcador.jugadorO = 7
        marcador.save()
        retrieved_marcador = Marcador.objects.get(jugadorX=10, jugadorO=7)
        self.assertEqual(retrieved_marcador.jugadorX, 10)
        self.assertEqual(retrieved_marcador.jugadorO, 7)

    