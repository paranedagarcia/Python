---
id: regexp
title: "Expresiones regulares"
sidebar_label: "​📊 Expresiones regulares"
sidebar_position: 2
---


El uso de expresiones regulares (regex) en Python es una de las técnicas más potentes para la **limpieza y preparación de datos** (también llamada *data wrangling* o *munging*), permitiendo identificar y transformar patrones complejos que los métodos de cadena básicos no pueden manejar.

A continuación, se presentan ejemplos de limpieza de datos extraídos de las fuentes, organizados por su aplicación práctica:

### 1. Limpieza de caracteres no deseados y puntuación
Cuando se trabaja con datos provenientes de encuestas o textos sin estructura, es común encontrar signos de puntuación o símbolos que interfieren con el análisis.
*   **Ejemplo:** Eliminar símbolos específicos como `!`, `#` o `?` de una lista de nombres de estados.
*   **Código:** Utilizando `re.sub()`, se puede definir un patrón que busque cualquiera de estos caracteres y los reemplace por una cadena vacía:
    ```python
    import re
    def clean_punctuation(text):
        return re.sub("[!#?]", "", text) #
    ```
*   **Aplicación en análisis de texto:** En el procesamiento de obras literarias (como el *Don Quijote*), se utiliza regex para eliminar signos de puntuación de todo el texto en un solo paso antes de contar frecuencias de palabras, lo que es mucho más eficiente que hacerlo palabra por palabra.

### 2. Estandarización de formatos numéricos
A menudo, los datos numéricos vienen "sucios" con caracteres de formato (paréntesis, guiones o espacios) que impiden su conversión a tipos `int` o `float`.
*   **Limpieza de números telefónicos:** Para extraer solo los dígitos de una cadena como `(123)/456-7890`, se utiliza el patrón `\D` (que coincide con cualquier carácter que **no** sea un dígito) y se reemplaza por nada.
*   **Detección en archivos CSV:** En Pandas, se puede usar `.str.extract(r'([^0-9.])')` para encontrar rápidamente todos los caracteres no numéricos que "ensucian" una columna que debería ser puramente numérica, permitiendo diagnosticarlos y eliminarlos antes de la conversión de tipo.

### 3. Expansión de contracciones y corrección de palabras
En el procesamiento de lenguaje natural (NLP), la limpieza implica normalizar el texto para que el análisis sea consistente.
*   **Contracciones en inglés:** Mediante una lista de patrones, se pueden expandir formas como "can't" a "cannot" o "i'm" a "i am".
*   **Caracteres repetidos:** Para limpiar errores de escritura como "looooove", se emplea un patrón con **retrorreferencias** (`r'(\w*)(\w)\2(\w*)'`) que identifica letras duplicadas accidentalmente y las reduce a una sola instancia de forma recursiva.

### 4. Extracción de información específica
La limpieza también consiste en separar datos valiosos de un bloque de texto irrelevante.
*   **Correos electrónicos y dominios:** Se utilizan grupos (paréntesis en el patrón) para descomponer una dirección de correo en usuario, dominio y sufijo.
*   **Análisis de registros (Logs):** Al limpiar archivos de registro de servidores, se utilizan expresiones regulares compiladas para extraer de forma precisa la marca de tiempo, el nivel de error (como "WARN") y el mensaje, ignorando el resto del ruido del archivo.

### 5. Limpieza vectorizada en Pandas
Pandas permite aplicar expresiones regulares de forma masiva a columnas enteras de un DataFrame mediante el accesor `.str`, gestionando automáticamente los valores nulos (`NaN`).
*   **Extracción de años de experiencia:** Si una columna de texto contiene "Menos de 1 año" o "10-20 años", se puede usar `.str.extract(r'(\d+)')` para limpiar la columna y quedarse únicamente con el primer número encontrado, facilitando cálculos matemáticos posteriores.
*   **Reemplazo parcial:** A diferencia del método `.replace` estándar de las series (que busca coincidencias totales), `.str.replace` con `regex=True` permite modificar solo fragmentos de la cadena basados en patrones, como cambiar guiones bajos por puntos en versiones de software.

### Resumen de patrones comunes para limpieza:
*   **`\s+`**: Coincide con uno o más caracteres de espacio en blanco (útil para normalizar separadores irregulares).
*   **`\d`**: Coincide con cualquier dígito numérico.
*   **`^` y `$`**: Marcan el inicio y el fin de una línea, asegurando que la limpieza se aplique exactamente donde se desea.
*   **`[^...]`**: Clase de caracteres negada; útil para eliminar todo lo que **no** sea un conjunto de caracteres permitidos.

