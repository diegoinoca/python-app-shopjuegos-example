#funcion para el menu principal
def options():
    print("Ingrese un número según la acción que desea realizar\n",
        "1:Mostrar lista de juegos\n",
        "2:Ver detalle de un juego\n",
        "3:Comprar Juegos\n",
        "4:Cerrar aplicación\n")

    return int(input("Seleccione una opción: "))

#funcion para listar juegos
def listaJuegos(juegos):
    print("\n---Lista de juegos---")
    i = 1
    #recorremos todo los juegos e imprimimos el nombre
    for clave, valor in juegos.items():
        print(i,"-", valor['nombre'], "-", clave)
        i += 1
    print("\n")


#funcion para mostrar el detalle de un juego
def detalleJuego(juego):
    print("\n---Detalle del juego---")
    #mapeo de valores para imprimir el detalle
    print(f"Nombre Juego:{juego['nombre']}")
    print(f"Cantidad de productos:{juego['cantidad']}")
    print(f"Alias del juego:{juego['alias']}")
    print(f"El rakin del juego:{juego['rankin']}")
    print("---Detalle del juego---\n \n")


#funcion para comprar el juego
def comprarJuego(juego):
    print("\n---Has comprado el juego---")
    if juego['cantidad'] > 0 :
        print(f"Se ha comprado un item del juego {juego['nombre']} \n")
        juego['cantidad'] = juego['cantidad'] - 1
    else:
        print(f"El juego {juego['nombre']} no se ecuentra en stock\n")
    return juego