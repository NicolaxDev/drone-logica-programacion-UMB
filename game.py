import tkinter as tk

root = tk.Tk()
root.title("Drone game")
colorBg = "#10002b"
root.configure(background=colorBg)

frame = tk.Frame(root, highlightbackground="blue", highlightthickness=5)

map = [
    ["D"," "," "," ","#"," "," "," "," "," "," "," "," "," "," ","#"],
    ["#"," ","#"," ","#"," "," "," "," "," "," ","#"," "," "," ","#"],
    ["#"," ","#"," "," "," ","#"," "," "," ","#","#"," ","V"," ","#"],
    ["#"," ","#"," ","#"," ","#"," ","#"," ","#"," "," ","#"," ","#"],
    ["#"," "," "," ","#"," "," "," ","#","V","#"," ","#"," "," ","#"],
    ["#"," ","#"," "," ","#"," "," "," ","#"," ","#"," "," "," ","#"],
    ["#"," ","#"," "," "," "," ","#"," "," ","V"," "," "," "," ","#"],
    ["#"," "," "," ","#"," ","#"," ","#","#"," ","#"," ","#"," ","#"],
    ["#"," ","#"," "," ","V"," ","#"," ","#"," "," "," ","#"," ","#"],
    ["#"," "," "," "," "," ","#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," ","#"," ","#"," "," "," ","V"," "," ","#"],
    ["#"," "," "," "," "," "," ","#"," ","#"," ","#"," "," "," ","#"],
    ["#"," ","#"," ","#"," ","#"," ","#","#","#","#"," ","#"," ","#"],
    ["#"," "," "," "," ","#"," "," ","#"," "," "," ","#"," "," ","#"],
    ["#"," ","#"," ","#"," "," "," "," "," "," "," "," ","#"," ","#"],
    ["#"," "," "," ","#","#"," ","V","#"," "," "," ","#"," "," ","#"],
    ["#"," ","#"," "," ","#"," "," "," "," "," "," ","#"," "," ","#"],
    ["#"," ","#"," "," "," "," ","#"," "," ","#"," "," "," "," ","#"],
    ["#"," "," "," ","V"," "," "," "," "," ","V"," "," "," ","T","#"],
    ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
]

wallscolor = "#613dc1"
droneColor = "#f4effa"
powerUpColor = "#76c893"
destinationColor = "#edf67d"

class Entitie:
    pass


class Drone(Entitie):
    def __init__(self, posX=0, posY=0):
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
            def manejar_presion_tecla(event):
                keyPressd = {event.char}
                print(f"{event.char}")
                return keyPressd
            
            tecla = root.bind("<Key>", manejar_presion_tecla)
            if tecla == "q":
                print("Saliendo...")
                break

            dy, dx = 0, 0
            aumento = 0

            if tecla == "w":
                dy = -1
                if self.power_up:
                    dy *= 2
                    self.power_up = False
                    print("Power-up usado: avance doble hacia adelante.")
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
wallscolor = "#613dc1"
droneColor = "#f4effa"
powerUpColor = "#76c893"
destinationColor = "#edf67d"
#mapa
for fila_idx, fila in enumerate(map):
    for columna_idx, valor in enumerate(fila):
        frame_celda = tk.Frame(root, padx=20, pady=10, )
        frame_celda.grid(row=fila_idx, column=columna_idx)
        labelColor=colorBg
        if valor == "#":
            frame_celda.config(bg=wallscolor)
            labelColor = wallscolor
        elif valor == "V":
            frame_celda.config(bg=powerUpColor, padx=10, pady=2)
            labelColor = powerUpColor
        elif valor == "D":
            frame_celda.config(bg=droneColor, padx=10, pady=2)
            labelColor = droneColor
        elif valor == "T":
            frame_celda.config(bg=destinationColor,)
            labelColor = destinationColor
        else:
            frame_celda.config(bg=colorBg)
            labelColor = colorBg
            
        label_valor = tk.Label(frame_celda, bg=labelColor)#text=str(valor))
        label_valor.pack()

root.mainloop()