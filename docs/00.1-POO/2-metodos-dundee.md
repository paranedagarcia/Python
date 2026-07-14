---
id: dunder
title: "Métodos Dunder"
sidebar_label: "Métodos Dunder"
sidebar_position: 2
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
*   **`__str__(self)`**: Devuelve una cadena de texto amigable diseñada para el usuario final. Se invoca al usar `print(objeto)` o la función `str()`.
*   **`__repr__(self)`**: Genera una representación técnica y detallada del objeto. La convención establece que debe ser una cadena que, evaluada con `eval()`, sea capaz de recrear el objeto original.

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

