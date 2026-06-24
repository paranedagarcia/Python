---
id: funciones
title: "Funciones"
sidebar_label: "Funciones"
sidebar_position: 7
---



Las funciones son bloques de código reutilizables que realizan una tarea específica. Nos ayudan a organizar nuestro código, hacerlo más legible y evitar repetir código.

### Funciones Preconstruidas (Built-in) de Python

Python viene con muchas funciones ya listas para usar. Aquí te presento algunas de las más comunes y básicas.


```python
# Función: print()
# Uso: Muestra un mensaje o el valor de una variable en la consola.
# Parámetros: Puede recibir cero o más argumentos (valores a mostrar).

print("Hola, mundo!") # Sin variables, solo texto

nombre = "Ana"
print("Mi nombre es", nombre) # Con una variable

edad = 30
print("Tengo", edad, "años.") # Con múltiples variables y texto
```

---


```python
# Función: len()
# Uso: Devuelve la longitud (cantidad de elementos) de un objeto.
# Parámetros: Recibe un único argumento, que debe ser un objeto con longitud (como una cadena, lista o tupla).

cadena = "Python"
longitud_cadena = len(cadena)
print(f"La longitud de '{cadena}' es: {longitud_cadena}")

lista_numeros = [1, 2, 3, 4, 5]
longitud_lista = len(lista_numeros)
print(f"La longitud de la lista es: {longitud_lista}")
```

---


```python
# Función: type()
# Uso: Devuelve el tipo de un objeto.
# Parámetros: Recibe un único argumento (el objeto del que quieres saber el tipo).

numero_entero = 10
print(f"El tipo de {numero_entero} es: {type(numero_entero)}")

texto = "ejemplo"
print(f"El tipo de '{texto}' es: {type(texto)}")

es_verdad = True
print(f"El tipo de {es_verdad} es: {type(es_verdad)}")
```

---


```python
# Función: input()
# Uso: Permite al usuario introducir datos a través de la consola.
# Parámetros: Opcionalmente, recibe un mensaje (string) que se muestra al usuario antes de que introduzca el dato.

nombre_usuario = input("Por favor, introduce tu nombre: ")
print(f"¡Hola, {nombre_usuario}!")

edad_usuario = input("¿Cuántos años tienes? ") # input siempre devuelve una cadena (string)
print(f"Tienes {edad_usuario} años.")
```

### Funciones Personalizadas (Definidas por el Usuario)

Ahora, aprenderemos a crear nuestras propias funciones. Usamos la palabra clave `def` para definirlas.

#### A. Funciones Simples: Sin parámetros y/o sin valor de retorno


```python
# Función sin parámetros y sin valor de retorno
# Uso: Realiza una acción simple sin necesidad de información externa ni devolver un resultado específico.

def saludar():
    print("¡Hola desde mi primera función!")

# Llamar a la función para ejecutarla
saludar()
```

---


```python
# Función con un parámetro y sin valor de retorno
# Uso: Realiza una acción utilizando un valor que le pasamos.
# Parámetros: `nombre` es el parámetro que la función espera recibir.

def saludar_a_persona(nombre):
    print(f"¡Mucho gusto, {nombre}!")

# Llamar a la función, pasándole un argumento
saludar_a_persona("Carlos")
saludar_a_persona("Maria")
```

---


```python
# Función con un parámetro y con valor de retorno
# Uso: Calcula un resultado y lo 'devuelve' para que podamos usarlo fuera de la función.
# La palabra clave `return` se usa para devolver un valor.

def duplicar_numero(numero):
    resultado = numero * 2
    return resultado

# Llamar a la función y guardar el valor que devuelve
mi_numero = 7
numero_duplicado = duplicar_numero(mi_numero)
print(f"El doble de {mi_numero} es: {numero_duplicado}")

# También puedes usar el valor directamente
print(f"El doble de 15 es: {duplicar_numero(15)}")
```

#### B. Funciones Más Complejas: 
Múltiples parámetros y características avanzadas


```python
# Función con múltiples parámetros
# Uso: Requiere varios valores para realizar su tarea.
# Parámetros: `num1` y `num2` son los dos números que la función sumará.

def sumar_numeros(num1, num2):
    suma = num1 + num2
    return suma

resultado_suma = sumar_numeros(10, 5)
print(f"La suma de 10 y 5 es: {resultado_suma}")

resultado_otra_suma = sumar_numeros(-3, 8)
print(f"La suma de -3 y 8 es: {resultado_otra_suma}")
```

