ronda_penales: int = 1
goles_primer_jugador: int = 0
goles_segundo_jugador: int = 0

while ronda_penales <= 5:
    # Tiro del primer jugador
    tiro_primer_jugador = input("Primer jugador: ¿a dónde deseas tirar (<-), (-), (->)?: ")
    atajada_segundo_jugador = input("Segundo jugador: ¿a dónde deseas atajar (<-), (-), (->)?: ")
    if tiro_primer_jugador != atajada_segundo_jugador:
        goles_primer_jugador += 1

    # Tiro del segundo jugador
    tiro_segundo_jugador = input("Segundo jugador: ¿a dónde deseas tirar (<-), (-), (->)?: ")
    atajada_primer_jugador = input("Primer jugador: ¿a dónde deseas atajar (<-), (-), (->)?: ")
    if tiro_segundo_jugador != atajada_primer_jugador:
        goles_segundo_jugador += 1

    # Verificar condiciones de victoria después del tiro del segundo jugador
    if ronda_penales == 3 and goles_primer_jugador == 3 and goles_segundo_jugador == 0:
        print(f"El primer jugador gana con un marcador de {goles_primer_jugador}-{goles_segundo_jugador}")
        break
    elif ronda_penales == 4 and goles_primer_jugador == 4 and goles_segundo_jugador <= 1:
        print(f"El primer jugador gana con un marcador de {goles_primer_jugador}-{goles_segundo_jugador}")
        break
    elif ronda_penales == 5 and goles_primer_jugador == 5 and goles_segundo_jugador <= 2:
        print(f"El primer jugador gana con un marcador de {goles_primer_jugador}-{goles_segundo_jugador}")
        break

    # Verificar si el segundo jugador puede ganar o empatar
    if ronda_penales == 3 and goles_segundo_jugador == 3 and goles_primer_jugador == 0:
        print(f"El segundo jugador gana con un marcador de {goles_segundo_jugador}-{goles_primer_jugador}")
        break
    elif ronda_penales == 4 and goles_segundo_jugador == 4 and goles_primer_jugador <= 1:
        print(f"El segundo jugador gana con un marcador de {goles_segundo_jugador}-{goles_primer_jugador}")
        break
    elif ronda_penales == 5 and goles_segundo_jugador == 5 and goles_primer_jugador <= 2:
        print(f"El segundo jugador gana con un marcador de {goles_segundo_jugador}-{goles_primer_jugador}")
        break

    ronda_penales += 1

# Si no hay un ganador después de 5 rondas
if ronda_penales > 5:
    if goles_primer_jugador > goles_segundo_jugador:
        print(f"El primer jugador gana con un marcador de {goles_primer_jugador}-{goles_segundo_jugador}")
    elif goles_segundo_jugador > goles_primer_jugador:
        print(f"El segundo jugador gana con un marcador de {goles_segundo_jugador}-{goles_primer_jugador}")
    else:
        # En caso de empate, jugar rondas adicionales hasta que alguien gane
        while True:
            tiro_primer_jugador = input("Primer jugador: ¿a dónde deseas tirar (<-), (-), (->)?: ")
            atajada_segundo_jugador = input("Segundo jugador: ¿a dónde deseas atajar (<-), (-), (->)?: ")
            if tiro_primer_jugador != atajada_segundo_jugador:
                goles_primer_jugador += 1

            tiro_segundo_jugador = input("Segundo jugador: ¿a dónde deseas tirar (<-), (-), (->)?: ")
            atajada_primer_jugador = input("Primer jugador: ¿a dónde deseas atajar (<-), (-), (->)?: ")
            if tiro_segundo_jugador != atajada_primer_jugador:
                goles_segundo_jugador += 1

            if goles_primer_jugador > goles_segundo_jugador:
                print(f"El primer jugador gana con un marcador de {goles_primer_jugador}-{goles_segundo_jugador}")
                break
            elif goles_segundo_jugador > goles_primer_jugador:
                print(f"El segundo jugador gana con un marcador de {goles_segundo_jugador}-{goles_primer_jugador}")
                break