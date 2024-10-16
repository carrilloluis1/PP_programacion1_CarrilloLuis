# Realizar un menú de opciones:

# 1. Obtener existencias: para ello deberá cargar en el main la existencia de cada juguete
# en todos los depósitos. En una lista de cantidad, no uno por uno. Por lo que habrá una
# matriz con 3 columnas o filas, provincia, tipo de juguete y cantidad.

lista_ubicacion = ["PBA", "CABA", "Chubut", "Tucuman", "Mendoza"]
lista_juguetes = ["Autos", "Muñecas", "Trenes", "Peluches", "Spinners", "Cartas"]
cantidad = []

for i in range(len(lista_ubicacion)):
    
    for j in range(len(lista_juguetes)):
        
        cantidad_juguetes = int(input(f'Cantidad de {lista_juguetes[j]} que hay en {lista_ubicacion[i]}: '))
        if cantidad_juguetes < 0:
            cantidad_juguetes = int(input("Cantidad de juguete Incorrecto!!! Reingrese la cantidad: "))
        cantidad += [cantidad_juguetes]
    
    print("---------------------------------------------------------")

cantidad_general = [lista_ubicacion, lista_juguetes, cantidad]
print(cantidad_general)
