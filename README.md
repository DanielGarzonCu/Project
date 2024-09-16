# Project

Explicación del código y diagramas de flujo
Este código representa un juego basado en la elección de equipos de fútbol (Barcelona y Real Madrid) y la evaluación de sus jugadores durante un número específico de rondas. Se basa en la interacción entre jugadores y las decisiones tomadas en cada ronda, como seleccionar equipos y jugadores, evaluar sus ataques y defensas, y calcular el marcador.

1. Importación de módulos
ruby
Copiar código
from Equipos.Barcelona import *
from Equipos.Real_madri import *
Aquí se importan los módulos Barcelona y Real_madri, que probablemente contienen información y funcionalidades relacionadas con estos equipos. La estructura sugiere que estos módulos contienen información sobre jugadores, atributos de ataque, defensa, y costo.

Diagrama de flujo (simplificado):

```mermaid
graph TD
    A[Inicio] --> B[Importar Equipos]
    B --> C[Barcelona]
    B --> D[Real Madrid]
    C --> E[Datos de jugadores y atributos]
    D --> E
````
2. Función elegir_equipo
```ruby
def elegir_equipo(jugador: str) -> dict:
Esta función permite a cada jugador seleccionar entre dos equipos: Barcelona o Real Madrid. El equipo elegido se devuelve como un diccionario que contiene los jugadores y sus atributos (ataque, defensa, costo).
````
Diagrama de flujo para elegir_equipo:

```mermaid
graph TD
    A[Inicio] --> B[Mostrar Opciones de Equipos]
    B --> C{Selecciona un equipo}
    C -->|1| D[Elegir Barcelona]
    C -->|2| E[Elegir Real Madrid]
    D --> F[Mostrar escudo del equipo]
    E --> F
    F --> G[Devolver jugadores, ataque, defensa, costo]
```
3. Función elegir_modo_juego
```ruby
Copiar código
def elegir_modo_juego() -> int:
Esta función permite a los jugadores elegir entre tres modos de juego, cada uno con un número diferente de rondas (9, 12 o 15).
```
Diagrama de flujo para elegir_modo_juego:

```mermaid
Copiar código
graph TD
    A[Inicio] --> B[Mostrar Modos de Juego]
    B --> C{Selecciona un modo}
    C -->|1| D[Número de rondas: 9]
    C -->|2| E[Número de rondas: 12]
    C -->|3| F[Número de rondas: 15]
    D --> G[Devolver rondas]
    E --> G
    F --> G
```
4. Función evaluar_columna
```ruby
Copiar código
def evaluar_columna(fila_p1, columna_p1, fila_p2, columna_p2, numero_jugador_escogido, numero_segundo_escogido) -> int:
````
Esta función evalúa una columna de la matriz de juego, en la que los jugadores colocan sus jugadores seleccionados. Dependiendo de la columna y las posiciones de los jugadores, se calculan los goles para cada equipo.

Diagrama de flujo para evaluar_columna:

```mermaid
Copiar código
graph TD
    A[Inicio] --> B[Evaluar posiciones]
    B --> C{Hay jugadores en la columna?}
    C -->|No| D[Termina evaluación]
    C -->|Sí| E{Evaluar ataques y defensas}
    E -->|Gana P1| F[Sumar goles a P1]
    E -->|Gana P2| G[Sumar goles a P2]
    F --> H[Actualizar matriz visual]
    G --> H
    H --> I[Devolver goles]