---


```python
# Función con parámetros por defecto
# Uso: Algunos parámetros pueden tener un valor predefinido. Si no se proporciona un valor al llamar la función, se usa el predeterminado.
# Parámetros: `mensaje` tiene un valor por defecto 'Hola'. `veces` tiene un valor por defecto 1.

def saludar_personalizado(mensaje="Hola", nombre="visitante", veces=1):
    for _ in range(veces):
        print(f"{mensaje}, {nombre}!")

# Usar solo parámetros obligatorios (si los hubiera, aquí todos tienen defecto)
saludar_personalizado() # -> Hola, visitante!

# Sobrescribir un parámetro por defecto
saludar_personalizado("Buenos días", "Elena") # -> Buenos días, Elena!

# Sobrescribir todos los parámetros
saludar_personalizado("Adiós", "Pedro", 3) # -> Adiós, Pedro! (3 veces)
```

---


```python
# Función con argumentos variables (*args y **kwargs)
# Uso: Cuando no sabes cuántos argumentos vas a pasar a la función.
# *args: Recopila un número variable de argumentos posicionales en una tupla.
# **kwargs: Recopila un número variable de argumentos con palabras clave en un diccionario.

def mostrar_argumentos(arg_fijo, *args, **kwargs):
    print(f"Argumento fijo: {arg_fijo}")
    print(f"Argumentos posicionales (*args): {args}")
    print(f"Argumentos con palabra clave (**kwargs): {kwargs}")

mostrar_argumentos("Primer argumento", 1, 2, 3, clave1="valor1", clave2=False)
print("\n---\n")
mostrar_argumentos("Solo fijo", "otro", nombre="Juan")
```

---


```python
# Función con Type Hints (Sugerencias de Tipo)
# Uso: Mejora la legibilidad del código y ayuda a herramientas de desarrollo a detectar errores antes de ejecutar el programa.
# Nota: Son solo sugerencias, Python no las "obliga" en tiempo de ejecución.

def multiplicar(a: int, b: int) -> int:
    """Multiplica dos números enteros y devuelve el resultado."""
    return a * b

resultado_mult = multiplicar(4, 5)
print(f"4 * 5 = {resultado_mult}")

# Puedes pasar tipos incorrectos, pero las herramientas de análisis de código te advertirían
# resultado_incorrecto = multiplicar("hola", 2) # Esto generaría un error de tipo en tiempo de ejecución
```

---

### Argumentos Posicionales vs. Argumentos por Nombre (Keyword Arguments)

Es fundamental entender cómo se pasan los valores a las funciones. En Python, hay dos formas principales:

#### Argumentos Posicionales

Son los argumentos que se pasan a una función basándose en su **posición** u orden. La función asigna los valores a los parámetros en el mismo orden en que se reciben.

**Características:**
*   El orden importa. Si cambias el orden, la función puede interpretar los valores de forma diferente o incluso generar un error.
*   Son la forma más común y sencilla de pasar argumentos.


```python
# Ejemplo de argumentos posicionales
def describir_persona(nombre, edad, ciudad):
    print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}.")

# Los valores se asignan por orden: 'Juan' a nombre, 30 a edad, 'Madrid' a ciudad
describir_persona("Juan", 30, "Madrid")

# Si cambiamos el orden, el significado cambia
describir_persona(30, "Juan", "Madrid") # ¡Esto no tiene sentido! Edad es 30, nombre es 'Juan'.
```

#### Argumentos por Nombre (Keyword Arguments)

Son argumentos que se pasan a una función identificándolos por el **nombre de su parámetro**, seguido de un signo igual (`=`) y el valor. Esto nos permite pasar los argumentos en cualquier orden.

**Características:**
*   El orden no importa, ya que cada valor está vinculado directamente a un nombre de parámetro específico.
*   Mejoran la legibilidad del código, especialmente cuando una función tiene muchos parámetros, ya que queda claro qué valor corresponde a cada parámetro.
*   Permiten omitir parámetros que tienen valores por defecto si no se quiere cambiar su valor predefinido.


