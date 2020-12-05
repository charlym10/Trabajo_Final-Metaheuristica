from random import randint
from models.Mochila import Mochila


def swap(hijo: Mochila, n: int) -> Mochila:
    hijo_mutado: Mochila = hijo.copy()
    aleatorio_1: int = randint(1, n) - 1
    aleatorio_2: int  = randint(1, n) - 1
    
    temp: int = hijo_mutado.elementos[aleatorio_1]
    hijo_mutado.elementos[aleatorio_1] = hijo_mutado.elementos[aleatorio_2]
    hijo_mutado.elementos[aleatorio_2] = temp

    hijo_mutado.elementos = hijo_mutado.elementos # Actualizar cálculos

    return hijo_mutado