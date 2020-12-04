from models.Variables import Variables
from typing import List


def extraer_variables(datos: List[str]) -> Variables:
    etiquetas: List[str] = datos[0].split()
    articulo: List[int] = []
    peso: List[int] = []
    valor: List[int] = []

    n: int = len(datos) - 1

    for i in range(n):
        fila = datos[i + 1].split()

        articulo.append(int(fila[0]))
        peso.append(int(fila[1]))
        valor.append(int(fila[2]))

    resultado = {
        'etiquetas': etiquetas,
        'articulos': articulo,
        'pesos': peso,
        'valores': valor
    }

    resultado = Variables(**resultado)

    return resultado