from Equipos.Barcelona import *
from Equipos.Real_madri import *

teams = {
    1: barcelona,
    2: real_madrid
}

print("| 1 : Barca |\n| 2: Real Madrid |")
seleccion_jugador_uno = int(input("¿Cuál equipo desea escoger?: "))
equipo_jugador_uno = teams.get(seleccion_jugador_uno)

if equipo_jugador_uno:
    for linea in equipo_jugador_uno["escudo"]:
        print(linea)
else:
    print("Equipo no válido")

print("| 1 : Barca |\n| 2: Real Madrid |")
seleccion_jugador_dos = int(input("¿Cuál equipo desea escoger?: "))
equipo_jugador_dos = teams.get(seleccion_jugador_dos)

if equipo_jugador_dos:
    for linea in equipo_jugador_dos["escudo"]:
        print(linea)
else:
    print("Equipo no válido")

jugadores_p1 = equipo_jugador_uno["jugadores"]
ataque_jugadores_p1 = equipo_jugador_uno["ataque"]
defensa_jugadores_p1 = equipo_jugador_uno["defensa"]
costo_jugadores_p1 = equipo_jugador_uno["costo"]

jugadores_p2 = equipo_jugador_dos["jugadores"]
ataque_jugadores_p2 = equipo_jugador_dos["ataque"]
defensa_jugadores_p2 = equipo_jugador_dos["defensa"]
costo_jugadores_p2 = equipo_jugador_dos["costo"]