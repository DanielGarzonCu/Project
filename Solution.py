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


def evaluar_columna(fila_p1, columna_p1, fila_p2, columna_p2, numero_jugador_escogido, numero_segundo_escogido) -> int:
    """
    Función optimizada para evaluar una columna de juego.

    Args:
    fila_p1, columna_p1, fila_p2, columna_p2 (int): Posiciones del jugador 1 y jugador 2 en la matriz.
    numero_jugador_escogido, numero_segundo_escogido (int): Números de jugadores seleccionados.

    Returns:
    int: Goles del jugador 1 y goles del jugador 2.
    """
    
    # Diccionario para las columnas de ambos jugadores
    columnas_p1 = {1: {}, 2: {}, 3: {}, 4: {}}
    columnas_p2 = {1: {}, 2: {}, 3: {}, 4: {}}

    # Función auxiliar para asignar jugadores a una columna
    def asignar_jugador(fila, columna, jugador, columnas):
        if fila not in columnas[columna]:
            columnas[columna][f"fila{fila}"] = [jugador]
        else:
            columnas[columna][f"fila{fila}"].append(jugador)

    # Asignación de jugadores del jugador 1 y jugador 2
    asignar_jugador(fila_p1, columna_p1, numero_jugador_escogido, columnas_p1)
    asignar_jugador(fila_p2, columna_p2, numero_segundo_escogido, columnas_p2)

    goles_p1 = goles_p2 = 0

    # Función auxiliar para calcular goles basado en las posiciones de los jugadores
    def calcular_goles(columnas_jugador, ataque_jugadores, defensa_jugadores, columnas_rival, goles):
        for columna, filas in columnas_jugador.items():
            for fila, jugadores in filas.items():
                if columna in columnas_rival and fila in columnas_rival[columna]:
                    # Lógica de ataque y defensa entre jugador 1 y jugador 2
                    for jugador in jugadores:
                        defensa_rival = defensa_jugadores[jugador]
                        ataque_rival = ataque_jugadores[jugador]
                        defensa_rival -= ataque_rival
                        if defensa_rival <= 0:
                            goles += ataque_rival
                else:
                    # Solo el jugador 1 está en la columna
                    for jugador in jugadores:
                        goles += ataque_jugadores[jugador]
        return goles

    # Calcular goles de ambos jugadores
    goles_p1 = calcular_goles(columnas_p1, ataque_jugadores_p1, defensa_jugadores_p2, columnas_p2, goles_p1)
    goles_p2 = calcular_goles(columnas_p2, ataque_jugadores_p2, defensa_jugadores_p1, columnas_p1, goles_p2)

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
        7: milan,
        8: city
    }

    jugadores_p1, ataque_jugadores_p1, defensa_jugadores_p1, costo_jugadores_p1 = elegir_equipo("Jugador 1")
    jugadores_p2, ataque_jugadores_p2, defensa_jugadores_p2, costo_jugadores_p2 = elegir_equipo("Jugador 2")
    rondas_totales = elegir_modo_juego()
    goles_primer_jugador, goles_segundo_jugador = evaluar_columna()

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
            except ValueError:
                print("Entrada inválida. Deben ser números.")

            filas_p2 = (fila_p2 - 1) * 44

            for i in range(len(segundo_escogido)):
                if filas_p2 + i < len(matriz_visual):
                    matriz_visual[filas_p2 + i][columna_p2] = segundo_escogido[i]

            for r in matriz_visual:
                print("".join(r))

                goles_primer_jugador, goles_segundo_jugador = evaluar_columna(fila_p1, fila_p2, columna_p1, columna_p2, numero_jugador_escogido, numero_segundo_escogido)
        ronda += 1
        talentos_jugador_1 += ronda
        talentos_jugador_2 += ronda

    for r in matriz_visual:
        print("".join(r))
