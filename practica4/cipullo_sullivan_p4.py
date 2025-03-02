def verticesADiccionario(grafo):
    graph = {v: [] for v in grafo[0]}
    for (u, v, p) in grafo[1]:
        graph[u].append([v, p])
        graph[v].append([u, p])
    return graph

def dijkstra(grafo, vertice):
    """
    Dado un grafo (en formato de listas con pesos), aplica el algoritmo de
    Dijkstra para hallar el COSTO del camino mas corto desde el vertice de origen
    al resto de los vertices.
    Formato resultado: {'a': 10, 'b': 5, 'c': 0}
    (Nodos que no son claves significa que no hay camino a ellos)
    """
    vertices = grafo[0]
    aristas = grafo[1]
    dicc_aristas = verticesADiccionario(grafo)
    distancia = {}
    vertices_visitados = [vertice]
    for v in vertices:
        if v != vertice:
            distancia[v] = float('inf')
        else:
            distancia[v] = 0
    vertice_actual = vertice
    while len(vertices_visitados) < len(vertices):
        for ver in dicc_aristas[vertice_actual]:
            if distancia[ver[0]] > distancia[vertice_actual] + ver[1]:
                distancia[ver[0]] = distancia[vertice_actual] + ver[1]
        next_vertice = []
        dist_min = float('inf')
        for v in vertices:
            if v not in vertices_visitados:
                if dist_min > distancia[v]:
                    dist_min = distancia[v]
                    next_vertice = v
        vertice_actual = next_vertice
        vertices_visitados.append(vertice_actual)
    for v in vertices:
        if distancia[v] == float('inf'):
            del distancia[v]
    return distancia
