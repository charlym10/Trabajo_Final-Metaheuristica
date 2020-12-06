import unittest
from functions.cruzamiento import cruzamiento
from functions.suma_lista import suma_lista
from functions.swap import swap
from typing import Any, Dict
from models.Mochila import Mochila
from random import seed


class TestCruzamiento(unittest.TestCase):

    def setUp(self) -> None:

        self.data: Dict[str, Any] = {
            'tamano': 10,
            'pesos':  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'valores': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'capacidad': 15,
            'elementos': [None for i in range(10)]
        }

        self.padre: Mochila = Mochila(
            elementos=[0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
            tamano=self.data['tamano'],
            pesos=self.data['pesos'],
            valores=self.data['valores'],
            capacidad=self.data['capacidad']
        )
            
        self.madre: Mochila = Mochila(
            elementos=[0, 1, 1, 1, 0, 0, 1, 0, 1, 1],
            tamano=self.data['tamano'],
            pesos=self.data['pesos'],
            valores=self.data['valores'],
            capacidad=self.data['capacidad']
        )

        seed(30) # aleatorio_1=8, aleatorio_2=4, aleatorio_3=9, aleatorio_4=0, aleatorio_5=9, aleatorio_6=3
        
        return super().setUp()

    def test_resultado_cruzamiento(self):

        hijos = cruzamiento(padre=self.padre, madre=self.madre, data=self.data, cantidad_articulos=self.data['tamano'])

        hijo_1 = hijos['hijo_1']
        hijo_2 = hijos['hijo_2']
        
        self.assertEqual(hijo_1.elementos, [0, 1, 1, 0, 1, 0, 1, 0, 1, 0])
        self.assertEqual(hijo_2.elementos, [0, 1, 1, 1, 0, 1, 1, 0, 1, 1])
        
        hijos = cruzamiento(padre=self.padre, madre=self.madre, data=self.data, cantidad_articulos=self.data['tamano'])

        hijo_1 = hijos['hijo_1']
        hijo_2 = hijos['hijo_2']

        self.assertEqual(hijo_1.elementos, [0, 1, 1, 1, 0, 0, 1, 0, 1, 0])
        self.assertEqual(hijo_2.elementos, [0, 1, 1, 0, 1, 1, 1, 0, 1, 1])

        hijos = cruzamiento(padre=self.padre, madre=self.madre, data=self.data, cantidad_articulos=self.data['tamano'])

        hijo_1 = hijos['hijo_1']
        hijo_2 = hijos['hijo_2']

        self.assertEqual(hijo_1.elementos, [0, 1, 1, 0, 0, 0, 1, 0, 1, 0])
        self.assertEqual(hijo_2.elementos, [0, 1, 1, 1, 1, 1, 1, 0, 1, 1])

    def test_actualizacion_variables_cruzamiento(self):

        hijos = cruzamiento(padre=self.padre, madre=self.madre, data=self.data, cantidad_articulos=self.data['tamano'])

        hijo_1 = hijos['hijo_1']
        hijo_2 = hijos['hijo_2']

        self.assertEqual(hijo_1.f_objetivo, suma_lista([a*b for a,b in zip(hijo_1.valores, hijo_1.elementos)]))
        self.assertEqual(hijo_1.ocupacion, suma_lista([a*b for a,b in zip(hijo_1.pesos, hijo_1.elementos)]))
        self.assertEqual(hijo_1.es_factible, hijo_1.ocupacion <= hijo_1.capacidad)

        self.assertEqual(hijo_2.f_objetivo, suma_lista([a*b for a,b in zip(hijo_2.valores, hijo_2.elementos)]))
        self.assertEqual(hijo_2.ocupacion, suma_lista([a*b for a,b in zip(hijo_2.pesos, hijo_2.elementos)]))
        self.assertEqual(hijo_2.es_factible, hijo_2.ocupacion <= hijo_2.capacidad)

        hijos = cruzamiento(padre=self.padre, madre=self.madre, data=self.data, cantidad_articulos=self.data['tamano'])

        hijo_1 = hijos['hijo_1']
        hijo_2 = hijos['hijo_2']

        self.assertEqual(hijo_1.f_objetivo, suma_lista([a*b for a,b in zip(hijo_1.valores, hijo_1.elementos)]))
        self.assertEqual(hijo_1.ocupacion, suma_lista([a*b for a,b in zip(hijo_1.pesos, hijo_1.elementos)]))
        self.assertEqual(hijo_1.es_factible, hijo_1.ocupacion <= hijo_1.capacidad)

        self.assertEqual(hijo_2.f_objetivo, suma_lista([a*b for a,b in zip(hijo_2.valores, hijo_2.elementos)]))
        self.assertEqual(hijo_2.ocupacion, suma_lista([a*b for a,b in zip(hijo_2.pesos, hijo_2.elementos)]))
        self.assertEqual(hijo_2.es_factible, hijo_2.ocupacion <= hijo_2.capacidad)

class TestSwap(unittest.TestCase):

    def setUp(self) -> None:

        self.data: Dict[str, Any] = {
            'tamano': 10,
            'pesos':  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'valores': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'capacidad': 15,
            'elementos': [None for i in range(10)]
        }

        self.hijo: Mochila = Mochila(
            elementos=[0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
            tamano=self.data['tamano'],
            pesos=self.data['pesos'],
            valores=self.data['valores'],
            capacidad=self.data['capacidad']
        )

        seed(30) # aleatorio_1=8, aleatorio_2=4, aleatorio_3=9, aleatorio_4=0, aleatorio_5=9, aleatorio_6=3

        return super().setUp()

    def test_sawp(self):

        hijo_mutado = swap(self.hijo, self.hijo.tamano)

        self.assertEqual(hijo_mutado.elementos, [0, 1, 1, 0, 1, 1, 1, 0, 1, 0])

        hijo_mutado = swap(self.hijo, self.hijo.tamano)

        self.assertEqual(hijo_mutado.elementos, [0, 1, 1, 0, 1, 1, 1, 0, 1, 0])

        hijo_mutado = swap(self.hijo, self.hijo.tamano)

        self.assertEqual(hijo_mutado.elementos, [0, 1, 1, 0, 1, 1, 1, 0, 1, 0])
