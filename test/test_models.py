from models.Mochila import Mochila
from typing import Any, Dict
import unittest


class TestMochila(unittest.TestCase):

    def setUp(self) -> None:

        self.data: Dict[str, Any] = {
            'tamano': 10,
            'pesos':  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'valores': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'capacidad': 15,
            'elementos': [None for i in range(10)]
        }

        return super().setUp()

    def test_mochila_con_elementos(self):

        individuo: Mochila = Mochila(
            elementos=[0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
            tamano=self.data['tamano'],
            pesos=self.data['pesos'],
            valores=self.data['valores'],
            capacidad=self.data['capacidad']
        )

        comparacion: str = (
            'Solución: [0, 1, 1, 0, 1, 1, 1, 0, 1, 0]' + '\n' +
            'Función Objetivo: 32' + '\n' +
            'Ocupación: [■■■■■■■■■■■■■■■■■■■■]213.33%' + '\n' +
            'Es Factible: False'
        )
        
        self.assertEqual(individuo.__str__(), comparacion)

    def test_mochila_sin_elementos(self):

        individuo: Mochila = Mochila(
            tamano=self.data['tamano'],
            pesos=self.data['pesos'],
            valores=self.data['valores'],
            capacidad=self.data['capacidad']
        )
        
        lista_vacia: list = []

        self.assertNotEqual(individuo.elementos, lista_vacia)

    def test_mochila_elementos_ceros(self):

        individuo: Mochila = Mochila(
            elementos=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            tamano=self.data['tamano'],
            pesos=self.data['pesos'],
            valores=self.data['valores'],
            capacidad=self.data['capacidad']
        )

        comparacion: str = (
            'Solución: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]' + '\n' +
            'Función Objetivo: 0' + '\n' + 
            'Ocupación: [                    ]0.00%' + '\n' +
            'Es Factible: True'
        )
        
        self.assertEqual(individuo.__str__(), comparacion)

