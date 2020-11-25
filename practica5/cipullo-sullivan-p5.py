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
    vertices_visitados.append(vertices[0])
    for a in dicc_aristas[vertices[0]]:
        aristas_a_recorrer.append((vertices[0], a[0], a[1]))
    while len(vertices_visitados) < len(vertices):
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