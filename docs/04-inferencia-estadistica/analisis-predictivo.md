---
id: analisis-predictivo
title: Análisis Predictivo
sidebar_label: Análisis Predictivo
sidebar_position: 6
---

# El Análisis Predictivo: Regresión Lineal y Covarianza

Una vez que entendemos los datos, podemos empezar a responder preguntas más complejas: ¿Hay una relación entre dos variables? ¿Podemos usar el conocimiento de una variable para predecir otra? Estas preguntas son el núcleo del análisis predictivo, una de las áreas más prácticas y valiosas de la ciencia de datos. Dos de las herramientas estadísticas más fundamentales para explorar relaciones y construir predicciones son la **covarianza** y la **regresión lineal**.

## Covarianza

La **covarianza** es una medida que cuantifica la dirección de la relación lineal entre dos variables cuantitativas. Específicamente, mide si los cambios en una variable están asociados con cambios en la otra. Una covarianza positiva indica que cuando una variable tiende a aumentar, la otra también lo hace. Una covarianza negativa indica que cuando una variable aumenta, la otra tiende a disminuir. Sin embargo, la principal limitación de la covarianza es que su valor numérico no está estandarizado, por lo que es difícil interpretar la magnitud de la relación; su signo es lo único que realmente importa para la dirección. Por esta razón, se suele utilizar una versión estandarizada de la covarianza: el **coeficiente de correlación de Pearson**.

## Análisis de regresión sobre datos
El **análisis de regresión** es una técnica estadística utilizada para modelar y analizar la relación entre una variable dependiente (o respuesta) y una o más variables independientes (o predictoras). La forma más simple y común de análisis de regresión es la **regresión lineal simple** (RLS), que examina la relación entre dos variables cuantitativas. Aquí, una variable se identifica como la variable de respuesta o dependiente (Y), y la otra como la variable predictora o independiente (X). En la RLS, se busca dibujar una línea recta que mejor se ajuste a sus datos, permitiendo predecir el valor de Y a partir de un valor conocido de X. La ecuación de la línea de regresión se expresa generalmente como:
$$ Y = \beta_0 + \beta_1 X + \epsilon $$
donde:
- $ Y $ es la variable dependiente (lo que queremos predecir).
- $X $ es la variable independiente (la que usamos para hacer la predicción).
- $ \beta_0 $ es la intersección (el valor de $ Y $ cuando $ X = 0 $).
- $ \beta_1 $ es la pendiente de la línea (cuánto cambia $ Y $ por un cambio unitario en $ X $).
- $ \epsilon $ es el término de error (la variabilidad en $ Y $ que no puede ser explicada por $ X $).

## Regresión Lineal

Mientras que la correlación describe una relación existente, la **regresión lineal** va un paso más allá y permite modelar y predecir. La regresión lineal simple se utiliza para modelar la relación entre una variable dependiente (o respuesta, *y*) y una única variable independiente (o predictor, *x*) suponiendo que esa relación es lineal. El objetivo es encontrar la línea recta "mejor ajustada" que pasa a través de los puntos de datos en un gráfico de dispersión. Esta línea se describe mediante la ecuación `y = mx + b`, donde `m` es la pendiente (indica cómo cambia *y* por cada unidad de cambio en *x*) y `b` es la intersección en el eje *y*. En el contexto de la inferencia estadística, se construyen intervalos de confianza para la pendiente para determinar si es estadísticamente significativa (es decir, si difiere de cero).

La regresión lineal múltiple extiende este concepto para incorporar más de un predictor. Por ejemplo, podríamos querer predecir el precio de una casa (`price`) basándonos en su tamaño (`square_feet`), el número de habitaciones (`bedrooms`) y su antigüedad (`age`). La ecuación se generaliza a `y = b0 + b1*x1 + b2*x2 + ... + bn*xn`. La regresión lineal es un modelo paramétrico que a menudo asume que los residuos (las diferencias entre los valores observados y los predichos por el modelo) se distribuyen normalmente y tienen una varianza constante. Validar estas suposiciones es una parte crítica del proceso de modelado.

Estos métodos son la base de muchas aplicaciones en la ciencia de datos. El comercio electrónico utiliza la regresión para analizar la relación entre el tiempo de permanencia en una página y las ventas. Los fabricantes usan el análisis de correlación para identificar factores que influyen en la calidad de un producto. Los economistas utilizan la regresión para modelar la relación entre el gasto en publicidad y las ventas de un producto. El aprendizaje automático y la inteligencia artificial se basan enormemente en estas bases estadísticas para crear modelos predictivos que impulsan sistemas de recomendación, detección de fraudes, diagnóstico médico y mucho más. Entender cómo funcionan la covarianza y la regresión no solo ayuda a analizar datos, sino que también proporciona una comprensión profunda de cómo se construyen muchos de los modelos que impulsan la tecnología moderna.