### EJEMPLOS:

Las expresiones regulares (**regex**) son herramientas esenciales en Python para el procesamiento de texto y la **limpieza de datos** (*data wrangling*), permitiendo identificar y transformar patrones complejos que los métodos de cadena estándar no pueden gestionar eficientemente.

A continuación, se presentan ejemplos prácticos de limpieza de datos extraídos de las fuentes:

#### 1. Normalización de números telefónicos
Cuando los datos provienen de entradas libres, pueden incluir diversos separadores. Para obtener una forma canónica (solo dígitos), se utiliza el patrón `\D`, que coincide con cualquier carácter que **no** sea un número.

```python showLineNumbers
import re
sucio = "(123)/456-7890"
# re.sub reemplaza todo lo que no sea dígito por una cadena vacía
limpio = re.sub(r'\D', '', sucio) 
# Resultado: '1234567890'
```

#### 2. Eliminación de signos de puntuación
En el análisis de grandes bloques de texto (como obras literarias), es común querer eliminar símbolos que ensucian el conteo de palabras. Se recomienda usar `re.compile()` para mejorar la eficiencia si la operación se repite.

```python showLineNumbers
import re
texto = "¡Hola mundo! #Python? [limpieza]"
# El patrón busca los caracteres específicos dentro de los corchetes
patron_punc = re.compile(r"[!#?\[\]]")
limpio = patron_punc.sub("", texto)
# Resultado: 'Hola mundo Python limpieza'
```

#### 3. Expansión de contracciones (Normalización de texto)
Para que un analizador de texto sea consistente, se pueden expandir contracciones comunes. Este proceso utiliza **grupos de captura** y referencias (como `\g<1>`) para mantener la raíz de la palabra.

```python showLineNumbers
import re
def expandir_contracciones(texto):
    # Ejemplo para 'can't' y formas con ''ll'
    patrones = [
        (r"can't", "cannot"),
        (r"(\w+)'ll", r"\g<1> will")
    ]
    for reg, rep in patrones:
        texto = re.sub(reg, rep, texto)
    return texto

print(expandir_contracciones("I can't, they'll do it"))
# Resultado: 'I cannot, they will do it'
```

#### 4. Limpieza de caracteres repetidos
En redes sociales o encuestas, los usuarios suelen exagerar palabras (ej. "looooove"). Se pueden usar **retrorreferencias** (`\2`) para identificar letras duplicadas y reducirlas.

```python showLineNumbers
import re
# Busca un carácter (\w) seguido de sí mismo (\2)
patron_rep = re.compile(r'(\w*)(\w)\2(\w*)')
def limpiar_repeticion(palabra):
    nueva = patron_rep.sub(r'\1\2\3', palabra)
    if nueva != palabra:
        return limpiar_repeticion(nueva) # Recursivo hasta que no haya más
    return nueva

print(limpiar_repeticion("looooove")) 
# Resultado: 'love'
```

#### 5. Limpieza de columnas en Pandas
Pandas permite aplicar regex de forma masiva a columnas mediante el accesor `.str`. Es muy útil para extraer números de cadenas de texto "sucias" o identificar caracteres inválidos en archivos CSV.

```python showLineNumbers
import pandas as pd
df = pd.DataFrame({'experiencia': ['Menos de 1 año', '10-20 años', '5 años']})

# Extracción de solo los dígitos de la columna
df['años_num'] = df['experiencia'].str.extract(r'(\d+)').astype(float)
# Resultado: 1.0, 10.0, 5.0

# Identificar caracteres no numéricos accidentales en una columna que debería ser float
# df['col'].str.extract(r'([^0-9.])').value_counts()
```

#### 6. Descomposición de registros (Logs)
Para limpiar archivos de registro (*logs*), se definen patrones con **grupos nombrados** (`?P<nombre>`). Esto permite separar la marca de tiempo, el nivel de error y el mensaje en una estructura de diccionario lista para analizar.

```python showLineNumbers
import re
log_line = "Apr 05, 2021 20:04:41 WARNING Watch for warnings."
# Definición con grupos nombrados para mayor claridad
patron_log = re.compile(
    r"(?P<fecha>\w{3} \d{2}, \d{4} \d{2}:\d{2}:\d{2})\s+"
    r"(?P<nivel>\w+)\s+"
    r"(?P<msg>.*)"
)
match = patron_log.match(log_line)
if match:
    datos = match.groupdict()
    # Resultado: {'fecha': 'Apr 05...', 'nivel': 'WARNING', 'msg': 'Watch...'}
```

