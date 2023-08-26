from django.test import TestCase
from miapp.models import Tablero,Marcador,Turno,Game
from miapp.constants import EMPTY_CELL
import pdb

class TestGame(TestCase):

    # Tests that a Game object can be created with valid Tablero, Marcador, and Turno objects
    def test_game_creation_with_valid_objects(self):
        # Create valid Tablero, Marcador, and Turno objects
        tablero = Tablero(...)
        marcador = Marcador(...)
        turno = Turno(...)
    
        # Create a Game object with the valid objects
        game = Game(tablero=tablero, marcador=marcador, turno=turno)
    
        # Assert that the Game object was created successfully
        self.assertEqual(game.tablero, tablero)
        self.assertEqual(game.marcador, marcador)
        self.assertEqual(game.turno, turno)
        self.assertEqual(game.__str__(),f'Tablero:{game.tablero}\nMarcador: {game.marcador}')

    # Tests that a Game object cannot be created without Tablero, Marcador, and Turno objects
    def test_game_creation_without_objects(self):
        # Attempt to create a Game object without the required objects
        game = Game()
        with self.assertRaises(Game.tablero.RelatedObjectDoesNotExist):
            # Assert that the Game object was created successfully
            self.assertEqual(game.tablero, Tablero())

    # Tests that a Game object cannot be created with non-existent Tablero, Marcador, or Turno objects
    def test_game_creation_with_nonexistent_objects(self):
        # Create non-existent Tablero, Marcador, and Turno objects
        tablero = None
        marcador = None
        turno = None

        game = Game(tablero=tablero, marcador=marcador, turno=turno)
        with self.assertRaises(Game.tablero.RelatedObjectDoesNotExist):
            # Assert that the Game object was created successfully
            self.assertEqual(game.tablero, tablero)

    # Tests that a Game object can be updated with valid Tablero, Marcador, and Turno objects
    def test_game_update_with_valid_objects(self):
        # Create a Game object with valid Tablero, Marcador, and Turno objects
        tablero = Tablero(...)
        marcador = Marcador(...)
        turno = Turno(...)
        game = Game(tablero=tablero, marcador=marcador, turno=turno)
    
        # Create new valid Tablero, Marcador, and Turno objects
        new_tablero = Tablero(...)
        new_marcador = Marcador(...)
        new_turno = Turno(...)
    
        # Update the Game object with the new valid objects
        game.tablero = new_tablero
        game.marcador = new_marcador
        game.turno = new_turno
    
        # Assert that the Game object was updated successfully
        self.assertEqual(game.tablero, new_tablero)
        self.assertEqual(game.marcador, new_marcador)
        self.assertEqual(game.turno, new_turno)
        self.assertEqual(game.__str__(),f'Tablero:{game.tablero}\nMarcador: {game.marcador}')
        