#desacoplamos programa importando las funciones de otro archivo
from functions import  *

#inicializamos las variables globales
juegos = {  '001':{'nombre':'League of Legends', 'cantidad':3,'alias':'lol', 'rankin':'4'}, 
            '002':{'nombre':'The Legend of Zelda', 'cantidad':1,'alias':'zelda', 'rankin':'8'},
            '003':{'nombre':'Mario World', 'cantidad':10,'alias':'Mario', 'rankin':'12'},
            '004':{'nombre':'Mortal Kombat', 'cantidad':5,'alias':'Mortal Kombat', 'rankin':'3'}
        }

#definimos la función principal
def run():
    #imprimimos por pantalla el inicio de programa
    print("Inicio del programa")
    #ejecutamos ciclo para las opciones del programa
    while True: 
        #llamamos al menú principal y capturamos el valor de la selección
        selection = options()
        if selection == 1:
            listaJuegos(juegos)
        elif selection == 2:
            #rescatamos el código del juego
            codigo = str(input('Ingresa el código del juego:'))

            #buscamos que el juego se encuentre en la lista
            if codigo in juegos:
                detalleJuego(juegos[codigo])
            else:
                #si no se encuentra el producto lo mostramos por pantalla
               print(f"Juego con el código:{codigo} no encontrado \n") 
        elif selection == 3:
            #rescatamos el código del juego
            codigo = str(input('Ingresa el código del juego a comprar:'))

            #buscamos que el juego se encuentre en la lista
            if codigo in juegos:
                juego = comprarJuego(juegos[codigo])
                juegos[codigo] = juego
            else:
                #si no se encuentra el producto lo mostramos por pantalla
               print(f"Juego con el código:{codigo} no encontrado, no se puede comprar \n") 
        elif selection == 4:
            break;
            
    print("Ha cerrado el programa")

#ejecutamos el inicio de programa (función principal)
run()