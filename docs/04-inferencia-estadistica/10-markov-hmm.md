---
id: markov-hmm
title: Modelo de Markov HMM
sidebar_label: Modelo oculto Markov
sidebar_position: 10
---


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
