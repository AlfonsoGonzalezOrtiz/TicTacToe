from django.shortcuts import render,redirect,get_object_or_404
from miapp.models import Tablero,Marcador,Turno
from miapp.utils import string_to_matrix,find_selected_cell,update_cell
from miapp.utils import check_tic_tac_toe,lock_configuration
from miapp.constants import JUGADOR1_LETTER, JUGADOR2_LETTER, EMPTY_CELL
import pdb

# Create your views here.

def play(request):
    marcador = get_object_or_404(Marcador, id=1)
    playerX = marcador.playerX
    playerO = marcador.playerO
    num_games = marcador.num_games

    tablero = get_object_or_404(Tablero, id=1)
    tablero_matrix = string_to_matrix(tablero.__str__())

    turn = str(get_object_or_404(Turno, id=1))

    context = {'tablero': tablero_matrix, 'playerX': playerX, 'playerO': playerO, 'turn': turn,'num_games':num_games}
    return render(request, "miplantilla.html", context)

def turn(request):
    if request.method == 'POST':
        tablero_db = Tablero.objects.first()
        tablero = string_to_matrix(tablero_db.__str__())
        turn_db = Turno.objects.first()
        str = get_player_letter(turn_db.turno)
        marcador = Marcador.objects.get(id=1)
        cell_name = find_selected_cell(request)
        
        win, updated = process_turn(tablero_db, cell_name, str)
        
        str_tablero = string_to_matrix(tablero_db.__str__())
        win = check_tic_tac_toe(str_tablero)
        bloqueo = lock_configuration(str_tablero)

        handle_game_outcome(request,tablero_db,str, marcador, win, bloqueo)
        handle_turn_update(turn_db,updated, win, bloqueo)

    return redirect('/tictactoe')

def reset(request):
    tablero_db = Tablero.objects.first()
    marcador = Marcador.objects.first()
    reset_board(True,tablero_db)
    reset_scoreboard(marcador)
    return redirect('/tictactoe')

def get_player_letter(turn):
    if not isinstance(turn, bool):
        raise ValueError("turn must be a boolean value")

    return JUGADOR1_LETTER if turn else JUGADOR2_LETTER

def process_turn(tablero_db, cell_name, player_letter):
    updated = update_cell(tablero_db, cell_name, player_letter, False)
    str_tablero = string_to_matrix(tablero_db.__str__())
    win = check_tic_tac_toe(str_tablero)
    return win, updated

def handle_game_outcome(request,tablero_db,player_letter, marcador, win, bloqueo):
    if win:
        if player_letter == JUGADOR1_LETTER:
            marcador.playerO += 1
        else:
            marcador.playerX += 1
        marcador.num_games += 1
        marcador.save()
        new_game(win,tablero_db)
    elif bloqueo:
        marcador.num_games += 1
        marcador.save()
        new_game(True,tablero_db)

def handle_turn_update(turn_db, updated, win, bloqueo):
    if updated and not (win or bloqueo):
        turn_db.turno = not turn_db.turno
        turn_db.save()

def new_game(win,tablero_db):
    reset_board(win,tablero_db)
    return redirect('/tictactoe')

def reset_scoreboard(marcador):
    if marcador is not None:
        marcador.playerO = 0
        marcador.playerX = 0
        marcador.num_games = 0
        marcador.save()

def reset_board(end, tablero_db):
    if not isinstance(tablero_db, Tablero):
        raise ValueError("tablero_db must be an instance of Tablero")

    if not isinstance(end, bool):
        raise ValueError("end must be a boolean value")

    for row in range(3):
        for col in range(3):
            cell_name = f'cell_{row + 1}_{col + 1}'
            update_cell(tablero_db, cell_name, EMPTY_CELL, end)


