from math import inf
from functions.swap import swap
from random import random
from functions.cruzamiento import cruzamiento
from functions.seleccion_torneo import seleccion_torneo
from models.Mochila import Mochila
from models.Variables import Variables
from functions.extraer_variables import extraer_variables
from typing import Any, Dict, List
from pandas import DataFrame

def main():
    # Leer datos
    with open('datos.txt', 'r', encoding='utf-8') as f:
        nombre_archivo: str = f.name
        datos: List[str] = f.readlines()

    # Extraer variables
    e_variables: Variables = extraer_variables(datos)

    etiquetas: List[str] = e_variables.etiquetas
    articulos: List[int] = e_variables.articulos
    pesos: List[int] = e_variables.pesos
    valores: List[int] = e_variables.valores

    # Formatear etiquetas
    etiquetas = [i.lower().capitalize() for i in etiquetas]

    # Parametros
    print('--- Datos de Entrada ---')
    capacidad_mochila: int = int(input("Capacidad de la mochila: "))
    num_individuos_poblacion: int = int(input("Cantidad de individuos de la población: (100) ") or "100")
    tamano_muestra_torneo: int = int(input("Tamaño de la muestra para selección por torneo: (10) ") or "10")
    max_generaciones: int = int(input("Número máximo de generaciones: (100) ") or "100")
    tasa_mutacion: float = float(input("Tasa de mutación: (0.10) ") or "0.10")
    num_busqueda_local: int = int(input("Número de busquedas locales: (25) ") or "25")
    print('--- Fin ---')

    # Calculos iniciales
    cantidad_articulos: int = len(articulos)

    # Algoritmo genético
    ## Generar población inicial
    poblacion: List[Mochila] = []

    data: Dict[str, Any] = {
        'tamano': cantidad_articulos,
        'pesos':  pesos,
        'valores': valores,
        'capacidad': capacidad_mochila
    }

    for i in range(num_individuos_poblacion):
        mochila = Mochila(**data)
        poblacion.append(mochila)

    ## Calcular la incumbente
    data: Dict[str, Any] = {
        'tamano': cantidad_articulos,
        'pesos':  pesos,
        'valores': valores,
        'capacidad': capacidad_mochila,
        'elementos': [None for i in range(cantidad_articulos)]
    }

    solucion_incumbente: Mochila = Mochila(**data)

    for i in poblacion:
        if i.es_factible:
            if i.f_objetivo > solucion_incumbente.f_objetivo:
                solucion_incumbente = i.copy()

    print(f'Solución Incumbente: {solucion_incumbente.f_objetivo}')
    
    ## Ciclo generacional
    for i in range(max_generaciones):
        ### Seleccion
        padre: Mochila = seleccion_torneo(poblacion, num_individuos_poblacion, data)
        madre: Mochila = seleccion_torneo(poblacion, num_individuos_poblacion, data)

        ### Cruzamiento
        hijos: Dict[str, Mochila] = cruzamiento(padre, madre, data, cantidad_articulos)

        hijo_1: Mochila = hijos["hijo_1"]
        hijo_2: Mochila = hijos["hijo_2"]

        ### Seleccionar el mejor hijo
        if hijo_1.f_objetivo > hijo_2.f_objetivo:
            hijo: Mochila = hijo_1.copy()
        else:
            hijo: Mochila = hijo_2.copy()

        ### Busqueda local
        for i in range(num_busqueda_local):
            #### Mutación
            aleatorio_mutacion = random();
            if aleatorio_mutacion <= tasa_mutacion:
                hijo_mutado: Mochila = swap(hijo, cantidad_articulos);
            else:
                hijo_mutado: Mochila = hijo.copy()

            #### Seleccionar entre hijo e hijo mutado
            if hijo_mutado.f_objetivo > hijo.f_objetivo:
                mejor: Mochila = hijo_mutado.copy()
            else:
                mejor: Mochila = hijo.copy()

            #### Comparar con la solución Incumbente
            if mejor.f_objetivo > solucion_incumbente.f_objetivo:
                if mejor.es_factible:
                    solucion_incumbente = mejor.copy();
                    print(f'Solución Incumbente: {solucion_incumbente.f_objetivo}')

            #### Actualizar poblacion inicial
            encontrado = False;
            for i in range(num_individuos_poblacion):
                if mejor in poblacion:
                    encontrado = True
                    break
            
            if not encontrado:
                peor_valor: float =  inf
                peor_individuo: Mochila = Mochila(**data)
                peor_posicion: int = 0

                indice: int = 0
                for i in poblacion:
                    if i.f_objetivo < peor_valor:
                        peor_individuo = i.copy()
                        peor_posicion = indice
                        indice += 1

                if mejor.f_objetivo > peor_individuo.f_objetivo:
                    poblacion[peor_posicion] = mejor.copy();

    # Salida
    salida_parametros = (
        f'Capacidad de la mochila: {capacidad_mochila}' + '\n' +
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