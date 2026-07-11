---
id: datos
title: "Datos y estructuras"
sidebar_label: "💻 Datos y estructuras"
sidebar_position: 5
---

:::info[Codigo:]
- https://colab.research.google.com/drive/1S3lUwphZRBF6mobRPb_fym7AZ2AbNjcB
:::

En Python, los datos se representan mediante **objetos**, y los nombres (lo que usualmente llamamos variables) son simplemente **etiquetas** que hacen referencia a estos objetos en la memoria,.

A continuación se definen los tipos de datos principales y sus límites:

### Tipos Numéricos
*   **Enteros (`int`):** Representan números sin decimales. En Python 3, los enteros tienen **precisión arbitraria**, lo que significa que no tienen un límite fijo de tamaño más allá de la memoria virtual disponible en el sistema.
*   **Punto Flotante (`float`):** Se utilizan para números reales con decimales. Python implementa este tipo siguiendo el estándar **IEEE 754 de doble precisión** (64 bits).
    *   **Límites:** El valor máximo suele ser aproximadamente $1.79 \times 10^{308}$ y el mínimo cercano a $2.22 \times 10^{-308}$.
    *   **Limitación crítica:** Sufren de **errores de redondeo** ya que no pueden representar exactamente muchas fracciones decimales (como 0.1), lo que puede acumular imprecisiones en cálculos extensos.
*   **Complejos (`complex`):** Consisten en un par de números de punto flotante que representan la parte real y la imaginaria (denotada con `j` en Python). Comparten las mismas limitaciones de precisión que los `float`.

### Tipos de Secuencia y Colecciones
*   **Cadenas (`str`):** Secuencias inmutables de caracteres Unicode,. No tienen un límite intrínseco de longitud; pueden procesar tantos datos como la memoria del sistema permita (por ejemplo, archivos de texto con millones de líneas).
*   **Listas (`list`):** Colecciones ordenadas y **mutables** que pueden contener elementos de cualquier tipo,. Su límite es la memoria RAM disponible.
*   **Tuplas (`tuple`):** Similares a las listas pero **inmutables** (no pueden cambiarse tras su creación),. Son más ligeras en memoria que las listas.
*   **Diccionarios (`dict`):** Mapas de clave-valor donde las claves deben ser objetos inmutables y "hasheables",. Permiten búsquedas muy rápidas independientemente del tamaño de la colección.
*   **Conjuntos (`set`):** Colecciones desordenadas de elementos únicos e inmutables. Optimizan la verificación de pertenencia mediante el uso de *hashes*.

### Tipos Especiales y de Extensión
*   **Booleanos (`bool`):** Solo pueden ser `True` o `False`. Internamente son una subclase de los enteros, donde `True` equivale a 1 y `False` a 0,.
*   **`None`:** Un objeto especial que representa la ausencia de valor o "nada" (similar a `null` en otros lenguajes).
*   **`Decimal` (módulo `decimal`):** Ofrece punto flotante de precisión ajustable para evitar los errores de redondeo de los `float` binarios. Es ideal para aplicaciones financieras, aunque es más lento computacionalmente.
*   **`Fraction` (módulo `fractions`):** Permite trabajar con números racionales (numerador y denominador) para mantener la exactitud matemática total.

## Fecha y hora
Manejo de fechas y horas en Python

Python ofrece el módulo **datetime** para trabajar con fechas y horas.

