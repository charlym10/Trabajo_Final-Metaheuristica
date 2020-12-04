from typing import Any, Dict, List
from models.Mochila import Mochila
from random import choices


def seleccion_torneo(poblacion: List[Mochila], tamano_muetra: int, data: Dict[str, Any]) -> Mochila:
    vector_aleatorios: List[Mochila] = choices(poblacion, k=tamano_muetra)

    individuo = Mochila(**data)
    
    for i in vector_aleatorios:
        if i.es_factible:
            if i.f_objetivo > individuo.f_objetivo:
                individuo = i.copy()

    return individuo
    
