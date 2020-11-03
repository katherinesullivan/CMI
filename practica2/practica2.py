#! /usr/bin/python

# 2da Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

# Un disjointSet lo representaremos como un diccionario. 
# Ejemplo: {'A':1, 'B':2, 'C':1} (Nodos A y C pertenecen al conjunto 
# identificado con 1, B al identificado on 2)

grafo_lista =  (['A','B','C','D','E','F','G'],[('A','B'),('B','C'),('A','B'),('C','D'),('E','F')])

def make_set(lista):
    '''
    Inicializa una lista de vértices de modo que cada uno de sus elementos pasen a ser conjuntos unitarios. 
    Retorna un disjointSet.
    '''
    indices = [*range(1, len(lista)+1)]
    disjoint_set = dict(zip(lista, indices))
    return disjoint_set

def find(elem, disjoint_set):
    '''
    Obtiene el identificador del conjunto de vértices al que pertenece el elemento.
    '''
    return disjoint_set[elem]


def union(id_1, id_2, disjoint_set):
    '''
    Dado dos identificadores de conjuntos de vértices, une dichos conjuntos.
    Retorna la estructura actualizada
    '''
    new_value = disjoint_set[id_1]
    disjoint_set[id_2] = new_value
    return disjoint_set


def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo:
        Entrada: [['a','b','c','d'], [('a', 'b')]]  
        Salida: [['a, 'b'], ['c'], ['d']]
    '''
    disjoint_set = make_set(grafo_lista[0])
    for arista in grafo_lista[1]:
        union(arista[0], arista[1], disjoint_set)
    conexas = {}
    for key, value in disjoint_set.items():
        if value not in conexas:
            conexas[value] = [key]
        else:
            conexas[value].append(key)
    return list(conexas.values())




def main():
    print(componentes_conexas(grafo_lista))
    return 0

if __name__ == '__main__':
    main()