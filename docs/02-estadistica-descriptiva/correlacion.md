---
id: correlacion
title: Correlación
sidebar_label: Correlación
sidebar_position: 5
---

# Correlación

La **correlación** es una métrica que oscila entre -1 y +1 y mide tanto la dirección como la fuerza de la relación lineal entre dos variables. Un valor de correlación cercano a +1 indica una fuerte relación lineal positiva, un valor cercano a -1 indica una fuerte relación lineal negativa, y un valor cercano a 0 indica una falta de relación lineal. La correlación es adimensional, lo que significa que no depende de las unidades de medida de las variables, a diferencia de la covarianza. Por ejemplo, podríamos encontrar una correlación positiva baja pero estadísticamente significativa de 0.464 entre la edad y los ingresos en un dataset, lo que sugeriría que existe una relación, aunque no sea perfecta. Es crucial recordar que la correlación no implica causalidad; dos variables pueden estar altamente correlacionadas sin que una cause la otra (puede haber una tercera variable oculta influyendo en ambas).

Existen 3 medidas para cuantificar la correlación:
1. **Coeficiente de correlación de Pearson**: Mide la relación lineal entre dos variables cuantitativas.
2. **Coeficiente de correlación de Spearman**: Mide la relación monótona entre dos variables, sin asumir que la relación es lineal.
3. **Coeficiente de correlación de Kendall**: Mide la concordancia entre dos variables, evaluando la relación ordinal.


### Coeficiente de correlación de Pearson
El coeficiente de correlación de Pearson es una medida estadística que evalúa la fuerza y la dirección de la relación lineal entre dos variables cuantitativas. Su valor oscila entre -1 y 1, donde:
- 1 indica una correlación positiva perfecta: a medida que una variable aumenta, la otra también lo hace.
- -1 indica una correlación negativa perfecta: a medida que una variable aumenta, la otra disminuye.
- 0 indica que no hay correlación lineal entre las variables.

La fórmula para calcular el coeficiente de correlación de Pearson $( r )$ es:

```math
r = \frac{n(\sum xy) - (\sum x)(\sum y)}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}}
```

Donde:
- $ n $ es el número de pares de datos.
- $ x $ e $ y $ son las variables que se están correlacionando.

El coeficiente de correlación de Pearson es sensible a valores atípicos, por lo que es importante visualizarlos mediante diagramas de dispersión antes de realizar el análisis. Además, solo captura relaciones lineales, por lo que no debe usarse para evaluar relaciones no lineales.

Las condiciones que se deben de cumplir para que el coeficiente de correlación de Pearson sea válido son:

* La relación que se quiere estudiar es de tipo lineal (de lo contrario, el coeficiente de Pearson no la puede detectar).

* Las dos variables deben de ser numéricas.

* Normalidad: ambas variables se tienen que distribuir de forma normal. En la práctica, se suele considerar válido aun cuando se alejan moderadamente de la normalidad.

* Homocedasticidad: la varianza de 𝑌 debe ser constante a lo largo de la variable 𝑋. Esto se puede contrastar si en un scatterplot los valores de 𝑌 mantienen la misma dispersión en las distintas zonas de la variable 𝑋.

A continuación, se muestra una tabla con la interpretación de los valores del coeficiente de correlación de Pearson:

| Valor de r de Pearson | Interpretación de la correlación entre x e y                 |
|----------------------|---------------------------------------------------------------|
| igual a 1            | relación lineal positiva perfecta                             |
| mayor que 0          | correlación positiva                                          |
| igual a 0            | no hay relación lineal                                        |
| menor que 0          | correlación negativa                                          |
| igual a -1           | relación lineal negativa perfecta                             |


### Coeficiente de correlación de Spearman
El coeficiente de correlación de Spearman es una medida no paramétrica que evalúa la relación monótona entre dos variables. A diferencia del coeficiente de Pearson, que asume que la relación es lineal, Spearman se basa en los rangos de los datos en lugar de los valores brutos. Esto lo hace más robusto frente a valores atípicos y adecuado para datos ordinales.

La fórmula para calcular el coeficiente de correlación de Spearman $( \rho )$ es:

```math
\rho = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}
```

Donde:
- $ d_i $ es la diferencia entre los rangos de cada par de datos.
- $ n $ es el número de pares de datos.

