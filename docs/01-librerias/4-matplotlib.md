---
id: matplotlib
title: "Matplotlib"
sidebar_label: "​📊 Matplotlib"
sidebar_position: 4
---

**Matplotlib** es la biblioteca de Python más conocida y utilizada para la creación de gráficos y visualizaciones de datos bidimensionales de alta calidad. Fue diseñada originalmente por John Hunter para ofrecer una interfaz de trazado similar a MATLAB dentro de Python, y permite generar figuras aptas para su publicación en una amplia variedad de formatos (PDF, PNG, SVG, etc.).

Es una herramienta fundamental en el ecosistema científico, ya que sirve de base para otras bibliotecas como **Seaborn** y tiene una integración nativa muy fuerte con **Pandas**.

### Ejemplos de uso básicos

Para utilizarla, habitualmente se importa el módulo `pyplot` con el alias `plt`:
```python
import matplotlib.pyplot as plt
import numpy as np
```

#### 1. Gráfico de líneas sencillo
Es el tipo de gráfico por defecto. Puedes pasarle una lista de números y Matplotlib se encarga de generar los ejes y trazar la línea.
```python
# Datos: cuadrados de los números del 1 al 5
cuadrados =
plt.plot(cuadrados)
plt.show()
```

#### 2. Gráfico de dispersión (Scatter plot)
Útil para visualizar puntos individuales y encontrar relaciones entre variables.
```python
# Trazar un solo punto en la coordenada (2, 4) con un tamaño de punto de 200
plt.scatter(2, 4, s=200)
plt.show()
```

#### 3. Histograma
Ideal para explorar la distribución de un conjunto de datos.
```python
datos = np.random.standard_normal(100)
plt.hist(datos, bins=20, color="black", alpha=0.3)
plt.show()
```

### Personalización de gráficos
Matplotlib permite ajustar casi cualquier elemento de la visualización para mejorar su legibilidad:

*   **Títulos y etiquetas:** Se usan métodos como `set_title()`, `set_xlabel()` y `set_ylabel()`.
*   **Leyendas:** Identifican las diferentes series de datos en un mismo gráfico mediante el argumento `label` y la función `plt.legend()`.
*   **Estilos de línea:** Puedes cambiar el color, el grosor (`linewidth`) o el tipo de trazo (discontinuo, puntos, etc.).

**Ejemplo de gráfico personalizado:**
```python
fig, ax = plt.subplots()
ax.plot(,, linewidth=3, label="Cuadrados")
ax.set_title("Números al cuadrado", fontsize=24)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Resultado", fontsize=14)
ax.legend()
plt.show()
```

### Integración con Pandas
Una de las mayores ventajas es que puedes generar gráficos directamente desde objetos de Pandas (Series o DataFrames) con una sintaxis muy simplificada.
```python
import pandas as pd
df = pd.DataFrame(np.random.randn(10, 4).cumsum(0), columns=['A', 'B', 'C', 'D'])
df.plot() # Crea automáticamente un gráfico de líneas con leyenda para las 4 columnas
plt.show()
```

### Visualizaciones avanzadas
Las fuentes también mencionan que Matplotlib puede utilizarse para:
*   **Anotaciones:** Añadir texto y flechas en puntos específicos de interés.
*   **Subgráficos:** Crear cuadrículas con múltiples gráficos en una sola figura usando `plt.subplots()`.
*   **Mapas de calor:** Visualizar matrices de datos bidimensionales mediante funciones como `imshow()`.
*   **Animaciones:** Generar secuencias de gráficos para crear archivos de video o GIFs.

## plt.plot vs ax.plot

La diferencia principal entre usar **`plt.plot`** y **`ax.plot`** radica en el nivel de control y la estructura del código dentro de la librería Matplotlib. Mientras que el primero es una función de conveniencia de alto nivel, el segundo es un método de un objeto específico que ofrece mayor flexibilidad para visualizaciones complejas.

A continuación se detallan las disparidades clave:

