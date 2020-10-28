#! /usr/bin/python

# 1ra Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

import sys
import string

def lee_grafo_stdin():
    '''
    Lee un grafo desde entrada estandar y devuelve su representacion como lista.
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
    n = int(input())
    while (n != 0):
        vertice = input().strip(" ")
        vertices.append(vertice)
        n-=1
    for arista in sys.stdin:
        #arista.translate({ord(c): None for c in string.whitespace})
        arista_new = []
        arista_new.append(arista[0])
        arista_new.append(arista[2])
        aristas.append(tuple(arista_new))
    return grafo
    #else:
    #  print("No se ingreso un numero de vertices")


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




def imprime_grafo_lista(grafo):
    '''
    Muestra por pantalla un grafo. El argumento esta en formato de lista.
    '''
    pass

def vertices_a_numeros(lista):
    diccionario = {}

    for x in lista:
        diccionario[x]= i


def lista_a_incidencia(grafo_lista):
    '''
    Transforma un grafo representado por listas a su representacion 
    en matriz de incidencia.
    '''
    vertices = grafo_lista[0]
    aristas = grafo_lista[1]
    filas = []
    matriz = (vertices, filas)
    #fila_vacia = list(map(int, list('0'*len(vertices))))
    dicc = {}
    i = 0
    for x in vertices:
        filas.append(list(map(int, list('0'*len(aristas)))))
        dicc[x] = i
        i+=1
    j=0
    while(j<len(aristas)):
        origen = dicc[aristas[j][0]]
        print(k)
        destino = dicc[aristas[j][1]]
        print(j)
        filas[origen][j] = 1
        filas[destino][j] = 2
        j+=1
    return matriz




        
    #for arista in aristas:
        
    

    

def incidencia_a_lista(grafo_incidencia):
    '''
    Transforma un grafo representado una matriz de incidencia a su 
    representacion por listas.
    '''
    vertices = grafo_incidencia[0]
    matriz = grafo_incidencia[1]
    n = len(vertices)
    cant_columnas = len(matriz[0])
    aristas = []
    arista_a_formar = [0,0]
    nro_columna = 0
    while (nro_columna < cant_columnas):
        fila_vertice = 0
        while (fila_vertice < n):
            if (matriz[fila_vertice][columna] == 1):
                arista_a_formar[0] = vertices[fila_vertice]
            if (matriz[fila_vertice][columna] == 2):
                arista_a_formar[1] = vertices[fila_vertice]
            if (fila_vertice == n-1):
                aristas.append(tuple(arista_a_formar))
            fila_vertice +=1
        nro_columna += 1
    grafo = (n, vertices, aristas)
    return grafo

    


def imprime_grafo_incidencia(grafo_incidencia):
    '''
    Muestra por pantalla un grafo. 
    El argumento esta en formato de matriz de incidencia.
    '''
    pass


def lista_a_adyacencia(grafo_lista):
    '''
    Transforma un grafo representado por listas a su representacion 
    en matriz de adyacencia.
    '''
    vertices = grafo_lista[0]
    aristas = grafo_lista[1]
    filas = []
    matriz = (vertices, filas)
    #fila_vacia = list(map(int, list('0'*len(vertices))))
    dicc = {}
    i = 0
    for x in vertices:
        #fila = []
        #for n in vertices:
        #    fila.append(0)
        filas.append(list(map(int, list('0'*len(vertices)))))
        dicc[x] = i
        i+=1
    for arista in aristas:
        #definicion bien? pq hay un 2 en el ejemplo
        k = dicc[arista[0]]
        print(k)
        j = dicc[arista[1]]
        print(j)
        filas[k][j] = 1
    return matriz


def adyacencia_a_lista(grafo_adyacencia):
    '''
    Transforma un grafo representado una matriz de adyacencia a su 
    representacion por listas.
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
                # en este caso, estamos trabajando con grafos dirigidos 
                # simples (es decir, sin lazos y no multigrafos), por lo tanto
                # no vamos a encontrarnos con entradas mayores a 1
                aristas.append((vertices[i], vertices[j]))
            j+=1
        i+=1
    grafo_lista = (vertices, aristas)
    return grafo_lista


def imprime_grafo_adyacencia(grafo_adyacencia):
    '''
    Muestra por pantalla un grafo. 
    El argumento esta en formato de matriz de adyacencia.
    '''
    pass


#################### FIN EJERCICIO PRACTICA ####################
grafo_adyacencia1 = (
    ['A', 'B', 'C', 'D'], 
    [[0, 1, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0],]
)

grafo_adyacencia2 = (
    ['A', 'B', 'C', 'D'], 
    [[0, 2, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0],]
)



# import sys
def lee_entrada_0():
	count = 0
	for line in sys.stdin:
		count = count + 1
		print ('Linea: [{0}]'.format(line.strip()))
	print ('leidas {0} lineas'.format(count))

	
def lee_entrada_1():
	count = 0
	try:
		while True:
			line = input().strip()
			count = count + 1
			print ('Linea: [{0}]'.format(line))
	except EOFError:
		pass
	
	print ('leidas {0} lineas'.format(count))
   

def lee_archivo(file_path):
	print ('leyendo archivo: {0}'.format(file_path))
	count = 0

	with open(file_path, 'r') as f:
		first_line = f.readline()
		print ('primer linea: [{}]'.format(first_line))
		for line in f:
			count = count + 1
			print ('Linea: [{0}]'.format(line))	
	print ('leidas {0} lineas'.format(count))


def main():
    grafo = lee_grafo_archivo("prueba.txt")
    print(lista_a_adyacencia(grafo))
    print(adyacencia_a_lista(lista_a_adyacencia(grafo)))
    #p="prueba.txt"
    #lee_archivo(p)

if __name__ == '__main__':
    main()

#lee_entrada_1()

# ctrl+d para terminar stdin


#CONSULTAS:

#dirigido
#definicion
#imprimir
#complejidad