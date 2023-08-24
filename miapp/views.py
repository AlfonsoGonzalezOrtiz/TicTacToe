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
            
        update_cell(tablero_db,cell_name,str)

        if check_tic_tac_toe(string_to_matrix(tablero_db.__str__())):
            if str == 'O':
                marcador.jugadorO += 1
            else:
                marcador.jugadorX += 1
            marcador.save()
            reset(request)

        turno_db.turno = not turno_db.turno
        turno_db.save()
        

    return redirect('/tictactoe')


    
def update_cell(tablero_db, cell_name, turno):
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
        setattr(tablero_db, attribute, value)
        tablero_db.save()


def reset(request):
    tablero_db = Tablero.objects.first()
    for row in range(3):
        for col in range(3):
            cell_name = f'cell_{row + 1}_{col + 1}'
            update_cell(tablero_db,cell_name,' ')

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