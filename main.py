# primero se genera el tablero
# se muestra tablero
# se comienza el juego y se asignan turnos
# solicita posicion a jugador y se verifica que no este ocupada
# se marca posicion
# verificar si alguien gano
# ver si hay 3 simbolos iguales en una fila, columna o diagonal
# ver si empataron
# cambiar turno de jugador

tablero = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def mostrar_tablero():
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8]),


#ejecuta el tablero
mostrar_tablero()

seguir_jugando = True

jugador_activo = "X"

posicion = ""

ganador = None  #none es igual a null


def turno():
    global tablero, jugador_activo, posicion
    #global quiere decir que utilizara todas las variables nombradas
    #dentro del metodo turno
    print("El turno es de: " + jugador_activo)

    posicion = ""

    valido = False

    while not valido:

        posicion = input("Elegi una posicion del 1 al 9:  ")

        posicion = int(posicion) - 1

        if tablero[posicion] == "-":
            valido = True
        else:
            print("Esta posicion esta ocupada")

    tablero[posicion] = jugador_activo

    mostrar_tablero()


def verificar_columnas():
    global seguir_jugando, ganador
    col_1 = tablero[0] == tablero[3] == tablero[6] != "-"
    col_2 = tablero[1] == tablero[4] == tablero[7] != "-"
    col_3 = tablero[2] == tablero[5] == tablero[8] != "-"

    if col_1 == True or col_2 == True or col_3 == True:
        seguir_jugando = False
        ganador = jugador_activo


def verificar_diagonales():
    global seguir_jugando, ganador
    diag_1 = tablero[0] == tablero[3] == tablero[6] != "-"
    diag_2 = tablero[1] == tablero[4] == tablero[7] != "-"

    if diag_1 == True or diag_2 == True:
        seguir_jugando = False
        ganador = jugador_activo


def verificar_filas():
    global seguir_jugando, ganador
    fil_1 = tablero[0] == tablero[1] == tablero[2] != "-"
    fil_2 = tablero[3] == tablero[4] == tablero[5] != "-"
    fil_3 = tablero[6] == tablero[7] == tablero[8] != "-"

    if fil_1 == True or fil_2 == True or fil_3 == True:
        seguir_jugando = False
        ganador = jugador_activo


def verificar_empate():
    global seguir_jugando

    if "-" not in tablero:
        seguir_jugando = False


while seguir_jugando == True:
    turno()

    verificar_filas()
    verificar_diagonales()
    verificar_columnas()

    if jugador_activo == "X":
        jugador_activo = "O"
    else:
        jugador_activo = "X"

if ganador == "X" or ganador == "O":
    print("El ganador es: " + ganador)
else:
    print("Empate")




