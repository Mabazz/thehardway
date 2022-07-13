def queso_y_galleta(recuento_quesos, cajas_galletas):
    print(f"Tenes {recuento_quesos} quesos.")
    print(f"Tenes {cajas_galletas} cajas de galletas.")
    print("Suficiente para un camping.")
    print("Traete la sabana. \n")

print("Directamente le podemos dar números a esta función: ")
queso_y_galleta(20, 30)

print("O... podemos trabajar con variables desde nuestro script:")
cantidad_quesos = 10
cantidad_galletas = 50

queso_y_galleta(cantidad_quesos, cantidad_galletas)

print("Hasta podemos hacer operaciones matematicas dentro:")
queso_y_galleta(10 + 20, 5 + 6)

print("Y podemos combinar ambas, variables y operaciones:")
queso_y_galleta(cantidad_quesos + 100, cantidad_galletas + 1000)
