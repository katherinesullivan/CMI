import argparse
import matplotlib.pyplot as plt
import numpy as np

def coordenadas_random(N):
    return np.random.rand(N) * 1000 


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
    
    return 0
    


def main():
    g = (['A','B','C'],[('A','B'),('B','C'),('C','A')])

    plt.show()
    for i in range(5):
        plt.axis([0,1000,0,1000])
        draws_graph(g)
        plt.pause(0.5)
        plt.clf()


if __name__ == '__main__':
    main()