from functions.suma_lista import suma_lista
from typing import Any, List
from pydantic.main import BaseModel
from random import randint


class Mochila(BaseModel):
    tamano: int
    elementos: List[bool] = []
    pesos: List[int]
    valores: List[int]
    capacidad: int
    ocupacion: int = 0
    f_objetivo: int = 0
    es_factible: bool = False

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        if __pydantic_self__.elementos == []:
            __pydantic_self__.elementos = [randint(0, 1) for i in range(__pydantic_self__.tamano)]
        __pydantic_self__.f_objetivo = suma_lista([
            __pydantic_self__.valores[i]*__pydantic_self__.elementos[i]
                for i in range(__pydantic_self__.tamano)
        ])
        __pydantic_self__.ocupacion = suma_lista([
            __pydantic_self__.pesos[i]*__pydantic_self__.elementos[i]
                for i in range(__pydantic_self__.tamano)
        ])
        __pydantic_self__.es_factible = __pydantic_self__.ocupacion <= __pydantic_self__.capacidad

    def __str__(self) -> str:
        porcentaje_ocupacion: int = self.ocupacion/self.capacidad

        barra: int = '['
        comparativo: int = 0
        for i in range(20):
            if comparativo < int(porcentaje_ocupacion*20):
                barra += '■'
            else:
                barra += ' '
            comparativo += 1
        barra += ']'

        salida: str = (
            f'Solución: {self.elementos}' + '\n' +
            f'Función Objetivo: {self.f_objetivo}' + '\n' +
            f'Ocupación: ' + barra + f'{porcentaje_ocupacion*100:.2f}%' + '\n' +
            f'Es Fatible: {self.es_factible}'
        )
        return salida # super().__str__()