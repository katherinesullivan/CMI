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
    vertices = grafo[0]
    aristas = grafo[1]
    dicc_aristas = verticesADiccionario(grafo)
    vertices_visitados = []
    aristas_visitadas = []

    while len(aristas_visitadas) < (len(vertices) - 1):
        peso_min = float('inf')
        min_arista = []
        for arista in aristas:
            if arista[2] < peso_min:
                if ((arista[0] not in vertices_visitados) | (arista[1] not in vertices_visitados)):
                    min_arista = arista
                    peso_min = arista[2]
        if min_arista != []:
            aristas_visitadas.append(min_arista)
            aristas.remove(min_arista)
            # vertices_visitados.append(min_arista[0])
            vertices_visitados.append(min_arista[1])
            vertices_visitados = list(set(vertices_visitados))

            for [ar,p] in dicc_aristas[min_arista[0]]:
                    if min_arista[1] == ar:
                        if [min_arista[1],ar,p] in aristas:
                            aristas.remove([min_arista[1],ar,p])
                        if [ar,min_arista[1],p] in aristas:
                            aristas.remove([ar,min_arista[1],p])
            for [ar,p] in dicc_aristas[min_arista[1]]:
                    if min_arista[0] == ar:
                        if [min_arista[0],ar,p] in aristas:
                            aristas.remove([min_arista[0],ar,p])
                        if [ar,min_arista[0],p] in aristas:
                            aristas.remove([ar,min_arista[0],p])
            
            
            
            
            
            
            # if min_arista[0] in vertices_visitados: 
            #     # vertices_visitados.append(min_arista[1])
            #     for [ar,p] in dicc_aristas[min_arista[1]]: # dudoso
            #         if min_arista[0] == ar:
            #             if [min_arista[0],ar,p] in aristas:
            #                 aristas.remove([min_arista[0],ar,p])
            #             if [ar,min_arista[0],p] in aristas:
            #                 aristas.remove([ar,min_arista[0],p])
            # else:
            #     # vertices_visitados.append(min_arista[0])
            #     for [ar,p] in dicc_aristas[min_arista[0]]:
            #         if min_arista[1] == ar:
            #             if [min_arista[1],ar,p] in aristas:
            #                 aristas.remove([min_arista[1],ar,p])
            #             if [ar,min_arista[1],p] in aristas:
            #                 aristas.remove([ar,min_arista[1],p])
    MST = (vertices, aristas_visitadas)



    return MST





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