**Nota técnica:** Se recomienda el uso de **literales de cadena cruda** (`r""`) para definir los patrones, ya que evitan que Python interprete las barras invertidas (`\`) antes de que lleguen al motor de expresiones regulares.

```python showLineNumbers
import re

# Para comprobar si la cadena consiste en 3 caracteres seguidos de un 
# punto, por ejemplo, podríamos utilizar lo siguiente:
re.match(“...\.”, “abc.”)

"""  expresión que sólo resultara cierta para las cade-
nas “python”, “jython” y “cython” y ninguna otra, podríamos utilizar 
el carácter ‘|’ para expresar alternativa escribiendo los tres subpatro-
nes completos
"""
exp = re.match(“python|jython|cython”, “python”)

""" tan solo la parte que pueda cambiar, encerrada entre paréntesis, 
formando lo que se conoce como un grupo."""
exp = re.match(“(p|j|c)ython”, “python”)
# ó
exp = re.match(“[pjc]ython”, “python”)

""" comprobar si la cadena es “python0”, “python1”, “python2”, ... , “python9” """
exp = re.match(“python[0-9]”, “python0”)
```

## Validar emails

Las expresiones regulares (**regex**) son herramientas potentes para identificar patrones complejos en cadenas de texto, como las direcciones de correo electrónico. Es importante destacar que, aunque existen patrones que cubren la mayoría de los casos comunes, la especificación completa para validar todos los correos electrónicos posibles según los estándares oficiales (RFC) es extremadamente larga y compleja, por lo que en la práctica se suelen utilizar versiones simplificadas.

A continuación, se presentan ejemplos de expresiones regulares para validar emails extraídos de las fuentes:

### 1. Patrón Básico y Funcional
Este es un ejemplo estándar capaz de identificar la mayoría de las direcciones de correo electrónico comunes. Se recomienda usarlo con el indicador `re.IGNORECASE` para que no distinga entre mayúsculas y minúsculas.

*   **Patrón:** `r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}"`.
*   **Explicación:** Busca una secuencia de caracteres permitidos (letras, números y símbolos como `.` o `_`), seguida de un símbolo `@`, luego el dominio y finalmente un sufijo de 2 a 4 caracteres.

### 2. Patrón con Grupos de Captura
Si además de validar deseas extraer partes específicas del correo (usuario, dominio y sufijo), puedes usar paréntesis para crear grupos.

*   **Patrón:** `r"([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})"`.
*   **Uso en Python:** Al usar `re.findall()`, este patrón devolverá una lista de tuplas con los tres componentes separados.

### 3. Patrón con Grupos Nombrados
Para mayor claridad en el código, Python permite asignar nombres a los grupos de captura dentro de la expresión regular mediante la sintaxis `(?P<nombre>...)`.

*   **Ejemplo:** `r"(?P<name>[a-z0-9._%+-]+)@(?P<domain>[a-z0-9.-]+\.[a-z]{2,})"`.
*   **Ventaja:** Permite acceder a los resultados mediante el método `.groupdict()`, obteniendo un diccionario donde las claves son "name" y "domain".

### 4. Ejemplo "Verbose" (Legible)
Para patrones complejos, se recomienda usar el modificador `re.VERBOSE` (o `(?x)`), que permite añadir comentarios y espacios dentro de la regex para que sea más fácil de leer.

```python showLineNumbers
import re
pat_email = re.compile(r'''
    (?xm)                    # Modo verbose y multilínea
    ([A-Za-z0-9-]+\.)?       # Parte inicial opcional (ej. nombre.)
    [A-Za-z0-9-]+            # Usuario principal
    @                        # Símbolo arroba obligatorio
    (\w+\.?){2,}             # Al menos dos grupos de dominio (ej. gmail.com)
    (?=[\s\.,>)’"\]])       # Aserción: seguido de espacio o puntuación
''')
```

### Consideraciones técnicas
*   **Cadenas "Raw":** Se recomienda siempre prefijar los patrones con una `r` (ej. `r"..."`) para que las barras invertidas (`\`) se traten de forma literal y no como caracteres de escape de Python.
*   **Compilación:** Si vas a validar muchos correos en un bucle, utiliza `re.compile()` para crear un objeto regex reutilizable y ahorrar ciclos de CPU.
*   **Emails no ASCII:** Aunque los patrones anteriores se centran en caracteres estándar, existen validaciones que permiten caracteres de otros alfabetos (como el griego o cirílico), lo cual es relevante en aplicaciones globales.