#! /usr/bin/python

# 6ta Practica Laboratorio 
# Complementos Matematicos I
# Ejemplo parseo argumentos

import math
import argparse
import matplotlib.pyplot as plt
import numpy as np

DIMENSION = 500 # rango del gráfico

# SI EL ALGORITMO ESTA BIEN IMPLEMENTADO, CADA GRAFO DEBERIA TENER UNA ÚNICA REPRESENTACIÓN ???

def lee_grafo_archivo(file_path):
    '''
    Lee un grafo desde un archivo y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''
    vertices = []
    aristas = []
    grafo = (vertices, aristas)
    with open(file_path, 'r') as f:
        n = int(f.readline())
        while (n != 0):
            vertice = f.readline().rstrip()
            vertices.append(vertice)
            n-=1
        for line in f:
            arista = line.split()
            aristas.append(tuple(arista))
    return grafo


# Devuelve una lista con N números randon del 0 al 1000
def coordenadas_random(N):
    return np.random.rand(N) * DIMENSION # rango 1000 como en el gif?? yup


# def draws_graph(grafo, x_coordenadas, y_coordenadas):
#     n_vertices = len(grafo[0])
#     # x_coordenadas = coordenadas_random(n_vertices) # las coordenadas abria que pasarlas como parametro
#     # y_coordenadas = coordenadas_random(n_vertices)
#     plt.scatter(x_coordenadas,y_coordenadas)
#     for i in range(n_vertices):
#         x_aristas = []
#         y_aristas = []
#         for j in range(n_vertices):
#             v1 = grafo[0][i]
#             v2 = grafo[0][j]
#             if (v1,v2) in grafo[1]:
#                 x_aristas.append(x_coordenadas[i])
#                 x_aristas.append(x_coordenadas[j])
#                 y_aristas.append(y_coordenadas[i])
#                 y_aristas.append(y_coordenadas[j])
#                 plt.plot(x_aristas,y_aristas)
#     plt.draw()
#     plt.show()


# Inicializa los acumuladores en cero, N es el conjunto de los vértices.
def initialize_accumulators(N):
    accum_x = {v: 0 for v in N}
    accum_y = {v: 0 for v in N}
    return accum_x, accum_y

# Calcula la fuerza de atracción
def f_attraction(d,k):
    return (d**2)/k

# Calcula la fuerza de repulsión
def f_repultion(d,k):
    return -(k**2)/d

def evitar_colisiones (i, x_coordenadas, y_coordenadas):
    changed = []

    for j in range(i):
        distance = math.sqrt((x_coordenadas[i] - x_coordenadas[j])**2 + (y_coordenadas[i] - y_coordenadas[j])**2)
        if distance < 0.05:
            changed += [j]
            vector_direccion = (np.random.rand(), np.random.rand())
            vector_direccion_op = (-vector_direccion[0], -vector_direccion[1])
            x_coordenadas[i]= x_coordenadas[i] * vector_direccion[0]
            y_coordenadas[i]= y_coordenadas[i] * vector_direccion[1]
            x_coordenadas[j]= x_coordenadas[j] * vector_direccion_op[0]
            y_coordenadas[j]= y_coordenadas[j] * vector_direccion_op[1]

    if changed == [] :
        return

    else:
        for elem in changed: 
            evitar_colisiones(elem, x_coordenadas, y_coordenadas)

        evitar_colisiones(i, x_coordenadas, y_coordenadas)

    return

class LayoutGraph:

    def __init__(self, grafo, iters, refresh, c1, c2, temperatura, verbose=False):
        """
        Parámetros:
        grafo: grafo en formato lista
        iters: cantidad de iteraciones a realizar
        refresh: cada cuántas iteraciones graficar. Si su valor es cero, entonces debe graficarse solo al final.
        c1: constante de repulsión
        c2: constante de atracción
        verbose: si está encendido, activa los comentarios
        """

        # Guardo el grafo
        self.grafo = grafo

        # Inicializo estado
        # Completar
        self.posiciones = {}
        self.fuerzas = {}

        # Guardo opciones
        self.iters = iters
        self.verbose = verbose
        # TODO: faltan opciones
        self.temperatura = temperatura
        self.refresh = refresh
        self.c1 = c1
        self.c2 = c2


    def draws_graph(self, x_coordenadas, y_coordenadas):
        n_vertices = len(self.grafo[0])
        # x_coordenadas = coordenadas_random(n_vertices) # las coordenadas abria que pasarlas como parametro
        # y_coordenadas = coordenadas_random(n_vertices)
        plt.scatter(x_coordenadas,y_coordenadas)
        for i in range(n_vertices):
            x_aristas = []
            y_aristas = []
            for j in range(n_vertices):
                v1 = self.grafo[0][i]
                v2 = self.grafo[0][j]
                if (v1,v2) in self.grafo[1]:
                    x_aristas.append(x_coordenadas[i])
                    x_aristas.append(x_coordenadas[j])
                    y_aristas.append(y_coordenadas[i])
                    y_aristas.append(y_coordenadas[j])
                    plt.plot(x_aristas,y_aristas)


    def layout(self):
        """
        Aplica el algoritmo de Fruchtermann-Reingold para obtener (y mostrar)
        un layout
        """
        n_vertices = len(self.grafo[0])

        x_coordenadas = coordenadas_random(n_vertices)
        y_coordenadas = coordenadas_random(n_vertices)

        # ESTO SE PUEDE DEFINIR DE FORMA GLOBAL?
        # k es el valor que refiere a la disperción de los nodos del grafo
        kr = self.c1 * math.sqrt((DIMENSION*DIMENSION) / n_vertices)
        ka = self.c2 * math.sqrt((DIMENSION*DIMENSION) / n_vertices)
        kg = 0.098 * math.sqrt((DIMENSION*DIMENSION) / n_vertices)

        c_temp = 0.95 # constante de reducción de temperatura

        centro = (DIMENSION/2,DIMENSION/2)
        
        dicc_vert_a_idx = {}
        for i in range(n_vertices):
            dicc_vert_a_idx[self.grafo[0][i]] = i
        
        plt.show()
        for k in range(1, self.iters+1):
            
            ### BEGIN STEP ###
            
            # Inicializar temperatura
            t = self.temperatura

            # Inicializar acumuladores a cero
            accum_x, accum_y = initialize_accumulators(self.grafo[0])


            # HABRIA QUE ARMAR UN ENUMERADO ENTRE LOS VERTICES Y SUS INDICES
            # Calcular fuerzas de atracción
            for e in self.grafo[1]:
                distance = math.sqrt((x_coordenadas[dicc_vert_a_idx[e[0]]] - x_coordenadas[dicc_vert_a_idx[e[1]]])**2 + 
                    (y_coordenadas[dicc_vert_a_idx[e[0]]] - y_coordenadas[dicc_vert_a_idx[e[1]]])**2)
                mod_fa = f_attraction(distance,ka)
                fx = mod_fa * (x_coordenadas[dicc_vert_a_idx[e[1]]] - x_coordenadas[dicc_vert_a_idx[e[0]]]) / distance # ESTO ESTA BIEN? (EL *)
                fy = mod_fa * (y_coordenadas[dicc_vert_a_idx[e[1]]] - y_coordenadas[dicc_vert_a_idx[e[0]]]) / distance
                accum_x[e[0]] = accum_x[e[0]] + fx
                accum_y[e[0]] = accum_y[e[0]] + fy
                accum_x[e[1]] = accum_x[e[1]] - fx
                accum_y[e[1]] = accum_y[e[1]] - fy

            # Calcular fuerzas de repulsión
            for i in range(n_vertices):
                for j in range(n_vertices):
                    if i != j:
                        distance = math.sqrt((x_coordenadas[i] - x_coordenadas[j])**2 + (y_coordenadas[i] - y_coordenadas[j])**2)
                        mod_fr = f_repultion(distance,kr)
                        fx = mod_fr * (x_coordenadas[j] - x_coordenadas[i]) / distance # ESTO ESTA BIEN? (EL *)
                        fy = mod_fr * (y_coordenadas[j] - y_coordenadas[i]) / distance
                        accum_x[self.grafo[0][i]] = accum_x[self.grafo[0][i]] + fx
                        accum_y[self.grafo[0][i]] = accum_y[self.grafo[0][i]] + fy
                        accum_x[self.grafo[0][j]] = accum_x[self.grafo[0][j]] - fx
                        accum_y[self.grafo[0][j]] = accum_y[self.grafo[0][j]] - fy
            
            # NI IDEA SI ESTA BIEN, FALTARIA LA FUNCION QUE CALCULA LA FUERZA DE GRAVEDAD
            # Calcular fuerzas de gravedad
            for i in range(n_vertices):
                distance = math.sqrt((x_coordenadas[i] - centro[0])**2 + (y_coordenadas[i] - centro[1])**2)
                #mod_fg = f_attraction(distance,kg)
                fx = kg * (centro[0] - x_coordenadas[i]) / distance
                fy = kg * (centro[1] - y_coordenadas[i]) / distance
                accum_x[self.grafo[0][i]] = accum_x[self.grafo[0][i]] + fx
                accum_y[self.grafo[0][i]] = accum_y[self.grafo[0][i]] + fy

            # Actualizar posiciones
            for i in range(n_vertices):
                f = (accum_x[self.grafo[0][i]],accum_y[self.grafo[0][i]])
                modulo_f = math.sqrt((f[0])**2 + (f[1])**2)
                if modulo_f > t:
                    f = (f[0]/modulo_f*t, f[1]/modulo_f*t)
                    accum_x[self.grafo[0][i]], accum_y[self.grafo[0][i]] = f

                x_coordenadas[i] = x_coordenadas[i] + accum_x[self.grafo[0][i]]
                y_coordenadas[i] = y_coordenadas[i] + accum_y[self.grafo[0][i]]

                # QUE ONDA LOS BORDES DE LA VENTANA?
                if x_coordenadas[i] < 0:
                    x_coordenadas[i] = 0
                elif x_coordenadas[i] > DIMENSION:
                    x_coordenadas[i] = DIMENSION
                if y_coordenadas[i] < 0:
                    y_coordenadas[i] = 0
                elif y_coordenadas[i] > DIMENSION:
                    y_coordenadas[i] = DIMENSION

                # Chequeamos que no choque con ningun vértice anterior
                evitar_colisiones(i, x_coordenadas, y_coordenadas)
                
                # El volver a chocar?
                # Pense fc como esta con un while hasta que nada choque
                # pero eso clearly es costoso
                # chequea solo hasta el punto que estamos y solo va achequear comparando
                # con estos 2 nuevos

                # NO SE
                # seria afuera pero
                

                # cosas que capaz estaria weno pero si no fue
                # ver de que no cambien tanto los numeros en esto que hice pues dumb
                # y no se me ocurre otra forma de hacer esa fuerza~
                # definir una funcion distance


            # Actualizar temperatura
            t = c_temp * t

            ### END STEP ###


            ### PLOTEO ###
            if (k % self.refresh) == 0:
                plt.axis([0,DIMENSION,0,DIMENSION])
                self.draws_graph(x_coordenadas,y_coordenadas)
                plt.pause(1)
                plt.clf()

        return




def main():
    # Definimos los argumentos de linea de comando que aceptamos
    parser = argparse.ArgumentParser()

    # Verbosidad, opcional, False por defecto
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Muestra mas informacion al correr el programa'
    )
    # Cantidad de iteraciones, opcional, 50 por defecto
    parser.add_argument(
        '--iters',
        type=int,
        help='Cantidad de iteraciones a efectuar',
        default=50
    )
    # Temperatura inicial
    parser.add_argument(
        '--temp',
        type=float,
        help='Temperatura inicial',
        default=100.0
    )
    # Archivo del cual leer el grafo
    parser.add_argument(
        'file_name',
        help='Archivo del cual leer el grafo a dibujar'
    )

    args = parser.parse_args()

    # Descomentar abajo para ver funcionamiento de argparse
    # print(args.verbose)
    # print(args.iters) 
    # print(args.file_name)
    # print(args.temp)
    # return


    # Leo el grafo del archivo pasado
    grafo_archivo = lee_grafo_archivo(args.file_name)

    print(grafo_archivo)


    # TODO: Borrar antes de la entrega
    grafo1 = ([1, 2, 3, 4, 5, 6, 7],
              [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 1)])

    # Creamos nuestro objeto LayoutGraph
    layout_gr = LayoutGraph(
        grafo=grafo_archivo,  # TODO: Cambiar para usar grafo leido de archivo
        iters=args.iters,
        refresh=1,
        c1=0.1,
        c2=5.0,
        temperatura=args.temp,
        verbose=args.verbose
    )

    # Ejecutamos el layout
    layout_gr.layout()
    return


if __name__ == '__main__':
    main()
