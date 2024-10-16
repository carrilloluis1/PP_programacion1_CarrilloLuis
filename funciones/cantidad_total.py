# 2. Calcular por cada depósito la cantidad total de juguetes almacenados entre todos los
# tipos.

# cantidad_general = [[lista_ubicacion], [lista_juguetes], [cantidad]]

lista_ubicacion = ["PBA", "CABA", "Chubut", "Tucuman", "Mendoza"]
lista_juguetes = ["Autos", "Muñecas", "Trenes", "Peluches", "Spinners", "Cartas"]
cantidad = [2,5,6,9,7,8,1,2,3]
matriz = [lista_ubicacion, lista_juguetes, cantidad]

def calcular_suma_total(matriz: list) -> int: 
    
    lista_cantidades = matriz[2]
    suma = 0
    for i in range(len(lista_cantidades)):
        suma += lista_cantidades[i]

    return suma

