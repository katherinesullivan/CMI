import unittest

from practica2 import componentes_conexas


class TestComponentesConexas(unittest.TestCase):

    graph_1 = ([], [])
    graph_2 = (['a'], [])
    graph_3 = (['a'], [('a', 'a')])
    graph_4 = (['a', 'b'], [('a', 'b')])
    graph_5 = (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])
    graph_6 = (['a', 'b', 'c', 'd'],
               [('a', 'b'), ('b', 'c'), ('a', 'd'), ('c', 'd'), ('d', 'a')])
    graph_7 = (['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'b'), ('b', 'c'), ('d', 'e')])
    graph_8 = (['a', 'b', 'c', 'd', 'e', 'f'], [('c', 'f'), ('b', 'c'), ('a', 'a'), ('e', 'a')])

    componentes_conexas = [
        (graph_1, {}),
        (graph_2, {'a': 0}),
        (graph_3, {'a': 0}),
        (graph_4, {'a': 0, 'b': 0}),
        (graph_5, {'a': 0, 'b': 0, 'c': 0}),
        (graph_6, {'a': 0, 'b': 0, 'c': 0, 'd': 0}),
        (graph_7, {'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 1, 'f': 2}),
        (graph_8, {'a': 0, 'b': 1, 'c': 1, 'd': 2, 'e': 0, 'f': 1})
    ]

    def componentes_conexas_set(self, disjoint_set):
        """
        Dado un disjoint set, obtiene sus componentes conexas como sets.
        Ejemplo formato salida:
            {{'a, 'b'}, {'c'}, {'d'}}
        """
        comps = set(disjoint_set.values())
        return {frozenset([k for k in disjoint_set.keys() if disjoint_set[k] == n]) for n in comps}

    def test_componentes_conexas(self):
        for graph, disjoint_set in self.componentes_conexas:
            result = componentes_conexas(graph)
            self.assertTrue(
                self.componentes_conexas_set(disjoint_set) == self.componentes_conexas_set(result),
                'caso: test_componentes_conexas({})'.format(graph)
            )