# 1. Conceptos Fundamentales de Regresión

## 1.1 El Concepto Básico del Modelo
Cualquier modelo estadístico describe una variable de respuesta (Y) como la suma de dos componentes [8]:

$$
\text{Variable de respuesta } = \text{ Componente sistemático } + \text{ Componente de error}
$$

El **Componente Sistemático** describe la variación de Y que puede ser explicada por el modelo (las variables $X$) [8]. El **Componente de Error** ($e_i$) representa la variación en Y que no se puede explicar; esto incluye errores de medición o la influencia de otras variables no incluidas [8].

## 2. Regresión Lineal Simple (RLS)

La RLS asume que la relación entre la variable de respuesta ($Y$) y la variable predictora ($X$) se puede describir con una línea recta [3, 9].

### 2.1 La Fórmula del Modelo RLS
El modelo de RLS para un sujeto $i$ se expresa como [8]:

$$
Y_{i} = \beta_{0} + \beta_{1}X_{i} + e_{i}
$$

**Explicación:**
*   $Y_i$: Es el valor observado de la variable de respuesta para el sujeto $i$.
*   $X_i$: Es el valor observado de la variable predictora para el sujeto $i$.
*   $\beta_0$: Es el **Intercepto**. Es el valor esperado de $Y$ cuando $X$ es cero [9].
*   $\beta_1$: Es la **Pendiente** (o coeficiente de regresión). Mide cuánto cambia $Y$ por cada unidad de cambio en $X$ [3].
*   $e_i$: Es el **Error Aleatorio** para el sujeto $i$ [8].

La parte sistemática, que es la línea recta que estamos estimando, es el valor esperado de $Y$ dado $X$ ($\mu_{Y|X}$) [9, 10]:

$$
\mu_{Y|X} = \beta_{0} + \beta_{1}X
$$

### 2.2 Relación con Modelos Lineales
La RLS es un caso de Modelo de Regresión Lineal [5]. Un modelo es "lineal" si sus parámetros ($\beta_0, \beta_1$, etc.) no están en funciones complejas (como el exponente) [4].

**Ejemplos de modelos considerados Lineales (por ser lineales en los $\beta$s) [4]:**
1.  **RLS Estándar (Relación Recta):**
    $$Y_{i} = \beta_{0} + \beta_{1}X_{i} + e_{i}$$
2.  **Transformación Logarítmica de Y:**
    $$\ln(Y_{i}) = \beta_{0} + \beta_{1}X_{i} + e_{i}$$
3.  **Modelo Polinómico (Relación Curva):** Se utiliza para modelar una asociación no lineal (curva) entre $Y$ y $X$, pero se ajusta usando técnicas de regresión lineal porque los $\beta$s no están elevados a potencias [7].
    $$Y_{i} = \beta_{0} + \beta_{1}X_{i} + \beta_{2}X_{i}^{2} + e_{i}$$

## 3. Modelos de Regresión No Lineal (MRNL)

Un modelo es considerado verdaderamente **No Lineal** si es no lineal en los parámetros ($\beta$s) [4].

**Ejemplo de MRNL (No lineal en $\beta$s):**
$$
Y_{i} = \beta_{0} + e^{\beta_{1}X_{i}}
$$
**Explicación:** Aquí, el parámetro $\beta_1$ está dentro de una función exponencial, lo que requiere métodos de estimación diferentes a los utilizados para los modelos de regresión lineal [4].

## 4. Métodos de Validación y Adecuación del Modelo

La validación es esencial para determinar si se cumplen los supuestos del modelo antes de realizar inferencias [11]. El procedimiento principal de validación es el **Análisis de Residuales** [12].

### 4.1 Definición de Residual
El residual ($\hat{e}_i$) es la diferencia entre el valor observado de Y ($y_i$) y el valor predicho ($\hat{y}_i$) por el modelo [12]:
$$
\hat{e}_{i}=y_{i}-\hat{y}_{i}
$$

### 4.2 Verificación de Supuestos mediante Gráficos [13, 14]