```python showLineNumbers
from datetime import datetime, date, time, timedelta
import pytz

# Ejemplo 1: Obtener la fecha y hora actual
ahora = datetime.now()
print(f"Fecha: {ahora}")
print("Ejemplo 1 - Fecha y hora actual:", ahora)

# Ejemplo 2: Crear un objeto fecha
fecha_simple = date(2024, 6, 1)
print("Ejemplo 2 - Fecha simple:", fecha_simple)

# Ejemplo 3: Crear un objeto hora
hora_simple = time(14, 30, 0)
print("Ejemplo 3 - Hora simple:", hora_simple)

# Ejemplo 4: Formatear fechas a string
formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")
print("Ejemplo 4 - Fecha formateada:", formateada)

# Ejemplo 5: Parsear string a fecha
fecha_str = "2024-06-01 15:45:00"
fecha_parseada = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
print("Ejemplo 5 - Fecha parseada:", fecha_parseada)

# Ejemplo 6: Sumar y restar días con timedelta
manana = ahora + timedelta(days=1)
ayer = ahora - timedelta(days=1)
print("Ejemplo 6 - Mañana:", manana)
print("Ejemplo 6 - Ayer:", ayer)

# Ejemplo 7: Diferencia entre dos fechas
fecha1 = datetime(2024, 6, 1)
fecha2 = datetime(2024, 6, 10)
diferencia = fecha2 - fecha1
print("Ejemplo 7 - Diferencia de días:", diferencia.days)

# Ejemplo 8: Obtener solo la fecha o la hora de un datetime
solo_fecha = ahora.date()
solo_hora = ahora.time()
print("Ejemplo 8 - Solo fecha:", solo_fecha)
print("Ejemplo 8 - Solo hora:", solo_hora)

# Ejemplo 9: Trabajar con zonas horarias (requiere módulo pytz)
zona = pytz.timezone("America/Mexico_City")
zona_stgo = pytz.timezone("America/Santiago")
ahora_mx = datetime.now(zona)
ahora_stgo = datetime.now(zona_stgo)
print("Ejemplo 9 - Fecha y hora en CDMX:", ahora_mx)
print("Ejemplo 9 - Fecha y hora en Santiago:", ahora_stgo)

# Ejemplo 10: Comparar fechas
if fecha1 < fecha2:
    print(f"Ejemplo 10 - {fecha1.date()} es anterior a {fecha2.date()}")
else:
    print(f"Ejemplo 10 - {fecha1.date()} es posterior o igual a {fecha2.date()}")
```

### Resumen de Límites
| Tipo | Límite Principal | Notas |
| :--- | :--- | :--- |
| **`int`** | Memoria del sistema | Precisión arbitraria e ilimitada en Python 3,. |
| **`float`** | IEEE 754 (64 bits) | Inexactitud inherente por representación binaria,. |
| **`str`** | Memoria del sistema | Inmutables; cualquier cambio crea un objeto nuevo,. |
| **`list`/`dict`**| Memoria del sistema | Mutables; el ID del objeto persiste tras modificaciones,. |
| **`complex`** | Basado en `float` | No soportan comparaciones de orden (ej. `<` o `>`). |

**Ejemplos de código:**
```python
print('--- Python Data Types Example ---')

# 1. Numeric Types: int, float, complex
# Integer
int_var = 10
print(f"Integer: {int_var}, Type: {type(int_var)}")
```


```python
# Float
float_var = 10.5
print(f"Float: {float_var}, Type: {type(float_var)}")
```


```python
# Complejo (opcional, menos comun para iniciados)
complex_var = 1 + 2j
print(f"Complex: {complex_var}, Type: {type(complex_var)}")

print('\n')
```
```python
# 2. Boolean Type: bool
bool_true = True
bool_false = False
print(f"Boolean True: {bool_true}, Type: {type(bool_true)}")
print(f"Boolean False: {bool_false}, Type: {type(bool_false)}")

print('\n')
```

```python
# 3. Tipos de secuencia: str, list, tuple
# String
str_var = "Hello Python!"
print(f"String: '{str_var}', Type: {type(str_var)}")
```
```python
# List (mutable ordenada secuencia)
list_var = [1, 2, 'three', 4.0]
print(f"List: {list_var}, Type: {type(list_var)}")
```

```python
# Tuple (immutable ordenda secuencia)
tuple_var = (10, 20, 'thirty')
print(f"Tuple: {tuple_var}, Type: {type(tuple_var)}")

print('\n')
```
```python
# 4. Set Type: set (coleccion desordenada de itemes únicos)
set_var = {1, 2, 3, 2, 1}
print(f"Set: {set_var}, Type: {type(set_var)}")

print('\n')
```
```python
# 5. Mapping Type: dict (coleccion desordenada de pares clave-valor)
dict_var = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(f"Dictionary: {dict_var}, Type: {type(dict_var)}")
```

**diferencia principal entre una lista y un conjunto**

La principal diferencia entre una lista y un conjunto en Python se centra en dos aspectos clave:

**Orden:**

- Una lista es una colección ordenada de elementos. Esto significa que los elementos tienen una posición definida y mantienen el orden en que fueron insertados. Puedes acceder a los elementos por su índice (por ejemplo, mi_lista[0]).
- Un conjunto es una colección no ordenada de elementos. Los elementos no tienen una posición definida y su orden puede variar. No puedes acceder a los elementos de un conjunto por un índice.

**Elementos duplicados:**

- Una lista permite elementos duplicados. Puedes tener el mismo valor múltiples veces en una lista (por ejemplo, [1, 2, 2, 3]).
- Un conjunto no permite elementos duplicados. Solo almacena elementos únicos. Si intentas agregar un elemento que ya existe, el conjunto simplemente lo ignora (como se vio en el ejemplo anterior, set_var = {1, 2, 3, 2, 1} resultó en {1, 2, 3}).

