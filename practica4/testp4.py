#! /usr/bin/python

"""Tests complementarios practica 4"""

import unittest

import practica4 as p4


class TestEj1(unittest.TestCase):

    def test_1_1(self):
        grafo1 = (['a', 'b'], [('a', 'b', 1)])
        
        res = p4.dijkstra(grafo1, 'a')
        
        self.assertTrue('a' in res) # se puede llegar a 'a'      
        self.assertTrue('b' in res) # se puede llegar a 'b'
      
        self.assertEqual(res['a'], 0) # Costo a 'a'
        self.assertEqual(res['b'], 1) # Costo a 'b'

    def test_1_2(self):
        grafo2 = (['a', 'b', 'c', 'd'], [('a', 'b', 1), ('a', 'a', 0.5), ('b', 'c', 1.5), ('a', 'c', 5)])

        res = p4.dijkstra(grafo2, 'a')

        self.assertTrue('a' in res) # se puede llegar a 'a'      
        self.assertTrue('b' in res) # se puede llegar a 'b'
        self.assertTrue('c' in res) # se puede llegar a 'c'
        self.assertFalse('d' in res) # no se puede llegar a 'd'

        self.assertEqual(res['a'], 0) # Costo a 'a'
        self.assertEqual(res['b'], 1) # Costo a 'b'
        self.assertEqual(res['c'], 2.5) # Costo a 'c'


class TestEj2(unittest.TestCase):

    def test_2_1(self):
        grafo1 = (['a', 'b'], [('a', 'b', 1)])
        caminos_esperados = {
            'a' : ['a'],
            'b' : ['a', 'b']          
        }

        res = p4.dijkstra_2(grafo1, 'a')

        self.assertTrue('a' in res) # se puede llegar a 'a'      
        self.assertTrue('b' in res) # se puede llegar a 'b'
        
        for nodo, camino_res in res.items():
            camino_esperado = caminos_esperados[nodo]
            self.comparar_caminos(camino_res, camino_esperado)

    def test_2_2(self):
        grafo2 = (['a', 'b', 'c', 'd'], [('a', 'b', 1), ('a', 'a', 0.5), ('b', 'c', 1.5), ('a', 'c', 5)])
        caminos_esperados = {
            'a' : ['a'],
            'b' : ['a', 'b'],
            'c' : ['a', 'b', 'c']
        }
        
        res = p4.dijkstra_2(grafo2, 'a')
        
        self.assertTrue('a' in res) # se puede llegar a 'a'      
        self.assertTrue('b' in res) # se puede llegar a 'b'
        self.assertTrue('c' in res) # se puede llegar a 'c'
        self.assertFalse('d' in res) # no se puede llegar a 'd'

        for nodo, camino_res in res.items():
            camino_esperado = caminos_esperados[nodo]
            self.comparar_caminos(camino_res, camino_esperado)

    def test_2_3(self):
        grafo3 = (['a', 'b', 'c', 'd'], [('a', 'b', 1), ('a', 'a', 0.5), ('b', 'c', 1.5), ('a', 'c', 0.5)])
        caminos_esperados = {
            'a' : ['a'],
            'b' : ['a', 'b'],
            'c' : ['a','c']
        }
        
        res = p4.dijkstra_2(grafo3, 'a')
        
        self.assertTrue('a' in res) # se puede llegar a 'a'      
        self.assertTrue('b' in res) # se puede llegar a 'b'
        self.assertTrue('c' in res) # se puede llegar a 'c'
        self.assertFalse('d' in res) # no se puede llegar a 'd'

        for nodo, camino_res in res.items():
            camino_esperado = caminos_esperados[nodo]
            self.comparar_caminos(camino_res, camino_esperado)
            
    def comparar_caminos(self, camino_1, camino_2):
        # Comparar longitud caminos
        self.assertEqual(len(camino_1), len(camino_2))
        # Comparar elementos
        for i in range(len(camino_1)):
            self.assertEqual(camino_1[i], camino_2[i])


if __name__ == '__main__':
    unittest.main()
