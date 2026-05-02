---
id: markov
title: Modelo de Markov
sidebar_label: Modelo de Markov
sidebar_position: 4
---

# Modelo de Markov

Este documento proporciona una descripción científica y técnica del **modelo de Markov** y las **cadenas de Markov**, integrando los fundamentos matemáticos necesarios y ejemplos prácticos en Python utilizando conjuntos de datos reales.

---

# El Modelo de Markov y las Cadenas de Markov

### 1. Definición y Propiedad de Markov
Una **cadena de Markov** es un proceso estocástico (una secuencia de variables aleatorias) en el que la probabilidad de que el sistema se mueva a un estado futuro depende exclusivamente del estado actual y no de la serie de eventos que le precedieron. En otras palabras, el estado futuro depende únicamente del estado presente, no de la historia completa del sistema Esta característica fundamental se conoce como la **propiedad de Markov** o la "falta de memoria" del sistema.

Matemáticamente, para una secuencia de variables aleatorias $X_0, X_1, X_2, \dots$ con un espacio de estados discreto $S$, la propiedad de Markov se expresa como:

```math
P(X_{n+1} = i_{n+1} | X_n = i_n, X_{n-1} = i_{n-1}, \dots, X_0 = i_0) = P(X_{n+1} = i_{n+1} | X_n = i_n)
```

Una cadena de Markov es un proceso de Markov con espacio de estados discreto y tiempo discreto. Es la formulación más utilizada en aplicaciones prácticas.

### 2. Fundamentos Matemáticos

```math
P\bigl(X_{t+1}=j\mid X_t=i, X_{t-1}=i_{t-1},\dots\bigr)=P\bigl(X_{t+1}=j\mid X_t=i\bigr)=p_{ij}
```

donde $p_{ij}$ son las probabilidades de transición que forman la matriz de transición $P$:




#### Matriz de Transición Estocástica
La evolución de una cadena de Markov homogénea en el tiempo se describe mediante una **matriz de transición** $P$, donde cada elemento $P_{ij}$ representa la probabilidad de pasar del estado $i$ al estado $j$ en un solo paso.
Una matriz estocástica debe cumplir que:
1.  Sus elementos son no negativos: $P_{ij} \ge 0$.

2.  La suma de cada fila es igual a 1: $\sum_{j} P_{ij} = 1$.

#### Ecuación de Chapman-Kolmogorov
Para calcular las probabilidades de transición en $n$ pasos, se utiliza la **ecuación de Chapman-Kolmogorov**, que establece que la matriz de transición para $n$ pasos es simplemente la $n$-ésima potencia de la matriz de un solo paso:

```math
P(n+m) = P(n)P(m) \implies P^{(n)} = P^n
```

#### Distribución Estacionaria
Una distribución de probabilidad $\pi$ es **estacionaria** para una cadena de Markov si el sistema permanece en esa distribución después de una transición:

```math
\pi P = \pi, \quad \text{donde} \sum_i \pi_i = 1
```


---

### 3. Implementación en Python con Datasets Reales

A continuación, se presentan dos ejemplos prácticos de análisis secuencial.


#### Ejemplo: Predicción meteorológica (dataset NOAA)

```r
#r

```

---

### 4. Clasificación de Estados y Ergodicidad
*   **Recurrencia:** Un estado es recurrente si la probabilidad de regresar a él en un tiempo finito es 1.
*   **Transitoriedad:** Un estado es transitorio si existe una probabilidad mayor a 0 de nunca regresar a él.
*   **Ergodicidad:** Una cadena es ergódica si es irreducible (todos los estados se comunican), positiva recurrente y aperiódica. En este estado, los promedios temporales convergen a las esperanzas de la distribución estacionaria.

### 5. Casos de Uso Comunes
1.  **MCMC (Monte Carlo por Cadenas de Markov):** Utilizado para obtener muestras de distribuciones posteriores complejas en estadística bayesiana mediante algoritmos como Metropolis-Hastings o el muestreo de Gibbs.
2.  **Procesamiento de Lenguaje Natural:** Modelado de secuencias de palabras para predicción de texto y reconocimiento de voz.
3.  **Economía y Finanzas:** Análisis de fluctuaciones de mercado y volatilidad de activos.
4.  **Bioinformática:** Alineación de secuencias de proteínas y análisis de genomas.


### Diferencias entre una cadena de Markov y modelo oculto de Markov

La diferencia fundamental entre una **cadena de Markov** y un **modelo oculto de Markov (HMM)** radica en la **visibilidad de los estados**: mientras que en una cadena de Markov los estados son directamente observables, en un HMM los estados internos están "ocultos" y solo pueden inferirse a través de una serie de observaciones o emisiones producidas por dicho sistema.

A continuación se detallan las diferencias principales organizadas por categorías:

### 1. Observabilidad y Estructura
*   **Cadena de Markov (MC):** Es una secuencia de variables aleatorias donde cada estado es conocido y visible para el observador. El sistema evoluciona a través de transiciones entre estos estados observables siguiendo la **propiedad de Markov**.

