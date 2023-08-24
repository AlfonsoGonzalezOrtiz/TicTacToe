from django.shortcuts import render,redirect
from miapp.models import Tablero,Marcador,Turno

class Juego(object):
    def __init__(self):
        self.tablero = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]
        ]
        self.marcador = [0,0]
        self.turno = 'x'  

# Create your views here.
def jugar(request):

    tablero = Tablero.objects.all().first().__str__()
    tablero = string_to_matrix(tablero)
    jugadorX = Marcador.objects.filter(id=1).first().jugadorX
    jugadorO = Marcador.objects.filter(id=1).first().jugadorO
    turno = Turno.objects.filter(id=1).first().__str__()

    params = {'tablero':tablero, 'jugadorX': jugadorX,'jugadorO': jugadorO,'turno': turno}
    return render(request,"miplantilla.html",params)


def string_to_matrix(input_string):
    #if len(input_string) != 9:
        #raise ValueError("El string debe tener tamaño 9")

    matrix = []
    for i in range(0, 9, 3):
        row = input_string[i:i+3]
        matrix.append(list(row))

    return matrix

def turno(request):

    if request.method == 'POST':
        tablero_db = Tablero.objects.first()
        tablero = string_to_matrix(tablero_db.__str__())

        turno_db = Turno.objects.first()
        
        str = ''
        if turno_db.turno:
            str = 'O'
        else:
            str = 'X'

        marcador = Marcador.objects.filter(id=1).first()

        found = 0
        for row in range(3):
            for col in range(3):
                cell_name = f'cell_{row + 1}_{col + 1}'
                if request.POST.get(cell_name):
                    found = 1
                    break
            if found:
                break
        
        fin = False
        updated = update_cell(tablero_db,cell_name,str,fin)

        str_tablero = string_to_matrix(tablero_db.__str__())
        fin = check_tic_tac_toe(str_tablero)
        bloqueo = configuracion_bloqueo(str_tablero)
        if fin:
            if str == 'O':
                marcador.jugadorO += 1
            else:
                marcador.jugadorX += 1
            marcador.save()
            new_game(request,fin)
        elif bloqueo:
            new_game(request,True)

        if updated and not fin and not bloqueo:
            turno_db.turno = not turno_db.turno
            turno_db.save()

    return redirect('/tictactoe')


    
def update_cell(tablero_db, cell_name, turno,fin):
    updated = False
    switch_cases = {
        'cell_1_1': ('a1', turno),
        'cell_1_2': ('a2', turno),
        'cell_1_3': ('a3', turno),
        'cell_2_1': ('b1', turno),
        'cell_2_2': ('b2', turno),
        'cell_2_3': ('b3', turno),
        'cell_3_1': ('c1', turno),
        'cell_3_2': ('c2', turno),
        'cell_3_3': ('c3', turno),
    }

    if cell_name in switch_cases:
        attribute, value = switch_cases[cell_name]
        cell_value = getattr(tablero_db, attribute)
        if cell_value == ' ' or fin:  # Verificar si la celda está vacía
            setattr(tablero_db, attribute, value)
            tablero_db.save()
            updated = True
    return updated


def reset(request):
    fin = True
    reiniciar_tablero(fin)
    reiniciar_marcador()
    return redirect('/tictactoe')

def new_game(request,fin):
    reiniciar_tablero(fin)
    return redirect('/tictactoe')

def check_tic_tac_toe(board):
    # Comprobar filas
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True

    # Comprobar columnas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    # Comprobar diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def configuracion_bloqueo(tablero):
    for fila in tablero:
        for elemento in fila:
            if elemento == ' ':
                return False  # Se encontró una cadena vacía, por lo que retornamos False
    return True  # No se encontró ninguna cadena vacía, retornamos True


def reiniciar_marcador():
    marcador = Marcador.objects.first()
    marcador.jugadorO = 0
    marcador.jugadorX = 0
    marcador.save()

def reiniciar_tablero(fin):
    tablero_db = Tablero.objects.first()
    for row in range(3):
        for col in range(3):
            cell_name = f'cell_{row + 1}_{col + 1}'
            update_cell(tablero_db, cell_name,' ',fin)
