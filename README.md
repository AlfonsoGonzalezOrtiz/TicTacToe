# Tres en Línea (Tic Tac Toe) en Django

Este es un proyecto de Tres en Línea (Tic Tac Toe) desarrollado en Django. El proyecto permite a los jugadores jugar al clásico juego de tres en línea en línea.

## Los requisitos mínimos a cumplir son
- Permitir Jugar a 2 Players y validar el orden. :white_check_mark:
- Validar la entrada e impedir movimientos no válidos. :white_check_mark:
- Visualizar el estado del tablero y comprobar si se ha producido un ganador. :white_check_mark:
- Usar git para subir el código a un repositorio público (github o bitbucket) :white_check_mark:

## Requisitos valorables
- Implementar el juego usando un API REST y usar curl/wget como cliente. :white_check_mark:
- Llevar un control de partidas jugadas, incluida la puntuación. :white_check_mark:
- Realización de Test Unitarios. :white_check_mark: 100 % coverage
- Establecer una persistencia para no perder el estado en caso de reinicio de
servidor/aplicación. :white_check_mark:
- Establecer control de sesiones con autenticación para permitir múltiples
partidas/jugadores.
- Registrar un log de partidas y dar la capacidad de ser consultado. :white_check_mark:


## Capturas de Pantalla
http://localhost:8000/tictactoe/
![](https://i.imgur.com/scKWKi7.png "TicTacToe")
http://localhost:8000/games/
![](https://i.imgur.com/DmPdbEq.png "Log games")

## Manual de Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

### Requisitos Previos

- Python (versión 3.10.4)
- Django (versión 4.2.4)

### Pasos de Instalación

1. **Clona el Repositorio**
		git clone https://github.com/AlfonsoGonzalezOrtiz/TicTacToe

2. **Crea un entorno virtual**
		python -m venv venv
		source venv/bin/activate  # En sistemas Unix/Linux
		venv\Scripts\activate     # En Windows

3. **Instala las Dependencias**
En sistemas Unix/Linux/macOS:
		pip install --user --upgrade pip
		pip install -r requirements.txt
En sistemas Windows:
		python -m pip install --user --upgrade pip
		pip install -r requirements.txt

4. **Configura la Base de Datos**
python manage.py migrate

5. **Inicia el Servidor de Desarrollo**
python manage.py runserver

6. **Accede a la Aplicación**
Abre tu navegador y visita: http://127.0.0.1:8000/tictactoe

## Tutorial de Juego: Tic Tac Toe

¡Bienvenido al emocionante juego de Tres en Línea (Tic Tac Toe)!

### Cómo Jugar

1. Accede a la pantalla del Tic Tac Toe en tu navegador.

2. Una vez en la pantalla, puedes comenzar a jugar.

3. Empieza el **Jugador O**. Los jugadores se turnan para hacer sus movimientos.

4. Haz clic en la casilla en la que deseas colocar tu símbolo (X o O). El sistema automáticamente asignará tu símbolo a la casilla.

5. El juego detectará automáticamente cuando la partida ha terminado:

   - Si hay un **ganador**, el sistema sumará 1 punto en el marcador al jugador correspondiente y aumentará el contador de partidas en 1.
   
   - Si la partida ha terminado y **nadie ha ganado**, el tablero se reiniciará, se sumará 1 al contador de partidas y el marcador permanecerá inmutable.

6. Si deseas comenzar una nueva partida, puedes hacer clic en el botón de **reset**. Esto reiniciará el tablero, el marcador y el contador de partidas, dándote un nuevo comienzo.

7. ¡Diviértete jugando al Tic Tac Toe y disfruta de la competición!

## Ejecución de los tests

### Ejecutar tests
python manage.py test miapp/tests/utils miapp/tests/views miapp/tests/models
### Mostrar reporte
```bash
coverage run manage.py test miapp/tests/utils miapp/tests/views miapp/tests/models
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........................................................................................
----------------------------------------------------------------------
Ran 90 tests in 0.423s

OK
Destroying test database for alias 'default'...
```
```bash
coverage report -m
Name                                                                                   Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------------------------------------------------
manage.py                                                                                 12      2    83%   12-13
miapp\__init__.py                                                                          0      0   100%
miapp\admin.py                                                                             1      0   100%
miapp\apps.py                                                                              4      0   100%
miapp\constants.py                                                                         5      0   100%
miapp\migrations\0001_initial.py                                                           5      0   100%
miapp\migrations\0002_alter_tablero_a1_alter_tablero_a2_alter_tablero_a3_and_more.py       4      0   100%
miapp\migrations\0003_rename_cl_tablero_c1.py                                              4      0   100%
miapp\migrations\0004_rename_bl_tablero_b1.py                                              4      0   100%
miapp\migrations\0005_remove_marcador_jugadoro_remove_marcador_jugadorx_and_more.py        5      0   100%
miapp\migrations\0006_alter_turno_turno.py                                                 4      0   100%
miapp\migrations\__init__.py                                                               0      0   100%
miapp\models.py                                                                           46      0   100%
miapp\tests\models\test_models_game.py                                                    40      0   100%
miapp\tests\models\test_models_marcador.py                                                29      0   100%
miapp\tests\models\test_models_tablero.py                                                 42      0   100%
miapp\tests\models\test_models_turno.py                                                   21      0   100%
miapp\tests\utils\tests_utils_check_line.py                                               19      0   100%
miapp\tests\utils\tests_utils_check_tic_tac_toe.py                                        28      0   100%
miapp\tests\utils\tests_utils_find_selected_cell.py                                       40      0   100%
miapp\tests\utils\tests_utils_lock_configuration.py                                       12      0   100%
miapp\tests\utils\tests_utils_modify_cell.py                                              23      0   100%
miapp\tests\utils\tests_utils_string_to_matrix.py                                         23      0   100%
miapp\tests\utils\tests_utils_update_cell.py                                              33      0   100%
miapp\tests\views\tests_views_games.py                                                    60      0   100%
miapp\tests\views\tests_views_get_player_letter.py                                        24      0   100%
miapp\tests\views\tests_views_handle_game_outcome.py                                      53      0   100%
miapp\tests\views\tests_views_handle_turn_update.py                                       39      0   100%
miapp\tests\views\tests_views_new_game.py                                                 34      0   100%
miapp\tests\views\tests_views_play.py                                                     32      0   100%
miapp\tests\views\tests_views_process_turn.py                                             34      0   100%
miapp\tests\views\tests_views_reset.py                                                    24      0   100%
miapp\tests\views\tests_views_reset_board.py                                              37      0   100%
miapp\tests\views\tests_views_reset_scoreboard.py                                         18      0   100%
miapp\tests\views\tests_views_turn.py                                                     45      0   100%
miapp\utils.py                                                                            54      0   100%
miapp\views.py                                                                           115      0   100%
tictactoe\__init__.py                                                                      0      0   100%
tictactoe\settings.py                                                                     19      0   100%
tictactoe\urls.py                                                                          4      0   100%
--------------------------------------------------------------------------------------------------------------------
TOTAL                                                                                    996      2    99%
```


[![AlfonsoGonzalez's GitHub stats](https://github-readme-stats.vercel.app/api?username=AlfonsoGonzalezOrtiz)](https://github.com/anuraghazra/github-readme-stats)

