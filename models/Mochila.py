from functions.suma_lista import suma_lista
from typing import Any, List
from pydantic.main import BaseModel
from random import randint


class Mochila(BaseModel):
    tamano: int
    elementos: List[Any] = []
    pesos: List[int]
    valores: List[int]
    capacidad: int
    ocupacion: int = 0
    f_objetivo: int = 0
    es_factible: bool = False

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)

        __pydantic_self__.__actualizar_elementos()
        

    def __str__(__pydantic_self__) -> str:
        porcentaje_ocupacion: int = __pydantic_self__.ocupacion/__pydantic_self__.capacidad

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
            f'Solución: {__pydantic_self__.elementos}' + '\n' +
            f'Función Objetivo: {__pydantic_self__.f_objetivo}' + '\n' +
            f'Ocupación: ' + barra + f'{porcentaje_ocupacion*100:.2f}%' + '\n' +
            f'Es Fatible: {__pydantic_self__.es_factible}'
        )
        return salida

    def __setattr__(__pydantic_self__, name: str, value: Any) -> None:
        super().__setattr__(name, value)
        if name == 'elementos':
            __pydantic_self__.__actualizar_f_objetivo()
            __pydantic_self__.__actualizar_ocupacion()
            __pydantic_self__.__actualizar_factibilidad()

            

    def __actualizar_elementos(__pydantic_self__):
        if __pydantic_self__.elementos == []:
            __pydantic_self__.elementos = [randint(0, 1) for i in range(__pydantic_self__.tamano)]

    def __actualizar_f_objetivo(__pydantic_self__):
        __pydantic_self__.f_objetivo = suma_lista([
            __pydantic_self__.valores[i]*__pydantic_self__.elementos[i]
                for i in range(len(__pydantic_self__.elementos))
                    if type(__pydantic_self__.elementos[i]) == int
        ])

    def __actualizar_ocupacion(__pydantic_self__):
        __pydantic_self__.ocupacion = suma_lista([
            __pydantic_self__.pesos[i]*__pydantic_self__.elementos[i]
                for i in range(len(__pydantic_self__.elementos))
                    if type(__pydantic_self__.elementos[i]) == int
        ])
    
    def __actualizar_factibilidad(__pydantic_self__):
        __pydantic_self__.es_factible = __pydantic_self__.ocupacion <= __pydantic_self__.capacidad