| Supuesto | Método de Verificación | Indicación de Incumplimiento |
| :--- | :--- | :--- |
| **Linealidad y Varianza Constante** | Gráfico de Residuales vs. Valores Predichos (o vs. Predictor X) [13]. | Un patrón **no lineal** en los puntos indica que la suposición lineal no es adecuada [13]. Si la dispersión de los residuales no es uniforme alrededor de cero, la varianza no es constante [13]. |
| **Normalidad de Errores** | Histogramas y gráficos de probabilidad (Q-Q plots) de los residuales [13-15]. | Si los residuales no siguen aproximadamente una campana (distribución normal) en el histograma o una línea recta en el Q-Q plot [15]. |
| **Detección de Valores Influyentes** | Estadísticas de diagnóstico (e.g., Cook's Distance, DFFITS) [16, 17]. | Valores extremadamente altos en estas estadísticas sugieren que ciertas observaciones tienen un impacto fuerte en los resultados de la regresión y deben ser revisadas [15, 18]. |

## 5. Ejemplo de Código (RLS en Python)

Este ejemplo ilustra cómo ajustar un Modelo de Regresión Lineal Simple (RLS) y cómo iniciar el análisis gráfico de residuales. Utilizamos datos ficticios donde el "Peso Corporal" (Y) se explica por la "Edad" (X).

## 6. Modelos de Regresión Polinómica (MRP)

Un Modelo de Regresión Polinómica se utiliza cuando existe una **asociación curvilínea** (curva) entre la variable de respuesta ($Y$) y la variable predictora ($X$) [12].

A pesar de que la relación modelada es curva, se ajusta utilizando la metodología de Regresión Lineal Múltiple (MLRM) porque el modelo es **lineal en los parámetros** ($\beta$s) [12-14].

### 6.1 Fórmula Matemática
El modelo polinómico más común (cuadrático) incluye el predictor $X$ elevado a la segunda potencia:

$$
Y_{i} = \beta_{0} + \beta_{1}X_{i} + \beta_{2}X_{i}^{2} + e_{i}
$$

**Explicación:**
*   $\beta_0, \beta_1, \beta_2$: Son los coeficientes o parámetros a estimar. Debido a que estos coeficientes no están elevados a potencias o incluidos en funciones no lineales (como el exponente), el modelo se considera lineal en sus parámetros [13].
*   $X_i$ y $X_i^2$: Son las variables predictoras. La inclusión de $X^2$ permite que la línea ajustada sea una parábola (curva) en lugar de una línea recta.

### 6.2 Ejemplo de Código (Regresión Polinómica Cuadrática)

Usaremos el ejemplo de los niveles de triglicéridos ($Y$) explicados por la edad ($X$) y la edad al cuadrado ($X^2$), tal como se encuentra en los estudios de regresión lineal múltiple.

```python

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Datos de ejemplo 
# Usaremos datos ficticios que muestran una relación curva con la edad.
np.random.seed(42)
edad = np.random.randint(20, 80, 100)
# Creamos la edad al cuadrado (la variable polinómica)
edad_cuadrado = edad**2 

# Relación: Triglicéridos = a + b1*edad + b2*edad^2 + error
# Donde la relación con edad^2 es positiva para simular una curva.
trigliceridos = 50 - 0.5 * edad + 0.01 * edad_cuadrado + np.random.normal(0, 15, 100)

# Crear DataFrame y definir variables
data = pd.DataFrame({'Edad': edad, 'Edad_Cuadrado': edad_cuadrado, 'Trigliceridos': trigliceridos})

# Definir predictores (X) y respuesta (Y)
# Note que incluimos tanto Edad como Edad_Cuadrado
X = data[['Edad', 'Edad_Cuadrado']]
Y = data['Trigliceridos']

# Añadir la constante (Intercepto, β0)
X = sm.add_constant(X) 

# Ajuste del modelo de Regresión Polinómica (MLRM)
modelo_polinomico = sm.OLS(Y, X).fit()

print("--- Resumen del Modelo de Regresión Polinómica (Cuadrático) ---")
print(modelo_polinomico.summary())

# --- Visualización de la Curva Ajustada ---
# Generar puntos para dibujar la curva
x_fit = np.linspace(edad.min(), edad.max(), 100)
X_fit = pd.DataFrame({'Edad': x_fit, 'Edad_Cuadrado': x_fit**2})
X_fit = sm.add_constant(X_fit, has_constant='add')

y_pred = modelo_polinomico.predict(X_fit)

plt.figure(figsize=(10, 6))
plt.scatter(data['Edad'], data['Trigliceridos'], label='Datos Observados', alpha=0.6)
plt.plot(x_fit, y_pred, color='red', label='Modelo Polinómico Ajustado')
plt.xlabel('Edad (Años)')
plt.ylabel('Nivel de Triglicéridos')
plt.title('Regresión Polinómica Cuadrática')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# --- Análisis de Residuales para Linealidad ---
# Un residual plot plano (distribución uniforme alrededor de cero)
# es un buen indicador de que el modelo polinómico capturó la no-linealidad.
residuales = modelo_polinomico.resid
predichos = modelo_polinomico.fittedvalues

plt.figure(figsize=(8, 5))
plt.scatter(predichos, residuales)
plt.axhline(0, color='blue', linestyle='--')
plt.xlabel('Valores Predichos (Fitted Values)')
plt.ylabel('Residuales')
plt.title('Residuales vs. Valores Predichos (Debe ser uniforme)')
plt.show()
```
