---
id: dunder
title: "Métodos Dunder"
sidebar_label: "📄 Métodos Dunder"
description: "Métodos Dunder"
---



Los **métodos dunder** (término derivado de *double underscore* o doble guion bajo) son funciones especiales en Python cuyos nombres comienzan y terminan con `__`. También son conocidos como **métodos mágicos** o **métodos especiales**.

Estos métodos constituyen un **protocolo** que determina cómo responde el lenguaje Python ante ciertas operaciones sintácticas o funciones integradas. En lugar de llamarlos directamente de forma habitual, Python los invoca "tras bambalinas" cuando se utiliza un operador o una función específica.

### Características principales
*   **Integración con la sintaxis nativa:** Permiten que los objetos creados por el usuario se comporten como tipos de datos integrados (como listas o números).
*   **Sobrecarga de operadores:** Gracias a ellos, es posible definir el comportamiento de operadores como `+`, `-`, `*` o `==` para clases personalizadas.
*   **Nomenclatura reservada:** La convención de los dos guiones bajos ayuda a evitar conflictos entre los nombres de métodos predeterminados de Python y los definidos por el programador.

### Ejemplos comunes y su funcionamiento
| Método | Acción que lo invoca | Propósito |
| :--- | :--- | :--- |
| `__init__` | `Objeto()` | **Constructor:** Inicializa una nueva instancia de la clase. |
| `__str__` | `print(objeto)` | Devuelve una representación en cadena legible para el usuario. |
| `__repr__` | `repr(objeto)` | Devuelve una representación detallada y "exacta" del objeto. |
| `__len__` | `len(objeto)` | Devuelve el tamaño o número de elementos de una estructura. |
| `__add__` | `objeto1 + objeto2` | Define el comportamiento de la suma (+) entre objetos. |
| `__getitem__` | `objeto[indice]` | Permite el acceso a elementos mediante índices o corchetes. |
| `__call__` | `objeto()` | Permite que una instancia se comporte y sea llamada como una función. |

### Recomendaciones de uso
**Nunca se deben inventar nombres propios** que sigan esta convención de doble guion bajo (como `__mi_metodo__`). Estos nombres están reservados para el núcleo de Python, y crear uno nuevo podría causar errores si en versiones futuras del lenguaje se introduce un método oficial con ese mismo nombre.


A continuación se detallan los más utilizados:

### 1. Inicialización y Construcción
*   **`__init__(self, ...)`**: Es el método más común, conocido como inicializador o constructor. Se ejecuta automáticamente al crear una nueva instancia de la clase para establecer el estado inicial de sus atributos.
*   **`__new__(cls, ...)`**: Se encarga de construir y devolver la instancia del objeto antes de que se llame a `__init__`. Se utiliza principalmente en casos avanzados como la creación de *singletons* o metaclases.

### 2. Representación de Objetos

El método **`def __str__(self)`** es un método especial (o *dunder method*) en Python que define la **representación en texto legible e informal** de una instancia de clase.

*   **`__str__(self)`**: Devuelve una cadena de texto amigable orientado al **usuario final**. Se invoca al usar `print(objeto)` o la función `str()`. Prima la legibilidad y la presentación informal.

*   **`__repr__(self)`**: Genera una representación técnica y detallada del objeto. La convención establece que debe ser una cadena que, evaluada con `eval()`, sea capaz de recrear el objeto original. Orientado al **desarrollador y depuración**. Busca dar una representación formal e inequívoca de la estructura interna del objeto (idealmente una expresión que permita recrearlo).

### `__str__`

#### ¿Para qué sirve y cuándo se invoca?

Su propósito es transformar el estado interno de un objeto en una cadena de texto clara y comprensible para las personas. Python llama automáticamente a `__str__(self)` en las siguientes situaciones:

* Al imprimir un objeto directamente con **`print(objeto)`**.
* Al realizar una conversión explícita mediante **`str(objeto)`**.
* Al interpolar el objeto en cadenas usando **f-strings** (`f"{objeto}"`), el método `.format()` o especificadores como `%s`.

Si una clase **no** define `__str__`, Python muestra por defecto el nombre de la clase y la dirección de memoria donde está almacenada (por ejemplo: `<__main__.Persona object at 0x7f8a...>`).


#### Ejemplo

**Sin implementar `__str__`:**
```python showLineNumbers
class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

est = Estudiante("Ana", "Ingeniería")
print(est)  # Muestra la dirección de memoria: <__main__.Estudiante object at 0x7f9a...>
```

**Con `__str__` implementado:**
```python showLineNumbers
class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def __str__(self) -> str:
        return f"Estudiante: {self.nombre} | Carrera: {self.carrera}"

est = Estudiante("Ana", "Ingeniería")
print(est)  # Muestra: Estudiante: Ana | Carrera: Ingeniería
```


