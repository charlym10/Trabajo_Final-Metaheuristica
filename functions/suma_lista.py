from typing import List


def suma_lista(lista: List[int]) -> int:
    suma: int = 0
    for i in lista:
        suma = suma + i
    return suma