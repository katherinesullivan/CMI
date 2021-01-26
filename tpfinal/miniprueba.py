import math
import numpy as np

def main():
    i = 1
    x_coordenadas = [1,2]
    y_coordenadas = [1,2]
    x_coordenadas[0] = 100
    y_coordenadas[0] = 200
    x_coordenadas[1] = 100
    y_coordenadas[1] = 200
    for j in range(i):
        distance = math.sqrt((x_coordenadas[i] - x_coordenadas[j])**2 + (y_coordenadas[i] - y_coordenadas[j])**2)
        if distance < 0.05:
            vector_direccion = (np.random.rand(), np.random.rand())
            vector_direccion_op = (-vector_direccion[0], -vector_direccion[1])
            x_coordenadas[i]= x_coordenadas[i] + vector_direccion[0]
            y_coordenadas[i]= y_coordenadas[i] * vector_direccion[1]
            x_coordenadas[j]= x_coordenadas[j] * vector_direccion_op[0]
            y_coordenadas[j]= y_coordenadas[j] * vector_direccion_op[1]
    print(vector_direccion)
    print(vector_direccion_op)
    print(x_coordenadas[0])
    print(y_coordenadas[0])
    print(x_coordenadas[1])
    print(y_coordenadas[1])
    lista4 = []
    lista2 = [1]
    lista3 = [2]
    lista4 += lista2
    lista3 += lista2
    print(lista4)
    print(lista3)

main()