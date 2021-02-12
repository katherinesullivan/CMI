Laboratorio de la materia Complementos de Matemática I
Trabajo práctico final 
Inés Cipullo - Katherine Sullivan

El objetivo del programa es la visualización de grafos. Para ello se requerirá de la librería matplotlib. 
Para hacer uso del mismo se debe correr el archivo 'Cipullo_Sullivan_TPFinal.py'.

El único parámetro obligatorio para correr el programa es el nombre del archivo donde se encuentra el grafo a visualizar. El mismo debe seguir la forma:
número de vértices
nombre de vértice 1
...
nombre de vértice n
vértice1 de la arista1 espacio vértice2 de la arista1
...
vértice1 de la aristak espacio vértice2 de la aristak
fin archivo

Luego existen los siguientes argumentos opcionales:
Verbosidad, opcional, False por defecto: '-v', '--verbose'
Cantidad de iteraciones, opcional, 50 por defecto: '--iters'
Temperatura inicial, opcional, 100 por defecto: '--temp'
Color del grafo, opcional, negro por defecto: '-c', '--color'
Cantidad de iteraciones cada cuantas se muestra una imagen del grafo: '-r', '--refresh'