"""
    Decidi solo manejar una clase dentro de mi codigo, el dron, con el metodo principal que es el de permitir el movimiento del drone, este tambien verifica
    las colisiones del drone con los diferentes objetivos como lo puede ser el muro (#), el destino o meta (T) y un espacio en blanco que permite que 
    avance el drone. todo como se estipulaba en las guias 4 y 5.

    mediante la logica de las colisiones se pueden agregar varios objetos de mapa, por ejemplo un power up que permita al drone avanzar 2 veces mas rapido 
    solamente cuando se avanza hacia adelante.
"""

map = [
    ["D"," "," "," ","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
    ["#"," ","#"," ","#"," "," "," "," "," ","#"," "," "," "," ","#"," "," "," ","#"],
    ["#"," ","#"," "," "," "," ","#"," "," "," "," "," ","#"," ","#"," ","V"," ","#"],
    ["#"," ","#"," ","#"," "," ","#"," ","#"," "," "," ","#"," "," "," ","#"," ","#"],
    ["#"," "," "," ","#"," "," "," "," ","#"," ","V"," ","#"," "," ","#"," "," ","#"],
    ["#"," ","#"," "," "," ","#"," "," "," "," ","#"," "," "," ","#"," "," "," ","#"],
    ["#"," ","#"," "," ","#"," "," ","#"," "," "," "," ","V","#"," "," "," "," ","#"],
    ["#"," "," "," ","#"," "," ","#"," ","#"," ","#"," "," "," ","#"," ","#"," ","#"],
    ["#"," ","#"," "," "," ","V"," ","#"," "," ","#"," "," "," "," "," ","#"," ","#"],
    ["#"," ","#"," "," ","#"," ","#"," "," "," "," ","#"," ","#"," "," "," "," ","#"],
    ["#"," ","#"," "," ","#"," ","#"," ","#"," "," ","#"," ","#"," ","V"," "," ","#"],
    ["#"," "," "," "," ","#"," "," ","#"," "," ","#"," "," "," ","#"," "," "," ","#"],
    ["#"," ","#"," ","#"," "," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"],
    ["#"," ","#"," "," "," ","#"," "," ","#"," "," ","#"," "," "," ","#"," "," ","#"],
    ["#"," ","#"," ","#"," "," "," "," "," ","#"," ","#"," "," "," "," ","#"," ","#"],
    ["#"," "," "," ","#"," ","#"," ","V","#"," "," "," "," ","#"," ","#"," "," ","#"],
    ["#"," ","#"," "," "," ","#"," "," "," "," "," ","#"," "," "," ","#"," "," ","#"],
    ["#"," ","#"," "," "," "," "," ","#"," ","#"," "," ","#"," "," "," "," "," ","#"],
    ["#"," ","#"," ","V"," "," "," "," "," ","#"," "," ","V"," "," "," "," ","T","#"],
    ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
]



class Drone:
    def __init__(self, mapa, posX=0, posY=0):
        self.mapa = mapa
        self.posX = posX
        self.posY = posY
        self.power_up = False
        print(f"Drone creado en x: {posX}, y: {posY}")

    def mostrar_mapa(self):
        for fila in self.mapa:
            for elemento in fila:
                print(elemento, end=" ")
            print()

    def mover(self):
        while True:
            self.mostrar_mapa()
            print("Presione W, A, S o D para moverse. Q para salir.")
            tecla = input(">> ").strip().lower()

            if tecla == "q":
                print("Saliendo...")
                break

            dy, dx = 0, 0
            aumento = 0

            #Up
            if tecla == "w":
                dy = -1
                if self.power_up:
                    dy *= 2
                    self.power_up = False
                    print("💨 Power-up usado: avance doble hacia adelante.")
            elif tecla == "s":
                dy = 1 + aumento
            elif tecla == "a":
                dx = -1
            elif tecla == "d":
                dx = 1 + aumento
            else:
                print("Movimiento no válido.")
                continue

            ny = self.posY + dy
            nx = self.posX + dx

            if not (0 <= ny < len(self.mapa) and 0 <= nx < len(self.mapa[0])):
                print("No puedes salirte del mapa.")
                continue

            destino = self.mapa[ny][nx]

            if destino == "#":
                print("############################### Colisión con muro, no puedes pasar ###############################")
                continue
            elif destino == "T":
                self.mapa[self.posY][self.posX] = " "
                self.mapa[ny][nx] = "D"
                self.mostrar_mapa()
                print("¡Llegaste al objetivo!")
                break
            elif destino == "V":
                print("Power-up obtenido")
                self.power_up = True
                self.mapa[self.posY][self.posX] = " "
                self.mapa[ny][nx] = "D"
                self.posY = ny
                self.posX = nx
            else:
                self.mapa[self.posY][self.posX] = " "
                self.mapa[ny][nx] = "D"
                self.posY = ny
                self.posX = nx

            print("\n" * 5)


dron = Drone(map)
dron.mover()
