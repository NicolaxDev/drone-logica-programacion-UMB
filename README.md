# Poryecto final Logica de programacion

## Jhonatan Nicolas Sandoval Rojas

###### El proyecto se centra en el desarrollo de un juego en python usando la libreria externa Tkinter como visualizador de UI para el mapa y el personaje principal del juego. el objetivo del juego es conseguir puntos (casillas verdes) y llegar a una meta, pero tienes que tener cuidado con los muros, si te estrellas tus vidas iran disminuyendo.

### Como ejecutar el programa

* Dentro del archivo game.py presiona ejecutar
* Al momento de que se abra la ventana del juego es recomendable colocarlo en pantalla /  ventana completa para una mejor visualizacion de las label que se encuentran bajo el mapa
* Puedes controlar el personaje (Cuadro blanco, es el drone) usando WASD.
* Al momento de llegar a la meta el programa finalizara su ejecucion.

### Paquetes necesarios para una correcta ejecucion

1. Tkinter
2. Pyhton
3. VScode

## Clase Drone

###### La clase se encarga enteramente  del comportamiendo del drone en el mapa y dentro de ella se manejan los diferentes metodos de control para las vidas, puntos y la posicion del drone.

## Clase World

###### Se encarga del renderizado completo del mapa teniendo en cuenta una matriz previamente definida con la estructura de los muros, puntos y el objetivo.

## Como podria mejorar?

###### Pienso que algo que podria darle un plus de interactividad al juego seria la inclusion de sonidos y referencias auditivas para cuando el drone se mueve o cuando toma un punto, tambien se podria hacer que la estructura (matriz) del mapa se generara de forma aleatoria para darle mayor dinamismo al juego.
