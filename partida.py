from Equipos.Barcelona import *
from Equipos.Real_madri import *

teams = {
    1: barcelona,
    2: real_madrid
}

print("| 1 : Barca |\n| 2: Real Madrid |")
seleccion_jugador_uno = int(input("¿Cuál equipo desea escoger?: "))
while not seleccion_jugador_uno >= 1 and seleccion_jugador_uno <= 2:
    seleccion_jugador_uno = int(input("ERROR, escoga nuevamente: "))
equipo_jugador_uno = teams.get(seleccion_jugador_uno)
if equipo_jugador_uno:
    for linea in equipo_jugador_uno["escudo"]:
        print(linea)

print("| 1 : Barca |\n| 2: Real Madrid |")
seleccion_jugador_dos = int(input("¿Cuál equipo desea escoger?: "))
while not seleccion_jugador_dos >= 1 and seleccion_jugador_dos <= 2:
    seleccion_jugador_dos = int(input("ERROR, escoga nuevamente: "))
equipo_jugador_dos = teams.get(seleccion_jugador_dos)
if equipo_jugador_dos:
    for linea in equipo_jugador_dos["escudo"]:
        print(linea)

# Diccionario de jugadores

jugadores_p1 = equipo_jugador_uno["jugadores"]
ataque_jugadores_p1 = equipo_jugador_uno["ataque"]
defensa_jugadores_p1 = equipo_jugador_uno["defensa"]
costo_jugadores_p1 = equipo_jugador_uno["costo"]

jugadores_p2 = equipo_jugador_dos["jugadores"]
ataque_jugadores_p2 = equipo_jugador_dos["ataque"]
defensa_jugadores_p2 = equipo_jugador_dos["defensa"]
costo_jugadores_p2 = equipo_jugador_dos["costo"]

# Crear una línea vacía para la matriz visual
Linea_vacia = " " * 100 
# Crear la matriz visual correctamente como una lista de listas
matriz_visual = [[Linea_vacia for _ in range(5)] for _ in range(226)]

# Lógica de manejo del juego
ronda = 1
talentos_primer_jugador = 1
talentos_segundo_jugador = 1

# Solicitar el modo de juego
modo_escogido = int(input("Escoga un modo de juego 1, 2, 3: "))
while not modo_escogido >= 1 and modo_escogido <= 3:
    modo_escogido = int(input("ERROR, escoga nuevamente: "))

# Determinar la cantidad de rondas según el modo de juego
if modo_escogido == 1:
    ronda_escogida = 9
elif modo_escogido == 2:
    ronda_escogida = 12
elif modo_escogido == 3:
    ronda_escogida = 15


goles_primer_jugador : int = 0
goles_segundo_jugador : int = 0

