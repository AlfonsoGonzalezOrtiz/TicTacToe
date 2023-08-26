from django.shortcuts import render,redirect,get_object_or_404
from miapp.models import Tablero,Marcador,Turno,Game
from miapp.utils import string_to_matrix,find_selected_cell,update_cell
from miapp.utils import check_tic_tac_toe,lock_configuration
from miapp.constants import JUGADOR1_LETTER, JUGADOR2_LETTER, EMPTY_CELL
from django.db import transaction
import pdb

# Create your views here.

def play(request):
    with transaction.atomic():
        try:
            latest_game = Game.objects.latest('id')
        except Exception:
            marcador = Marcador.objects.create(playerX=0, playerO=0, num_games=0)
            marcador.save()
            tablero = Tablero.objects.create(a1=EMPTY_CELL,a2=EMPTY_CELL,a3=EMPTY_CELL,b1=EMPTY_CELL,b2=EMPTY_CELL,b3=EMPTY_CELL,c1=EMPTY_CELL,c2=EMPTY_CELL,c3=EMPTY_CELL)
            tablero.save()
            turno = Turno.objects.create(turno=True)
            turno.save()
            game = Game.objects.create(tablero=tablero,marcador=marcador,turno=turno)
            game.save()

            latest_game = Game.objects.latest('id')

        marcador = get_object_or_404(Marcador, id=latest_game.marcador.id)
        tablero = get_object_or_404(Tablero, id=latest_game.tablero.id)
        turno = get_object_or_404(Turno, id=latest_game.turno.id)
        
    
        tablero_matrix = string_to_matrix(tablero.__str__())
        player_letter = get_player_letter(turno.turno)
        context = {
            'tablero': tablero_matrix,
            'playerX': marcador.playerX,
            'playerO': marcador.playerO,
            'turn': player_letter,
            'num_games': marcador.num_games,
        }

    return render(request, "miplantilla.html", context)

def turn(request):
    if request.method == 'POST':
        latest_game = Game.objects.latest('id')

        marcador = get_object_or_404(Marcador, id=latest_game.__getattribute__('marcador').id)
        tablero_db = get_object_or_404(Tablero,id=latest_game.__getattribute__('tablero').id)
        turn_db = get_object_or_404(Turno,id=latest_game.__getattribute__('turno').id)

        
        tablero = string_to_matrix(tablero_db.__str__())
        player_letter  = get_player_letter(turn_db.turno)
        
        cell_name = find_selected_cell(request)
        win, updated = process_turn(tablero_db, cell_name, player_letter)
        
        str_tablero = string_to_matrix(tablero_db.__str__())
        win = check_tic_tac_toe(str_tablero)
        bloqueo = lock_configuration(str_tablero)

        handle_game_outcome(request,tablero_db,player_letter,marcador,turn_db, win, bloqueo)
        handle_turn_update(turn_db,updated, win, bloqueo)

    return redirect('/tictactoe')

def reset(request):
    with transaction.atomic():
        latest_game = Game.objects.latest('id')
        marcador = Marcador.objects.create(playerX=0, playerO=0, num_games=0)
        marcador.save()
        tablero = Tablero.objects.create(a1=EMPTY_CELL,a2=EMPTY_CELL,a3=EMPTY_CELL,b1=EMPTY_CELL,b2=EMPTY_CELL,b3=EMPTY_CELL,c1=EMPTY_CELL,c2=EMPTY_CELL,c3=EMPTY_CELL)
        tablero.save()
        turno = get_object_or_404(Turno,id=latest_game.__getattribute__('turno').id)
        turno.turno = True
        turno.save()
        game = Game.objects.create(tablero=tablero,marcador=marcador,turno=turno)
        game.save()
    return redirect('/tictactoe')

def games(request):
    games = Game.objects.order_by('-id')[:10]
    return render(request, "games.html", {'games':games})

def get_player_letter(turn):
    if not isinstance(turn, bool):
        raise ValueError(f"turn must be a boolean value: {turn}")

    return JUGADOR1_LETTER if turn else JUGADOR2_LETTER

def process_turn(tablero_db, cell_name, player_letter):
    updated = update_cell(tablero_db, cell_name, player_letter, False)
    str_tablero = string_to_matrix(tablero_db.__str__())
    win = check_tic_tac_toe(str_tablero)
    return win, updated

def handle_game_outcome(request,tablero,player_letter, marcador,turno, win, bloqueo):
    if win:
        if player_letter == JUGADOR1_LETTER:
            marcador.playerO += 1
        else:
            marcador.playerX += 1
        marcador.num_games += 1
        marcador.save()
        new_game(win,tablero,marcador,turno)
    elif bloqueo:
        marcador.num_games += 1
        marcador.save()
        new_game(True,tablero,marcador,turno)

def handle_turn_update(turno, updated, win, bloqueo):
    if updated and not (win or bloqueo):
        turno.turno = not turno.turno
        turno.save()

def new_game(win,tablero,marcador,turno):
    if win:
        new_tablero = Tablero.objects.create()
        new_tablero.save()
        new_marcador = Marcador.objects.create(playerX=marcador.playerX,playerO=marcador.playerO,num_games=marcador.num_games)
        new_marcador.save()
        game = Game.objects.create(tablero=new_tablero,marcador=new_marcador,turno=turno) # Turn is irrelevant
        game.save()
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
        raise ValueError(f"end must be a boolean value: {end}")

    for row in range(3):
        for col in range(3):
            cell_name = f'cell_{row + 1}_{col + 1}'
            update_cell(tablero_db, cell_name, EMPTY_CELL, end)