Además, tanto las listas como los conjuntos son mutables, lo que significa que puedes añadir o eliminar elementos después de su creación.

### Matrices

Las **matrices** en Python suelen representarse como listas de listas, ya que Python no tiene un tipo de dato específico para matrices en su núcleo. Sin embargo, existen librerías como `numpy` que facilitan el trabajo con matrices.

```python showLineNumbers
import numpy as np

# Ejemplo 1: Crear una matriz 2x2 como lista de listas
matriz_1 = [[1, 2], [3, 4]]
print("Ejemplo 1:", matriz_1)

# Ejemplo 2: Acceder a un elemento específico (fila 1, columna 2)
print("Ejemplo 2:", matriz_1[0][1])  # Salida: 2

# Ejemplo 3: Recorrer una matriz e imprimir sus elementos
print("Ejemplo 3:")
for fila in matriz_1:
    for elemento in fila:
        print(elemento, end=' ')
    print()

# Ejemplo 4: Crear una matriz 3x3 con ceros
matriz_2 = [[0 for _ in range(3)] for _ in range(3)]
print("Ejemplo 4:", matriz_2)

# Ejemplo 5: Sumar dos matrices 2x2
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
suma = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
print("Ejemplo 5:", suma)

# Ejemplo 6: Transponer una matriz 3x2
matriz_3 = [[1, 2], [3, 4], [5, 6]]
transpuesta = [[fila[i] for fila in matriz_3] for i in range(len(matriz_3[0]))]
print("Ejemplo 6:", transpuesta)

# Ejemplo 7: Multiplicar una matriz 2x3 por una 3x2
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]
producto = [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(2)] for i in range(2)]
print("Ejemplo 7:", producto)

# Ejemplo 8: Encontrar el valor máximo de una matriz
matriz_4 = [[3, 8, 1], [4, 6, 9], [7, 2, 5]]
maximo = max(max(fila) for fila in matriz_4)
print("Ejemplo 8:", maximo)

# Ejemplo 9: Usar numpy para crear una matriz identidad 4x4
identidad = np.eye(4)
print("Ejemplo 9:\n", identidad)

# Ejemplo 10: Calcular el determinante de una matriz 3x3 usando numpy
matriz_5 = np.array([[2, 1, 3], [1, 0, 2], [4, 1, 8]])
det = np.linalg.det(matriz_5)
print("Ejemplo 10:", det)
```

### Diccionarios
Un diccionario en Python es una estructura de datos que almacena pares de clave-valor

Permite acceder, modificar y eliminar valores asociados a una clave única.

```python showLineNumbers
# Crear un diccionario simple y acceder a un valor
persona = {"nombre": "Carlos", "edad": 32, "ciudad": "Madrid"}
print("Ejemplo 1:", persona["nombre"])  # Salida: Carlos

# Agregar y modificar elementos en un diccionario
persona["profesion"] = "Ingeniero"
persona["edad"] = 33
print("Ejemplo 2:", persona)

# Recorrer un diccionario e imprimir sus claves y valores
for clave, valor in persona.items():
    print(f"Ejemplo 3: {clave} -> {valor}")
```
```text
Resultado:
Ejemplo 1: Carlos
Ejemplo 2: {'nombre': 'Carlos', 'edad': 33, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}
Ejemplo 3: nombre -> Carlos
Ejemplo 3: edad -> 33
Ejemplo 3: ciudad -> Madrid
Ejemplo 3: profesion -> Ingeniero
```