```python
# Ejemplo de argumentos por nombre
def describir_coche(marca, modelo, año, color="rojo"):
    print(f"Este coche es un {marca} {modelo}, del año {año}, de color {color}.")

# Los argumentos se pasan por su nombre, el orden no importa
describir_coche(año=2020, marca="Toyota", modelo="Corolla") # color toma el valor por defecto 'rojo'
describir_coche(modelo="Focus", color="azul", marca="Ford", año=2022) # Orden diferente, mismo resultado

# Combinando ambos: los posicionales deben ir primero
describir_coche("BMW", "Serie 3", año=2023) # 'BMW' y 'Serie 3' son posicionales, 'año' es por nombre.

# Esto sería un error: un argumento por nombre antes de un posicional
# describir_coche(año=2023, "BMW", "Serie 3") # -> SyntaxError: positional argument follows keyword argument
```

#### En Resumen:

*   **Posicionales**: Se identifican por su **orden**. Si cambias el orden, cambias la asignación. Requieren que se pasen todos los argumentos esperados en la posición correcta.
*   **Por Nombre (Keyword)**: Se identifican por el **nombre** del parámetro. El orden no importa. Hacen el código más claro y permiten una mayor flexibilidad, especialmente con parámetros con valores por defecto.

Generalmente, cuando defines una función, puedes usar ambos tipos de argumentos. La buena práctica es usar argumentos posicionales para los valores requeridos y luego argumentos por nombre para opciones o configuraciones, a menudo con valores por defecto.

¿Qué pasa si combino argumentos posicionales y por nombre en una misma función?
¡Buena pregunta! De hecho, esto lo mencioné brevemente en la sección de 'Argumentos por Nombre'.

Cuando combinas argumentos posicionales y argumentos por nombre en la llamada a una función, la regla principal es que todos los argumentos posicionales deben ir primero, antes que cualquier argumento por nombre.

Python leerá los argumentos en el orden en que se proporcionan: primero asignará los valores a los parámetros por su posición, y luego usará los nombres para asignar los argumentos restantes. Si intentas poner un argumento por nombre antes de un argumento posicional, Python generará un SyntaxError.

Puedes ver un ejemplo de esto en la celda de código con la función describir_coche en la sección de 'Argumentos por Nombre'. En esa celda, la línea describir_coche("BMW", "Serie 3", año=2023) es un ejemplo válido de combinación, mientras que la línea comentada # describir_coche(año=2023, "BMW", "Serie 3") muestra el error que se produciría.

### Funciones que devuelven Múltiples Valores

En Python, una función puede devolver más de un valor a la vez. Cuando haces esto, los valores se agrupan automáticamente en una **tupla**.


```python
# Ejemplo de función que devuelve múltiples valores
def obtener_info_calculo(numero):
    cuadrado = numero ** 2
    cubo = numero ** 3
    es_par = numero % 2 == 0
    return cuadrado, cubo, es_par

# Llamar a la función y desempaquetar los resultados directamente
valor_original = 4
cuad, cub, par = obtener_info_calculo(valor_original)

print(f"Para el número {valor_original}:")
print(f"  Cuadrado: {cuad}")
print(f"  Cubo: {cub}")
print(f"  Es par: {par}")

print("\n---\n")

# También puedes capturar el resultado como una tupla única
resultados_tupla = obtener_info_calculo(5)
print(f"Resultados para 5 (como tupla): {resultados_tupla}")
print(f"  El cuadrado es: {resultados_tupla[0]}") # Accediendo por índice
```

Como puedes ver, la función `obtener_info_calculo` devuelve tres valores: el cuadrado, el cubo y si el número es par. Luego, puedes asignar estos tres valores a tres variables diferentes en una sola línea (`cuad, cub, par = ...`). Esto se llama **desempaquetado de tuplas** y es una característica muy útil de Python.



### Funciones Lambda (Funciones Anónimas)

Las **funciones lambda** en Python son pequeñas funciones anónimas, es decir, funciones que no se definen con la palabra clave `def` ni tienen un nombre. Se crean con la palabra clave `lambda`.

**Características Principales:**

