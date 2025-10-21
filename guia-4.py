#import os

map = [
    ["D", " ", "#", "#", "#", "#", "#"],
    ["#", " ", "#", " ", " ", " ", "#"],
    ["#", " ", " ", "#", "#", " ", "#"],
    ["#", "#", " ", " ", " ", " ", "#"],
    ["#", " ", " ", "#", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "T", "#"],
]

while True:
    for row in map:
        for element in row:
            print(element, end=" ")
        print()
    
    colision = False
    if colision == True:
        break

    y = 0
    x = 0
    
    print("Presione alguna de las siguientes teclas para moverse: W, A, S, D")
    tecla = input(">> ")
    if tecla == "w" or tecla == "W":
        y += 1
    elif tecla == "a" or tecla == "A":
        x -= 1
    elif tecla == "s" or tecla == "S":
        y -= 1
    elif tecla == "d" or tecla == "D":
        x += 1
    else:
        print("movimiento no valido")

    #os.system('clear')

    map[y][x] = "D"

    for row in map:
        for element in row:
            print(element, end=" ")
        print()