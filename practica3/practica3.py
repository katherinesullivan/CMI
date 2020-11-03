#! /usr/bin/python
# -*- coding: utf-8 -*-

# 3ra Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

"""
Recordatorio: 
- Un camino/ciclo es Euleriano si contiene exactamente 1 vez
a cada arista del grafo
- Un camino/ciclo es Hamiltoniano si contiene exactamente 1 vez
a cada vértice del grafo
"""


def esCaminoEuleriano(grafo, path):
    """Comprueba si una lista de aristas constituye un camino euleriano
    en un grafo.

    Args:
        graph (grafo): Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

        path (lista de aristas): posible camino
                                 Ej: [('a', 'b'), ('b', 'c')]

    Returns:
        boolean: path es camino euleriano en graph

    Raises:
        TypeError: Cuando el tipo de un argumento es inválido
    """
    # chequeamos que sea efectivamente un camino con aristas del grafo
    #for arista in path:
    #    if arista not in grafo[1]:
    #        return False
    # podríamos chequear que las aristas consecutivas sean correctas con
    # podría meter esto en el de arriba usando esta iteración 
    i = 0
    while (i<=len(path)-2):
        if path[i][1] != path[i+1][0]:
            return False
        if (path[i] not in grafo[1]):
            return False
        i+=1
    if path[i] not in grafo[1]:
        return False
    # chequeamos que no haya aristas repetidas
    right_path = list(dict.fromkeys(path).keys())
    if right_path != path:
        return False
    # chequeamos que el camino sea euleriano
    for arista in grafo[1]:
        if arista not in path:
            return False
    return True


def esCicloEuleriano(grafo, path):
    """Comprueba si una lista de aristas constituye un ciclo euleriano
    en un grafo.

    Args:
        graph (grafo): Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

        path (lista de aristas): posible ciclo
                                 Ej: [('a', 'b'), ('b', 'c')]

    Returns:
        boolean: path es ciclo euleriano en graph

    Raises:
        TypeError: Cuando el tipo de un argumento es inválido
    """
    if not esCaminoEuleriano(grafo, path):
        return False
    # chequeamos que sea efectivamente un ciclo
    primer_vertice = path[0][0]
    ultimo_vertice = path[len(path)-1][1]
    if primer_vertice != ultimo_vertice:
        return False
    return True
    


def esCaminoHamiltoniano(grafo, camino):
    """Comprueba si una lista de aristas constituye un camino hamiltoniano
    en un grafo.

    Args:
        graph (grafo): Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

        path (lista de aristas): posible camino
                                 Ej: [('a', 'b'), ('b', 'c')]

    Returns:
        boolean: path es camino hamiltoniano en graph

    Raises:
        TypeError: Cuando el tipo de un argumento es inválido
    """
    # chequeamos que sea con aristas del grafo y que constituyan un camino
    i = 0
    utilizados = []
    while (i<=len(path)-2):
        if path[i][1] != path[i+1][0]:
            return False
        if (path[i] not in grafo[1]):
            return False
        # vamos chequeando que los vértices no se repitan
        if path[i][1] in utilizados:
            return False
        else:
            utilizados.append(path[i][1])
        i+=1
    if path[i] not in grafo[1]:
        return False
    # vemos que hayamos usado todo los vértices
    utilizados.append(path[0][0])
    if set(utilizados) != set(grafo[1]):
        return False
    return True
    
    


def esCicloHamiltoniano(grafo, ciclo):
    """Comprueba si una lista de aristas constituye un ciclo hamiltoniano
    en un grafo.

    Args:
        graph (grafo): Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

        path (lista de aristas): posible ciclo
                                 Ej: [('a', 'b'), ('b', 'c')]

    Returns:
        boolean: path es ciclo hamiltoniano en graph

    Raises:
        TypeError: Cuando el tipo de un argumento es inválido
    """
    if not esCaminoHamiltoniano(path):
        return False
    # chequeamos que sea un ciclo
    primer_vertice = path[0][0]
    ultimo_vertice = path[len(path)-1][1]
    if primer_vertice != ultimo_vertice:
        return False
    return True

def tieneCaminoEuleriano(grafo):
    """Comprueba si un grafo no dirigido tiene un camino euleriano.

    Args:
        graph (grafo): Grafo en formato de listas.
                       Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

    Returns:
        boolean: graph tiene un camino euleriano

    Raises:
        TypeError: Cuando el tipo del argumento es inválido
    """
    grados_impares = 0
    grado = dict.fromkeys(grafo[0], 0)
    for vertice in grafo[0]:
        for arista in grafo[1]:
            if vertice in arista:
                grado[vertice] += 1
        # aca ya tengo el grado de este vértice
        if (grado[vertice] % 2 != 0):
            grados_impares += 1
    # una vez que ya tengo todos los grados
    if (grados_impares != 0 and grados_impares != 2):
        return False
    return True



class Graph:
    """Definimos esta clase como ayuda a la implementación del algoritmo de Fleury
    """

    def __init__(self, grafo_lista):
        """Inicializamos el grafo a partir de un grafo en representación de lista
        """

        self.V = grafo_lista[0]
        self.graph = self.fromListToDicc(grafo_lista)

    def fromListToDicc(self, grafo_lista):
        """Toma un grafo no dirigido en representación de lista y retorna un diccionario, en donde las claves
        son vértices y los valores son listas de vértices, representando cada una de las aristas. Por ejemplo:
        {'a': ['b', 'e'],..} representa la existencia de las aristas ('a','b') y ('a','e')
        """
        graph = {v: [] for v in grafo_lista[0]}
        for (u, v) in grafo_lista[1]:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def removeEdge(self, u, v):
        """Dados dos vértices (u y v), elimina la arista (u,v) (y también la arista (v,u) puesto que es un grafo
        no dirigido)
        """
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def addEdge(self, u, v):
        """Dados dos vértices (u y v), agrega la arista (u,v) (y también la arista (v,u) puesto que es un grafo
        no dirigido)"""
        self.graph[u].append(v)
        self.graph[v].append(u)

    def reachableVertices(self, v, visited):
        """Cuenta la cantidad de vértices alcanzables desde v, haciendo una búsqueda en profundidad.
        El argumento visited es un diccionario en donde las claves son los vértices, y los valores
        corresponden a un booleano indicando si el vértice fue visitado o no.
        La primera vez que se llama al método, ningún vértice debe haber sido visitado.
        """
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                count = count + self.reachableVertices(i, visited)
        return count

    def isElegibleNextEdge(self, u, v):
        """Determina si la arista (u,v) es elegible como próxima arista a visitar."""
        pass

    def printEuler(self, u):
        """Imprime un camino o ciclo euleriano comenzando desde el vértice u.
        """
        pass


def caminoEuleriano(grafo_lista):
    """Obtiene un camino euleriano en un grafo no dirigido, si es posible

    Argumentos:
        grafo: Grafo en formato de listas. 
                Ej: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])

    Retorno:
        lista de aristas: ciclo euleriano, si existe
        None: si no existe un camino euleriano
    """
    # Determinar el vértice de inicio v
    # grafo = Graph(grafo_lista)
    # grafo.printEuler(v)
    pass


def main():
    grafo = (['a', 'b', 'c'], [('a', 'b'), ('b', 'c'), ('c', 'a')])
    path = [('a', 'b'), ('b', 'c'), ('c', 'a')]
    print(esCicloEuleriano(grafo, path))
    


if __name__ == '__main__':
    main()