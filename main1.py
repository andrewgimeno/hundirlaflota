import numpy as np
import random
# Primero creamos los 3 tableros
tablero_jugador = np.full((10,10), " ")
tablero_maquina = np.full((10,10), " ")
tablero_oculto = np.full((10,10), " ")

def disparar(casilla, tablero):
    if tablero[casilla] == 'B':
        tablero[casilla] = 'X'
        print("Tocado")
    else:
        tablero[casilla] = "-"
        print("Agua")
    return tablero

def crear_barco_random(eslora, tamaño):
    barco_random = []
    fila_random = random.randint(0,9)
    columna_random = random.randint(0,9)
    barco_random.append((fila_random,columna_random))
    orient = random.choice(["N","S","E","O"])

    while len(barco_random) < eslora:
        if orient == "O":
            columna_random = columna_random - 1 
        elif orient == "E":
            columna_random = columna_random + 1
        elif orient == "N":
            fila_random = fila_random - 1
        elif orient == "S":
            fila_random = fila_random + 1

        if fila_random not in range(tamaño) or columna_random not in range(tamaño):
            fila_random = random.randint(0,9)
            columna_random = random.randint(0,9)
            barco_random = []
            barco_random.append((fila_random,columna_random))
        else:
            barco_random.append((fila_random,columna_random))
    return barco_random
#tblero1
#Se están creando barcos de eslora 1
count = 0
while count <= 4:
    count +=1
    for i in crear_barco_random(1,10):
        tablero_jugador[i] = 'B'

#Se están creando barcos de eslora 2
count = 0
while count <= 3:
    count +=1
    for i in crear_barco_random(2,10):
        tablero_jugador[i] = 'B'
#Se están creando barcos de eslora 3
count = 0
while count <= 2:
    count +=1
    for i in crear_barco_random(3,10):
        tablero_jugador[i] = 'B'
#Se están creando barcos de eslora 4
count = 0
while count <= 1:
    count +=1
    for i in crear_barco_random(4,10):
        tablero_jugador[i] = 'B'
print(tablero_jugador)
#------------------------------
#tblero2
#Se están creando barcos de eslora 1
count = 0
while count <= 4:
    count +=1
    for i in crear_barco_random(1,10):
        tablero_maquina[i] = 'B'

#Se están creando barcos de eslora 2
count = 0
while count <= 3:
    count +=1
    for i in crear_barco_random(2,10):
        tablero_maquina[i] = 'B'
#Se están creando barcos de eslora 3
count = 0
while count <= 2:
    count +=1
    for i in crear_barco_random(3,10):
        tablero_maquina[i] = 'B'
#Se están creando barcos de eslora 4
count = 0
while count <= 1:
    count +=1
    for i in crear_barco_random(4,10):
        tablero_maquina[i] = 'B'
print(tablero_maquina)
x = int(input("Coordenada x:"))
y = int(input("Coordenada y:"))

tablero_maquina = disparar((x,y), tablero_maquina)
print(tablero_maquina)

fin = False
while fin == False:
    x = int(input("Coordenada x:"))
    y = int(input("Coordenada y:"))
    tablero_jugador = disparar((random.randint(0,9),random.randint(0,9)), tablero_jugador)
    print(tablero_jugador)
    tablero_maquina = disparar((x,y), tablero_maquina)
    print(tablero_maquina)

    
    fin = True
    for i in range(len(tablero_maquina)):
        for j in range(len(tablero_maquina[i])):
            if tablero_maquina[i][j] == 'B':
                fin = False

        
        
        

print('fin del juego')


