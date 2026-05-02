---
id: pandas
title: Pandas
sidebar_label: Pandas
sidebar_position: 1
---

# Pandas

Pandas es una biblioteca de Python diseñada para análisis y manipulación de datos. Proporciona estructuras de datos eficientes y herramientas para trabajar con datos tabulares y series temporales.

## Características principales

- **DataFrames**: Estructuras bidimensionales similares a tablas SQL o hojas de cálculo
- **Series**: Arreglos unidimensionales etiquetados
- **Manipulación de datos**: Filtrado, transformación, agregación y limpieza
- **Lectura/Escritura**: Soporte para múltiples formatos (CSV, Excel, JSON, SQL, etc.)
- **Análisis estadístico**: Cálculos rápidos y resúmenes de datos
- **Manejo de valores faltantes**: Herramientas para detectar y tratar datos ausentes

## Instalación

```python
pip install pandas
```

## Uso básico

```python
import pandas as pd

# Crear un DataFrame
df = pd.DataFrame({'columna1': [1, 2, 3], 'columna2': ['a', 'b', 'c']})

# Ver primeras filas
df.head()
```

Pandas es esencial para ciencia de datos, análisis exploratorio y preparación de datos en Python.