:::info[**Nota:**] 
Si una clase define únicamente `__repr__`, Python lo utilizará también como alternativa para `print()` y `str()` cuando `__str__` esté ausente.
:::

---
### `__repr__`

El método especial **`__repr__(self)`** está diseñado específicamente para los desarrolladores y el proceso de **depuración (*debugging*)**. Mientras que `__str__` busca presentar una salida amigable e informal para el usuario final, `__repr__` tiene como objetivo proporcionar una **representación formal, transparente e inequívoca del estado interno del objeto**.

Por convención, el valor devuelto por `__repr__` debería parecerse al código en Python necesario para reconstruir el objeto (cumpliendo idealmente la regla `eval(repr(obj)) == obj`) o seguir la estructura `NombreClase(atributo1=valor1, atributo2=valor2)`.


#### Donde `__repr__` Facilita la Depuración

1. **Inspección en consolas interactivas y depuradores (`pdb` / REPL)**:
   Al ejecutar un script en la terminal, evaluar código interactivamente o pausar la ejecución con depuradores como `pdb` o `ipdb`, escribir el nombre de la variable invoca automáticamente a `__repr__`.
   * **Sin `__repr__`:** `<__main__.Producto object at 0x7f8a...>` (no revela el estado interno).
   * **Con `__repr__`:** `Producto(nombre='Monitor 4K', precio=350.0)`.

2. **Visualización dentro de contenedores (Listas, Diccionarios y Tuplas)**:
   Al imprimir una colección de objetos (por ejemplo, `print([prod1, prod2])`), Python **siempre llama a `__repr__`** para representar cada elemento dentro del contenedor, ignorando el método `__str__`.

3. **F-Strings autodocumentadas con `=` y `!r`**:
   Desde Python 3.8, las f-strings admiten la sintaxis de depuración con el signo `=`, la cual imprime la expresión y evalúa su `__repr__` de forma automática:
   ```python showLineNumbers
   producto = Producto("Monitor 4K", 350.0)

   # Imprime la variable y su representación repr()
   print(f"{producto=}")   # Salida: producto=Producto(nombre='Monitor 4K', precio=350.0)

   # Fuerza explícitamente el uso de __repr__ en lugar de __str__
   print(f"{producto!r}")  # Salida: Producto(nombre='Monitor 4K', precio=350.0)
   ```


#### Ejemplo

```python showLineNumbers
class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    # Representación formal para logs y debugging
    def __repr__(self) -> str:
        # Usa !r para asegurar que el string lleve comillas en la representación
        return f"Producto(nombre={self.nombre!r}, precio={self.precio})"

p1 = Producto("Monitor 4K", 350.0)
p2 = Producto("Teclado Mecánico", 80.0)

# 1. Depuración rápida en logs
print(f"{p1=}")  
# Salida: p1=Producto(nombre='Monitor 4K', precio=350.0)

# 2. Impresión dentro de colecciones
inventario = [p1, p2]
print(inventario)  
# Salida: [Producto(nombre='Monitor 4K', precio=350.0), Producto(nombre='Teclado Mecánico', precio=80.0)]
```

La regla de oro en Python para decidir entre ambos métodos es: **`__repr__` está pensado para desarrolladores**, mientras que **`__str__` está pensado para el usuario final**.



### ¿Cuándo usar `__repr__` en lugar de `__str__`?

Debes implementar o preferir **`__repr__`** en los siguientes escenarios principales:

#### 1. Si solo vas a implementar un único método de representación (Regla de respaldo)
Si solo quieres escribir un método de texto en tu clase, **escribe `__repr__`**. 
* Python utiliza `__repr__` como **mecanismo de reserva (*fallback*)** cuando se invoca `print()` o `str()` y `__str__` no está definido.

* De manera inversa no funciona: si solo defines `__str__`, las consolas interactivas y las colecciones seguirán mostrando la dirección de memoria por defecto (`<__main__.Objeto at 0x...>`).

#### 2. Cuando inspeccionas objetos dentro de colecciones (Listas, Tuplas, Diccionarios)
Cuando imprimes una lista o contenedor que guarda tus objetos (por ejemplo, `print([obj1, obj2])`), Python **siempre invoca el `__repr__`** de cada elemento interno, ignorando por completo `__str__`.

#### 3. Para tareas de depuración (*debugging*) y generación de *logs*
`__repr__` debe mostrar el estado exacto e inequívoco del objeto (incluyendo diferencias entre cadenas y números, comillas, etc.). Idealmente, su salida debería seguir el formato de código ejecutable que permita recrear el objeto con la función `eval()`.

#### 4. Para inspección en consolas interactivas (REPL, IPython, Jupyter)
Al escribir el nombre de una variable en la terminal o celda interactiva sin usar `print()`, el entorno invoca automáticamente a `__repr__` para mostrar el resultado.



#### Resumen Comparativo

