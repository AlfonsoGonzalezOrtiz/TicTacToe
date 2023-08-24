from django.shortcuts import render,redirect,get_object_or_404
from miapp.models import Tablero,Marcador,Turno
from miapp.utils import string_to_matrix,find_selected_cell,update_cell
from miapp.utils import check_tic_tac_toe,configuracion_bloqueo
from miapp.constants import JUGADOR1_LETTER, JUGADOR2_LETTER, EMPTY_CELL

# Create your views here.

def play(request):
    marcador = get_object_or_404(Marcador, id=1)
    jugadorX = marcador.jugadorX
    jugadorO = marcador.jugadorO

    tablero = get_object_or_404(Tablero, id=1)
    tablero_matrix = string_to_matrix(tablero.__str__())

    turno = str(get_object_or_404(Turno, id=1))

    context = {'tablero': tablero_matrix, 'jugadorX': jugadorX, 'jugadorO': jugadorO, 'turno': turno}
    return render(request, "miplantilla.html", context)

def turno(request):
    if request.method == 'POST':
        tablero_db = Tablero.objects.first()
        tablero = string_to_matrix(tablero_db.__str__())
        turno_db = Turno.objects.first()
        str = get_player_letter(turno_db.turno)
        marcador = get_marcador()
        cell_name = find_selected_cell(request)
        
        fin, updated = process_turn(tablero_db, cell_name, str)
        
        str_tablero = string_to_matrix(tablero_db.__str__())
        fin = check_tic_tac_toe(str_tablero)
        bloqueo = configuracion_bloqueo(str_tablero)

        handle_game_outcome(request,str, marcador, fin, bloqueo)
        handle_turn_update(turno_db, updated, fin, bloqueo)

    return redirect('/tictactoe')

def get_player_letter(turno):
    return JUGADOR1_LETTER if turno else JUGADOR2_LETTER

def get_marcador():
    return Marcador.objects.get(id=1)

def process_turn(tablero_db, cell_name, player_letter):
    updated = update_cell(tablero_db, cell_name, player_letter, False)
    str_tablero = string_to_matrix(tablero_db.__str__())
    fin = check_tic_tac_toe(str_tablero)
    return fin, updated

def handle_game_outcome(request,player_letter, marcador, fin, bloqueo):
    if fin:
        if player_letter == JUGADOR1_LETTER:
            marcador.jugadorO += 1
        else:
            marcador.jugadorX += 1
        marcador.save()
        new_game(request, fin)
    elif bloqueo:
        new_game(request, True)

def handle_turn_update(turno_db, updated, fin, bloqueo):
    if updated and not (fin or bloqueo):
        turno_db.turno = not turno_db.turno
        turno_db.save()


def reset(request):
    fin = True
    reiniciar_tablero(fin)
    reiniciar_marcador()
    return redirect('/tictactoe')

def new_game(request,fin):
    reiniciar_tablero(fin)
    return redirect('/tictactoe')

def reiniciar_marcador():
    marcador = Marcador.objects.first()
    if marcador is not None:
        marcador.jugadorO = 0
        marcador.jugadorX = 0
        marcador.save()

def reiniciar_tablero(fin):
    tablero_db = Tablero.objects.first()
    for row in range(3):
        for col in range(3):
            cell_name = f'cell_{row + 1}_{col + 1}'
            update_cell(tablero_db, cell_name,EMPTY_CELL,fin)