*   **Modelo Oculto de Markov (HMM):** Es un "modelo de mezcla dependiente" que consta de dos partes: una **cadena de Markov subyacente** (parámetro de proceso) que no se puede ver, y un **proceso dependiente del estado** que genera los datos que sí observamos. Por ejemplo, en el reconocimiento de voz, los estados son fonemas ocultos y las observaciones son las señales de audio grabadas.

### 2. Componentes Matemáticos
Para definir cada modelo, se requieren distintos conjuntos de parámetros:

| Característica | Cadena de Markov | Modelo Oculto de Markov (HMM) |
| :--- | :--- | :--- |
| **Estados** | Todos son visibles. | Existen estados ocultos y observaciones visibles. |
| **Probabilidades de Transición** | Definen el salto entre estados conocidos. | Definen el salto entre los estados ocultos. |
| **Probabilidades de Emisión** | No existen (el estado *es* la observación). | Definen la probabilidad de que un estado oculto genere una observación específica. |
| **Parámetros base** | Matriz de transición ($\Gamma$) y distribución inicial ($\delta$). | Matriz de transición, matriz de emisión (o densidades) y distribución inicial. |

### 3. Aplicación de la Propiedad de Markov
*   **Consistencia:** Una cadena de Markov siempre satisface la propiedad de que el futuro depende únicamente del presente.
*   **Deterioro en HMM:** Aunque el proceso oculto es una cadena de Markov, la secuencia de **observaciones visibles en un HMM generalmente no cumple con la propiedad de Markov**. Esto significa que conocer solo la observación actual no siempre es suficiente para predecir la siguiente sin considerar la historia del modelo.

### 4. Objetivos e Inferencia
*   **En Cadenas de Markov:** El interés suele estar en calcular las **probabilidades de transición**, el tiempo promedio en un estado o el comportamiento del sistema a largo plazo (estado estacionario).

*   **En HMM:** Los desafíos son más complejos y se dividen en tres problemas clásicos:
    1.  **Evaluación:** Calcular la probabilidad de una secuencia de observaciones.
    2.  **Decodificación:** Determinar la secuencia más probable de estados ocultos que generó las observaciones (comúnmente mediante el **algoritmo de Viterbi**).
    3.  **Aprendizaje:** Estimar los parámetros del modelo (transiciones y emisiones) a partir de los datos observados (usando el **algoritmo de Baum-Welch**).

***

**En resumen:** Una cadena de Markov es un sistema donde lo que ves es lo que sucede. Un HMM es un sistema donde lo que ves es solo el resultado (emisión) de un mecanismo interno invisible que se comporta como una cadena de Markov.


## Modelo oculto de Markov (HMM)

En un Modelo Oculto de Markov (HMM), la **matriz de emisión** (o probabilidades dependientes del estado) define la probabilidad de obtener una observación específica dado que el sistema se encuentra en un estado oculto determinado,. El cálculo de esta matriz depende de si los estados son conocidos (aprendizaje supervisado) o si deben inferirse de los datos (aprendizaje no supervisado).

### 1. Definición Conceptual
Cada elemento de la matriz representa la probabilidad condicionada $P(X_t = x | C_t = i)$, donde $X_t$ es la observación y $C_t$ es el estado en el tiempo $t$. En modelos con observaciones discretas, esto forma una matriz de probabilidades; en modelos continuos, se utilizan **funciones de densidad de probabilidad** (como la Gaussiana) cuyos parámetros deben ser estimados.

### 2. Estimación mediante el Algoritmo de Baum-Welch (EM)
Cuando los estados son ocultos, el método estándar para calcular estos parámetros es el **algoritmo de Baum-Welch**, que es una versión del algoritmo de Esperanza-Maximización (EM),. Este proceso es iterativo y se divide en dos pasos principales:

*   **Paso E (Esperanza):** Se calculan las **probabilidades forward ($\alpha$) y backward ($\beta$)** para determinar la "responsabilidad" o probabilidad de que el modelo esté en el estado $j$ en el momento $t$, dada la secuencia de observaciones. Esta cantidad se denota como:

    ```math
    \hat{u}_j(t) = P(C_t = j | x^{(T)}) = \frac{\alpha_t(j)\beta_t(j)}{L_T}
    ```
    donde $L_T$ es la verosimilitud total de las observaciones.

*   **Paso M (Maximización):** Se utilizan estas probabilidades para actualizar los parámetros de emisión de modo que se maximice la verosimilitud de los datos,.

### 3. Fórmulas de Reestimación según la Distribución
El cálculo específico de los valores de emisión varía según la naturaleza de las observaciones:

*   **Para distribuciones de Poisson:**
    El parámetro $\lambda$ (media) para el estado $j$ se actualiza como un promedio ponderado de las observaciones $x_t$:
    ```math
    \hat{\lambda}_j = \frac{\sum_{t=1}^T \hat{u}_j(t) x_t}{\sum_{t=1}^T \hat{u}_j(t)}
    ```


