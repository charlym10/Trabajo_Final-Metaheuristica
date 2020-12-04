from typing import List
from pydantic import BaseModel


class Variables(BaseModel):
    etiquetas: List[str]
    articulos: List[int]
    pesos: List[int]
    valores: List[int]