El coeficiente de Spearman también oscila entre -1 y 1, con interpretaciones similares a las del coeficiente de Pearson. Un valor de 1 indica una correlación monótona positiva perfecta, -1 indica una correlación monótona negativa perfecta y 0 indica que no hay correlación monótona.

### Coeficiente de correlación de Kendall
El coeficiente de correlación de Kendall es una medida no paramétrica que evalúa la concordancia entre dos variables ordinales. A diferencia de Pearson y Spearman, que se centran en las relaciones lineales y monótonas, respectivamente, Kendall se basa en la comparación de pares de observaciones para determinar la dirección y la fuerza de la relación.

La fórmula para calcular el coeficiente de correlación de Kendall $( \tau )$ es:

```math
\tau = \frac{(n_c - n_d)}{\frac{1}{2}n(n-1)}
```

Donde:
- $ n_c $ es el número de pares concordantes.
- $ n_d $ es el número de pares discordantes.
- $ n $ es el número total de observaciones.

El coeficiente de Kendall también oscila entre -1 y 1, con interpretaciones similares a las de Pearson y Spearman. 
* Un valor de 1 indica una concordancia perfecta, 
* -1 indica una discordancia perfecta y 
* 0 indica que no hay concordancia.


### ¿Cuándo debo usar cada coeficiente de correlación?

- **Pearson**: Úsalo cuando ambas variables sean numéricas, la relación sea lineal y los datos cumplan (aproximadamente) con la normalidad y homocedasticidad. Es sensible a valores atípicos.
- **Spearman**: Úsalo cuando la relación entre variables sea monótona pero no necesariamente lineal, o cuando los datos sean ordinales o tengan valores atípicos.
- **Kendall**: Úsalo con variables ordinales o cuando quieras evaluar la concordancia entre rangos. Es más robusto en muestras pequeñas y menos sensible a empates que Spearman.

En resumen:  
- Pearson para relaciones lineales y datos normales.  
- Spearman para relaciones monótonas o datos no normales/ordinales.  
- Kendall para evaluar concordancia en rangos, especialmente con muestras pequeñas o muchos empates.

**La correlación no implica causalidad**

No podríamos terminar este tutorial sin mencionar una advertencia importante: la correlación no implica causalidad.

La correlación solo cuantifica la fuerza y la dirección de la relación entre dos variables. Puede haber una fuerte correlación entre dos variables, pero esto no permite concluir que una causa la otra. Cuando las correlaciones fuertes no son causales, las llamamos correlaciones espurias.


***
## Datasets clásicos con alta correlación
Existen conjuntos de datos muy conocidos en el mundo del machine learning y la estadística que naturalmente tienen variables altamente correlacionadas, un fenómeno conocido como multicolinealidad. 

**Dataset de cáncer de mama (Breast Cancer Wisconsin):** Un análisis de las características de las células mamarias muestra una alta correlación entre variables como el radio, el perímetro y el área, tanto en su media como en su peor caso (radius_mean y radius_worst, por ejemplo, tienen una correlación muy alta). Puedes encontrarlo en la librería scikit-learn.

**Dataset de salarios y años de experiencia:** Un ejemplo clásico de regresión lineal simple, donde existe una fuerte correlación positiva entre los años de experiencia y el salario de un empleado. Este tipo de datos se encuentra fácilmente en plataformas como Kaggle.

**Dataset de precios de casas (California Housing, Boston Housing):** En estos conjuntos de datos, variables como el número de habitaciones, la superficie habitable y el valor de la propiedad suelen estar altamente correlacionadas.

### Cancer de mama
Desde el dataset **Breast Cancer Wisconsin (Diagnostic) (WBCD)**, se pueden observar altas correlaciones entre varias características. Por ejemplo, las características relacionadas con el tamaño y la forma de las células tienden a estar altamente correlacionadas entre sí. Algunas de las correlaciones más notables incluyen:
- **Radio (radius_mean)** y **Perímetro (perimeter_mean)**: Estas dos características están altamente correlacionadas, ya que ambas miden aspectos relacionados con el tamaño de las células.

- **Área (area_mean)** y **Radio (radius_mean)**: También muestran una fuerte correlación, ya que el área es una función del radio.

- **Suavidad (smoothness_mean)** y **Textura (texture_mean)**: Estas características, que describen la textura de las células, también tienden a estar correlacionadas.

**Referencia:**
- https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
- Wolberg, W., Mangasarian, O., Street, N., & Street, W. (1993). Breast Cancer Wisconsin (Diagnostic) [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5DW2B.