| Criterio | `__repr__(self)` | `__str__(self)` |
| :--- | :--- | :--- |
| **Audiencia** | Desarrollador / Depuración. | Usuario final / Interfaz. |
| **Objetivo** | Inequívoco, técnico y detallado. | Legible, amigable y simplificado. |
| **Formato ideal** | Estructura ejecutable: `Clase(attr=valor)`. | Texto libre para visualización ("pretty print"). |
| **Cuándo se llama** | `repr(obj)`, consola interactiva, objetos dentro de listas/diccionarios. | `print(obj)`, `str(obj)`, f-strings simples. |



#### Ejemplo Ilustrativo

```python
class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    # Representación técnica para desarrolladores
    def __repr__(self):
        return f"Producto(nombre={self.nombre!r}, precio={self.precio})"

    # Representación amigable para usuarios
    def __str__(self):
        return f"{self.nombre} (${self.precio:.2f})"

p = Producto("Laptop", 1200.0)

# Uso de __str__ (usuario final)
print(p)         # Salida: Laptop ($1200.00)

# Uso de __repr__ (dentro de listas o depuración)
print([p])       # Salida: [Producto(nombre='Laptop', precio=1200.0)]
print(f"{p!r}")  # Salida: Producto(nombre='Laptop', precio=1200.0)
```


---
### 3. Operadores Aritméticos y de Comparación
Permiten la **sobrecarga de operadores**, logrando que los objetos respondan a símbolos matemáticos estándar.
*   **Aritmética**: 
`__add__` , `__sub__` , `__mul__` , `__truediv__` , `__pow__`
*   **Comparación**: 
`__eq__` , `__ne__` , `__lt__` , `__gt__`, `__le__`, `__ge__`

### 4. Colecciones, Secuencias e Iteración
*   **`__len__(self)`**: Es llamado por la función `len()` para devolver el número de elementos que contiene un objeto.
*   **`__getitem__(self, key)`**: Permite el acceso mediante índices o claves, como en `objeto[i]`.
*   **`__setitem__(self, key, value)`**: Permite asignar valores a una posición específica, como en `objeto[i] = valor`.
*   **`__iter__(self)`**: Devuelve un objeto iterador, permitiendo que la instancia se use en bucles `for`.
*   **`__contains__(self, item)`**: Implementa el operador de membresía `in`.

### 5. Contexto y Otros Propósitos
*   **`__call__(self, ...)`**: Permite que una instancia de clase se comporte como una función y pueda ser llamada mediante paréntesis: `objeto()`.
*   **`__enter__` y `__exit__`**: Son los pilares de los **administradores de contexto** y se ejecutan al entrar y salir de un bloque `with`.
*   **`__hash__(self)`**: Devuelve un número entero que identifica al objeto, necesario para que una instancia pueda usarse como clave en un diccionario.
*   **`__del__(self)`**: Conocido como el destructor, se llama cuando el objeto está a punto de ser eliminado de la memoria para realizar tareas de limpieza.

### método dunder personalizado

Para definir un método **dunder** personalizado (término derivado de *double underscore* o doble guion bajo) en Python, se debe crear una función dentro de una clase utilizando uno de los nombres reservados por el lenguaje que comienzan y terminan con `__`. Estos métodos, también conocidos como **métodos especiales** o **mágicos**, permiten que tus objetos se integren con la sintaxis nativa de Python, como el uso de operadores o funciones integradas.

A continuación se detallan los pasos y reglas fundamentales para su definición:

### 1. Definición dentro de una clase
Un método dunder debe definirse obligatoriamente dentro del bloque de una **clase** para que tenga efecto sobre las instancias de esa clase. Por ejemplo, para personalizar la representación en texto de un objeto, se define el método `__str__`.

### 2. El parámetro `self`
Como cualquier método de instancia, el primer argumento de la definición debe ser **`self`**. Este parámetro representa a la instancia específica que está llamando al método y permite acceder a sus atributos internos.

### 3. Sintaxis básica
La estructura sigue el formato de una función estándar de Python:
```python
class MiClase:
    def __nombre_especial__(self, otros_parametros):
        # Lógica del método
        return resultado
```
*   **Ejemplo de inicialización (`__init__`):** Se usa para establecer el estado inicial de un objeto al ser creado.
*   **Ejemplo de acceso por índice (`__getitem__`):** Permite que un objeto use corchetes como una lista: `objeto[idx]`.
*   **Ejemplo de operadores (`__add__`):** Permite definir qué sucede cuando se usa el signo `+` entre dos objetos de tu clase.

### 4. Sobrecarga y Protocolos
Definir estos métodos es, en esencia, **sobrescribir** comportamientos predeterminados. Python utiliza estos métodos para implementar "protocolos"; por ejemplo, si tu clase define `__len__`, Python la reconoce como una colección que puede ser medida con la función `len()`.