*   **Anónimas:** No tienen un nombre.
*   **Pequeñas y Concisas:** Están limitadas a una única expresión. El resultado de esa expresión es lo que la función `lambda` devuelve.
*   **Sintaxis:** `lambda argumentos: expresión`
*   **Uso:** Son útiles para tareas sencillas que requieren una función de un solo uso, especialmente como argumentos para funciones de orden superior (funciones que toman otras funciones como argumentos), como `map()`, `filter()`, `sorted()`, etc.

### Ejemplo Básico de una Función Lambda


```python
# Una función normal para sumar dos números
def sumar_normal(a, b):
    return a + b

print(f"Suma normal (1, 2): {sumar_normal(1, 2)}")

# La función lambda equivalente
sumar_lambda = lambda a, b: a + b

print(f"Suma lambda (1, 2): {sumar_lambda(1, 2)}")

# Otro ejemplo: una lambda para duplicar un número
duplicar = lambda x: x * 2
print(f"Duplicar 5 con lambda: {duplicar(5)}")
```

Como puedes ver, la sintaxis es mucho más compacta para funciones sencillas. El `lambda` toma `a` y `b` como argumentos, y la expresión `a + b` es lo que se evalúa y se devuelve.

### Uso de Lambda con Funciones de Orden Superior

Aquí es donde las funciones `lambda` realmente brillan, ya que nos permiten pasar una pequeña lógica como argumento a otra función sin necesidad de definir una función completa con `def`.

#### 1. `filter()`

`filter(funcion, iterable)` construye un iterador a partir de elementos de un `iterable` para los que `funcion` devuelve verdadero.


```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando una función normal para filtrar números pares
def es_par(num):
    return num % 2 == 0

pares_normal = list(filter(es_par, numeros))
print(f"Números pares (función normal): {pares_normal}")

# Usando una función lambda para filtrar números pares
pares_lambda = list(filter(lambda num: num % 2 == 0, numeros))
print(f"Números pares (lambda): {pares_lambda}")
```

#### 2. `map()`

`map(funcion, iterable)` aplica `funcion` a cada elemento de un `iterable` y devuelve un iterador con los resultados.


```python
numeros = [1, 2, 3, 4, 5]

# Usando una función normal para obtener el cuadrado de cada número
def cuadrado(num):
    return num ** 2

cuadrados_normal = list(map(cuadrado, numeros))
print(f"Cuadrados (función normal): {cuadrados_normal}")

# Usando una función lambda para obtener el cuadrado de cada número
cuadrados_lambda = list(map(lambda num: num ** 2, numeros))
print(f"Cuadrados (lambda): {cuadrados_lambda}")
```

#### 3. `sorted()`

`sorted(iterable, key=funcion)` devuelve una nueva lista ordenada a partir de los elementos del `iterable`. El argumento `key` acepta una función para personalizar el criterio de ordenación.


```python
palabras = ["Python", "es", "un", "lenguaje", "genial"]

# Ordenar por la longitud de la palabra usando una función lambda
palabras_ordenadas_por_longitud = sorted(palabras, key=lambda palabra: len(palabra))
print(f"Palabras ordenadas por longitud: {palabras_ordenadas_por_longitud}")

# Una lista de diccionarios (objetos)
estudiantes = [
    {'nombre': 'Ana', 'edad': 20},
    {'nombre': 'Carlos', 'edad': 22},
    {'nombre': 'Beatriz', 'edad': 19}
]

# Ordenar la lista de estudiantes por edad usando una función lambda
estudiantes_ordenados_por_edad = sorted(estudiantes, key=lambda estudiante: estudiante['edad'])
print(f"Estudiantes ordenados por edad: {estudiantes_ordenados_por_edad}")
```

### Cuándo Usar y Cuándo No Usar Lambda

**Usa Lambda cuando:**

*   Necesitas una función simple y de un solo uso.
*   La lógica puede expresarse en una sola línea.
*   La estás pasando como argumento a una función de orden superior (`map`, `filter`, `sorted`, etc.).

**Evita Lambda cuando:**

*   La lógica es compleja o requiere múltiples declaraciones/pasos.
*   Necesitas que la función tenga un nombre (para reutilizarla o para mayor legibilidad en el código).
*   La función realiza una acción en lugar de devolver un valor (aunque técnicamente se puede hacer, es menos idiomático y menos legible).

En resumen, las funciones lambda son una herramienta poderosa para mejorar la concisión de tu código, pero es importante usarlas con moderación y solo cuando la simplicidad de la función lo justifique.
