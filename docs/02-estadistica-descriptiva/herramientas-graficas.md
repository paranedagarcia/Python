---
id: herramientas-graficas
title: Herramientas gráficas
sidebar_label: Herramientas gráficas
sidebar_position: 3
---

# Herramientas gráficas
Además de estas medidas, la estadística descriptiva utiliza diversas herramientas gráficas. Los **histogramas** son diagramas de barras que muestran la frecuencia de datos dentro de intervalos consecutivos, revelando la forma o distribución de los datos. Los **diagramas de caja (box plots)** visualizan la distribución de los datos a través de su cinco números resumen: mínimo, primer cuartil (Q1), mediana, tercer cuartil (Q3) y máximo, destacando eficazmente los valores atípicos. Otras medidas de posición incluyen los **cuartiles** (dividen los datos en cuatro partes iguales) y los **percentiles** (dividen los datos en cien partes iguales), que son útiles para evaluar el rendimiento relativo de una observación dentro de un grupo. En resumen, la estadística descriptiva es el proceso de limpieza, exploración y resumen inicial que prepara el camino para todas las fases posteriores del análisis de datos.

### Histogramas
Un histograma es una representación gráfica que organiza un conjunto de datos numéricos en intervalos (o "bins") y muestra la frecuencia de datos dentro de cada intervalo mediante barras. A diferencia de un gráfico de barras tradicional, que se utiliza para datos categóricos, un histograma es ideal para datos continuos y ayuda a visualizar la distribución de los datos.


### Diagramas de Caja (Box Plots)
Un diagrama de caja, o box plot, es una herramienta gráfica que resume la distribución de un conjunto de datos a través de sus cinco números resumen: 
- mínimo, 
- primer cuartil (Q1), 
- mediana, 
- tercer cuartil (Q3) y 
- máximo. 

El box plot muestra la mediana como una línea dentro de la caja, que representa el rango intercuartílico (IQR, por sus siglas en inglés), que es la distancia entre Q1 y Q3. Los "bigotes" se extienden desde la caja hasta los valores mínimo y máximo, excluyendo los valores atípicos, que se representan como puntos individuales fuera de los bigotes.

![Histogram](./img/boxplot-1.webp)
* *Box plot de ejemplo*

![Box Plot](https://upload.wikimedia.org/wikipedia/commons/1/1a/Boxplot_vs_PDF.svg)
* *Box plot comparado con una función de densidad de probabilidad (PDF)*
* *Fuente: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Boxplot_vs_PDF.svg)*

## Diagramas de dispersión
Un diagrama de dispersión, o scatter plot, es una representación gráfica que utiliza puntos para mostrar la relación entre dos variables numéricas. Cada punto en el gráfico representa un par de valores correspondientes a las dos variables, con una variable representada en el eje X (horizontal) y la otra en el eje Y (vertical).
![Scatter Plot](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Scatter_diagram_for_quality_characteristic_XXX.svg/1200px-Scatter_diagram_for_quality_characteristic_XXX.svg.png)
* *Diagrama de dispersión de ejemplo*
* Fuente: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Scatter_diagram_for_quality_characteristic_XXX.svg)


### Iris Dataset
El conjunto de datos Iris es un conjunto de datos clásico en el campo del aprendizaje automático y la estadística. Fue introducido por el estadístico y biólogo Ronald A. Fisher en 1936 como un ejemplo para ilustrar técnicas de clasificación. El conjunto de datos contiene 150 muestras de flores de iris, divididas en tres especies diferentes: Iris setosa, Iris versicolor e Iris virginica. Cada muestra tiene cuatro características numéricas: longitud del sépalo, ancho del sépalo, longitud del pétalo y ancho del pétalo, todas medidas en centímetros. Estas características permiten a los investigadores y científicos de datos analizar y clasificar las flores en función de sus atributos físicos. El conjunto de datos Iris es ampliamente utilizado como un punto de partida para aprender y practicar técnicas de análisis de datos y aprendizaje automático debido a su simplicidad y claridad.

#### Referencias
- Freedman, D., Pisani, R., & Purves, R. (2007). *Statistics* (4th ed.). W. W. Norton & Company.

![Iris Dataset Image](./img/iris.png)
![Iris Dataset Image](./img/iris-sepal.png)

```r
# crea un ejemplo de diagrama de dispersión utilizando el dataset iris

```
