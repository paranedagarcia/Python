---
id: medidas-dispersion
title: Medidas
sidebar_label: Medidas de dispersión
sidebar_position: 3
---


## Medidas de Dispersión
Las medidas de dispersión, por otro lado, cuantifican la variabilidad o esparcimiento de los datos alrededor de la medida de tendencia central. Son igualmente cruciales porque describen la consistencia de los datos.

### Rango
**Rango:** Es la diferencia entre el valor máximo y el mínimo del conjunto de datos. Es fácil de calcular pero muy sensible a los valores atípicos.

### Varianza
La **Varianza ($\sigma^2$)** Mide el promedio de las diferencias al cuadrado de cada dato respecto a la media. Al elevar al cuadrado las diferencias, se asegura que los valores positivos y negativos no se cancelen, y se da más peso a las observaciones más alejadas de la media. Sin embargo, sus unidades son las de los datos originales al cuadrado, lo que puede dificultar su interpretación directa.
#### Varianza Poblacional

La **varianza poblacional** mide el promedio de las desviaciones al cuadrado de cada observación respecto a la media de toda la población. Su fórmula es:

```math
\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2
```

**Donde:**

- $\sigma^2$ (sigma cuadrada): **Varianza poblacional**. Es la medida de dispersión que queremos calcular.
- $N$: **Tamaño total de la población** (número de observaciones en la población completa).
- $x_i$: **Valor de la $i$-ésima observación** en la población.
- $\mu$ (mu): **Media poblacional**, calculada como $\mu = \frac{1}{N} \sum_{i=1}^{N} x_i$.
- $\sum_{i=1}^{N}$: **Sumatoria** que indica que se deben sumar las desviaciones al cuadrado para todas las observaciones desde $i = 1$ hasta $i = N$.


> **Nota:** Se eleva al cuadrado la diferencia $(x_i - \mu)$ para evitar que las desviaciones positivas y negativas se cancelen entre sí, y para dar mayor peso a los valores que están más alejados de la media.

#### Varianza Muestral
La **varianza muestral** estima la varianza de una población a partir de una muestra. Su fórmula es:

```math
S^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2
```

**Donde:**

- $S^2$ (S cuadrada): **Varianza muestral**. Es la medida de dispersión que queremos calcular.
- $n$: **Tamaño de la muestra** (número de observaciones en la muestra).
- $x_i$: **Valor de la $i$-ésima observación** en la muestra.
- $\bar{x}$ (x barra): **Media muestral**, calculada como $\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$.
- $\sum_{i=1}^{n}$: **Sumatoria** que indica que se deben sumar las desviaciones al cuadrado para todas las observaciones desde $i = 1$ hasta $i = n$.


> **Nota:** Se eleva al cuadrado la diferencia $(x_i - \bar{x})$ para evitar que las desviaciones positivas y negativas se cancelen entre sí, y para dar mayor peso a los valores que están más alejados de la media.

### Desviación Estándar
**Desviación Estándar ($\sigma$):** Es la raíz cuadrada de la varianza. Es la medida de dispersión más utilizada porque vuelve a las unidades a las originales de los datos, facilitando su interpretación. Una desviación estándar baja indica que los datos están agrupados cerca de la media, mientras que una alta indica que los datos están más dispersos.

La formula de la desviacion estandar es:
```math
\sigma = \sqrt{\sigma^2}
``` 
**Donde:**
- $\sigma$ (sigma): **Desviación estándar poblacional**. Es la medida de dispersión que queremos calcular.
- $\sigma^2$ (sigma cuadrada): **Varianza poblacional**. Es la medida de dispersión que queremos calcular.


### Ejemplo de Cálculo de Medidas de Dispersión
Consideremos el conjunto de datos: [4, 8, 6, 5, 3, 7]
1. **Rango:**
   - Valor máximo = 8
   - Valor mínimo = 3
   - Rango = 8 - 3 = 5  

2. **Varianza:**
   - Media ($\bar{x}$) = (4 + 8 + 6 + 5 + 3 + 7) / 6 = 5.5
   - Desviaciones al cuadrado:
     - (4 - 5.5)² = 2.25
     - (8 - 5.5)² = 6.25
     - (6 - 5.5)² = 0.25
     - (5 - 5.5)² = 0.25
     - (3 - 5.5)² = 6.25
     - (7 - 5.5)² = 2.25
   - Varianza ($S^2$) = (2.25 + 6.25 + 0.25 + 0.25 + 6.25 + 2.25) / (6 - 1) = 17.5 / 5 = 3.5
   
3. **Desviación Estándar:** $S = \sqrt{S^2} = \sqrt{3.5} \approx 1.87$     
La desviación estándar de aproximadamente 1.87 indica que, en promedio, los datos se desvían de la media en esa cantidad.

