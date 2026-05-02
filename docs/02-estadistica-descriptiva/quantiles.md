---
id: quantiles
title: Quantiles
sidebar_label: Quantiles
<<<<<<<< HEAD:docs/02-estadistica-descriptiva/quantiles.md
sidebar_position: 4
========
sidebar_position: 5
>>>>>>>> a1ed4ca (actualizacion):docs/02-estadistica-descriptiva/5-quantiles.md
---


## Análisis de Cuantiles 

Los **cuantiles** son valores que dividen una distribución de datos en partes iguales. Un cuantil de orden *q* (donde 0 ≤ q ≤ 1) es el valor por debajo del cual se encuentra el *q*×100% de los datos.

**Ejemplos comunes:**
- **Q1 (cuantil 0.25)**: el 25% de los datos está por debajo de este valor.
- **Q2 (cuantil 0.50)**: la mediana; el 50% de los datos está por debajo.
- **Q3 (cuantil 0.75)**: el 75% de los datos está por debajo de este valor.

**Características principales:**
- Son medidas **no paramétricas** que no asumen normalidad de los datos.
- Ideales para entender la **dispersión y posición** de los datos sin verse afectadas por valores extremos.
- Fundamentales en análisis exploratorio y en la construcción de visualizaciones como boxplots.

### (Q1/Q2/Q3), IQR, Outliers y Boxplots

**Objetivos:**  
1) Calcular **Q1, Q2 (mediana)** y **Q3**.  
2) Obtener el **IQR**.  
3) Identificar **outliers** con la regla de 1.5×IQR.  
4) Visualizar con **boxplots**.  
5) (Opcional) Repetir con **Polars** para datasets grandes.


:::note 
El notebook intenta leer `ventas_100.csv` del directorio de trabajo.  
Si no lo encuentra, genera un **dataset sintético** reproducible para que todo se ejecute igual.
:::


### 🔹 Concepto estadístico: cuartil y cuantiles

La función quantile(q=0.25) devuelve el primer cuartil (Q1) de los datos en cada columna (o fila) del DataFrame, usando por defecto el método de interpolación lineal.

Significado: Q1 es el valor por debajo del cual se encuentra el 25% de los datos. Es una medida de posición que nos ayuda a entender la dispersión y la tendencia central de los datos, y es ampliamente usado en estadística para resumir datos y en boxplots para definir el bigote inferior.

:::tip
Si el DataFrame tiene valores faltantes (NaN), por defecto los omitirá en el cálculo, a menos que se especifique lo contrario.
:::

Formalmente:

Q(q)=el valor tal que P(X≤Q(q))=q

Esto significa que el 25% de los valores de la variable son menores o iguales a ese valor, y el 75% son mayores.
Es una medida no paramétrica de tendencia y dispersión, que no depende de supuestos de normalidad.

**En términos prácticos**

Si tienes una serie de datos numéricos, por ejemplo:

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40, 50])
s.quantile(q=0.25)
```

El resultado será 20.0, porque el 25% de los valores se encuentran por debajo de 20 (en este caso, entre 10 y 20, interpolando si es necesario).

### 🔹 Métodos de interpolación

La función permite especificar cómo se interpola cuando el cuantil no coincide exactamente con un índice de la muestra.

Por ejemplo:
```python
df.quantile(0.25, interpolation='linear')
```

Opciones comunes para interpolación:
- 'linear' (por defecto): interpola entre los dos valores más cercanos.
- 'lower': usa el valor más bajo.
- 'higher': usa el valor más alto.
- 'midpoint': promedio de ambos.
- 'nearest': el valor más cercano.

Esto es importante cuando trabajas con muestras pequeñas o datos discretos.

### 🔹 En el contexto de análisis estadístico

El cuantil del 25% (Q1) es una medida clave:

- Se usa para detectar asimetrías y dispersión.
- Permite calcular el rango intercuartílico (IQR):

IQR=Q3−Q1=quantile(0.75)−quantile(0.25)

- que mide la variabilidad central sin verse afectada por valores extremos.
- En boxplots, Q1 es el límite inferior de la caja.


```python
# Por columnas (axis=0 - default)
q1_columnas = df_completo.quantile(0.25, axis=0)

# Por filas (axis=1)
q1_filas = df_completo.quantile(0.25, axis=1)
print("Q1 por filas:")
print(q1_filas)
```


## Interpretación y uso analítico

- **Q1 (25%)**: valor bajo el cual cae el 25% de la distribución.  
- **Q2 (50%) / Mediana**: tendencia central robusta.  
- **Q3 (75%)**: límite superior del rango central.  
- **IQR = Q3 - Q1**: variabilidad central sin impacto de outliers.  
- **Outliers** (regla 1.5×IQR): candidatos a revisión (errores, casos especiales, segmentos premium).

### Recomendaciones prácticas (precio/ingreso/metros, etc.)
- IQR alto → alta heterogeneidad del portafolio; segmenta o normaliza.  
- Asimetría (Q3 muy alejado de Q2) → evalúa transformaciones (log) o métricas robustas (mediana, MAD).  
- Outliers frecuentes → valida calidad de datos, caps/winsorization, reglas de negocio.