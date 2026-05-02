---
id: python-basico
title: Python para Bioestadística
sidebar_label: Python Básico
sidebar_position: 1
---

# Python para Bioestadística

[Python](https://www.python.org/) es un lenguaje de programación versátil y poderoso, con un ecosistema excepcional para análisis de datos y bioestadística.

## Instalación

### Python
Descarga Python desde [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Anaconda (recomendado)
[Anaconda](https://www.anaconda.com/products/distribution) incluye Python + todas las bibliotecas científicas preinstaladas, incluyendo Jupyter Notebook.

### Jupyter Notebook / JupyterLab
Para análisis interactivo, ideal para aprendizaje:
```bash
# Instalar con pip
pip install jupyterlab

# Iniciar
jupyter lab
```

## Bibliotecas Esenciales

```python
# Instalar (si no usas Anaconda)
# pip install numpy pandas scipy matplotlib seaborn statsmodels scikit-learn

import numpy as np          # Operaciones numéricas
import pandas as pd         # Manipulación de datos
import matplotlib.pyplot as plt  # Visualización
import seaborn as sns       # Visualización estadística
from scipy import stats     # Estadística
import statsmodels.api as sm  # Modelos estadísticos
```

## Conceptos Básicos

### Tipos de Datos

```python
# Numérico
x = 3.14
type(x)   # float

# Entero
n = 5
type(n)   # int

# Cadena de texto
nombre = "Bioestadística"
type(nombre)   # str

# Booleano
es_verdad = True
type(es_verdad)   # bool

# Lista
edades = [25, 30, 35, 28, 32, 40, 27, 33]
```

### NumPy

```python
import numpy as np

# Array NumPy
edades = np.array([25, 30, 35, 28, 32, 40, 27, 33])

# Estadísticas básicas
print(f"Media: {np.mean(edades):.2f}")
print(f"Mediana: {np.median(edades):.2f}")
print(f"Desv. estándar: {np.std(edades, ddof=1):.2f}")
print(f"Varianza: {np.var(edades, ddof=1):.2f}")
print(f"Mínimo: {np.min(edades)}")
print(f"Máximo: {np.max(edades)}")
print(f"Percentil 25: {np.percentile(edades, 25)}")
print(f"Percentil 75: {np.percentile(edades, 75)}")
```

### Pandas - DataFrames

```python
import pandas as pd

# Crear DataFrame
pacientes = pd.DataFrame({
    'id': range(1, 7),
    'nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Elena', 'Pedro'],
    'edad': [45, 52, 38, 61, 29, 47],
    'sexo': pd.Categorical(['F', 'M', 'F', 'M', 'F', 'M']),
    'presion_sistolica': [120, 135, 115, 145, 110, 128]
})

# Explorar el DataFrame
print(pacientes.head())           # Primeras filas
print(pacientes.info())           # Información del DataFrame
print(pacientes.describe())       # Estadísticas descriptivas
print(pacientes.shape)            # (filas, columnas)
print(pacientes.dtypes)           # Tipos de datos
print(pacientes.isnull().sum())   # Valores faltantes
```

## Manipulación de Datos con Pandas

```python
# Seleccionar columnas
pacientes['edad']
pacientes[['nombre', 'edad', 'presion_sistolica']]

# Filtrar filas
mujeres = pacientes[pacientes['sexo'] == 'F']
mayores_40 = pacientes[pacientes['edad'] > 40]
hombres_hipertensos = pacientes[
    (pacientes['sexo'] == 'M') & 
    (pacientes['presion_sistolica'] >= 130)
]

# Crear nueva columna
pacientes['hipertenso'] = pacientes['presion_sistolica'] >= 130

# Agrupar y resumir
resumen = pacientes.groupby('sexo').agg(
    n=('edad', 'count'),
    media_edad=('edad', 'mean'),
    media_presion=('presion_sistolica', 'mean'),
    de_presion=('presion_sistolica', 'std')
).round(2)
print(resumen)
```

## Lectura de Datos

```python
import pandas as pd

# CSV
datos = pd.read_csv('datos.csv')
datos = pd.read_csv('datos.csv', sep=';', encoding='utf-8')

# Excel
datos = pd.read_excel('datos.xlsx', sheet_name='Hoja1')

# SPSS
datos = pd.read_spss('datos.sav')

# Stata
datos = pd.read_stata('datos.dta')

# Verificar los datos
print(datos.head())
print(datos.shape)
print(datos.info())
```

## Visualización con Matplotlib y Seaborn

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración global
plt.rcParams['figure.figsize'] = (8, 5)
sns.set_theme(style="whitegrid")

# Histograma con seaborn
fig, ax = plt.subplots()
sns.histplot(pacientes['presion_sistolica'], bins=8, kde=True, 
             color='steelblue', ax=ax)
ax.set_title('Distribución de la Presión Sistólica')
ax.set_xlabel('Presión Sistólica (mmHg)')
ax.set_ylabel('Frecuencia')
plt.tight_layout()
plt.show()

# Boxplot por grupo
fig, ax = plt.subplots()
sns.boxplot(x='sexo', y='presion_sistolica', data=pacientes,
            palette={'F': '#E91E8C', 'M': '#1E90FF'}, ax=ax)
sns.stripplot(x='sexo', y='presion_sistolica', data=pacientes,
              color='black', size=6, alpha=0.7, ax=ax)
ax.set_title('Presión Sistólica por Sexo')
ax.set_xlabel('Sexo')
ax.set_ylabel('Presión Sistólica (mmHg)')
plt.tight_layout()
plt.show()

# Gráfico de dispersión con línea de regresión
fig, ax = plt.subplots()
sns.regplot(x='edad', y='presion_sistolica', data=pacientes,
            scatter_kws={'s': 60, 'color': 'steelblue'},
            line_kws={'color': 'red', 'linewidth': 2}, ax=ax)
ax.set_title('Relación Edad - Presión Sistólica')
ax.set_xlabel('Edad (años)')
ax.set_ylabel('Presión Sistólica (mmHg)')
plt.tight_layout()
plt.show()
```

## Análisis Estadístico

```python
from scipy import stats
import statsmodels.formula.api as smf

# Pruebas de hipótesis
# t-test para dos muestras independientes
hombres = pacientes[pacientes['sexo'] == 'M']['presion_sistolica']
mujeres = pacientes[pacientes['sexo'] == 'F']['presion_sistolica']

t_stat, p_valor = stats.ttest_ind(hombres, mujeres)
print(f"t = {t_stat:.4f}, p-valor = {p_valor:.4f}")

# Correlación
r, p = stats.pearsonr(pacientes['edad'], pacientes['presion_sistolica'])
print(f"r = {r:.4f}, p-valor = {p:.4f}")

# Regresión lineal con statsmodels
modelo = smf.ols('presion_sistolica ~ edad', data=pacientes).fit()
print(modelo.summary())

# Regresión lineal con sklearn
from sklearn.linear_model import LinearRegression
import numpy as np

X = pacientes[['edad']].values
y = pacientes['presion_sistolica'].values

reg = LinearRegression().fit(X, y)
print(f"Intercepto: {reg.intercept_:.4f}")
print(f"Pendiente: {reg.coef_[0]:.4f}")
print(f"R²: {reg.score(X, y):.4f}")
```

## Tablas de Contingencia

```python
import pandas as pd
from scipy.stats import chi2_contingency

# Crear tabla de contingencia
pacientes['hipertenso'] = pacientes['presion_sistolica'] >= 130
tabla = pd.crosstab(pacientes['sexo'], pacientes['hipertenso'],
                    margins=True)
print(tabla)

# Chi-cuadrado
chi2, p, dof, expected = chi2_contingency(
    pd.crosstab(pacientes['sexo'], pacientes['hipertenso'])
)
print(f"\nχ² = {chi2:.4f}, p-valor = {p:.4f}, gl = {dof}")
```

## Recursos Adicionales

- [SciPy Stats Documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Statsmodels Documentation](https://www.statsmodels.org/)
- [Python for Data Analysis (libro)](https://wesmckinney.com/book/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [Google Colab (Python en el navegador)](https://colab.research.google.com/)
