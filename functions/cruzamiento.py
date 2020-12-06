from typing import Any, Dict, List
from models.Mochila import Mochila
from random import randint


def cruzamiento(padre: Mochila, madre: Mochila, data: Dict[str, Any], cantidad_articulos: int) -> Dict[str, Mochila]:
    """
    Cruzamiento PMX para el problema de la mochila.
    
    >>> from typing import Any, Dict, List
    >>> from models.Mochila import Mochila
    >>> from random import randint, seed

    >>> data: Dict[str, Any] = {
    ...     'tamano': 5,
    ...     'pesos':  [1, 2, 3, 4, 5],
    ...     'valores': [4, 4, 2, 1, 3],
    ...     'capacidad': 15,
    ...     'elementos': [None for i in range(5)]
    ... }

    >>> padre = Mochila(
    ...     elementos=[0, 1, 1, 0, 1],
    ...     tamano=data['tamano'],
    ...     pesos=data['pesos'],
    ...     valores=data['valores'],
    ...     capacidad=data['capacidad']
    ... )
    
    >>> madre = Mochila(
    ...     elementos=[0, 1, 1, 1, 0],
    ...     tamano=data['tamano'],
    ...     pesos=data['pesos'],
    ...     valores=data['valores'],
    ...     capacidad=data['capacidad']
    ... )

    >>> seed(30) # aleatorio_1 = 2, aleatorio_2 = 4

    >>> hijos = cruzamiento(padre=padre, madre=madre, data=data, cantidad_articulos=data['tamano'])

    >>> hijo_1 = hijos['hijo_1']
    >>> hijo_2 = hijos['hijo_2']

    >>> print(hijo_1.elementos)
    [0, 1, 1, 1, 1]
    >>> print(hijo_2.elementos)
    [0, 1, 1, 0, 0]

    """
    
    # 1. Se generan aleatoriamente dos puntos de corte Pc1 y Pc2.
    aleatorio_1: int = randint(1, cantidad_articulos) - 1
    aleatorio_2: int = randint(1, cantidad_articulos) - 1

    if aleatorio_1 > aleatorio_2:
        temp: int = aleatorio_1
        aleatorio_1 = aleatorio_2
        aleatorio_2 = temp
    
    # 2. Genes por fuera de la franja.
    hijo_1: Mochila = Mochila(**data)
    hijo_2: Mochila = Mochila(**data)

    for i in range(cantidad_articulos):
        if (i <= aleatorio_1 or i >= aleatorio_2):
            hijo_1.elementos[i] = padre.elementos[i];
            hijo_2.elementos[i] = madre.elementos[i];

    # 3. Genes por dentro de la franja.
    ## Hijo 1
    posiciones_ceros: List[int] = [i for i in range(cantidad_articulos) if hijo_1.elementos[i] == None]
    for i in posiciones_ceros:
        hijo_1.elementos[i] = madre.elementos[i]

    ## Hijo 2
    posiciones_ceros: List[int] = [i for i in range(cantidad_articulos) if hijo_2.elementos[i] == None]
    for i in posiciones_ceros:
        hijo_2.elementos[i] = padre.elementos[i]
    
    hijo_1.elementos = hijo_1.elementos # Actualizar calculos
    hijo_2.elementos = hijo_2.elementos # Actualizar calculos

    hijos: Dict[str, Mochila] = {
        'hijo_1': hijo_1,
        'hijo_2': hijo_2
    }

    return hijos