*   **Para distribuciones Normales (Gaussianas):**
    Se calculan la media ($\mu$) y la varianza ($\sigma^2$) de forma similar:
    ```math
    \hat{\mu}_j = \frac{\sum_{t=1}^T \hat{u}_j(t) x_t}{\sum_{t=1}^T \hat{u}_j(t)}
    ```



    ```math
    \hat{\sigma}_j^2 = \frac{\sum_{t=1}^T \hat{u}_j(t) (x_t - \hat{\mu}_j)^2}{\sum_{t=1}^T \hat{u}_j(t)}
    ```

*   **Para datos categóricos (Multinomial):**
    La probabilidad de observar el símbolo $k$ en el estado $i$ se estima dividiendo el número esperado de veces que aparece ese símbolo en ese estado por el número total esperado de veces que se visita dicho estado,.

### 4. Aprendizaje Supervisado
Si se dispone de un conjunto de entrenamiento donde tanto los estados como las observaciones están etiquetados, el cálculo es directo. En este caso, las probabilidades de emisión se obtienen simplemente calculando las **frecuencias relativas** de cada observación dentro de cada estado en los datos observados,.

**Calcula la matriz de emisión en un HMM**

La **matriz de emisión** (a veces denominada matriz $B$ o $M$) en un Modelo Oculto de Markov (HMM) contiene las probabilidades de que un estado oculto específico genere una observación particular. Su cálculo o estimación se realiza habitualmente mediante procesos iterativos cuando los estados no son observables, siendo el método estándar el **algoritmo de Baum-Welch** (una versión del algoritmo de Esperanza-Maximización o EM).

A continuación se detalla cómo se calcula y estima esta matriz:

### 1. Definición Conceptual
Cada elemento de la matriz, $m_{i,j}$, representa la probabilidad condicional de observar el símbolo $j$ dado que el sistema se encuentra en el estado oculto $i$:

```math
P(O_k = j | X_k = i)
```

Donde $O_k$ es la observación en el tiempo $k$ y $X_k$ es el estado oculto en ese mismo instante.

### 2. Estimación mediante el Algoritmo de Baum-Welch
Cuando se dispone de una secuencia de entrenamiento de observaciones pero los estados son ocultos, la matriz se estima siguiendo estos pasos:

*   **Paso E (Esperanza):** Se calculan las **probabilidades *forward* ($\alpha$) y *backward* ($\beta$)** para determinar la probabilidad de que el modelo haya estado en un estado $i$ en el momento $t$, dada toda la secuencia de observaciones. Esta probabilidad se conoce como "responsabilidad" o $\gamma_t(i)$.

*   **Paso M (Maximización):** Se actualizan los parámetros de emisión para maximizar la verosimilitud de los datos observados.

### 3. Fórmulas según el tipo de observación
El cálculo específico de los valores de la matriz depende de si las observaciones son discretas o continuas:

*   **Observaciones Discretas:**
    La probabilidad de emitir el símbolo $r$ desde el estado $i$ se actualiza como el cociente entre el número esperado de veces que se observó el símbolo $r$ estando en el estado $i$, y el número total esperado de veces que se visitó dicho estado:

    ```math
    \hat{p}_{i}(r) = \frac{\sum_{t=1, O_t=r}^{T} \gamma_t(i)}{\sum_{t=1}^{T} \gamma_t(i)}
    ```
    
*   **Observaciones Continuas (Parámetros):**
    Si las emisiones siguen una distribución (como una Gaussiana o Poisson), no se calcula una matriz de celdas fijas, sino que se actualizan los parámetros de la distribución para cada estado. 
    *   Para un **HMM-Poisson**, la media ($\lambda$) del estado $j$ se actualiza como un promedio ponderado de las observaciones:

        ```math
        \hat{\lambda}_j = \frac{\sum_{t=1}^{T} \gamma_t(j) x_t}{\sum_{t=1}^{T} \gamma_t(j)}
        ```

    *   Para un **HMM-Normal**, se actualizan la media ($\mu$) y la varianza ($\sigma^2$) de forma similar, ponderando cada dato por la probabilidad de pertenecer a ese estado en ese momento.

### 4. Estimación Supervisada (Viterbi Re-estimation)
Si se conoce la secuencia de estados (por ejemplo, en un conjunto de datos etiquetado para aprendizaje supervisado), el cálculo es directo mediante frecuencias relativas:
*   Se cuenta cuántas veces aparece cada observación en cada estado.
*   Se divide ese conteo por el número total de veces que se estuvo en ese estado.

**Nota sobre la estabilidad:** En implementaciones reales, estos cálculos suelen realizarse utilizando **logaritmos** o técnicas de **escalado** para evitar errores numéricos de subflujo (*underflow*), ya que las probabilidades multiplicadas a lo largo del tiempo pueden volverse extremadamente pequeñas.
