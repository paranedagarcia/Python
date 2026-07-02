---
id: regexp
title: "Expresiones regulares"
sidebar_label: "​📊 Expresiones regulares"
sidebar_position: 2
---


El uso de expresiones regulares (regex) en Python es una de las técnicas más potentes para la **limpieza y preparación de datos** (también llamada *data wrangling* o *munging*), permitiendo identificar y transformar patrones complejos que los métodos de cadena básicos no pueden manejar.

## Módulo `re`

El módulo **`re`** es la herramienta integrada en la biblioteca estándar de Python para trabajar con **expresiones regulares** (también conocidas como *regex* o *regexp*). Estas expresiones consisten en patrones compactos que describen conjuntos de cadenas de caracteres, permitiendo realizar búsquedas, extracciones y transformaciones de texto de manera mucho más potente que los métodos de cadena estándar.

A continuación, se detallan sus usos, funciones principales:

#### Conceptos Básicos y Configuración
Para utilizar este módulo, primero se debe importar en el script. Se recomienda el uso de **cadenas "raw"** (`r"..."`) para definir los patrones, ya que evitan que Python interprete las barras invertidas (`\`) antes de que lleguen al motor de expresiones regulares.

*   **Importación:** `import re`.
*   **Compilación:** Aunque se pueden usar funciones globales, es más eficiente usar `re.compile()` para crear un objeto de expresión regular reutilizable si se va a emplear el mismo patrón repetidamente.

#### Funciones Principales (Usos Comunes)
El módulo `re` organiza sus capacidades en tres categorías principales: coincidencia de patrones, reemplazo y división.

*   **`re.match(patron, cadena)`:** Comprueba si el patrón coincide **únicamente al principio** de la cadena.
*   **`re.search(patron, cadena)`:** Escanea toda la cadena y devuelve la **primera coincidencia** encontrada.
*   **`re.findall(patron, cadena)`:** Devuelve una lista con **todas** las ocurrencias no superpuestas del patrón.
*   **`re.sub(patron, reemplazo, cadena)`:** Sustituye las apariciones del patrón por un texto nuevo.
*   **`re.split(patron, cadena)`:** Divide la cadena en cada punto donde ocurre el patrón.

#### Metacaracteres y Clases de Caracteres
Los patrones se construyen utilizando caracteres literales y metacaracteres especiales:
*   **`.` (Punto):** Coincide con cualquier carácter excepto el de nueva línea.
*   **`\d`:** Cualquier dígito (0-9).
*   **`\w`:** Cualquier carácter alfanumérico (letras, números y guion bajo).
*   **`\s`:** Espacios en blanco (espacios, pestañas, nuevas líneas).
*   **`*`, `+`, `?`:** Cuantificadores que indican 0 o más, 1 o más, o 0/1 apariciones, respectivamente.
*   **`^` y `$`:** Anclas que marcan el inicio y el final de una cadena o línea.

## re.match y re.search()

La principal diferencia entre **`re.match()`** y **`re.search()`** radica en la ubicación dentro de la cadena donde buscan el patrón.

#### Diferencia fundamental en la búsqueda
*   **`re.match(patron, cadena)`**: Solo intenta encontrar una coincidencia **al principio** de la cadena. Si el patrón no está exactamente en el primer carácter, devolverá `None`, incluso si el patrón aparece más adelante en el texto.
*   **`re.search(patron, cadena)`**: Escanea toda la cadena y devuelve la **primera ubicación** donde el patrón coincide, sin importar si está al inicio, en el medio o al final.

#### Comportamiento y valores de retorno
Ambas funciones devuelven un objeto de tipo **`MatchObject`** si encuentran una coincidencia, lo que permite extraer detalles como la posición y el texto capturado. Si no hay coincidencia, ambas devuelven **`None`**.

| Característica | `re.match()` | `re.search()` |
| :--- | :--- | :--- |
| **Punto de inicio** | Debe ser el primer carácter. | Cualquier parte de la cadena. |
| **Uso común** | Validación de formatos (ej. verificar si una línea empieza con `<HTML>`). | Extracción de datos (ej. encontrar un email dentro de un párrafo). |
| **Equivalencia** | Es equivalente a usar `re.search()` con el ancla `^` o `\A` al inicio del patrón. | Es más flexible y similar a la función "match" de otros lenguajes como Perl. |

#### Ejemplos prácticos

#### Caso A: Patrón en medio del texto
Si buscamos la palabra "mundo" en "Hola mundo":
*   `re.match(r"mundo", "Hola mundo")` devolverá `None` porque la cadena empieza con "Hola".
*   `re.search(r"mundo", "Hola mundo")` encontrará la coincidencia exitosamente.

#### Caso B: El parámetro opcional `pos`
A diferencia de las funciones globales, el método `.match()` de un objeto de expresión regular compilado permite un argumento **`pos`** para indicar dónde empezar.
```python showLineNumbers
import re
patron = re.compile(r"mundo")
# match() puede tener éxito si le decimos que empiece en el índice 5
match = patron.match("Hola mundo", 5) 
```
Esto permite que `match()` funcione como una búsqueda localizada a partir de un punto específico.

#### Caso C: Búsqueda multilínea
Cuando se usa la bandera `re.MULTILINE`, el comportamiento de `re.search()` cambia si el patrón incluye el ancla `^`.
*   `re.search(r"^mundo", "Hola\nmundo", re.M)` encontrará la coincidencia porque detecta el inicio de la **segunda línea**.
*   `re.match()` seguirá fallando porque solo considera el inicio absoluto de toda la cadena (a menos que se especifique `pos`).

#### Resumen
Debes usar **`re.match()`** cuando necesites confirmar que una cadena (o línea) sigue una estructura desde su primer carácter, como en la validación estricta de protocolos o encabezados. Usa **`re.search()`** cuando tu objetivo sea localizar información relevante que puede estar "escondida" en cualquier parte de un bloque de texto.

## re.sub

La función **`re.sub()`** del módulo `re` es una de las herramientas más potentes de Python para la limpieza de datos, ya que permite reemplazar patrones complejos de texto que las funciones estándar de cadenas (como `.replace()`) no pueden manejar.

A continuación, se presentan ejemplos prácticos de su uso para limpiar datos, clasificados por categorías:

#### 1. Limpieza básica de caracteres no deseados
Un uso común es eliminar o reemplazar caracteres que ensucian un conjunto de datos, como signos de puntuación o caracteres no numéricos.

*   **Eliminar caracteres no numéricos:** Útil para normalizar números de teléfono o identificadores.
    ```python showLineNumberson
    import re
    telefono = "(123)/456-7890"
    # \D coincide con cualquier carácter que no sea un dígito
    limpio = re.sub(r'\D', '', telefono)
    print(limpio) # Resultado: '1234567890'
    ```

*   **Quitar signos de puntuación específicos:** Ideal para limpiar entradas de encuestas.
    ```python showLineNumberson
    texto = "¡Hola! ¿Cómo estás? #Python"
    # Reemplaza !, # y ? por una cadena vacía
    limpio = re.sub("[!#?]", "", texto)
    print(limpio) # Resultado: 'Hola Cómo estás Python'
    ```

#### 2. Normalización de formato mediante Retroreferencias
Las retroreferencias permiten extraer partes del texto original y reordenarlas en el nuevo formato.

*   **Reformatear números telefónicos:** Convertir una secuencia de 10 dígitos en un formato estándar estadounidense.
    ```python showLineNumberson
    num = "1234567890"
    patron = r"({3})({3})({4})"
    # \1, \2 y \3 se refieren a los grupos capturados entre paréntesis
    formateado = re.sub(patron, r"(\1) \2-\3", num)
    print(formateado) # Resultado: '(123) 456-7890'
    ```

*   **Invertir nombres:** Útil para bases de datos donde se requiere el formato "Apellido, Nombre".
    ```python showLineNumberson
    nombre = "Ada Lovelace"
    limpio = re.sub(r'^(.+?) ([^\s,]+)$', r'\2, \1', nombre)
    print(limpio) # Resultado: 'Lovelace, Ada'
    ```
  

#### 3. Limpieza de texto para Procesamiento de Lenguaje Natural (NLP)
En tareas de texto avanzado, `re.sub` ayuda a expandir contracciones o corregir errores ortográficos comunes.

*   **Expansión de contracciones:**
    ```python showLineNumberson
    texto = "I can't wait"
    # Reemplaza "can't" por su forma expandida
    limpio = re.sub(r"can't", "cannot", texto)
    # Ejemplo genérico para terminaciones como 'll
    limpio = re.sub(r"(\w+)'ll", r"\g<1> will", "I'll go") # 'I will go'
    ```
  

*   **Eliminación de caracteres repetidos:** Corregir exageraciones en redes sociales (ej. "looooove" a "love").
    ```python showLineNumberson
    def remove_repeats(word):
        pattern = re.compile(r'(\w*)(\w)\2(\w*)')
        repl = r'\1\2\3'
        new_word = pattern.sub(repl, word)
        if new_word != word:
            return remove_repeats(new_word) # Recursión para limpiar todo
        return new_word

    print(remove_repeats("looooove")) # Resultado: 'love'
    ```
  

#### 4. Uso de funciones como reemplazo (Callbacks)
`re.sub` permite pasar una función en lugar de una cadena como segundo argumento. Esto permite realizar una lógica de limpieza dinámica basada en el contenido encontrado.

*   **Normalización condicional:** Imagine que necesita convertir códigos antiguos. Si empiezan con un guion deben empezar con 'A', de lo contrario con 'B'.
    ```python showLineNumberson
    def normalizar(matchobj):
        if matchobj.group(1) == '-': return "A"
        else: return "B"

    # Aplica la lógica de la función a cada coincidencia
    resultado = re.sub(r'([-|A-Z])', normalizar, "-1234-X567")
    ```
   

#### 5. Limpieza de espacios y marcas
*   **Colapsar múltiples espacios:** Reemplazar tabuladores y múltiples espacios por uno solo.
    ```python showLineNumberson
    limpio = re.sub(r"\s+", " ", "Texto    con   demasiados   espacios")
    ```
*   **Eliminar etiquetas HTML:** Para extraer solo el texto plano de un documento web.
    ```python showLineNumberson
    html = "<b>Texto importante</b>"
    plano = re.sub(r'<[^>]*>', '', html) # 'Texto importante'
    ```

## Expresiones de Agrupación, Captura y Control

A continuación se muestra una tabla detallada con las secuencias del módulo `re` de Python para la agrupación, captura, condicionales y control de flujo de patrones, junto con su significado.

| Secuencia | Categoría | Significado en Español |
| :--- | :--- | :--- |
| **`(...)`** | Agrupación / Captura | Agrupa patrones y **captura** el sub-texto coincidente en grupos numerados ( \1, \2, etc.). |
| **`(?P<name>...)`** | Captura Nombrada | Crea un grupo que captura el texto y permite referenciarlo mediante un **nombre** específico. |
| **`\n`** (ej. `\1`) | Referencia (Control) | Referencia numérica que coincide con el texto exacto capturado por el n-ésimo grupo previo. |
| **`(?P=name)`** | Referencia Nombrada | Coincide con el texto capturado previamente por el grupo con el nombre indicado. |
| **`(?:...)`** | Agrupación simple | Agrupa patrones para aplicar cuantificadores, pero **no captura** el texto (ahorra memoria). |
| **`(?>...)`** | Grupo Atómico | Agrupa patrones y **desactiva el retroceso** (backtracking); si falla después, no reintenta permutaciones. |
| **`(?(id/name)yes\|no)`** | Condicional | Si el grupo con ese ID o nombre coincidió, intenta el patrón **yes**; si no, intenta el patrón **no**. |
| **`(?iLmsux)`** | Modificadores (Control) | Establece banderas de compilación (ej. `i` ignora mayúsculas) dentro de la propia expresión. |
| **`(?#...)`** | Comentario | Permite incluir un **comentario** dentro de la expresión regular que el motor ignora al procesar. |
| **`(?=...)`** | Lookahead Positivo | Asegura que el patrón siguiente coincida, pero **no consume** caracteres del texto. |
| **`(?!...)`** | Lookahead Negativo | Asegura que el patrón siguiente **no** coincida; es una aserción de ancho cero. |
| **`(?<=...)`** | Lookbehind Positivo | Asegura que el patrón indicado **preceda** a la posición actual; requiere longitud fija en Python. |
| **`(?<!...)`** | Lookbehind Negativo | Asegura que el patrón indicado **no preceda** a la posición actual en el texto. |

### Notas Adicionales
*   **Captura vs. No captura:** Los grupos de captura `(...)` son esenciales para extraer información específica de una cadena, mientras que los grupos `(?:...)` se prefieren cuando solo se necesita aplicar repetición o alternación sin interés en recuperar ese fragmento por separado.
*   **Condicionales:** El patrón `no-pattern` en el condicional es opcional; si se omite, simplemente no se busca nada adicional si el grupo previo no existe.
*   **Grupos Atómicos:** Aunque no son soportados nativamente por el módulo estándar `re` de Python, se pueden emular o utilizar mediante el módulo externo `regex` para prevenir el "backtracking" catastrófico.

## Ejemplos

#### Básico: Extracción de números telefónicos
Para buscar un patrón simple de tres dígitos separados por un guion de otros tres y cuatro dígitos finales:
```pythpython showLineNumberson
import re
texto = "Llama al 123-456-7890"
patron = r"\d{3}-\d{3}-\d{4}"
coincidencia = re.search(patron, texto)
if coincidencia:
    print(f"Encontrado: {coincidencia.group()}") # Resultado: 123-456-7890
```

#### Intermedio: Grupos y validación de correos
El uso de paréntesis `()` permite crear **grupos de captura** para extraer partes específicas de una coincidencia.
```python showLineNumbers
patron_email = r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})"
email = "usuario@dominio.com"
match = re.match(patron_email, email)
if match:
    usuario, dominio = match.groups() # Extrae ('usuario', 'dominio.com')
```

#### Avanzado: Grupos Nombrados y Búsqueda Detallada (Verbose)
Para patrones complejos, se puede usar el flag `re.VERBOSE` para añadir comentarios y espacios, y **grupos nombrados** `(?P<nombre>...)` para mayor claridad.
```python showLineNumbers
patron_log = re.compile(r"""
    (?P<fecha>\w{3}\s\d{2},\s\d{4}) # Fecha (Ej: Apr 05, 2021)
    \s+
    (?P<nivel>\w+)                  # Nivel (Ej: WARNING)
    \s+
    (?P<mensaje>.*)                 # El resto de la línea
""", re.VERBOSE)

linea = "Apr 05, 2021 WARNING Watch for errors."
match = patron_log.match(linea)
if match:
    print(match.groupdict()) # Devuelve un diccionario con las claves 'fecha', 'nivel', 'mensaje'
```

#### Avanzado: Lookaround (Aseveraciones de ancho cero)
Las aseveraciones de tipo **Lookahead** (`(?=...)`) y **Lookbehind** (`(?<=...)`) permiten buscar patrones basados en lo que tienen delante o detrás sin "consumir" esos caracteres del resultado final.
*   **Búsqueda de palabra seguida de coma:** `r"\w+(?=,)"` encontrará "Félix" en "Félix, Víctor y Carlos" pero no incluirá la coma en el resultado.

#### Modificadores (Flags) de Compilación
El comportamiento del módulo puede alterarse mediante banderas:
*   **`re.IGNORECASE` (o `re.I`):** Ignora diferencias entre mayúsculas y minúsculas.
*   **`re.MULTILINE` (o `re.M`):** Permite que `^` y `$` coincidan con el inicio/final de cada línea y no solo de toda la cadena.
*   **`re.DOTALL` (o `re.S`):** Hace que el punto (`.`) coincida también con el carácter de nueva línea.

## Limpieza de datos

A continuación, se presentan ejemplos de limpieza, organizados por su aplicación práctica:

#### Limpieza de caracteres no deseados y puntuación
Cuando se trabaja con datos provenientes de encuestas o textos sin estructura, es común encontrar signos de puntuación o símbolos que interfieren con el análisis.
*   **Ejemplo:** Eliminar símbolos específicos como `!`, `#` o `?` de una lista de nombres de estados.
*   **Código:** Utilizando `re.sub()`, se puede definir un patrón que busque cualquiera de estos caracteres y los reemplace por una cadena vacía:
    ```python showLineNumbers
    import re
    def clean_punctuation(text):
        return re.sub("[!#?]", "", text) #
    ```
*   **Aplicación en análisis de texto:** En el procesamiento de obras literarias (como el *Don Quijote*), se utiliza regex para eliminar signos de puntuación de todo el texto en un solo paso antes de contar frecuencias de palabras, lo que es mucho más eficiente que hacerlo palabra por palabra.

#### Estandarización de formatos numéricos
A menudo, los datos numéricos vienen "sucios" con caracteres de formato (paréntesis, guiones o espacios) que impiden su conversión a tipos `int` o `float`.
*   **Limpieza de números telefónicos:** Para extraer solo los dígitos de una cadena como `(123)/456-7890`, se utiliza el patrón `\D` (que coincide con cualquier carácter que **no** sea un dígito) y se reemplaza por nada.
*   **Detección en archivos CSV:** En Pandas, se puede usar `.str.extract(r'([^0-9.])')` para encontrar rápidamente todos los caracteres no numéricos que "ensucian" una columna que debería ser puramente numérica, permitiendo diagnosticarlos y eliminarlos antes de la conversión de tipo.

#### Expansión de contracciones y corrección de palabras
En el procesamiento de lenguaje natural (NLP), la limpieza implica normalizar el texto para que el análisis sea consistente.
*   **Contracciones en inglés:** Mediante una lista de patrones, se pueden expandir formas como "can't" a "cannot" o "i'm" a "i am".
*   **Caracteres repetidos:** Para limpiar errores de escritura como "looooove", se emplea un patrón con **retrorreferencias** (`r'(\w*)(\w)\2(\w*)'`) que identifica letras duplicadas accidentalmente y las reduce a una sola instancia de forma recursiva.

#### Extracción de información específica
La limpieza también consiste en separar datos valiosos de un bloque de texto irrelevante.
*   **Correos electrónicos y dominios:** Se utilizan grupos (paréntesis en el patrón) para descomponer una dirección de correo en usuario, dominio y sufijo.
*   **Análisis de registros (Logs):** Al limpiar archivos de registro de servidores, se utilizan expresiones regulares compiladas para extraer de forma precisa la marca de tiempo, el nivel de error (como "WARN") y el mensaje, ignorando el resto del ruido del archivo.

#### Limpieza vectorizada en Pandas
Pandas permite aplicar expresiones regulares de forma masiva a columnas enteras de un DataFrame mediante el accesor `.str`, gestionando automáticamente los valores nulos (`NaN`).
*   **Extracción de años de experiencia:** Si una columna de texto contiene "Menos de 1 año" o "10-20 años", se puede usar `.str.extract(r'(\d+)')` para limpiar la columna y quedarse únicamente con el primer número encontrado, facilitando cálculos matemáticos posteriores.
*   **Reemplazo parcial:** A diferencia del método `.replace` estándar de las series (que busca coincidencias totales), `.str.replace` con `regex=True` permite modificar solo fragmentos de la cadena basados en patrones, como cambiar guiones bajos por puntos en versiones de software.

#### Resumen de patrones comunes para limpieza:
*   **`\s+`**: Coincide con uno o más caracteres de espacio en blanco (útil para normalizar separadores irregulares).
*   **`\d`**: Coincide con cualquier dígito numérico.
*   **`^` y `$`**: Marcan el inicio y el fin de una línea, asegurando que la limpieza se aplique exactamente donde se desea.
*   **`[^...]`**: Clase de caracteres negada; útil para eliminar todo lo que **no** sea un conjunto de caracteres permitidos.

## Ejemplos

Las expresiones regulares (**regex**) son herramientas esenciales en Python para el procesamiento de texto y la **limpieza de datos** (*data wrangling*), permitiendo identificar y transformar patrones complejos que los métodos de cadena estándar no pueden gestionar eficientemente.

A continuación, se presentan ejemplos prácticos de limpieza de datos:

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

**Nota técnica:** Se recomienda el uso de **literales de cadena cruda (raw)** (`r""`) para definir los patrones, ya que evitan que Python interprete las barras invertidas (`\`) antes de que lleguen al motor de expresiones regulares.

```python showLineNumbers
import re

# Para comprobar si la cadena consiste en 3 caracteres seguidos de un 
# punto, por ejemplo, podríamos utilizar lo siguiente:
re.match(“...\.”, “abc.”)

"""  
expresión que sólo resultara cierta para las cadenas “python”, “jython” y “cython” 
y ninguna otra, podríamos utilizar el carácter ‘|’ para expresar alternativa 
escribiendo los tres subpatrones completos
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

### Validar emails

Las expresiones regulares (**regex**) son herramientas potentes para identificar patrones complejos en cadenas de texto, como las direcciones de correo electrónico. Es importante destacar que, aunque existen patrones que cubren la mayoría de los casos comunes, la especificación completa para validar todos los correos electrónicos posibles según los estándares oficiales (RFC) es extremadamente larga y compleja, por lo que en la práctica se suelen utilizar versiones simplificadas.

A continuación, se presentan ejemplos de expresiones regulares para validar emails:

#### 1. Patrón Básico y Funcional
Este es un ejemplo estándar capaz de identificar la mayoría de las direcciones de correo electrónico comunes. Se recomienda usarlo con el indicador `re.IGNORECASE` para que no distinga entre mayúsculas y minúsculas.

*   **Patrón:** `r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}"`.
*   **Explicación:** Busca una secuencia de caracteres permitidos (letras, números y símbolos como `.` o `_`), seguida de un símbolo `@`, luego el dominio y finalmente un sufijo de 2 a 4 caracteres.

#### 2. Patrón con Grupos de Captura
Si además de validar deseas extraer partes específicas del correo (usuario, dominio y sufijo), puedes usar paréntesis para crear grupos.

*   **Patrón:** `r"([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})"`.
*   **Uso en Python:** Al usar `re.findall()`, este patrón devolverá una lista de tuplas con los tres componentes separados.

#### 3. Patrón con Grupos Nombrados
Para mayor claridad en el código, Python permite asignar nombres a los grupos de captura dentro de la expresión regular mediante la sintaxis `(?P<nombre>...)`.

*   **Ejemplo:** `r"(?P<name>[a-z0-9._%+-]+)@(?P<domain>[a-z0-9.-]+\.[a-z]{2,})"`.
*   **Ventaja:** Permite acceder a los resultados mediante el método `.groupdict()`, obteniendo un diccionario donde las claves son "name" y "domain".

#### 4. Ejemplo "Verbose" (Legible)
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




#### Consideraciones técnicas
*   **Cadenas "Raw":** Se recomienda siempre prefijar los patrones con una `r` (ej. `r"..."`) para que las barras invertidas (`\`) se traten de forma literal y no como caracteres de escape de Python.
*   **Compilación:** Si vas a validar muchos correos en un bucle, utiliza `re.compile()` para crear un objeto regex reutilizable y ahorrar ciclos de CPU.
*   **Emails no ASCII:** Aunque los patrones anteriores se centran en caracteres estándar, existen validaciones que permiten caracteres de otros alfabetos (como el griego o cirílico), lo cual es relevante en aplicaciones globales.

## Uso de condicionales

Las expresiones regulares en Python, a través del módulo **`re`**, permiten el uso de **condicionales**, los cuales funcionan de manera similar a una sentencia `if-else` tradicional,. Esta estructura intenta hacer coincidir un patrón específico dependiendo de si un grupo de captura previo tuvo éxito o no,.

### Sintaxis y Lógica
La sintaxis básica es: **`(?(id/name)yes-pattern|no-pattern)`**,.

*   **`id/name`**: Es el número de índice o el nombre del grupo de captura que se quiere verificar,.
*   **`yes-pattern`**: El patrón que debe coincidir si el grupo referenciado fue capturado.
*   **`no-pattern`**: (Opcional) El patrón que debe coincidir si el grupo referenciado **no** fue capturado,.

---

### Ejemplo Práctico: Validación de Identificadores
Imagina que tienes identificadores de productos con dos formatos posibles:
1.  Si empieza con un **código de país** (2 dígitos y un guion), debe terminar obligatoriamente con un **código de área** (2 dígitos). Ejemplo: `34-adr1-01`.
2.  Si **no** tiene código de país, debe terminar con un **nombre** (3-4 letras minúsculas). Ejemplo: `adr1-sala`.

#### Código en Python:
```python showLineNumbers
import re

# Definición del patrón con condicional
# Grupo 1: (\d\d-)? -> Código de país opcional
# Grupo 2: (\w{3,4}) -> ID de producto
# Condicional: (?(1)(\d\d)|[a-z]{3,4}) 
#   -> Si existe el Grupo 1, busca 2 dígitos.
#   -> Si NO existe el Grupo 1, busca 3-4 letras minúsculas.

pattern = re.compile(r"(\d\d-)?(\w{3,4})-(?(1)(\d\d)|[a-z]{3,4})$")

# Casos de prueba
test_cases = ["34-adr1-01", "adr1-sala", "34-adr1-sala", "adr1-01"]

for test in test_cases:
    match = pattern.match(test)
    if match:
        print(f"'{test}': Coincidencia encontrada.")
    else:
        print(f"'{test}': No coincide.")
```

---

### Desglose del ejemplo
1.  **`(\d\d-)?`**: Crea el **grupo 1**, que busca dos números seguidos de un guion. El signo `?` lo hace opcional.
2.  **`(\w{3,4})`**: El **grupo 2** busca el núcleo del ID (de 3 a 4 caracteres alfanuméricos).
3.  **`(?(1)(\d\d)|[a-z]{3,4})`**: Aquí reside la lógica condicional. El motor de regex pregunta: "¿Se capturó el grupo 1?". 
    *   Si la respuesta es **sí** (ej. `34-`), intenta emparejar el patrón `(\d\d)` (dos dígitos adicionales).
    *   Si la respuesta es **no**, intenta emparejar `[a-z]{3,4}` (letras minúsculas).
4.  **`$`**: Asegura que el patrón coincida hasta el final de la cadena para evitar validaciones parciales.

### Otros usos comunes
*   **Consistencia en delimitadores**: En formatos de fecha como ISO 8601, puedes usar un condicional para asegurar que, si se usó un guion después del año, también se use después del mes. Si el primer guion se omitió, el segundo también debe omitirse,.
*   **Validación estricta**: Puedes usar un "lookahead" negativo vacío `(?!)` en la parte del `else` para forzar que la expresión falle si un grupo obligatorio no está presente.

### Validación de fecha

Para validar fechas con la estructura condicional **`(?(id)yes|no)`**, el ejemplo más destacado en las fuentes es la validación del formato **ISO 8601**. Este mecanismo permite asegurar la **consistencia de los delimitadores**: si se usa un guion para separar el año del mes, también debe usarse para separar el mes del día.

:::info
**ISO 8601** es un estándar internacional creado por la Organización Internacional de Normalización (ISO) que especifica formatos uniformes para la representación y el intercambio de fechas y horas.
El estándar utiliza una jerarquía que va desde la unidad de tiempo más grande hasta la más pequeña (año-mes-día)
- **Fecha de calendario**: Se representa típicamente como YYYY-MM-DD, por ejemplo: 2025-05-21
- **Combinación de fecha y hora**: Se utiliza la letra "T" para separar ambos componentes. Un ejemplo completo sería 2021-03-28T15:25:16.258274
- **Referencia UTC**: Si la hora está en tiempo universal coordinado (UTC), se añade la letra "Z" al final (ej. 2021-08-31T01:01:01Z)
:::

#### Sintaxis y Funcionamiento
La estructura **`(?(id)yes-pattern|no-pattern)`** actúa como un "if-else". El motor de búsqueda verifica si el grupo de captura identificado por el `id` (un número) tuvo éxito; si es así, intenta coincidir con el `yes-pattern`, de lo contrario intenta el `no-pattern`.

#### Ejemplo: Consistencia en fechas y horas (ISO 8601)
Este patrón permite validar cadenas como `2023-10-25 14:30:05` o `20231025 143005`, pero **rechaza** formatos inconsistentes como `2023-1025`.



**Expresión regular:**
`^({4})(-)?(1|0)(?(2)-)(3|0|) (2)(?(2):)()(?(2):)()$`

**Desglose del condicional:**
1.  **`({4})`**: Grupo 1 (Año).
2.  **`(-)?`**: **Grupo 2 (Guion opcional)**. Este es el activador del condicional.
3.  **`(1|0)`**: Mes.
4.  **`(?(2)-)`**: El condicional. Dice: "Si el **Grupo 2** (el guion) existió, aquí **debe** haber otro guion".
5.  **`(3|0|)`**: Día.
6.  **`(2)`**: Hora.
7.  **`(?(2):)`**: Si el Grupo 2 existió, aquí **debe** haber dos puntos (`:`) para separar los minutos.

---

#### Código de ejemplo en Python
El módulo **`re`** de Python soporta completamente esta funcionalidad.

```python showLineNumbers
import re

# Patrón que exige consistencia en los delimitadores
# Si hay un guion en la fecha, debe haber guion en el día y ':' en la hora
pattern = re.compile(r"^({4})(-)?(1|0)(?(2)-)(3|0|) (2)(?(2):)()(?(2):)()$")

test_dates = [
    "2023-10-25 14:30:05",  # VÁLIDO (Delimitadores consistentes)
    "20231025 143005",     # VÁLIDO (Sin delimitadores, consistente)
    "2023-1025 14:30:05",   # INVÁLIDO (Falta guion en el día)
    "2023-10-25 143005"     # INVÁLIDO (Faltan ':' en la hora habiendo guiones)
]

for date in test_dates:
    if pattern.match(date):
        print(f"'{date}': Formato válido.")
    else:
        print(f"'{date}': Formato inválido.")
```

#### Versión con Grupos Nombrados
Python también permite usar nombres en lugar de números para los condicionales, lo que hace el código más legible:
`^(?P<year>{4})(?P<hyphen>-)?(?P<month>1|0)(?(hyphen)-)...`. En este caso, el condicional **`(?(hyphen)-)`** verifica si el grupo nombrado `hyphen` participó en la coincidencia.