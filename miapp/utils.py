from miapp.constants import EMPTY_CELL

def string_to_matrix(input_string):
    if len(input_string) != 9:
        raise ValueError("El string debe tener tamaño 9")

    matrix = []
    for i in range(0, 9, 3):
        row = input_string[i:i+3]
        matrix.append(list(row))

    return matrix
    
def find_selected_cell(request):
    if request.method == 'POST':  # Verificamos si la solicitud es de tipo POST
        if len(request.POST) == 2:  # Verificamos si solo hay un par clave valor en request.POST
            for row in range(3):
                for col in range(3):
                    cell_name = f'cell_{row + 1}_{col + 1}'
                    if request.POST.get(cell_name):
                        return cell_name
    return None


def update_cell(tablero_db, cell_name, turno, win):
    # Verificamos si tablero_db no es None, win es booleano y turno es string
    if tablero_db is not None and isinstance(win, bool) and isinstance(turno, str):  
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
            return modify_cell(tablero_db, attribute, value, win)

    return False


def modify_cell(tablero_db, attribute, value, win):
    cell_name = getattr(tablero_db, attribute)
    if cell_name == EMPTY_CELL or win:
        setattr(tablero_db, attribute, value)
        tablero_db.save()
        return True
    return False

def check_line(line):
    return line[0] == line[1] == line[2] and line[0] != EMPTY_CELL

def check_tic_tac_toe(board):
    # Comprobar filas
    for row in board:
        if check_line(row):
            return True

    # Comprobar columnas
    for col in range(3):
        if check_line([board[row][col] for row in range(3)]):
            return True

    # Comprobar diagonales
    if check_line([board[i][i] for i in range(3)]):
        return True
    if check_line([board[i][2-i] for i in range(3)]):
        return True

    return False

def lock_configuration(tablero):
    for fila in tablero:
        for elemento in fila:
            if elemento == EMPTY_CELL:
                return False  # Se encontró una cadena vacía, por lo que retornamos False
    return True  # No se encontró ninguna cadena vacía, retornamos True
