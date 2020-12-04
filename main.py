from functions.seleccion_torneo import seleccion_torneo
from numpy.core.numeric import Inf
from models.Mochila import Mochila
from models.Variables import Variables
from functions.extraer_variables import extraer_variables
from typing import Any, Dict, List
from pandas import DataFrame


def main():
    # Leer datos
    with open('datos.txt', 'r', encoding='utf-8') as f:
        nombre_archivo: str = f.name
        datos = f.readlines()

    # Extraer variables
    e_variables: Variables = extraer_variables(datos)

    etiquetas: List[str] = e_variables.etiquetas
    articulos: List[int] = e_variables.articulos
    pesos: List[int] = e_variables.pesos
    valores: List[int] = e_variables.valores

    # Formatear etiquetas
    etiquetas = [i.lower().capitalize() for i in etiquetas]

    # Parametros
    print('---')
    capacidad_mochila: int = int(input("Capacidad de la mochila: "))
    num_individuos_poblacion: int = int(input("Cantidad de individuos de la población: (100) ") or "100")
    tamano_muestra_torneo: int = int(input("Tamaño de la muestra para selección por torneo: (10) ") or "10")
    max_generaciones: int = int(input("Número máximo de generaciones: (1000) ") or "1000")
    tasa_mutacion: float = float(input("Tasa de mutación: (0.10) ") or "0.10")
    num_busqueda_local: int = int(input("Número de busquedas locales: (25) ") or "25")

    # Calculos iniciales
    tamano_poblacion: int = len(articulos)

    # Algoritmo genetico
    ## Generar población inicial
    mochila = Mochila(tamano=tamano_poblacion, pesos=pesos, valores=valores, capacidad=capacidad_mochila)
    poblacion_inicial: List[Mochila] = []

    for i in range(num_individuos_poblacion):
        data: Dict[str, Any] = {
            'tamano': tamano_poblacion,
            'pesos':  pesos,
            'valores': valores,
            'capacidad': capacidad_mochila
        }
        mochila = Mochila(**data)
        poblacion_inicial.append(mochila)

    ## Calcular la incumbente
    data: Dict[str, Any] = {
        'tamano': tamano_poblacion,
        'pesos':  pesos,
        'valores': valores,
        'capacidad': capacidad_mochila,
        'elementos': [0 for i in range(tamano_poblacion)]
    }

    solucion_incumbente: Mochila = Mochila(**data)

    for i in poblacion_inicial:
        if i.es_factible:
            if i.f_objetivo > solucion_incumbente.f_objetivo:
                solucion_incumbente = i.copy()
    
    ## Ciclo generacional
    ### Seleccion
    padre: Mochila = seleccion_torneo(poblacion_inicial, num_individuos_poblacion, data)
    madre: Mochila = seleccion_torneo(poblacion_inicial, num_individuos_poblacion, data)

    ### Cruzamiento

    ### Función objetivo hijos

    ### Seleccionar el mejor hijo
    # Salida
    salida_parametros = (
        f'Número Individuos Población: {num_individuos_poblacion}' + '\n' +
        f'Tamaño Muestra Torneo: {tamano_muestra_torneo}' + '\n' +
        f'Número Máximo Generaciones: {max_generaciones}' + '\n' +
        f'Tasa Mutación: {tasa_mutacion}' + '\n' +
        f'Número Busquedas Locales: {num_busqueda_local}'
    )

    datos = DataFrame({
        etiquetas[0]: articulos,
        etiquetas[1]: pesos,
        etiquetas[2]: valores},
    )
    datos.set_index(etiquetas[0], inplace=True, drop=True)

    print('--- Resultado ---')
    print('Nombre del archivo: ', nombre_archivo)
    print(datos)
    print('~~~')
    print(salida_parametros)
    print('~~~')
    print(solucion_incumbente)
    print('--- Fin ---')

if __name__ == "__main__":
    main()