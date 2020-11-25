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







def kruskal(grafo): # NO ANDA
    """
    Dado un grafo (en formato de listas con pesos), aplica el algoritmo de
    Kruskal y retorna el MST correspondiente (o un bosque, en el caso de que
    no sea conexo).
    """
    vertices = grafo[0]
    aristas = grafo[1]
    dicc_aristas = verticesADiccionario(grafo)
    # vertices_visitados = []
    aristas_visitadas = []
    MST = (vertices, aristas_visitadas)

    while len(aristas_visitadas) < (len(vertices) - 1):
        peso_min = float('inf')
        min_arista = []
        for arista in aristas:
            if arista[2] < peso_min:
                # if ((arista[0] not in vertices_visitados) | (arista[1] not in vertices_visitados)):
                if not(existe_camino(MST,arista[0],arista[1])):
                    print(existe_camino(MST,arista[0],arista[1]))
                    min_arista = arista
                    peso_min = arista[2]
        if min_arista != []:
            aristas_visitadas.append(min_arista)
            aristas.remove(min_arista)
            # vertices_visitados.append(min_arista[0])
            # vertices_visitados.append(min_arista[1])
            # vertices_visitados = list(set(vertices_visitados))


            
            # for [ar,p] in dicc_aristas[min_arista[0]]:
            #         if min_arista[1] == ar:
            #             if [min_arista[1],ar,p] in aristas:
            #                 aristas.remove([min_arista[1],ar,p])
            #             if [ar,min_arista[1],p] in aristas:
            #                 aristas.remove([ar,min_arista[1],p])
            # for [ar,p] in dicc_aristas[min_arista[1]]:
            #         if min_arista[0] == ar:
            #             if [min_arista[0],ar,p] in aristas:
            #                 aristas.remove([min_arista[0],ar,p])
            #             if [ar,min_arista[0],p] in aristas:
            #                 aristas.remove([ar,min_arista[0],p])




    return MST


def existe_camino(grafo, a, b):
    dicc_aristas = verticesADiccionario(grafo)
    if ((dicc_aristas[a] == []) | (dicc_aristas[b] == [])):
        return 0
    else:
        bandera = 0
        for [ar1,p1] in dicc_aristas[a]:
            for [ar2,p2] in dicc_aristas[b]:
                if ar1 == ar2:
                    bandera = 1
        return bandera



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
    grafo2 = (
            # Nodos
            ['a', 'b', 'c', 'd'], 
            # Aristas
            [ 
                ('a', 'b', 10),
                ('c', 'a', 30),
                ('a', 'd', 28),
                ('c', 'b', 20),
                ('d', 'c', 6),
                ('b', 'd', 15)
            ]
        )
    print(prim(grafo2))
    print(kruskal(grafo1))


if __name__ == "__main__":
    main()









# EJEMPLO DE KRUSKAL QUE ANDA PERO CON OTRA ESTRUCTURA DE GRAFOS


# parent = dict()
# rank = dict()

# def make_set(vertice):
#     parent[vertice] = vertice
#     rank[vertice] = 0

# def find(vertice):
#     if parent[vertice] != vertice:
#         parent[vertice] = find(parent[vertice])
#     return parent[vertice]

# def union(vertice1, vertice2):
#     root1 = find(vertice1)
#     root2 = find(vertice2)
#     if root1 != root2:
#         if rank[root1] > rank[root2]:
#             parent[root2] = root1
#         else:
#             parent[root1] = root2
#             if rank[root1] == rank[root2]: rank[root2] += 1

# def kruskal(graph):
#     for vertice in graph['vertices']:
#         make_set(vertice)

#     minimum_spanning_tree = set()
#     edges = sorted(graph['edges'], key=lambda e: e[2])

#     for edge in edges:
#         vertice1, vertice2, weight = edge
#         if find(vertice1) != find(vertice2):
#             union(vertice1, vertice2)
#             minimum_spanning_tree.add(edge)
#     return minimum_spanning_tree



# grafo2 = {
#         'vertices': ['a', 'b', 'c', 'd'], 
#         'edges': set([
#                 ('a', 'b', 10),
#                 ('c', 'a', 30),
#                 ('a', 'd', 28),
#                 ('c', 'b', 20),
#                 ('d', 'c', 6),
#                 ('b', 'd', 15)
#             ])
#         }


# graph = {
#     'vertices': [0,1, 2, 3, 4, 5],
#     'edges': set([     #(first node, second node, weight)
#         (0, 3,5),
#         (3, 5,2),
#         ( 5, 4,10),
#         ( 4, 1,3),
#         (1, 0,8),
#         (0, 2,1),(2,3,6),( 2,5,4),( 2,4,9),(2,1,7),
#         ])
#     }

# a = kruskal(grafo2)

# print(a)
