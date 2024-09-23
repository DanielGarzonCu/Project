from Equipos.Barcelona import *
from Equipos.Real_madri import *

teams = {
    1: barcelona,
    2: real_madrid
}

def elegir_equipo(jugador: str) -> dict:
    while True:
        try:
            print(f"| 1 : Barca |\n| 2: Real Madrid |")
            seleccion = int(input(f"{jugador}, ¿Cuál equipo desea escoger?: "))
            if 1 <= seleccion <= 2:
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

def insertar_en_columnas(fila, columna, numero_jugador, columnas):
    if fila == 1:
        columnas[columna - 1].insert(0, numero_jugador)
    elif fila == 2:
        columnas[columna - 1].insert(-1, numero_jugador)

def evaluar_columna(columna, columnas_uno, columnas_dos, goles_p1, goles_p2):
    if len(columnas_uno[columna]) == 1 and len(columnas_dos[columna]) == 0:
        goles_p1 += ataque_jugadores_p1[columnas_uno[columna][0]]

    elif len(columnas_dos[columna]) == 1 and len(columnas_uno[columna]) == 0:
        goles_p2 += ataque_jugadores_p2[columnas_dos[columna][0]]

    elif len(columnas_uno[columna]) == 2 and len(columnas_dos[columna]) == 0:
        goles_p1 += (ataque_jugadores_p1[columnas_uno[columna][0]] +  ataque_jugadores_p1[columnas_uno[columna][1]])

    elif len(columnas_dos[columna]) == 2 and len(columnas_uno[columna]) == 0:
        goles_p2 += (ataque_jugadores_p2[columnas_dos[columna][0]] + ataque_jugadores_p2[columnas_dos[columna][1]])

    # Evaluación en caso de que ambos jugadores estén en la misma columna
    elif len(columnas_uno[columna]) == 2 and len(columnas_dos[columna]) == 1:
    # Ajustar las defensas y ataques
        defensa_jugadores_p1[columnas_uno[columna][1]] -= ataque_jugadores_p2[columnas_dos[columna][0]]
        defensa_jugadores_p2[columnas_dos[columna][0]] -= ataque_jugadores_p1[columnas_uno[columna][1]]

    # Si el jugador 1 pierde defensa
        if defensa_jugadores_p1[columnas_uno[columna][1]] <= 0:
            for i in range(44):
                matriz_visual[44 + i][columna] = " " * 100

        # Si el jugador 2 pierde defensa
        if defensa_jugadores_p2[columnas_dos[columna][0]] <= 0:
            goles_p1 += ataque_jugadores_p1[columnas_uno[columna][0]]
            for i in range(88):
                matriz_visual[132 + i][columna] = " " * 100
    # elif len(columnas_uno[columna]) == 2 and len(columnas_dos[columna]) == 2:

    return goles_p1, goles_p2

if __name__ == "__main__":

    columnas_uno = [[], [], [], []]
    columnas_dos = [[], [], [], []]
    goles_p1 = 0
    goles_p2 = 0
    columna = 1
    goles_primer_jugador, goles_segundo_jugador = evaluar_columna(columna, columnas_uno, columnas_dos, goles_p1, goles_p2)
    jugadores_p1, ataque_jugadores_p1, defensa_jugadores_p1, costo_jugadores_p1 = elegir_equipo("Jugador 1")
    jugadores_p2, ataque_jugadores_p2, defensa_jugadores_p2, costo_jugadores_p2 = elegir_equipo("Jugador 2")
    rondas_totales = elegir_modo_juego() 
    ronda = 1

    talentos_jugador_1 = 1
    talentos_jugador_2 = 1

    matriz_visual = [[" " * 100 for _ in range(5)] for _ in range(226)]

    while ronda <= rondas_totales:
        print(f"--- Ronda {ronda} ---")
        print("--- Turno del primer jugador ---")
        print(f"-- GOLES -- {goles_primer_jugador}")
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

            try:
                fila_p1 = int(input("En qué fila (1-2): "))
                while fila_p1 not in [1, 2]:
                    fila_p1 = int(input("ERROR, ingrese una fila válida (1-2): "))

                columna_p1 = int(input("En qué columna (1-4): "))
                while columna_p1 not in [1, 2, 3, 4]:
                    columna_p1 = int(input("ERROR, ingrese una columna válida (1-4): "))
            except ValueError:
                print("Entrada inválida. Deben ser números.")

            filas_p1 = (fila_p1 - 1) * 44

            for i in range(len(jugador_escogido)):
                if filas_p1 + i < len(matriz_visual):
                    matriz_visual[filas_p1 + i][columna_p1] = jugador_escogido[i]

            for r in matriz_visual:
                print("".join(r))

        print("--- Turno del segundo jugador ---")
        print(f"-- GOLES -- {goles_segundo_jugador}")
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

            try:
                fila_p2 = int(input("En qué fila (4-5): "))
                while fila_p2 not in [4, 5]:
                    fila_p2 = int(input("ERROR, ingrese una fila válida (4-5): "))

                columna_p2 = int(input("En qué columna (1-4): "))
                while columna_p2 not in [1, 2, 3, 4]:
                    columna_p2 = int(input("ERROR, ingrese una columna válida (1-4): "))
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
        for r in matriz_visual:
            print("".join(r))
