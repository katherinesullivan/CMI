#! /usr/bin/python

# 5ta Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

def verticesADiccionario(grafo):
    graph = {v: [] for v in grafo[0]}
    for (u, v, p) in grafo[1]:
        graph[u].append([v, p])
        graph[v].append([u, p])
    return graph

def prim(grafo):
    """
    Dado un grafo (en formato de listas con pesos), aplica el algoritmo de Prim
    y retorna el MST correspondiente.
    NOTA: El grafo de entrada se asume conexo.
    """
    vertices = grafo[0]
    aristas = grafo[1]
    dicc_aristas = verticesADiccionario(grafo)
    vertices_visitados = []
    aristas_visitadas = []
    MST = (vertices_visitados, aristas_visitadas)
    aristas_a_recorrer = []
    for v in vertices:
        if v not in vertices_visitados:
            vertices_visitados.append(v)
            for a in dicc_aristas[v]:
                aristas_a_recorrer.append((v, a[0], a[1]))
        peso_min = float('inf')
        arista_a_agg = []
        for e in aristas_a_recorrer:
            if e[2] < peso_min:
                if e[1] not in vertices_visitados:
                    peso_min = e[2]
                    arista_a_agg = [e[0], e[1], e[2]]
        if arista_a_agg != []:
            vertices_visitados.append(arista_a_agg[1])
            for arista in dicc_aristas[arista_a_agg[1]]:
                aristas_a_recorrer.append((arista_a_agg[1], arista[0], arista[1]))
            aristas_visitadas.append(tuple(arista_a_agg))
    return MST







def kruskal(grafo):
    """
    Dado un grafo (en formato de listas con pesos), aplica el algoritmo de
    Kruskal y retorna el MST correspondiente (o un bosque, en el caso de que
    no sea conexo).
    """
    pass


def main():
    grafo1 = (
            # Nodos
            ['a', 'b', 'c'], 
            # Aristas
            [ 
                ('a', 'b', 1),
                ('b', 'a', 2),
                ('c', 'b', 4),
                ('b', 'c', 3),
                ('b', 'c', 5)
            ]
        )
    print(prim(grafo1))


if __name__ == "__main__":
    main()