# Bucle de juego por rondas
while ronda <= ronda_escogida:

    columnas_jugador_uno = [[], [], [], []]
    columnas_jugador_dos = [[], [], [], []]

    print(f"--- Ronda {ronda} ---")

    # Turno del primer jugador

    print("--- Turno del primer jugador ---")
    numero_jugador_escogido = 100
    while not numero_jugador_escogido != 0:

        numero_jugador_escogido = int(input("Ingrese el número del dorsal del jugador, ingresa 0 para continuar: "))
        while not numero_jugador_escogido in jugadores_p1:
            numero_jugador_escogido = int(input("ERROR, ingrese un dorsal válido o iingresa 0 para continuar: "))

        # Validación de costos y talentos para el primer jugador
        while not talentos_primer_jugador >= costo_jugadores_p1[numero_jugador_escogido]:
            numero_jugador_escogido = int(input("No tienes suficientes talentos, ingresa el dorsal de otro jugador, ingresa 0 para continuar: "))
        jugador_escogido = jugadores_p1.get(numero_jugador_escogido)
        talentos_primer_jugador -= costo_jugadores_p1[numero_jugador_escogido]

        # Solicitar fila y columna para el primer jugador
        fila_p1 = int(input("En qué fila (1-2): "))
        while fila_p1 not in [1, 2]:
            fila_p1 = int(input("ERROR, ingrese una fila válida: "))
        filas_p1 = (fila_p1 - 1) * 44
        columna_p1 = int(input("En qué columna (1-4): "))
        while columna_p1 not in [1, 2, 3, 4]:
            columna_p1 = int(input("ERROR, ingrese una columna válida: "))

        if fila_p1 == 1 and columna_p1 == 1:
            columnas_jugador_uno[0].insert(0, numero_jugador_escogido)
        if fila_p1 == 2 and columna_p1 == 1:
            columnas_jugador_uno[0].insert(-1, numero_jugador_escogido)
        if fila_p1 == 1 and columna_p1 == 2:
            columnas_jugador_uno[1].insert(0, numero_jugador_escogido)
        if fila_p1 == 2 and columna_p1 == 2:
            columnas_jugador_uno[1].insert(-1, numero_jugador_escogido)
        if fila_p1 == 1 and columna_p1 == 3:
            columnas_jugador_uno[2].insert(0, numero_jugador_escogido)
        if fila_p1 == 2 and columna_p1 == 3:
            columnas_jugador_uno[2].insert(-1, numero_jugador_escogido)
        if fila_p1 == 1 and columna_p1 == 4:
            columnas_jugador_uno[3].insert(0, numero_jugador_escogido)
        if fila_p1 == 2 and columna_p1 == 4:
            columnas_jugador_uno[3].insert(-1, numero_jugador_escogido)

          
        for i in range(len(jugador_escogido)):
            if filas_p1 + i < len(matriz_visual):
                matriz_visual[filas_p1 + i][columna_p1] = jugador_escogido[i]

        for r in matriz_visual:
            print("".join(r))

    # Turno del segundo jugador 
    numero_segundo_escogido = 100
    print("--- Turno del segundo jugador ---")
    numero_segundo_escogido = int(input("Segundo jugador, ingrese el número del dorsal del jugador: "))
    while numero_segundo_escogido != 0:
    
        while not numero_segundo_escogido in jugadores_p2:
                numero_segundo_escogido = int(input("ERROR, ingrese un dorsal válido o iingresa 0 para continuar: "))
    
        # Validación de costos y talentos para el segundo jugador
        while not talentos_segundo_jugador >= costo_jugadores_p2[numero_segundo_escogido]:
            numero_segundo_escogido = int(input("No tienes suficientes talentos, ingresa el dorsal de otro jugador, ingresa 0 para continuar: "))
        segundo_escogido = jugadores_p2.get(numero_segundo_escogido)
        talentos_segundo_jugador -= costo_jugadores_p2[numero_segundo_escogido]

        # Solicitar fila y columna para el segundo jugador
        fila_p2 = int(input("En qué fila (4-5): "))
        while fila_p2 not in [4, 5]:
            fila_p1 = int(input("ERROR, ingrese una fila válida: "))
        filas_p2 = (fila_p2 - 1) * 44
        columna_p2 = int(input("En qué columna (1-4): "))
        while columna_p2 not in [1, 2, 3, 4]:
            columna_p2 = int(input("ERROR, ingrese una columna válida: "))
 
        # Validar la columna y actualizar la matriz visual
        for i in range(len(segundo_escogido)):
            if filas_p2 + i < len(matriz_visual):
                matriz_visual[filas_p2 + i][columna_p2] = segundo_escogido[i]

        # Imprimir la matriz de manera legible después de cada ronda
        for r in matriz_visual:
            print("".join(r))
    
    actualizar_matriz : int = 44
    columna_evaluada : int = 0
    while columna_evaluada <= 4:

        if len(columnas_jugador_uno[columna_evaluada]) == 1 and len(columnas_jugador_dos[columna_evaluada]) == 0:
            goles_primer_jugador += ataque_jugadores_p1[numero_jugador_escogido]

        elif len(columnas_jugador_dos[columna_evaluada]) == 1 and len(columnas_jugador_uno) == 0:
            goles_segundo_jugador += ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]]

        elif len(columnas_jugador_uno[columna_evaluada]) == 2 and len(columnas_jugador_dos[columna_evaluada]) == 0:
            goles_primer_jugador += ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]] + ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]]

        elif len(columnas_jugador_dos[columna_evaluada]) == 2 and len(columnas_jugador_uno[columna_evaluada]) == 0:
            goles_segundo_jugador += ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] + ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[1]]]

        elif len(columnas_jugador_uno[columna_evaluada]) == 2 and len(columnas_jugador_dos[columna_evaluada]) == 1:
            
            defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]] -= ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]]
            if defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]] <= 0:
                for i in range(actualizar_matriz):
                    matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100

            defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] -= ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]]
            if defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] <= 0:
                goles_primer_jugador += ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]]
                for i in range(actualizar_matriz * 2):
                    matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
            else:
                defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] -= ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]]
                if defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] <= 0:
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

        elif len(columnas_jugador_dos[columna_evaluada]) == 2 and len(columnas_jugador_uno[columna_evaluada]) == 1:
            defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] -= ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]]
            if defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] <= 0:
                for i in range(actualizar_matriz):
                    matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

            defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]] -= ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]]
            if defensa_jugadores_p1|[columnas_jugador_uno[columna_evaluada[0]]] <= 0:
                goles_segundo_jugador += ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]]
                for i in range(actualizar_matriz * 2):
                    matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100
            else:
                defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]] -= ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[1]]]
                if defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]] <= 0:
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100

        elif len(columnas_jugador_uno[columna_evaluada]) == 2 and len(columnas_jugador_dos[columna_evaluada]) == 2:

            defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] -= ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]]
            defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]] -= ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]]


            if defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] <= 0:
                for i in range(actualizar_matriz):
                    matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada]
                defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[1]]] -= ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]]
                if defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[1]]] <= 0:
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 4) + i][columna_evaluada]
            elif defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] > 0:
                defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] -= ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]]
                if defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] <= 0:
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada]

            elif defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]] <= 0:
                for i in range(actualizar_matriz):
                    matriz_visual[(actualizar_matriz) + i][columna_evaluada]
                defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]] -= ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[1]]]
                if defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]] <= 0:
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada]
            elif defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]] > 0:
                defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]] -= ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[1]]]
                if defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]] <= 0:
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz) + i][columna_evaluada]

        columna_evaluada += 1

ronda += 1
talentos_segundo_jugador += ronda
talentos_primer_jugador += ronda
for r in matriz_visual:
    print("".join(r))
    