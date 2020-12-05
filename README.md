# TRABAJO FINAL – METAHEURÍSTICAS: Problema de la Mochila

## Resumen
Se escogió el problema de la mochila ya que no se encontró un algoritmo en el libro `OPTIMIZACIÓN COMBINATORIA - G. E. Mauricio y S. C. Jhon` que lo solucionara, además, es un problema bastante estudiado, de fácil implementación y que se ajusta bien al algoritmo genético (mismo que se trabajó en clase).
Para la implementación se escogió el lenguaje de programación Python utilizando el paradigma de `Programación Orientada a Objetos (POO)` con el apoyo principalmente de la librería `pydantic==1.7.3` y en menor medida la librería `pandas==1.1.4`, a si mismo se utilizó un repositorio remoto para almacenar el código y gestionar los cambios, este se encuentra disponible en el siguiente enlace: https://github.com/charlym10/Trabajo_Final-Metaheuristica.

## Problema
El problema consiste en decidir qué artículos empacar en una `Mochila` teniendo en cuenta el `Valor` que cada uno aparta y su `Peso` o costo de ser empacado, el algoritmo esta diseña para ser flexible respecto al tamaño del problema, sin embargo, se probó con un problema de 20 `Artículos`, los mismos se describen en el archivo `datos.txt`, como restricción, la mochila solo puede cargar un determinado `Peso`, sin embargo, el programa permite ingresar un valor a placer, por lo que para el caso en cuestión se digitó una restricción es de `250` unidades de `Peso`.

## Algoritmo
La filosofía del algoritmo se basa en exploración y explotación, aplicando una técnica de selección, cruzamiento y mutación que parte de una población inicial y que en la literatura se le llama Algoritmo Genético, por lo anterior, las variables de entrada necesarias para correr el algoritmo son: 

| Variable | Descripción |
| ------ | ------ |
| capacidad_mochila | Capacidad de la mochila para cargar artículos. |
| num_individuos_poblacion | Cantidad de individuos de la población, valor por defecto (100). |
| tamano_muestra_torneo | Tamaño de la muestra para selección por torneo, valor por defecto (10). |
| max_generaciones | Número máximo de generaciones, valor por defecto (100). |
| tasa_mutacion | Tasa de mutación, valor por defecto (0.1). |
| num_busqueda_local | Número de búsquedas locales, valor por defecto (25). |

> Para la selección de los dos individuos se utilizó selección por torneo, que tiene como variables de entrada la población y el tamaño de la muestra, para el cruzamiento se utilizó la técnica de Cruzamiento PMX y para la mutación se implementó la estrategia de swing.

## Resultados
Después de correr el modelo en varias ocasiones combinando los parámetros de entrada antes mencionados, se pudo observar que la función objetivo se estabiliza alrededor de 640 UNIDADES, algo importante a resaltar es que esto se consigue principalmente aumentando el tamaño de la población y estableciendo una tasa de mutación en 100%.
A continuación, se muestran las salidas del programa:

```sh
$ python main.py
--- Datos de Entrada ---
Capacidad de la mochila: 250
Cantidad de individuos de la población: (100) 10
Tamaño de la muestra para selección por torneo: (10) 4
Número máximo de generaciones: (100)
Tasa de mutación: (0.10)
Número de busquedas locales: (25)
--- Fin ---
Solución Incumbente: 558
Solución Incumbente: 605
Solución Incumbente: 643
--- Resultado ---
Nombre del archivo:  datos.txt
          Peso  Valor
Articulo
1           42    100
2           23     60
3           21     70
4           15     15
5            7     15
6           11     80
7           11     25
8           50     92
9           23     66
10          33     48
11          42    100
12          56     60
13          21     70
14          15     23
25           7     15
16          23     80
17          11     25
18          50     92
19          78    102
20          40     45
~~~
Capacidad de la mochila: 250
Número Individuos Población: 10
Tamaño Muestra Torneo: 4
Número Máximo Generaciones: 100
Tasa Mutación: 0.1
Número Busquedas Locales: 25
~~~
Solución: [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1]
Función Objetivo: 643
Ocupación: [■■■■■■■■■■■■■■■■■■■ ]99.60%
Es Fatible: True
--- Fin ---
```

## Conclusiones
Particularmente resultó mas sencilla la implementación del algoritmo en Python que en Matlab, sin embargo, esto se debe principalmente al dominio que ya se tiene del lenguaje, en términos de rendimiento, se notó mayor velocidad en la búsqueda de la solución en Matlab, siendo un punto importante a la hora de implementar un caso real con una complejidad más elevada.