```python
# Ejemplo 1: Crear un diccionario y acceder a valores
dic = {"a": 1, "b": 2, "c": 3}
print("Ejemplo 1:", dic["a"])  # Salida: 1

# Ejemplo 2: Agregar y modificar elementos
dic["d"] = 4
dic["a"] = 10
print("Ejemplo 2:", dic)

# Ejemplo 3: Métodos de diccionarios
print("Ejemplo 3 - keys():", list(dic.keys()))
print("Ejemplo 3 - values():", list(dic.values()))
print("Ejemplo 3 - items():", list(dic.items()))
print("Ejemplo 3 - get():", dic.get("b"))
print("Ejemplo 3 - pop():", dic.pop("c"))
print("Ejemplo 3 - after pop:", dic)

# Ejemplo 4: Iteración de un diccionario
for clave in dic:
    print("Ejemplo 4 - clave:", clave, "valor:", dic[clave])

for clave, valor in dic.items():
    print("Ejemplo 4 - clave:", clave, "valor:", valor)

# Ejemplo 5: Comprobación de claves
if "b" in dic:
    print("Ejemplo 5: 'b' está en el diccionario")

# Ejemplo 6: Diccionario por comprensión (complejo)
cuadrados = {x: x**2 for x in range(5)}
print("Ejemplo 6:", cuadrados)

# Ejemplo 7: Diccionarios anidados
alumnos = {
    "Ana": {"edad": 20, "nota": 9.5},
    "Luis": {"edad": 22, "nota": 8.7}
}
for nombre, datos in alumnos.items():
    print(f"Ejemplo 7: {nombre} -> Edad: {datos['edad']}, Nota: {datos['nota']}")
```
```
Resultado:
Ejemplo 1: 1
Ejemplo 2: {'a': 10, 'b': 2, 'c': 3, 'd': 4}
Ejemplo 3 - keys(): ['a', 'b', 'c', 'd']
Ejemplo 3 - values(): [10, 2, 3, 4]
Ejemplo 3 - items(): [('a', 10), ('b', 2), ('c', 3), ('d', 4)]
Ejemplo 3 - get(): 2
Ejemplo 3 - pop(): 3
Ejemplo 3 - after pop: {'a': 10, 'b': 2, 'd': 4}
Ejemplo 4 - clave: a valor: 10
Ejemplo 4 - clave: b valor: 2
Ejemplo 4 - clave: d valor: 4
Ejemplo 4 - clave: a valor: 10
Ejemplo 4 - clave: b valor: 2
Ejemplo 4 - clave: d valor: 4
Ejemplo 5: 'b' está en el diccionario
Ejemplo 6: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
Ejemplo 7: Ana -> Edad: 20, Nota: 9.5
Ejemplo 7: Luis -> Edad: 22, Nota: 8.7
```

## Limitaciones de Float en cálculos científicos
El tipo `float` en Python, que sigue el estándar **IEEE 754 de doble precisión** (64 bits), presenta limitaciones fundamentales para el cálculo científico debido a su naturaleza binaria y finita. Estas limitaciones pueden comprometer la exactitud de los resultados si no se manejan con precaución.

A continuación se detallan las principales limitaciones:

#### 1. Imprecisión en la representación
La limitación más crítica es que los ordenadores representan los números reales mediante una secuencia finita de bits (normalmente 53 bits para la mantisa), lo que obliga a truncar o aproximar la mayoría de los números.
*   **Fracciones decimales inexactas:** Muchos números que parecen simples en sistema decimal, como **0.1 o 0.3**, no tienen una representación binaria exacta y se almacenan como aproximaciones.
*   **Dígitos significativos:** Generalmente, un `float` solo puede mantener entre **15 y 17 dígitos decimales** de precisión.

#### 2. Errores de redondeo y su propagación
Los errores microscópicos de representación se acumulan y aumentan a medida que se realizan más cálculos, lo que se conoce como **errores de redondeo** (*round-off errors*).
*   **Falla de reglas algebraicas:** Debido a estos errores, reglas matemáticas estándar como la asociatividad o la transitividad no siempre se cumplen en la computación de punto flotante. Por ejemplo, sumar un número muy pequeño a uno muy grande puede no cambiar el valor del grande porque el pequeño cae fuera del rango de precisión de la mantisa.
*   **Operaciones inversas:** Realizar una serie de operaciones y luego sus inversas (como aplicar la raíz cuadrada y luego elevar al cuadrado repetidamente) puede no devolver el valor original debido a la pérdida de precisión en cada paso.

#### 3. Problemas en comparaciones
Nunca se deben comparar dos objetos `float` directamente usando los operadores de igualdad (`==` o `!=`).
*   **Falsos negativos:** Dos valores que son matemáticamente idénticos pueden tener representaciones binarias ligeramente distintas tras una serie de cálculos.
*   **Solución:** Se recomienda verificar si la diferencia absoluta entre los números es menor que una tolerancia pequeña denominada **épsilon de la máquina**.

#### 4. Inestabilidad en algoritmos específicos
Ciertos cálculos científicos son particularmente sensibles a las limitaciones del tipo `float`:
*   **Cancelación catastrófica:** Restar dos números que son casi iguales produce un resultado con muy pocos dígitos significativos correctos. Si este resultado se usa luego como denominador (como en la diferenciación numérica), el error puede amplificarse masivamente y destruir la precisión del cálculo.
*   **Búsqueda de raíces:** En algoritmos como el de bisección o Newton, si la función es muy "plana" cerca de la raíz, los errores de redondeo pueden hacer que el algoritmo devuelva signos incorrectos o diverja.

