#! /usr/bin/python

# 6ta Practica Laboratorio 
# Complementos Matematicos I
# Ejemplo parseo argumentos

import argparse
import matplotlib.pyplot as plt
import numpy as np


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
            arista= []
            arista.append(line[0])
            arista.append(line[2])
            aristas.append(tuple(arista))
    return grafo


def coordenadas_random(N):
    return np.random.rand(N) * 1000 # rango 1000 como en el gif??


def draws_graph(grafo):
    n_vertices = len(grafo[0])
    x_coordenadas = coordenadas_random(n_vertices)
    y_coordenadas = coordenadas_random(n_vertices)
    plt.scatter(x_coordenadas,y_coordenadas)
    for i in range(n_vertices):
        x_aristas = []
        y_aristas = []
        for j in range(n_vertices):
            v1 = grafo[0][i]
            v2 = grafo[0][j]
            if (v1,v2) in grafo[1]:
                x_aristas.append(x_coordenadas[i])
                x_aristas.append(x_coordenadas[j])
                y_aristas.append(y_coordenadas[i])
                y_aristas.append(y_coordenadas[j])
                plt.plot(x_aristas,y_aristas)
    plt.draw()
    plt.show()


def initialize_accumulators(N):
    accum_x = {v: 0 for v in N}
    accum_y = {v: 0 for v in N}
    return accum_x, accum_y





class LayoutGraph:

    def __init__(self, grafo, iters, refresh, c1, c2, verbose=False):
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
        self.refresh = refresh
        self.c1 = c1
        self.c2 = c2

    def layout(self):
        """
        Aplica el algoritmo de Fruchtermann-Reingold para obtener (y mostrar)
        un layout
        """

        pass


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
    # print args.verbose
    # print args.iters    
    # print args.file_name
    # print args.temp
    # return

    # TODO: Borrar antes de la entrega
    grafo1 = ([1, 2, 3, 4, 5, 6, 7],
              [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 1)])

    # Creamos nuestro objeto LayoutGraph
    layout_gr = LayoutGraph(
        grafo1,  # TODO: Cambiar para usar grafo leido de archivo
        iters=args.iters,
        refresh=1,
        c1=0.1,
        c2=5.0,
        verbose=args.verbose
    )

    # Ejecutamos el layout
    layout_gr.layout()
    return


if __name__ == '__main__':
    main()
