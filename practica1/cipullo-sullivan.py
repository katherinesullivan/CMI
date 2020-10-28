# Inés Cipullo C-6867/5
# Katherine Sullivan S-5436/4

# Entrega Práctica 1
# Laboratorio CMI

def adyacencia_a_lista(grafo_adyacencia):
    '''
    Transforma un grafo representado una matriz de adyacencia a su 
    representacion por listas.  
    En este caso, estamos trabajando con grafos dirigidos 
    simples (es decir, sin lazos y no multigrafos) y por lo tanto
    las entradas serán 1 o 0.
    '''
    vertices = grafo_adyacencia[0]
    n = len(vertices)
    aristas = []
    matriz = grafo_adyacencia[1]
    i = 0
    # por cada iteración recorreremos la i-ésima fila
    while (i<n):
        j = 0
        # viendo cada entrada
        while (j<n):
            if (matriz[i][j] == 1):
                aristas.append((vertices[i], vertices[j]))
            j+=1
        i+=1
    grafo_lista = (vertices, aristas)
    return grafo_lista