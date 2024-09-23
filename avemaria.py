from Equipos.Barcelona import *
from Equipos.Real_madri import *
from Equipos.Ac_milan import *
from Equipos.Bayern_munich import *
from Equipos.Inter_milan import *
from Equipos.Liverpool import *
from Equipos.Man_city import *
from Equipos.Psg import *


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
            print(f"| 1 : Barca |\n| 2: Real Madrid |\n| 3 : Bayern Munich |\n| 4 : Inter de Milan |\n| 5 : Paris Saint German |\n| 6 : Liverpool |\n| 7 : A.C Milan |\n| 8 : Manchester City |")
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

'''
def evaluar_columna(fila_p1, columna_p1, fila_p2, columna_p2, numero_jugador_escogido, numero_segundo_escogido) -> int:
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

    return goles_p1, goles_p2
'''
# Bucle de juego por rondas
if __name__ == "__main__":
    
    teams = {
        1: barcelona,
        2: real_madrid,
        3: bayern,
        4: inter,
        5: psg,
        6: liverpool,
        7: milan,
        8: city
    }


    columnas_uno = [[], [], [], []]
    columnas_dos = [[], [], [], []]

    jugadores_p1, ataque_jugadores_p1, defensa_jugadores_p1, costo_jugadores_p1 = elegir_equipo("Jugador 1")
    jugadores_p2, ataque_jugadores_p2, defensa_jugadores_p2, costo_jugadores_p2 = elegir_equipo("Jugador 2")
    rondas_totales = elegir_modo_juego()
    # goles_primer_jugador, goles_segundo_jugador = evaluar_columna(jugadores_p1, ataque_jugadores_p1, defensa_jugadores_p1, jugadores_p2, ataque_jugadores_p2, defensa_jugadores_p2)

    matriz_visual = [[" " * 100 for _ in range(5)] for _ in range(226)]
    talentos_jugador_1 : int = 1
    talentos_jugador_2 : int = 1
    ronda : int = 1
    goles_p1 : int = 0
    goles_p2 : int = 0
    while ronda <= rondas_totales:

        print(f"--- Ronda {ronda} ---")
        # Turno del jugador 1
        print("--- Turno del primer jugador ---")
        print(f"-- GOLES P1-- {goles_p1}")
        print(f"-- GOLES P2-- {goles_p2}")
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
            except ValueError:
                print("Entrada inválida. Deben ser números.")

                if fila_p1 == 1 and columna_p1 == 1:
                    columnas_uno[0].insert(0, numero_jugador_escogido)
                elif fila_p1 == 2 and columna_p1 == 1:
                    columnas_uno[0].insert(-1, numero_jugador_escogido)
                elif fila_p1 == 1 and columna_p1 == 2:
                    columnas_uno[1].insert(0, numero_jugador_escogido)
                elif fila_p1 == 2 and columna_p1 == 2:
                    columnas_uno[1].insert(-1, numero_jugador_escogido)
                elif fila_p1 == 1 and columna_p1 == 3:
                    columnas_uno[2].insert(0, numero_jugador_escogido)
                elif fila_p1 == 2 and columna_p1 == 3:
                    columnas_uno[2].insert(-1, numero_jugador_escogido)
                elif fila_p1 == 1 and columna_p1 == 4:
                    columnas_uno[3].insert(0, numero_jugador_escogido)
                elif fila_p1 == 2 and columna_p1 == 4:
                    columnas_uno[3].insert(-1, numero_jugador_escogido)
        
            filas_p1 = (fila_p1 - 1) * 44

            for i in range(len(jugador_escogido)):
                if filas_p1 + i < len(matriz_visual):
                    matriz_visual[filas_p1 + i][columna_p1] = jugador_escogido[i]

            for r in matriz_visual:
                print("".join(r))

        # Turno del jugador 2
        print("--- Turno del segundo jugador ---")
        print(f"-- GOLES P1-- {goles_p1}")
        print(f"-- GOLES P2-- {goles_p2}")
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
            except ValueError:
                print("Entrada inválida. Deben ser números.")

                if fila_p2 == 4 and columna_p2 == 1:
                    columnas_dos[0].insert(0, numero_segundo_escogido)
                elif fila_p2 == 5 and columna_p2 == 1:
                    columnas_dos[0].insert(-1, numero_segundo_escogido)
                elif fila_p2 == 4 and columna_p2 == 2:
                    columnas_dos[1].insert(0, numero_segundo_escogido)
                elif fila_p2 == 5 and columna_p2 == 2:
                    columnas_dos[1].insert(-1, numero_segundo_escogido)
                elif fila_p2 == 4 and columna_p2 == 3:
                    columnas_dos[2].insert(0, numero_segundo_escogido)
                elif fila_p2 == 5 and columna_p2 == 3:
                    columnas_dos[2].insert(-1, numero_segundo_escogido)
                elif fila_p2 == 4 and columna_p2 == 4:
                    columnas_dos[3].insert(0, numero_segundo_escogido)
                elif fila_p2 == 5 and columna_p2 == 4:
                    columnas_dos[3].insert(-1, numero_segundo_escogido)

            filas_p2 = (fila_p2 - 1) * 44

            for i in range(len(segundo_escogido)):
                if filas_p2 + i < len(matriz_visual):
                    matriz_visual[filas_p2 + i][columna_p2] = segundo_escogido[i]

            for r in matriz_visual:
                print("".join(r))

        actualizar_matriz = 44
        columna_evaluada = 0
        while columna_evaluada < 4 and not 0 == columnas_uno[0] == columnas_uno[1] == columnas_uno[2] == columnas_uno[3] == columnas_dos[0] == columnas_dos[1] == columnas_dos[2] == columnas_dos[3]:
        
            # Casos donde solo hay un jugador en la columna
            if len(columnas_uno[columna_evaluada]) == 1 and len(columnas_dos[columna_evaluada]) == 0:
                goles_p1 += ataque_jugadores_p1[columnas_uno[columna_evaluada][0]]

            elif len(columnas_dos[columna_evaluada]) == 1 and len(columnas_uno[columna_evaluada]) == 0:
                goles_p2 += ataque_jugadores_p2[columnas_dos[columna_evaluada][0]]

            # Casos donde hay dos jugadores del miso equipo en una columna
            elif len(columnas_uno[columna_evaluada]) == 2 and len(columnas_dos[columna_evaluada]) == 0:
                goles_p1 += ataque_jugadores_p1[columnas_uno[columna_evaluada][0]] + ataque_jugadores_p1[columnas_uno[columna_evaluada[1]]]

            elif len(columnas_dos[columna_evaluada]) == 2 and len(columnas_uno[columna_evaluada]) == 0:
                goles_p2 += ataque_jugadores_p2[columnas_dos[columna_evaluada][0]] + ataque_jugadores_p2[columnas_dos[columna_evaluada[1]]]


        # CASOS DONDE HAY UN JUGADOR DE UN EQUIPO Y DOS DE OTRO EN UNA MISMA COLUMNA

        # Dos jugadores del primer equipo y uno del segundo equipo
            elif len(columnas_uno[columna_evaluada]) == 2 and len(columnas_dos[columna_evaluada]) == 1:
            
                defensa_jugadores_p1[columnas_uno[columna_evaluada][1]] -= ataque_jugadores_p2[columnas_dos[columna_evaluada][0]]
                if defensa_jugadores_p1[columnas_uno[columna_evaluada][1]] <=  0:
                    columnas_uno[columna_evaluada].pop(1)
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p2[columnas_dos[columna_evaluada][0]] -= ataque_jugadores_p1[columnas_uno[columna_evaluada][1]]
                if defensa_jugadores_p2[columnas_dos[columna_evaluada][0]] <= 0:
                    columnas_dos[columna_evaluada].pop(0)
                    goles_p1 += ataque_jugadores_p1[columnas_uno[columna_evaluada][0]]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p2[columnas_dos[columna_evaluada][0]] -= ataque_jugadores_p1[columnas_uno[columna_evaluada][0]]
                    if defensa_jugadores_p2[columnas_dos[columna_evaluada][0]] <= 0:
                        columnas_dos[columna_evaluada].pop(0)
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

        # Dos jugadores del segundo equipo y uno del primer equipo
            elif len(columnas_dos[columna_evaluada]) == 2 and len(columnas_uno[columna_evaluada]) == 1:
                defensa_jugadores_p2[columnas_dos[columna_evaluada][0]] -= ataque_jugadores_p1[columnas_uno[columna_evaluada][0]]
                if defensa_jugadores_p2[columnas_dos[columna_evaluada][0]] <= 0:
                    columnas_dos[columna_evaluada].pop(0)
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

                defensa_jugadores_p1[columnas_uno[columna_evaluada][0]] -= ataque_jugadores_p2[columnas_dos[columna_evaluada][0]]
                if defensa_jugadores_p1[columnas_uno[columna_evaluada][0]] <= 0:
                    columnas_uno[columna_evaluada].pop(0)
                    goles_p2 += ataque_jugadores_p2[columnas_dos[columna_evaluada][1]]
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100
                else:
                    defensa_jugadores_p1[columnas_uno[columna_evaluada][0]] -= ataque_jugadores_p2[columnas_dos[columna_evaluada][1]]
                    if defensa_jugadores_p1[columnas_uno[columna_evaluada][0]] <= 0:
                        columnas_uno[columna_evaluada].pop(0)
                        for i in range(actualizar_matriz * 2):
                            matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100


            # CASOS DONDE HAY JUGADORES EN TODA LA COLUMNA  
            elif len(columnas_uno[columna_evaluada]) == 2 and len(columnas_dos[columna_evaluada]) == 2:

                defensa_jugadores_p2[columnas_dos[columna_evaluada][0]] -= ataque_jugadores_p1[columnas_uno[columna_evaluada][1]]
                defensa_jugadores_p1[columnas_uno[columna_evaluada][1]] -= ataque_jugadores_p2[columnas_dos[columna_evaluada][0]]

                if defensa_jugadores_p2[columnas_dos[columna_evaluada][0]] <= 0:
                    columnas_dos[columna_evaluada].pop(0)
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
                    defensa_jugadores_p2[columnas_dos[columna_evaluada][1]] -= ataque_jugadores_p1[columnas_uno[columna_evaluada][0]]
                    if defensa_jugadores_p2[columnas_dos[columna_evaluada][1]] <= 0:
                        columnas_dos[columna_evaluada].pop(1)
                        for i in range(actualizar_matriz):
                            matriz_visual[(actualizar_matriz * 4) + i][columna_evaluada] = " " * 100

                elif defensa_jugadores_p2[columnas_dos[columna_evaluada][0]] > 0:
                    defensa_jugadores_p2[columnas_dos[columna_evaluada][0]] -= ataque_jugadores_p1[columnas_uno[columna_evaluada][0]]
                    if defensa_jugadores_p2[columnas_dos[columna_evaluada][0]] <= 0:
                        columnas_dos[columna_evaluada].pop(0)
                        for i in range(actualizar_matriz):
                            matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

                elif defensa_jugadores_p1[columnas_uno[columna_evaluada][1]] <= 0:
                    columnas_uno[columna_evaluada].pop(1)
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100
                    defensa_jugadores_p1[columnas_uno[columna_evaluada][0]] -= ataque_jugadores_p2[columnas_dos[columna_evaluada][1]]
                    if defensa_jugadores_p1[columnas_uno[columna_evaluada][0]] <= 0:
                        columnas_uno[columna_evaluada].pop(0)
                        for i in range(actualizar_matriz):
                            matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100

                elif defensa_jugadores_p1[columnas_uno[columna_evaluada][1]] > 0:
                    defensa_jugadores_p1[columnas_uno[columna_evaluada][1]] -= ataque_jugadores_p2[columnas_dos[columna_evaluada][1]]
                    if defensa_jugadores_p1[columnas_uno[columna_evaluada][1]] <= 0:
                        columnas_uno[columna_evaluada].pop(1)
                        for i in range(actualizar_matriz):
                            matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100

        columna_evaluada += 1

        # goles_primer_jugador, goles_segundo_jugador = evaluar_columna(fila_p1, fila_p2, columna_p1, columna_p2, numero_jugador_escogido, numero_segundo_escogido)
        ronda += 1
        talentos_jugador_1 += ronda
        talentos_jugador_2 += ronda

        for r in matriz_visual:
            print("".join(r))
