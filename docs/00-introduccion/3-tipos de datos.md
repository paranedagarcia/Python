---
id: datos
title: "Datos y estructuras"
sidebar_label: "Datos y estructuras"
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
*   **`Fraction` (módulo `fractions`):** Permite trabajar con números racionales (numerador y denominador) para mantener la exactitud matemática total,
.

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


## Limitaciones de Float en cálculos científicos
El tipo `float` en Python, que sigue el estándar **IEEE 754 de doble precisión** (64 bits), presenta limitaciones fundamentales para el cálculo científico debido a su naturaleza binaria y finita. Estas limitaciones pueden comprometer la exactitud de los resultados si no se manejan con precaución.

A continuación se detallan las principales limitaciones:

### 1. Imprecisión en la representación
La limitación más crítica es que los ordenadores representan los números reales mediante una secuencia finita de bits (normalmente 53 bits para la mantisa), lo que obliga a truncar o aproximar la mayoría de los números.
*   **Fracciones decimales inexactas:** Muchos números que parecen simples en sistema decimal, como **0.1 o 0.3**, no tienen una representación binaria exacta y se almacenan como aproximaciones.
*   **Dígitos significativos:** Generalmente, un `float` solo puede mantener entre **15 y 17 dígitos decimales** de precisión.

### 2. Errores de redondeo y su propagación
Los errores microscópicos de representación se acumulan y aumentan a medida que se realizan más cálculos, lo que se conoce como **errores de redondeo** (*round-off errors*).
*   **Falla de reglas algebraicas:** Debido a estos errores, reglas matemáticas estándar como la asociatividad o la transitividad no siempre se cumplen en la computación de punto flotante. Por ejemplo, sumar un número muy pequeño a uno muy grande puede no cambiar el valor del grande porque el pequeño cae fuera del rango de precisión de la mantisa.
*   **Operaciones inversas:** Realizar una serie de operaciones y luego sus inversas (como aplicar la raíz cuadrada y luego elevar al cuadrado repetidamente) puede no devolver el valor original debido a la pérdida de precisión en cada paso.

### 3. Problemas en comparaciones
Nunca se deben comparar dos objetos `float` directamente usando los operadores de igualdad (`==` o `!=`).
*   **Falsos negativos:** Dos valores que son matemáticamente idénticos pueden tener representaciones binarias ligeramente distintas tras una serie de cálculos.
*   **Solución:** Se recomienda verificar si la diferencia absoluta entre los números es menor que una tolerancia pequeña denominada **épsilon de la máquina**.

### 4. Inestabilidad en algoritmos específicos
Ciertos cálculos científicos son particularmente sensibles a las limitaciones del tipo `float`:
*   **Cancelación catastrófica:** Restar dos números que son casi iguales produce un resultado con muy pocos dígitos significativos correctos. Si este resultado se usa luego como denominador (como en la diferenciación numérica), el error puede amplificarse masivamente y destruir la precisión del cálculo.
*   **Búsqueda de raíces:** En algoritmos como el de bisección o Newton, si la función es muy "plana" cerca de la raíz, los errores de redondeo pueden hacer que el algoritmo devuelva signos incorrectos o diverja.

### 5. Límites de magnitud (Desbordamiento)
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

### 1. Uso del módulo `decimal`
La herramienta principal para obtener precisión exacta es el módulo **`decimal`**, que permite trabajar con aritmética decimal de precisión ajustable. 
*   **Inicialización con cadenas:** Para evitar heredar la imprecisión inherente de los `float`, es fundamental crear objetos `Decimal` a partir de **cadenas de texto** (por ejemplo, `Decimal('0.1')`) o enteros, en lugar de pasar un número de punto flotante directamente.
*   **Control del contexto:** Es posible configurar la precisión (número de dígitos significativos) y las reglas de redondeo accediendo al contexto global mediante `decimal.getcontext().prec` o utilizando un contexto local con la sentencia `with localcontext()`.
*   **Aplicaciones financieras:** Este módulo es el estándar recomendado para el manejo de dinero y transacciones comerciales donde la exactitud es crítica.

### 2. Uso del módulo `fractions`
Cuando el problema requiere mantener la exactitud matemática total en operaciones con números racionales, se puede utilizar el módulo **`fractions`**. Este módulo almacena los números como un par de numerador y denominador, permitiendo realizar sumas y multiplicaciones sin ninguna pérdida de precisión por redondeo.

### 3. Comparaciones seguras (Estrategia del Épsilon)
En cálculos científicos donde se deben usar `float` por motivos de rendimiento, **nunca se debe comparar la igualdad directamente con `==`**.
*   La técnica correcta consiste en verificar si la diferencia absoluta entre dos valores es menor que una tolerancia muy pequeña denominada **épsilon de la máquina** o *machine epsilon*.
*   En entornos de prueba como `pytest`, se puede utilizar la función `pytest.approx()` para realizar estas comparaciones de forma simplificada.

### 4. Herramientas para cálculo científico avanzado
*   **NumPy y precisión extendida:** En computación intensiva, NumPy ofrece tipos de datos de mayor resolución como `float128` o `float96`, que minimizan (aunque no eliminan) los errores de redondeo en comparación con el `float64` estándar.
*   **SymPy para matemática simbólica:** Si se requiere una solución analítica perfecta, **SymPy** permite realizar cálculos de forma **simbólica**, manteniendo las variables y constantes (como $\pi$ o $\sqrt{2}$) sin convertirlas a números decimales hasta el final del proceso, evitando así cualquier error numérico acumulativo.

### 5. Técnicas de programación defensiva
Al implementar algoritmos numéricos, es preferible utilizar **fórmulas optimizadas** y bibliotecas probadas como SciPy, ya que sus rutinas están diseñadas para minimizar la inestabilidad numérica y la cancelación catastrófica (error que ocurre al restar números casi iguales). También es útil reescalar el problema para que las variables tengan magnitudes similares, lo que reduce el error relativo durante las operaciones de suma y resta.