#### 5. Límites de magnitud (Desbordamiento)
El formato tiene un rango finito, aproximadamente entre $\pm 2.22 \times 10^{-308}$ y $\pm 1.79 \times 10^{308}$.
*   **Overflow:** Intentar representar un número mayor al máximo resulta en un error de desbordamiento o en el valor especial `inf` (infinito).
*   **Underflow:** Los números más pequeños que el límite mínimo suelen redondearse automáticamente a cero, lo que puede causar pérdidas de información críticas en ciertos modelos físicos.

### Alternativas para mayor precisión
Cuando estas limitaciones son inaceptables (como en aplicaciones financieras o investigación de alta precisión), las fuentes sugieren:
*   **Módulo `decimal`:** Permite trabajar con aritmética decimal y precisión ajustable.
*   **Módulo `fractions`:** Para cálculos exactos con números racionales.
*   **NumPy:** Ofrece tipos específicos como `float128` (precisión extendida) para mejorar la resolución en cálculos masivos.
*   **SymPy:** Permite realizar cálculos de forma **simbólica y exacta**, evitando totalmente el uso de aproximaciones numéricas hasta el final del proceso.

## Errores de redondeo con decimales

Para evitar los errores de redondeo en Python, que surgen porque el tipo estándar `float` no puede representar exactamente muchas fracciones decimales debido a su naturaleza binaria (estándar IEEE 754), se deben emplear estrategias y módulos específicos diseñados para la alta precisión.

A continuación se detallan las principales formas de mitigar estos errores según las fuentes:

#### 1. Uso del módulo `decimal`
La herramienta principal para obtener precisión exacta es el módulo **`decimal`**, que permite trabajar con aritmética decimal de precisión ajustable. 
*   **Inicialización con cadenas:** Para evitar heredar la imprecisión inherente de los `float`, es fundamental crear objetos `Decimal` a partir de **cadenas de texto** (por ejemplo, `Decimal('0.1')`) o enteros, en lugar de pasar un número de punto flotante directamente.
*   **Control del contexto:** Es posible configurar la precisión (número de dígitos significativos) y las reglas de redondeo accediendo al contexto global mediante `decimal.getcontext().prec` o utilizando un contexto local con la sentencia `with localcontext()`.
*   **Aplicaciones financieras:** Este módulo es el estándar recomendado para el manejo de dinero y transacciones comerciales donde la exactitud es crítica.

#### 2. Uso del módulo `fractions`
Cuando el problema requiere mantener la exactitud matemática total en operaciones con números racionales, se puede utilizar el módulo **`fractions`**. Este módulo almacena los números como un par de numerador y denominador, permitiendo realizar sumas y multiplicaciones sin ninguna pérdida de precisión por redondeo.

#### 3. Comparaciones seguras (Estrategia del Épsilon)
En cálculos científicos donde se deben usar `float` por motivos de rendimiento, **nunca se debe comparar la igualdad directamente con `==`**.
*   La técnica correcta consiste en verificar si la diferencia absoluta entre dos valores es menor que una tolerancia muy pequeña denominada **épsilon de la máquina** o *machine epsilon*.
*   En entornos de prueba como `pytest`, se puede utilizar la función `pytest.approx()` para realizar estas comparaciones de forma simplificada.

#### 4. Herramientas para cálculo científico avanzado
*   **NumPy y precisión extendida:** En computación intensiva, NumPy ofrece tipos de datos de mayor resolución como `float128` o `float96`, que minimizan (aunque no eliminan) los errores de redondeo en comparación con el `float64` estándar.
*   **SymPy para matemática simbólica:** Si se requiere una solución analítica perfecta, **SymPy** permite realizar cálculos de forma **simbólica**, manteniendo las variables y constantes (como $\pi$ o $\sqrt{2}$) sin convertirlas a números decimales hasta el final del proceso, evitando así cualquier error numérico acumulativo.

#### 5. Técnicas de programación defensiva
Al implementar algoritmos numéricos, es preferible utilizar **fórmulas optimizadas** y bibliotecas probadas como SciPy, ya que sus rutinas están diseñadas para minimizar la inestabilidad numérica y la cancelación catastrófica (error que ocurre al restar números casi iguales). También es útil reescalar el problema para que las variables tengan magnitudes similares, lo que reduce el error relativo durante las operaciones de suma y resta.