### 1. Nivel de la API y Control
*   **`plt.plot`**: Es una función del módulo **`pyplot`** (importado habitualmente como `plt`). Se considera una función de **máximo nivel** que actúa sobre el subgráfico que esté activo en ese momento. Es ideal para trazados rápidos y sencillos donde solo hay un gráfico en la figura.
*   **`ax.plot`**: Es un **método de instancia** de un objeto de tipo **`Axes`** o `AxesSubplot`. Las fuentes indican que es **preferible utilizar métodos de eje** en lugar de funciones de nivel máximo como `plt.plot`, ya que permite personalizar y definir subgráficos de manera directa e independiente dentro de una misma figura.

### 2. Uso en subgráficos (Subplots)
La diferencia se vuelve evidente cuando se trabaja con múltiples gráficos a la vez:
*   Al utilizar la función **`plt.subplots()`**, se obtienen dos variables: **`fig`** (que representa toda la colección de trazados) y **`ax`** (que representa un solo trazado específico). 
*   En este esquema, se usa **`ax.plot()`** para dibujar datos en ese eje concreto, lo que permite un manejo más preciso si la figura tiene, por ejemplo, una cuadrícula de $2\times2$.

### 3. Filosofía de programación
*   **Enfoque de estado (Pyplot):** `plt.plot` sigue un estilo similar a MATLAB, donde el sistema mantiene un seguimiento del "gráfico actual" de forma implícita.
*   **Enfoque orientado a objetos:** `ax.plot` es más "pythónico" y estructurado. Al trabajar con objetos `Axes`, puedes acceder a métodos específicos como `set_title` o `set_xlabel` directamente sobre ese objeto, evitando ambigüedades sobre a qué gráfico te refieres en figuras complejas.

### Resumen comparativo

| Característica | `plt.plot` | `ax.plot` |
| :--- | :--- | :--- |
| **Origen** | Módulo `matplotlib.pyplot` | Clase `Axes` / `AxesSubplot` |
| **Contexto** | Global (actúa sobre el eje activo) | Local (específico de ese objeto `ax`) |
| **Recomendación** | Para gráficos rápidos y únicos | **Preferido** para figuras con múltiples subgráficos |
| **Sintaxis común** | `plt.plot(datos)` | `fig, ax = plt.subplots(); ax.plot(datos)` |

Para mostrar la diferencia entre el enfoque basado en estados (`plt.plot`) y el enfoque orientado a objetos (`ax.plot`), se presentan ejemplos que ilustran cómo se estructuran y cuándo es preferible cada uno.

### 1. Enfoque basado en estados (`plt.plot`)
Este método es el más sencillo y similar a la interfaz de MATLAB. Se utiliza el módulo `pyplot` (alias `plt`) para realizar trazados rápidos de forma implícita sobre la "figura actual" y el "eje actual".

**Ejemplo de uso:**
```python showLineNumbers title="plt.plot"
import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Se traza directamente sobre el estado global
plt.plot(x, y, label='Seno')
plt.title('Estilo Pyplot (plt.plot)') # Afecta al gráfico activo
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
```

### 2. Enfoque orientado a objetos (`ax.plot`)
Este es el enfoque **preferido para personalizaciones complejas**. Aquí se crean explícitamente objetos de tipo `Figure` (la ventana completa) y `Axes` (un trazado individual). Esto permite manipular cada gráfico de forma independiente y precisa.

**Ejemplo de uso:**
```python showLineNumbers title="ax.plot"
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.cos(x)

# Se crean explícitamente los objetos Figure y Axes
fig, ax = plt.subplots() 

# Se usa el método del objeto Axes
ax.plot(x, y, color='red', label='Coseno')
ax.set_title('Estilo Orientado a Objetos (ax.plot)') # Métodos del objeto ax
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
plt.show()
```

### 3. Diferencia clave en subgráficos (Múltiples ejes)
La mayor ventaja de `ax.plot` se hace evidente al trabajar con varias gráficas en una misma figura. Mientras que con `plt` tendrías que estar cambiando de subgráfico activo constantemente, con el enfoque orientado a objetos tienes un objeto `ax` para cada espacio.