```
5. Bucle principal del juego
```ruby
Copiar código
if __name__ == "__main__":
Este es el bucle principal del juego. Después de que los equipos son seleccionados y el modo de juego es elegido, se realiza el bucle por rondas, donde cada jugador escoge sus jugadores y se evalúan los resultados de los enfrentamientos.
```
Diagrama de flujo para el bucle principal:

mermaid
Copiar código
graph TD
    A[Inicio del juego] --> B[Elegir equipo P1 y P2]
    B --> C[Elegir modo de juego]
    C --> D[Iniciar rondas]
    D --> E{Turno del jugador 1}
    E -->|Escoge jugador| F[Evaluar columna]
    F --> G[Actualizar goles]
    G --> H{Turno del jugador 2}
    H -->|Escoge jugador| F
    G --> I[Fin de ronda]
    I --> J{Más rondas?}
    J -->|Sí| D
    J -->|No| K[Mostrar resultados finales]
    K --> L[Fin del juego]
Este diseño divide el código en bloques bien definidos, donde cada función tiene un propósito claro. El uso de diagramas de flujo ayuda a visualizar cómo se toman las decisiones en cada paso del juego, desde la selección de equipos hasta la evaluación de las columnas de juego y el cálculo del marcador.
```mermaid
graph TD
    subgraph Inicializar
        A1["Evaluar columnas de la matriz"]
        A2["Filas a evaluar: 22, 66, 154, 198"]
    end

    subgraph Evaluaciones
        B0["A qué jugador o jugadores pertenecen las str?"]
        B1["Fila 1 tiene str y demás vacías?"]
        B2["Fila 2 tiene str y demás vacías?"]
        B3["Fila 3 tiene str y demás vacías?"]
        B4["Fila 4 tiene str y demás vacías?"]
        B5["Fila 1 y 2 tienen str y demás vacías?"]
        B6["Fila 3 y 4 tienen str y demás vacías?"]
        C1["Fila 1 y 4 tienen str?"]
        C2["Fila 2 y 4 tienen str?"]
        C3["Fila 1 y 3 tienen str?"]
        C4["Fila 1, 2 y 4 tienen str?"]
        C5["Fila 1, 3 y 4 tienen str?"]
        C6["Fila 2 y 3 tienen str?"]
        C7["Fila 1, 2 y 3 tienen str?"]
        C8["Fila 2, 3 y 4 tienen str?"]
        C9["Filas 1, 2, 3 y 4 tienen str?"]
        C10["Ninguna de las filas tienen str?"]
    end

    subgraph Calculos
        D1["Calcular vida y daño del jugador fila 1"]
        D2["Calcular vida y daño del jugador fila 2"]
        D3["Calcular vida y daño del jugador fila 3"]
        D4["Calcular vida y daño del jugador fila 4"]
        D5["Calcular vida y daño de jugadores fila 1 y 2"]
        D6["Calcular vida y daño de jugadores fila 3 y 4"]
        E1["Calcular vida y daño del jugador de fila 1 y fila 4"]
        E2["Calcular vida y daño del jugador de fila 2 y fila 4"]
        E3["Calcular vida y daño del jugador de fila 1 y fila 3"]
        E4["Calcular vida y daño del jugador de fila 1, 2 y 4"]
        E5["Calcular vida y daño del jugador de fila 1, 3 y 4"]
        E6["Calcular vida y daño del jugador de fila 2 y 3"]
        E7["Calcular vida y daño del jugador de fila 1, 2 y 3"]
        E8["Calcular vida y daño del jugador de fila 2, 3 y 4"]
        E9["Calcular vida y daño del jugador de fila 1, 2, 3 y 4"]
        E10["Filas vacías"]
    end

    subgraph Acciones
        F1["Goles primer jugador += daño del jugador primera fila"]
        F2["Goles primer jugador += daño del jugador segunda fila"]
        F3["Goles segundo jugador += daño del jugador tercera fila"]
        F4["Goles segundo jugador += daño del jugador cuarta fila"]
        F5["Goles primer jugador += daño del jugador primera fila más daño del jugador segunda fila"]
        F6["Goles segundo jugador += daño del jugador tercera fila más daño del jugador cuarta fila"]
        G1["Vida jugador línea 1 -= Daño jugador línea 4 y vida jugador línea 4 -= daño jugador línea 1"]
        G2["Vida jugador línea 2 -= Daño jugador línea 4 y vida jugador línea 4 -= daño jugador línea 2"]
        G3["Vida jugador línea 1 -= Daño jugador línea 3 y vida jugador línea 4 -= daño jugador línea 3"]
        G4["Vida jugador línea 2 -= Daño jugador línea 4 y vida jugador línea 4 -= daño jugador línea 2"]
        G5["Vida jugador línea 1 -= Daño jugador línea 3 y vida jugador línea 3 -= daño jugador línea 1"]
        G6["Vida jugador línea 2 -= Daño jugador línea 3 y vida jugador línea 3 -= daño jugador línea 2"]

    end

    subgraph Condiciones
        H1["Vida jugador línea 4 <= 0?"]
        H2["Vida jugador línea 1 <=0?"]
        H3["Vida jugador línea 3 <= 0?"]
        H4["Vida jugador línea 2 <= 0?"]
    end

    subgraph Ultimas acciones
        U1["Goles primer jugador += daño jugador línea 1"]
        U2["Vida jugador línea 4 -= daño jugador línea 1"]
        U3["Goles segundo jugador += daño jugador línea 4"]
        U4["Vida jugador linea 1 += daño jugador linea 4"]
        U5["Vida jugador línea 3 -= daño jugador línea 1"]
        U6["Vida jugador línea 2 -= daño jugador línea 4"]
        I["Siguiente columna"]
    end


    A1 --> A2
    A2 --> B1
    B1 -- "Sí" --> B0
    B1 -- "No" --> B2
    B2 -- "Sí" --> B0
    B2 -- "No" --> B3
    B3 -- "Sí" --> B0
    B3 -- "No" --> B4
    B4 -- "Sí" --> B0
    B4 -- "No" --> B5
    B5 -- "Sí" --> B0
    B5 -- "No" --> B6
    B6 -- "Sí" --> B0
    B6 -- "No" --> C1
    C1 -- "Sí" --> B0
    C1 -- "No" --> C2
    C2 -- "Sí" --> B0
    C2 -- "No" --> C3
    C3 -- "Sí" --> B0
    C3 -- "No" --> C4
    C4 -- "Sí" --> B0
    C4 -- "No" --> C5
    C5 -- "Sí" --> B0
    C5 -- "No" --> C6
    C6 -- "Sí" --> B0
    C6 -- "No" --> C7
    C7 -- "Sí" --> B0
    C7 -- "No" --> C8
    C8 -- "Sí" --> B0
    C8 -- "No" --> C9
    C9 -- "Sí" --> B0
    C9 -- "No" --> C10
    C10 -- "Sí" --> E10

    B0 --> D1
    B0 --> D2 
    B0 --> D3
    B0 --> D4
    B0 --> D5
    B0 --> D6
    B0 --> E1
    B0 --> E2
    B0 --> E3
    B0 --> E4
    B0 --> E5
    B0 --> E6
    B0 --> E7
    B0 --> E8
    B0 --> E9

    D1 --> F1
    D2 --> F2
    D3 --> F3
    D4 --> F4
    D5 --> F5
    D6 --> F6

    E1 --> G1
    E2 --> G2
    E3 --> G3
    E4 --> G4
    E5 --> G5
    E6 --> G6
    E7 --> G6
    E8 --> G6
    E9 --> G6

    G4 --> H1
    G5 --> H2
    G6 --> H3
    G6 --> H4

    H1 -- "Sí" --> U1
    H1 -- "No" --> U2
    H2 -- "Sí" --> U3
    H2 -- "No" --> U4
    H3 -- "Sí" --> U5
    H3 -- "No" --> U6
    H4 -- "Sí" --> U5
    H4 -- "Sí" --> U6

    

```
