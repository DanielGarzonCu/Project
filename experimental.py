from Equipos.Barcelona import *
from Equipos.Real_madri import *
from Equipos.Bayern_munich import *
from Equipos.Inter_milan import *
from Equipos.Liverpool import *
from Equipos.Psg import *
from Equipos.Ac_milan import *
from Equipos.Man_city import *

def elegir_equipo(jugador: str) -> dict:
    """
    Función para elegir el equipo de fútbol.
    
    Args:
    jugador (str): El nombre del jugador que elige el equipo.
    
    Returns:
    dict: Un diccionario con la información del equipo elegido.
    """
    
    while True:
        try:
            print(f"| 1 : Barca |\n| 2: Real Madrid |\n| 3 : Bayern Munich |\n| 4 : Inter de Milan |\n| 5 : Paris Saint German |\n| 6 : Liverpool |\n| 7 : Manchester City |\n| 8 : A.C Milan")
            seleccion = int(input(f"{jugador}, ¿Cuál equipo desea escoger?: "))
            if 1 <= seleccion <= 8:
                break
            else:
                print("ERROR, escoja nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
    
    equipo_seleccionado = teams.get(seleccion)
    if equipo_seleccionado:
        print("Escudo del equipo:")
        for linea in equipo_seleccionado["escudo"]:
            print(linea)
    
    jugadores = equipo_seleccionado["jugadores"]
    ataque = equipo_seleccionado["ataque"]
    defensa = equipo_seleccionado["defensa"]
    costo = equipo_seleccionado["costo"]

    return jugadores, ataque, defensa, costo

def elegir_modo_juego() -> int:
    """
    Función para elegir el modo de juego.
    
    Returns:
    int: El número de rondas del juego.
    """
    
    while True:
        try:
            modo = int(input("Escoja un modo de juego (1, 2, 3): "))
            if 1 <= modo <= 3:
                rondas = {1: 9, 2: 12, 3: 15}[modo]
                return rondas
            else:
                print("ERROR, escoja nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")


def evaluar_columna(columnas_primer_uno : dict, columnas_segundo_uno : dict, ) -> int:
    """
    Función para evaluar una columna.
    
    Args:
    columna (int): La columna que se evaluará.
    columnas_uno (list): La lista de columnas del jugador 1.
    columnas_dos (list): La lista de columnas del jugador 2.
    goles_p1 (int): Los goles del jugador 1.
    goles_p2 (int): Los goles del jugador 2.
    
    Returns:
    int, int: Los goles del jugador 1 y del jugador 2 después de evaluar la columna.
    """
    goles_p1 : int = 0
    goles_p2 : int = 0
    actualizar_matriz = 44
    columna_evaluada = 0

    # CASOS DONDE SOLO HAY UN JUGADOR EN LAS FILAS DEL PRIMER PLAYER
    if len(columnas_primer_uno) == 1 and len(columnas_segundo_uno) == 0:
            if "fila1" in columnas_primer_uno:
                goles_p1 += ataque_jugadores_p1[columnas_primer_uno["fila1"]]
            elif "fila2" in columnas_primer_uno:
                goles_p1 += ataque_jugadores_p1[columnas_primer_uno["fila2"]]

    if len(columnas_primer_dos) == 1 and len(columnas_segundo_dos) == 0:
            if "fila1" in columnas_primer_dos:
                goles_p1 += ataque_jugadores_p1[columnas_primer_dos["fila1"]]
            elif "fila2" in columnas_primer_dos:
                goles_p1 += ataque_jugadores_p1[columnas_primer_dos["fila2"]]

    if len(columnas_primer_tres) == 1 and len(columnas_segundo_tres) == 0:
            if "fila1" in columnas_primer_tres:
                goles_p1 += ataque_jugadores_p1[columnas_primer_tres["fila1"]]
            elif "fila2" in columnas_primer_tres:
                goles_p1 += ataque_jugadores_p1[columnas_primer_tres["fila2"]]

    if len(columnas_primer_cuatro) == 1 and len(columnas_segundo_cuatro) == 0:
            if "fila1" in columnas_primer_cuatro:
                goles_p1 += ataque_jugadores_p1[columnas_primer_cuatro["fila1"]]
            elif "fila2" in columnas_primer_cuatro:
                goles_p1 += ataque_jugadores_p1[columnas_primer_cuatro["fila2"]]

    # CASOS DONDE SOLO HAY UN JUGADOR EN LAS FILAS DEL SEGUNDO PLAYER
    elif len(columnas_segundo_uno) == 1 and len(columnas_primer_uno) == 0:
            if "fila4" in columnas_segundo_uno:    
                goles_p2 += ataque_jugadores_p2[columnas_segundo_uno["fila4"]]
            elif "fila5" in columnas_segundo_uno:
                goles_p2 += ataque_jugadores_p2[columnas_segundo_uno["fila5"]]

    elif len(columnas_segundo_dos) == 1 and len(columnas_primer_dos) == 0:
            if "fila4" in columnas_segundo_dos:    
                goles_p2 += ataque_jugadores_p2[columnas_segundo_dos["fila4"]]
            elif "fila5" in columnas_segundo_dos:
                goles_p2 += ataque_jugadores_p2[columnas_segundo_dos["fila5"]]

    elif len(columnas_segundo_tres) == 1 and len(columnas_primer_tres) == 0:
            if "fila4" in columnas_segundo_tres:    
                goles_p2 += ataque_jugadores_p2[columnas_segundo_tres["fila4"]]
            elif "fila5" in columnas_segundo_tres:
                goles_p2 += ataque_jugadores_p2[columnas_segundo_tres["fila5"]]

    elif len(columnas_segundo_cuatro) == 1 and len(columnas_primer_cuatro) == 0:
            if "fila4" in columnas_segundo_cuatro:
                goles_p2 += ataque_jugadores_p2[columnas_segundo_cuatro["fila4"]]
            elif "fila5" in columnas_segundo_tres:
                goles_p2 += ataque_jugadores_p2[columnas_segundo_cuatro["fila5"]]

    # CASOS DONDE HAY DOS JUGADORES DEL PLAYER 1 EN LA COLUMNA
    elif len(columnas_primer_uno) == 2 and len(columnas_segundo_uno) == 0:
            goles_p1 += ataque_jugadores_p1[columnas_primer_uno["fila1"]] + ataque_jugadores_p1[columnas_primer_uno["fila2"]]

    elif len(columnas_primer_dos) == 2 and len(columnas_segundo_dos) == 0:
            goles_p1 += ataque_jugadores_p1[columnas_primer_dos["fila1"]] + ataque_jugadores_p1[columnas_primer_dos["fila2"]]

    elif len(columnas_primer_tres) == 2 and len(columnas_segundo_tres) == 0:
            goles_p1 += ataque_jugadores_p1[columnas_primer_tres["fila1"]] + ataque_jugadores_p1[columnas_primer_tres["fila2"]]

    elif len(columnas_primer_cuatro) == 2 and len(columnas_segundo_cuatro) == 0:
            goles_p1 += ataque_jugadores_p1[columnas_primer_cuatro["fila1"]] + ataque_jugadores_p1[columnas_primer_cuatro["fila2"]]
        

    # CASOS DONDE HAY DOS JUGADORES DEL SEGUNDO PLAYER EN LA COLUMNA
    elif len(columnas_segundo_uno) == 2 and len(columnas_primer_uno) == 0:
            goles_p2 += ataque_jugadores_p2[columnas_segundo_uno["fila4"]] + ataque_jugadores_p2[columnas_segundo_uno["fila5"]]

    elif len(columnas_segundo_dos) == 2 and len(columnas_primer_dos) == 0:
            goles_p2 += ataque_jugadores_p2[columnas_segundo_dos["fila4"]] + ataque_jugadores_p2[columnas_segundo_dos["fila5"]]

    elif len(columnas_segundo_tres) == 2 and len(columnas_primer_tres) == 0:
            goles_p2 += ataque_jugadores_p2[columnas_segundo_tres["fila4"]] + ataque_jugadores_p2[columnas_segundo_tres["fila5"]]

    elif len(columnas_segundo_cuatro) == 2 and len(columnas_primer_cuatro) == 0:
            goles_p2 += ataque_jugadores_p2[columnas_segundo_cuatro["fila4"]] + ataque_jugadores_p2[columnas_segundo_cuatro["fila5"]]   

    # CASOS DONDE HAY UN JUGADOR DE UN EQUIPO Y DOS DE OTRO EN UNA MISMA COLUMNA

    # DOS JUGADORES PLAYER 1 Y UN JUGADOR PLAYER 2 EN LA COLUMNA
    elif len(columnas_primer_uno) == 2 and len(columnas_segundo_uno) == 1:
            
            if "fila4" in columnas_segundo_uno:
                defensa_jugadores_p1[columnas_primer_uno["fila2"]] -= ataque_jugadores_p2[columnas_segundo_uno["fila4"]]
                if defensa_jugadores_p1[columnas_primer_uno["fila2"]] <=  0:
                    del columnas_primer_uno["fila2"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p2[columnas_segundo_uno["fila4"]] -= ataque_jugadores_p1[columnas_primer_uno["fila2"]]
                if defensa_jugadores_p2[columnas_segundo_uno["fila4"]] <= 0:
                    del columnas_segundo_uno["fila4"]
                    goles_p1 += ataque_jugadores_p1[columnas_primer_uno["fila1"]]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p2[columnas_segundo_uno["fila4"]] -= ataque_jugadores_p1[columnas_primer_uno["fila1"]]
                    if defensa_jugadores_p2[columnas_segundo_uno["fila4"]] <= 0:
                        del columnas_segundo_uno["fila4"]
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
            
            elif "fila5" in columnas_segundo_uno:
                defensa_jugadores_p1[columnas_primer_uno["fila2"]] -= ataque_jugadores_p2[columnas_segundo_uno["fila5"]]
                if defensa_jugadores_p1[columnas_primer_uno["fila2"]] <=  0:
                    del columnas_primer_uno["fila2"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p2[columnas_segundo_uno["fila5"]] -= ataque_jugadores_p1[columnas_primer_uno["fila2"]]
                if defensa_jugadores_p2[columnas_segundo_uno["fila5"]] <= 0:
                    del columnas_segundo_uno["fila5"]
                    goles_p1 += ataque_jugadores_p1[columnas_primer_uno["fila1"]]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p2[columnas_segundo_uno["fila5"]] -= ataque_jugadores_p1[columnas_primer_uno["fila1"]]
                    if defensa_jugadores_p2[columnas_segundo_uno["fila5"]] <= 0:
                        del columnas_segundo_uno["fila5"]
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
        
    elif len(columnas_primer_dos) == 2 and len(columnas_segundo_dos) == 1:

            if "fila4" in columnas_segundo_dos:
                defensa_jugadores_p1[columnas_primer_dos["fila2"]] -= ataque_jugadores_p2[columnas_segundo_dos["fila4"]]
                if defensa_jugadores_p1[columnas_primer_dos["fila2"]] <=  0:
                    del columnas_primer_dos["fila2"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p2[columnas_segundo_dos["fila4"]] -= ataque_jugadores_p1[columnas_primer_dos["fila2"]]
                if defensa_jugadores_p2[columnas_segundo_dos["fila4"]] <= 0:
                    del columnas_segundo_dos["fila4"]
                    goles_p1 += ataque_jugadores_p1[columnas_primer_dos["fila1"]]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p2[columnas_segundo_dos["fila4"]] -= ataque_jugadores_p1[columnas_primer_dos["fila1"]]
                    if defensa_jugadores_p2[columnas_segundo_dos["fila4"]] <= 0:
                        del columnas_segundo_dos["fila4"]
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

            elif "fila5" in columnas_segundo_dos:
                defensa_jugadores_p1[columnas_primer_dos["fila2"]] -= ataque_jugadores_p2[columnas_segundo_dos["fila5"]]
                if defensa_jugadores_p1[columnas_primer_dos["fila2"]] <=  0:
                    del columnas_primer_dos["fila2"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p2[columnas_segundo_dos["fila5"]] -= ataque_jugadores_p1[columnas_primer_dos["fila2"]]
                if defensa_jugadores_p2[columnas_segundo_dos["fila5"]] <= 0:
                    del columnas_segundo_dos["fila5"]
                    goles_p1 += ataque_jugadores_p1[columnas_primer_dos["fila1"]]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p2[columnas_segundo_dos["fila5"]] -= ataque_jugadores_p1[columnas_primer_dos["fila1"]]
                    if defensa_jugadores_p2[columnas_segundo_dos["fila5"]] <= 0:
                        del columnas_segundo_dos["fila5"]
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

    elif len(columnas_primer_tres) == 2 and len(columnas_segundo_tres) == 1:

            if "fila4" in columnas_segundo_tres:
                defensa_jugadores_p1[columnas_primer_tres["fila2"]] -= ataque_jugadores_p2[columnas_segundo_tres["fila4"]]
                if defensa_jugadores_p1[columnas_primer_tres["fila2"]] <=  0:
                    del columnas_primer_tres["fila2"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p2[columnas_segundo_tres["fila4"]] -= ataque_jugadores_p1[columnas_primer_tres["fila2"]]
                if defensa_jugadores_p2[columnas_segundo_tres["fila4"]] <= 0:
                    del columnas_segundo_tres["fila4"]
                    goles_p1 += ataque_jugadores_p1[columnas_primer_tres["fila1"]]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p2[columnas_segundo_tres["fila4"]] -= ataque_jugadores_p1[columnas_primer_tres["fila1"]]
                    if defensa_jugadores_p2[columnas_segundo_tres["fila4"]] <= 0:
                        del columnas_segundo_tres["fila4"]
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

            elif "fila5" in columnas_segundo_tres:
                defensa_jugadores_p1[columnas_primer_tres["fila2"]] -= ataque_jugadores_p2[columnas_segundo_tres["fila5"]]
                if defensa_jugadores_p1[columnas_primer_tres["fila2"]] <=  0:
                    del columnas_primer_tres["fila2"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p2[columnas_segundo_tres["fila5"]] -= ataque_jugadores_p1[columnas_primer_tres["fila2"]]
                if defensa_jugadores_p2[columnas_segundo_tres["fila5"]] <= 0:
                    del columnas_segundo_tres["fila5"]
                    goles_p1 += ataque_jugadores_p1[columnas_primer_tres["fila1"]]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p2[columnas_segundo_tres["fila5"]] -= ataque_jugadores_p1[columnas_primer_tres["fila1"]]
                    if defensa_jugadores_p2[columnas_segundo_tres["fila5"]] <= 0:
                        del columnas_segundo_tres["fila5"]
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

    elif len(columnas_primer_cuatro) == 2 and len(columnas_segundo_cuatro) == 1:

            if "fila4" in columnas_segundo_cuatro:
                defensa_jugadores_p1[columnas_primer_cuatro["fila2"]] -= ataque_jugadores_p2[columnas_segundo_cuatro["fila4"]]
                if defensa_jugadores_p1[columnas_primer_cuatro["fila2"]] <=  0:
                    del columnas_primer_cuatro["fila2"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p2[columnas_segundo_cuatro["fila4"]] -= ataque_jugadores_p1[columnas_primer_cuatro["fila2"]]
                if defensa_jugadores_p2[columnas_segundo_cuatro["fila4"]] <= 0:
                    del columnas_segundo_cuatro["fila4"]
                    goles_p1 += ataque_jugadores_p1[columnas_primer_cuatro["fila1"]]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p2[columnas_segundo_cuatro["fila4"]] -= ataque_jugadores_p1[columnas_primer_cuatro["fila1"]]
                    if defensa_jugadores_p2[columnas_segundo_cuatro["fila4"]] <= 0:
                        del columnas_segundo_cuatro["fila4"]
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

            elif "fila5" in columnas_segundo_cuatro:
                defensa_jugadores_p1[columnas_primer_cuatro["fila2"]] -= ataque_jugadores_p2[columnas_segundo_cuatro["fila5"]]
                if defensa_jugadores_p1[columnas_primer_cuatro["fila2"]] <=  0:
                    del columnas_primer_cuatro["fila2"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p2[columnas_segundo_cuatro["fila5"]] -= ataque_jugadores_p1[columnas_primer_cuatro["fila2"]]
                if defensa_jugadores_p2[columnas_segundo_cuatro["fila5"]] <= 0:
                    del columnas_segundo_cuatro["fila5"]
                    goles_p1 += ataque_jugadores_p1[columnas_primer_cuatro["fila1"]]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p2[columnas_segundo_cuatro["fila5"]] -= ataque_jugadores_p1[columnas_primer_cuatro["fila1"]]
                    if defensa_jugadores_p2[columnas_segundo_cuatro["fila5"]] <= 0:
                        del columnas_segundo_cuatro["fila5"]
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

    # DOS JUGADORES PLAYER 2 Y UN JUGADOR PLAYER 1 EN LA COLUMNA
    elif len(columnas_segundo_uno) == 2 and len(columnas_primer_uno) == 1:
            if "fila1" in columnas_primer_uno:
                defensa_jugadores_p2[columnas_segundo_uno["fila4"]] -= ataque_jugadores_p1[columnas_primer_uno["fila1"]]
                if defensa_jugadores_p2[columnas_segundo_uno["fila4"]] <= 0:
                    del columnas_segundo_uno["fila4"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p1[columnas_primer_uno["fila1"]] -= ataque_jugadores_p2[columnas_segundo_uno["fila4"]]
                if defensa_jugadores_p1[columnas_primer_uno["fila1"]] <= 0:
                    del columnas_primer_uno["fila1"]
                    goles_p2 += ataque_jugadores_p2[columnas_segundo_uno["fila5"]]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p1[columnas_primer_uno["fila1"]] -= ataque_jugadores_p2[ataque_jugadores_p2[columnas_segundo_uno["fila5"]]]
                    if defensa_jugadores_p1[columnas_primer_uno["fila1"]] <= 0:
                        del columnas_primer_uno["fila1"]
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100

            if "fila2" in columnas_primer_uno:
                defensa_jugadores_p2[columnas_segundo_uno["fila4"]] -= ataque_jugadores_p1[columnas_primer_uno["fila2"]]
                if defensa_jugadores_p2[columnas_segundo_uno["fila4"]] <= 0:
                    del columnas_segundo_uno["fila4"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p1[columnas_primer_uno["fila2"]] -= ataque_jugadores_p2[columnas_segundo_uno["fila4"]]
                if defensa_jugadores_p1[columnas_primer_uno["fila2"]] <= 0:
                    del columnas_primer_uno["fila2"]
                    goles_p2 += ataque_jugadores_p2[columnas_segundo_uno["fila5"]]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p1[columnas_primer_uno["fila2"]] -= ataque_jugadores_p2[ataque_jugadores_p2[columnas_segundo_uno["fila5"]]]
                    if defensa_jugadores_p1[columnas_primer_uno["fila2"]] <= 0:
                        del columnas_primer_uno["fila2"]
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100
        
    elif len(columnas_segundo_dos) == 2 and len(columnas_primer_dos) == 1:
            if "fila1" in columnas_primer_dos:
                defensa_jugadores_p2[columnas_segundo_dos["fila4"]] -= ataque_jugadores_p1[columnas_primer_dos["fila1"]]
                if defensa_jugadores_p2[columnas_segundo_dos["fila4"]] <= 0:
                    del columnas_segundo_dos["fila4"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p1[columnas_primer_dos["fila1"]] -= ataque_jugadores_p2[columnas_segundo_dos["fila4"]]
                if defensa_jugadores_p1[columnas_primer_dos["fila1"]] <= 0:
                    del columnas_primer_dos["fila1"]
                    goles_p2 += ataque_jugadores_p2[columnas_segundo_dos["fila5"]]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p1[columnas_primer_dos["fila1"]] -= ataque_jugadores_p2[ataque_jugadores_p2[columnas_segundo_dos["fila5"]]]
                    if defensa_jugadores_p1[columnas_primer_dos["fila1"]] <= 0:
                        del columnas_primer_dos["fila1"]
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100

            if "fila2" in columnas_primer_dos:
                defensa_jugadores_p2[columnas_segundo_dos["fila4"]] -= ataque_jugadores_p1[columnas_primer_dos["fila2"]]
                if defensa_jugadores_p2[columnas_segundo_dos["fila4"]] <= 0:
                    del columnas_segundo_dos["fila4"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p1[columnas_primer_dos["fila2"]] -= ataque_jugadores_p2[columnas_segundo_dos["fila4"]]
                if defensa_jugadores_p1[columnas_primer_dos["fila2"]] <= 0:
                    del columnas_primer_dos["fila2"]
                    goles_p2 += ataque_jugadores_p2[columnas_segundo_dos["fila5"]]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p1[columnas_primer_dos["fila2"]] -= ataque_jugadores_p2[ataque_jugadores_p2[columnas_segundo_dos["fila5"]]]
                    if defensa_jugadores_p1[columnas_primer_dos["fila2"]] <= 0:
                        del columnas_primer_dos["fila2"]
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100

    elif len(columnas_segundo_tres) == 2 and len(columnas_primer_tres) == 1:
            if "fila1" in columnas_primer_tres:
                defensa_jugadores_p2[columnas_segundo_tres["fila4"]] -= ataque_jugadores_p1[columnas_primer_tres["fila1"]]
                if defensa_jugadores_p2[columnas_segundo_tres["fila4"]] <= 0:
                    del columnas_segundo_tres["fila4"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p1[columnas_primer_tres["fila1"]] -= ataque_jugadores_p2[columnas_segundo_tres["fila4"]]
                if defensa_jugadores_p1[columnas_primer_tres["fila1"]] <= 0:
                    del columnas_primer_tres["fila1"]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p1[columnas_primer_tres["fila1"]] -= ataque_jugadores_p2[ataque_jugadores_p2[columnas_segundo_tres["fila5"]]]
                    if defensa_jugadores_p1[columnas_primer_tres["fila1"]] <= 0:
                        del columnas_primer_tres["fila1"]
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100

            elif "fila2" in columnas_primer_tres:
                defensa_jugadores_p2[columnas_segundo_tres["fila4"]] -= ataque_jugadores_p1[columnas_primer_tres["fila2"]]
                if defensa_jugadores_p2[columnas_segundo_tres["fila4"]] <= 0:
                    del columnas_segundo_tres["fila4"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p1[columnas_primer_tres["fila2"]] -= ataque_jugadores_p2[columnas_segundo_tres["fila4"]]
                if defensa_jugadores_p1[columnas_primer_tres["fila2"]] <= 0:
                    del columnas_primer_tres["fila2"]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p1[columnas_primer_tres["fila2"]] -= ataque_jugadores_p2[ataque_jugadores_p2[columnas_segundo_tres["fila5"]]]
                    if defensa_jugadores_p1[columnas_primer_tres["fila2"]] <= 0:
                        del columnas_primer_tres["fila2"]
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100
        
    elif len(columnas_segundo_cuatro) == 2 and len(columnas_primer_cuatro) == 1:

            if "fila1" in columnas_primer_cuatro:
                defensa_jugadores_p2[columnas_segundo_cuatro["fila4"]] -= ataque_jugadores_p1[columnas_primer_cuatro["fila1"]]
                if defensa_jugadores_p2[columnas_segundo_cuatro["fila4"]] <= 0:
                    del columnas_segundo_cuatro["fila4"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p1[columnas_primer_cuatro["fila1"]] -= ataque_jugadores_p2[columnas_segundo_cuatro["fila4"]]
                if defensa_jugadores_p1[columnas_primer_cuatro["fila1"]] <= 0:
                    del columnas_primer_cuatro["fila1"]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p1[columnas_primer_cuatro["fila1"]] -= ataque_jugadores_p2[ataque_jugadores_p2[columnas_segundo_cuatro["fila5"]]]
                    if defensa_jugadores_p1[columnas_primer_cuatro["fila1"]] <= 0:
                        del columnas_primer_cuatro["fila1"]
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100

            elif "fila2" in columnas_primer_cuatro:
                defensa_jugadores_p2[columnas_segundo_cuatro["fila4"]] -= ataque_jugadores_p1[columnas_primer_cuatro["fila2"]]
                if defensa_jugadores_p2[columnas_segundo_cuatro["fila4"]] <= 0:
                    del columnas_segundo_cuatro["fila4"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p1[columnas_primer_cuatro["fila2"]] -= ataque_jugadores_p2[columnas_segundo_cuatro["fila4"]]
                if defensa_jugadores_p1[columnas_primer_cuatro["fila2"]] <= 0:
                    del columnas_primer_cuatro["fila2"]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p1[columnas_primer_cuatro["fila2"]] -= ataque_jugadores_p2[ataque_jugadores_p2[columnas_segundo_cuatro["fila5"]]]
                    if defensa_jugadores_p1[columnas_primer_cuatro["fila2"]] <= 0:
                        del columnas_primer_cuatro["fila2"]
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100

    # CASOS DONDE HAY JUGADORES EN TODA LA COLUMNA  
    elif len(columnas_primer_uno) == 2 and len(columnas_segundo_uno) == 2:

            defensa_jugadores_p2[columnas_segundo_uno["fila4"]] -= ataque_jugadores_p1[columnas_primer_uno["fila2"]]
            defensa_jugadores_p1[columnas_primer_uno["fila2"]] -= ataque_jugadores_p2[columnas_segundo_uno["fila4"]]

            if defensa_jugadores_p2[columnas_segundo_uno["fila4"]] <= 0:
                del columnas_segundo_uno["fila4"]
                for i in range(actualizar_matriz):
                    matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
                defensa_jugadores_p2[columnas_segundo_uno["fila5"]] -= ataque_jugadores_p1[columnas_primer_uno["fila1"]]
                if defensa_jugadores_p2[columnas_segundo_uno["fila5"]] <= 0:
                    del columnas_segundo_uno["fila5"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 4) + i][columna_evaluada] = " " * 100

            elif defensa_jugadores_p2[columnas_segundo_uno["fila4"]] > 0:
                defensa_jugadores_p2[columnas_segundo_uno["fila4"]] -= ataque_jugadores_p1[columnas_primer_uno["fila1"]]
                if defensa_jugadores_p2[columnas_segundo_uno["fila4"]] <= 0:
                    del columnas_segundo_uno["fila4"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

            elif defensa_jugadores_p1[columnas_primer_uno["fila2"]] <= 0:
                del columnas_primer_uno["fila2"]
                for i in range(actualizar_matriz):
                    matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100
                defensa_jugadores_p1[columnas_primer_uno["fila1"]] -= ataque_jugadores_p2[columnas_segundo_uno["fila5"]]
                if defensa_jugadores_p1[columnas_primer_uno["fila1"]] <= 0:
                    del columnas_primer_uno["fila1"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100

            elif defensa_jugadores_p1[columnas_primer_uno["fila2"]] > 0:
                defensa_jugadores_p1[columnas_primer_uno["fila2"]] -= ataque_jugadores_p2[columnas_segundo_uno["fila5"]]
                if defensa_jugadores_p1[columnas_primer_uno["fila2"]] <= 0:
                    del columnas_primer_uno["fila2"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100

    elif len(columnas_primer_dos) == 2 and len(columnas_segundo_dos) == 2:

            defensa_jugadores_p2[columnas_segundo_dos["fila4"]] -= ataque_jugadores_p1[columnas_primer_dos["fila2"]]
            defensa_jugadores_p1[columnas_primer_dos["fila2"]] -= ataque_jugadores_p2[columnas_segundo_dos["fila4"]]

            if defensa_jugadores_p2[columnas_segundo_dos["fila4"]] <= 0:
                del columnas_segundo_dos["fila4"]
                for i in range(actualizar_matriz):
                    matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
                defensa_jugadores_p2[columnas_segundo_dos["fila5"]] -= ataque_jugadores_p1[columnas_primer_dos["fila1"]]
                if defensa_jugadores_p2[columnas_segundo_dos["fila5"]] <= 0:
                    del columnas_segundo_dos["fila5"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 4) + i][columna_evaluada] = " " * 100

            elif defensa_jugadores_p2[columnas_segundo_dos["fila4"]] > 0:
                defensa_jugadores_p2[columnas_segundo_dos["fila4"]] -= ataque_jugadores_p1[columnas_primer_dos["fila1"]]
                if defensa_jugadores_p2[columnas_segundo_dos["fila4"]] <= 0:
                    del columnas_segundo_dos["fila4"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

            elif defensa_jugadores_p1[columnas_primer_dos["fila2"]] <= 0:
                del columnas_primer_dos["fila2"]
                for i in range(actualizar_matriz):
                    matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100
                defensa_jugadores_p1[columnas_primer_dos["fila1"]] -= ataque_jugadores_p2[columnas_segundo_dos["fila5"]]
                if defensa_jugadores_p1[columnas_primer_dos["fila1"]] <= 0:
                    del columnas_primer_dos["fila1"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100

            elif defensa_jugadores_p1[columnas_primer_dos["fila2"]] > 0:
                defensa_jugadores_p1[columnas_primer_dos["fila2"]] -= ataque_jugadores_p2[columnas_segundo_dos["fila5"]]
                if defensa_jugadores_p1[columnas_primer_dos["fila2"]] <= 0:
                    del columnas_primer_dos["fila2"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100

    elif len(columnas_primer_tres) == 2 and len(columnas_segundo_tres) == 2:

            defensa_jugadores_p2[columnas_segundo_tres["fila4"]] -= ataque_jugadores_p1[columnas_primer_tres["fila2"]]
            defensa_jugadores_p1[columnas_primer_tres["fila2"]] -= ataque_jugadores_p2[columnas_segundo_tres["fila4"]]

            if defensa_jugadores_p2[columnas_segundo_tres["fila4"]] <= 0:
                del columnas_segundo_tres["fila4"]
                for i in range(actualizar_matriz):
                    matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
                defensa_jugadores_p2[columnas_segundo_tres["fila5"]] -= ataque_jugadores_p1[columnas_primer_tres["fila1"]]
                if defensa_jugadores_p2[columnas_segundo_tres["fila5"]] <= 0:
                    del columnas_segundo_tres["fila5"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 4) + i][columna_evaluada] = " " * 100

            elif defensa_jugadores_p2[columnas_segundo_tres["fila4"]] > 0:
                defensa_jugadores_p2[columnas_segundo_tres["fila4"]] -= ataque_jugadores_p1[columnas_primer_tres["fila1"]]
                if defensa_jugadores_p2[columnas_segundo_tres["fila4"]] <= 0:
                    del columnas_segundo_tres["fila4"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

            elif defensa_jugadores_p1[columnas_primer_tres["fila2"]] <= 0:
                del columnas_primer_tres["fila2"]
                for i in range(actualizar_matriz):
                    matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100
                defensa_jugadores_p1[columnas_primer_tres["fila1"]] -= ataque_jugadores_p2[columnas_segundo_tres["fila5"]]
                if defensa_jugadores_p1[columnas_primer_tres["fila1"]] <= 0:
                    del columnas_primer_tres["fila1"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100

            elif defensa_jugadores_p1[columnas_primer_tres["fila2"]] > 0:
                defensa_jugadores_p1[columnas_primer_tres["fila2"]] -= ataque_jugadores_p2[columnas_segundo_tres["fila5"]]
                if defensa_jugadores_p1[columnas_primer_tres["fila2"]] <= 0:
                    del columnas_primer_tres["fila2"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100

    elif len(columnas_primer_cuatro) == 2 and len(columnas_segundo_cuatro) == 2:

            defensa_jugadores_p2[columnas_segundo_cuatro["fila4"]] -= ataque_jugadores_p1[columnas_primer_cuatro["fila2"]]
            defensa_jugadores_p1[columnas_primer_cuatro["fila2"]] -= ataque_jugadores_p2[columnas_segundo_cuatro["fila4"]]

            if defensa_jugadores_p2[columnas_segundo_cuatro["fila4"]] <= 0:
                del columnas_segundo_cuatro["fila4"]
                for i in range(actualizar_matriz):
                    matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
                defensa_jugadores_p2[columnas_segundo_cuatro["fila5"]] -= ataque_jugadores_p1[columnas_primer_cuatro["fila1"]]
                if defensa_jugadores_p2[columnas_segundo_cuatro["fila5"]] <= 0:
                    del columnas_segundo_cuatro["fila5"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 4) + i][columna_evaluada] = " " * 100
                        
            if defensa_jugadores_p2[columnas_segundo_cuatro["fila4"]] > 0:
                defensa_jugadores_p2[columnas_segundo_cuatro["fila4"]] -= ataque_jugadores_p1[columnas_primer_cuatro["fila1"]]
                if defensa_jugadores_p2[columnas_segundo_cuatro["fila4"]] <= 0:
                    del columnas_segundo_cuatro["fila4"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

            if defensa_jugadores_p1[columnas_primer_cuatro["fila2"]] <= 0:
                del columnas_primer_cuatro["fila2"]
                for i in range(actualizar_matriz):
                    matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100
                defensa_jugadores_p1[columnas_primer_cuatro["fila1"]] -= ataque_jugadores_p2[columnas_segundo_cuatro["fila5"]]
                if defensa_jugadores_p1[columnas_primer_cuatro["fila1"]] <= 0:
                    del columnas_primer_cuatro["fila1"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100

            if defensa_jugadores_p1[columnas_primer_cuatro["fila2"]] > 0:
                defensa_jugadores_p1[columnas_primer_cuatro["fila2"]] -= ataque_jugadores_p2[columnas_segundo_cuatro["fila5"]]
                if defensa_jugadores_p1[columnas_primer_cuatro["fila2"]] <= 0:
                    del columnas_primer_cuatro["fila2"]
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100

    return goles_p1, goles_p2

# Bucle de juego por rondas
if __name__ == "__main__":
    
    teams = {
        1: barcelona,
        2: real_madrid,
        3: bayern,
        4: inter,
        5: psg,
        6: liverpool,
        7: city,
        8: milan 
    }

    jugadores_p1, ataque_jugadores_p1, defensa_jugadores_p1, costo_jugadores_p1 = elegir_equipo("Jugador 1")
    jugadores_p2, ataque_jugadores_p2, defensa_jugadores_p2, costo_jugadores_p2 = elegir_equipo("Jugador 2")
    rondas_totales = elegir_modo_juego()
    goles = evaluar_columna()
    
    columnas_primer_uno = {}
    columnas_primer_dos = {}
    columnas_primer_tres = {}
    columnas_primer_cuatro = {}
    
    columnas_segundo_uno = {}
    columnas_segundo_dos = {}
    columnas_segundo_tres = {}
    columnas_segundo_cuatro = {}

    goles_primer_jugador : int = 0
    goles_segundo_jugador : int = 0

    matriz_visual = [[" " * 100 for _ in range(5)] for _ in range(226)]
    talentos_jugador_1 : int = 1
    talentos_jugador_2 : int = 1
    ronda = 1
    while ronda <= rondas_totales:
        ronda : int = 1
        print(f"--- Ronda {ronda} ---")
        # Turno del jugador 1
        print("--- Turno del primer jugador ---")
        print(f"-- GOLES P1-- {goles_primer_jugador}")
        print(f"-- GOLES P2-- {goles_segundo_jugador}")
        print(f"-- CREDITOS -- {talentos_jugador_1}")
        numero_jugador_escogido = 100
        while numero_jugador_escogido != 0:
            try:
                numero_jugador_escogido = int(input("Jugador 1, ingresa el dorsal del jugador (0 para continuar): "))
                if numero_jugador_escogido == 0:
                    break
                if numero_jugador_escogido not in jugadores_p1:
                    print("Dorsal inválido, intenta de nuevo.")
                    continue
                
                if talentos_jugador_1 >= costo_jugadores_p1[numero_jugador_escogido]:
                    jugador_escogido = jugadores_p1[numero_jugador_escogido]
                    talentos_jugador_1 -= costo_jugadores_p1[numero_jugador_escogido]
                else:
                    print("No tienes suficientes talentos. Elige otro jugador.")
                    continue
            except ValueError:
                print("Entrada inválida. Debe ser un número.")

            # Solicitar fila y columna
            try:
                fila_p1 = int(input("En qué fila (1-2): "))
                while fila_p1 not in [1, 2]:
                    fila_p1 = int(input("ERROR, ingrese una fila válida (1-2): "))

                columna_p1 = int(input("En qué columna (1-4): "))
                while columna_p1 not in [1, 2, 3, 4]:
                    columna_p1 = int(input("ERROR, ingrese una columna válida (1-4): "))

                
                if fila_p1 == 1 and columna_p1 == 1:
                    columnas_primer_uno["fila1"] = [numero_jugador_escogido]
                elif fila_p1 == 2 and columna_p1 == 1:
                    columnas_primer_uno["fila2"] = [numero_jugador_escogido]
                elif fila_p1 == 1 and columna_p1 == 2:
                    columnas_primer_dos["fila1"] = [numero_jugador_escogido]
                elif fila_p1 == 2 and columna_p1 == 2:
                    columnas_primer_dos["fila2"] = [numero_jugador_escogido]
                elif fila_p1 == 1 and columna_p1 == 3:
                    columnas_primer_tres["fila1"] = [numero_jugador_escogido]
                elif fila_p1 == 2 and columna_p1 == 3:
                    columnas_primer_tres["fila2"] = [numero_jugador_escogido]
                elif fila_p1 == 1 and columna_p1 == 4:
                    columnas_primer_cuatro["fila1"] = [numero_jugador_escogido]
                elif fila_p1 == 2 and columna_p1 == 4:
                    columnas_primer_cuatro["fila2"] = [numero_jugador_escogido]
        
            except ValueError:
                print("Entrada inválida. Deben ser números.")

            filas_p1 = (fila_p1 - 1) * 44

            for i in range(len(jugador_escogido)):
                if filas_p1 + i < len(matriz_visual):
                    matriz_visual[filas_p1 + i][columna_p1] = jugador_escogido[i]

            for r in matriz_visual:
                print("".join(r))

        # Turno del jugador 2
        print("--- Turno del segundo jugador ---")
        print(f"-- GOLES P1-- {goles_primer_jugador}")
        print(f"-- GOLES P2-- {goles_segundo_jugador}")
        print(f"-- CREDITOS -- {talentos_jugador_2}")
        numero_segundo_escogido = 100
        while numero_segundo_escogido != 0:
            try:
                numero_segundo_escogido = int(input("Jugador 2, ingresa el dorsal del jugador (0 para continuar): "))
                if numero_segundo_escogido == 0:
                    break
                if numero_segundo_escogido not in jugadores_p2:
                    print("Dorsal inválido, intenta de nuevo.")
                    continue
                
                if talentos_jugador_2 >= costo_jugadores_p2[numero_segundo_escogido]:
                    segundo_escogido = jugadores_p2[numero_segundo_escogido]
                    talentos_jugador_2 -= costo_jugadores_p2[numero_segundo_escogido]
                else:
                    print("No tienes suficientes talentos. Elige otro jugador.")
                    continue
            except ValueError:
                print("Entrada inválida. Debe ser un número.")

            # Solicitar fila y columna
            try:
                fila_p2 = int(input("En qué fila (4-5): "))
                while fila_p2 not in [4, 5]:
                    fila_p2 = int(input("ERROR, ingrese una fila válida (4-5): "))

                columna_p2 = int(input("En qué columna (1-4): "))
                while columna_p2 not in [1, 2, 3, 4]:
                    columna_p2 = int(input("ERROR, ingrese una columna válida (1-4): "))



                if fila_p2 == 4 and columna_p2 == 1:
                    columnas_segundo_uno["fila4"] = [numero_segundo_escogido]
                elif fila_p2 == 5 and columna_p2 == 1:
                    columnas_segundo_uno["fila5"] = [numero_segundo_escogido]
                elif fila_p2 == 4 and columna_p2 == 2:
                    columnas_segundo_dos["fila4"] = [numero_segundo_escogido]
                elif fila_p2 == 5 and columna_p2 == 2:
                    columnas_segundo_dos["fila5"] = [numero_segundo_escogido]
                elif fila_p2 == 4 and columna_p2 == 3:
                    columnas_segundo_tres["fila4"] = [numero_segundo_escogido]
                elif fila_p2 == 5 and columna_p2 == 3:
                    columnas_segundo_tres["fila5"] = [numero_segundo_escogido]
                elif fila_p2 == 4 and columna_p2 == 4:
                    columnas_segundo_cuatro["fila4"] = [numero_segundo_escogido]
                elif fila_p2 == 5 and columna_p2 == 4:
                    columnas_segundo_cuatro["fila5"] = [numero_segundo_escogido]

            except ValueError:
                print("Entrada inválida. Deben ser números.")

            filas_p2 = (fila_p2 - 1) * 44

            for i in range(len(segundo_escogido)):
                if filas_p2 + i < len(matriz_visual):
                    matriz_visual[filas_p2 + i][columna_p2] = segundo_escogido[i]

            for r in matriz_visual:
                print("".join(r))

        ronda += 1
        talentos_jugador_1 += ronda
        talentos_jugador_2 += ronda

        goles_primer_jugador, goles_segundo_jugador = goles
        for r in matriz_visual:
            print("".join(r))