**Ejemplo con múltiples subgráficos:**
```python showLineNumbers title="ax.plot con subgraficos"
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

# Se crea una cuadrícula de 1 fila y 2 columnas
# subplots() devuelve un array de objetos Axes en la variable axes
fig, axes = plt.subplots(1, 2, figsize=(10, 4)) 

# Acceso directo al primer objeto Axes
axes.plot(x, np.sin(x), color='blue')
axes.set_title('Seno')

# Acceso directo al segundo objeto Axes
axes.plot(x, np.cos(x), color='green')
axes.set_title('Coseno')

plt.tight_layout() # Ajusta el espacio entre subgráficos
plt.show()
```

### Resumen de diferencias detectadas:
*   **`plt.plot`**: Es una función de **nivel alto** que actúa sobre el subgráfico que esté activo en ese momento de forma global. Es ideal para scripts rápidos o exploraciones breves.
*   **`ax.plot`**: Es un **método de instancia** de la clase `Axes`. Permite una arquitectura de código más limpia y organizada, facilitando la creación de flujos de trabajo donde se definen y personalizan múltiples trazados de manera independiente dentro de una misma figura.

## Anotaciones

Las anotaciones en Matplotlib se utilizan para resaltar puntos de interés, añadir etiquetas explicativas o dibujar formas que mejoren la interpretación de un gráfico. Según las fuentes, existen dos métodos principales para añadir información textual y visual: **`text`** y **`annotate`**.

### 1. El método `text`
Se utiliza para colocar una cadena de texto en coordenadas específicas $(x, y)$ del subgráfico. 
*   **Sintaxis básica:** `ax.text(x, y, "Mensaje", family="monospace", fontsize=10)`.
*   Permite personalizar el estilo de la fuente, el tamaño y otros atributos visuales.

### 2. El método `annotate`
Es una herramienta más avanzada que permite dibujar tanto el **texto** como una **flecha** que apunte a un punto determinado. Es especialmente útil en análisis de series temporales para marcar hitos o eventos específicos.

Los parámetros clave mencionados en los ejemplos son:
*   **`xy`**: Las coordenadas del punto que se desea señalar (por ejemplo, una fecha y un valor de precio).
*   **`xytext`**: Las coordenadas donde se ubicará el texto de la etiqueta.
*   **`arrowprops`**: Un diccionario que define las propiedades de la flecha, como el color (`facecolor`), el ancho (`width`) y las dimensiones de la punta (`headwidth`, `headlength`).
*   **Alineación**: Se pueden usar `horizontalalignment` y `verticalalignment` para ajustar la posición del texto respecto a su coordenada.

### 3. Dibujo de formas (Patches)
A menudo, las anotaciones se complementan con figuras geométricas para encerrar o destacar áreas. Matplotlib ofrece objetos llamados "figuras geométricas" (*patches*) en el módulo `matplotlib.patches`:
*   **Formas comunes:** `Rectangle` (rectángulo), `Circle` (círculo) y `Polygon` (polígono).
*   **Uso:** Se crea el objeto de la forma y luego se añade al subgráfico mediante el método **`ax.add_patch(forma)`**.

### Ejemplo lógico de anotación
En un gráfico de precios financieros, se podría iterar sobre una lista de fechas importantes para añadir anotaciones automáticas:
```python showLineNumbers
# Basado en el ejemplo de la crisis financiera 2008-2009
for fecha, etiqueta in datos_crisis:
    ax.annotate(etiqueta, 
                xy=(fecha, valor_en_fecha + 75), # Punto a señalar
                xytext=(fecha, valor_en_fecha + 225), # Posición del texto
                arrowprops=dict(facecolor="black", headwidth=4, width=2),
                horizontalalignment="left", verticalalignment="top")
```

**Nota sobre otras herramientas:** Si se utiliza la interfaz **Easyviz** (de la biblioteca SciTools), la función `text(x, y, 'texto')` también está disponible, aunque el soporte para flechas en posiciones arbitrarias puede depender del motor de trazado (*backend*) utilizado, como Gnuplot.
