---
id: funciones
title: "Funciones"
sidebar_label: "🔃 Funciones"
sidebar_position: 10
---

:::info[Codigo:]
- https://colab.research.google.com/drive/1ym02PRXCpqTB1cJhP4q8zvk2nUM_4ulq
:::

Las funciones son bloques de código reutilizables que realizan una tarea específica. Nos ayudan a organizar nuestro código, hacerlo más legible y evitar repetir código.

### Anatomía de una función

Toda función se compone de los siguientes elementos esenciales:
- `def`: como comando de definición de función

- `nombre de la función`: nombre de la función

- `(parametro)`: opcional si necesita un valor para operar

- `:`: indica el inicio del bloque de función

- Bloque de codigo de la función

- `return`: opcional si devuelve un resultado

```pyhton showLineNumbers
# creación de función que retorna el valor de un numero al cuadrado
def numero_cuadrado(numero):
    cuadrado = numero * numero
    return cuadrado
```

:::warning
Si una función en Python no incluye la sentencia `return`, o si llega al final de su ejecución sin encontrar una, la función devuelve automáticamente el objeto especial `None`
:::

La instrucción `**return**` sirve para indicar el resultado que la función "devuelve". Una vez que se alcanza la instrucción return la función termina y devuelve el valor indicado. En general es preferible devolver información usando return antes que imprimirla usando `print` ya que esto permite reutilizar la función para una mayor cantidad de casos.

### return `None`

*   **Retorno invisible:** Python inserta internamente una instrucción invisible de `return None` al final del bloque de código de la función. Esto asegura que todas las funciones en Python siempre devuelvan algo, manteniendo la consistencia del lenguaje.
*   **Comportamiento de la sentencia `return` vacía:** Si se incluye la palabra clave `return` pero no se especifica ningún valor después de ella (un *bare return*), el resultado es exactamente el mismo: la función devuelve `None`.
*   **Asignación de resultados:** Si intentas almacenar el resultado de una función que no tiene `return` en una variable (por ejemplo, `resultado = mi_funcion()`), la variable `resultado` hará referencia al objeto `None`.
*   **Significado de `None`:** Este es un objeto especial que representa la **ausencia de un valor**, "nada" o "datos vacíos". Es equivalente a lo que en otros lenguajes como C, C++ o Java se conoce como `void` o `null`.
*   **Visualización en el intérprete:** Cuando ejecutas una función que devuelve `None` en el intérprete interactivo, este normalmente **no muestra ninguna salida** para esa línea, a diferencia de cuando se devuelve un número o una cadena.
*   **Uso común:** Este tipo de funciones (a veces llamadas "procedimientos" en otros lenguajes) suelen utilizarse cuando el objetivo principal no es calcular un valor, sino realizar una **acción o efecto secundario**, como imprimir un mensaje en pantalla o modificar una lista global.

:::warning
Los parámetros de una función son utilizados como variable local a la función. A las que accede solo la función que las utiliza.

Por tanto no tienen valor fuera de la función.
:::

### Funciones Preconstruidas

Python viene con muchas funciones ya listas para usar. Algunas de las más comunes y básicas.


```python showLineNumbers
# Función: print()
# Uso: Muestra un mensaje o el valor de una variable en la consola.
# Parámetros: Puede recibir cero o más argumentos (valores a mostrar).

print("Hola, mundo!") # Sin variables, solo texto

nombre = "Ana"
print("Mi nombre es", nombre) # Con una variable

edad = 30
print("Tengo", edad, "años.") # Con múltiples variables y texto

# Función: len()
# Uso: Devuelve la longitud (cantidad de elementos) de un objeto.
# Parámetros: Recibe un único argumento, que debe ser un objeto con longitud (como una cadena, lista o tupla).

cadena = "Python"
longitud_cadena = len(cadena)
print(f"La longitud de '{cadena}' es: {longitud_cadena}")

lista_numeros = [1, 2, 3, 4, 5]
longitud_lista = len(lista_numeros)
print(f"La longitud de la lista es: {longitud_lista}")

# Función: type()
# Uso: Devuelve el tipo de un objeto.
# Parámetros: Recibe un único argumento (el objeto del que quieres saber el tipo).

numero_entero = 10
print(f"El tipo de {numero_entero} es: {type(numero_entero)}")

texto = "ejemplo"
print(f"El tipo de '{texto}' es: {type(texto)}")

es_verdad = True
print(f"El tipo de {es_verdad} es: {type(es_verdad)}")


# Función: input()
# Uso: Permite al usuario introducir datos a través de la consola.
# Parámetros: Opcionalmente, recibe un mensaje (string) que se muestra al usuario antes de que introduzca el dato.

nombre_usuario = input("Por favor, introduce tu nombre: ")
print(f"¡Hola, {nombre_usuario}!")

edad_usuario = input("¿Cuántos años tienes? ") # input siempre devuelve una cadena (string)
print(f"Tienes {edad_usuario} años.")
```

### Funciones Personalizadas

Ahora, aprenderemos a crear nuestras propias funciones. Usamos la palabra clave `def` para definirlas.

#### A. Funciones Simples: Sin parámetros y/o sin valor de retorno


```python showLineNumbers
# Función sin parámetros y sin valor de retorno
# Uso: Realiza una acción simple sin necesidad de información externa ni devolver un resultado específico.

def saludar():
    """
    Presenta un mensaje de saludo en formato str
    Argumento: None
    Respuesta: mensaje (str) 
    """
    print("¡Hola desde mi primera función!")

# Llamar a la función para ejecutarla
saludar()
```

---


```python showLineNumbers
# Función con un parámetro y sin valor de retorno
# Uso: Realiza una acción utilizando un valor que le pasamos.
# Parámetros: `nombre` es el parámetro que la función espera recibir.

def saludar_a_persona(nombre):
    """
    Presenta un mensaje de saludo

    Args:
        nombre (str): nombre de la persona a saludar

    Returns:
        str: Mensaje de saludo
    """
    print(f"¡Mucho gusto, {nombre}!")

# Llamar a la función, pasándole un argumento
saludar_a_persona("Carlos")
saludar_a_persona("Maria")
```

---


```python showLineNumbers
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


```python showLineNumbers
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


```python showLineNumbers
# Función con parámetros por defecto
# Uso: Algunos parámetros pueden tener un valor predefinido. 
# Si no se proporciona un valor al llamar la función, se usa el predeterminado.
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


```python showLineNumbers
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


```python showLineNumbers
# Función con Type Hints (Sugerencias de Tipo)
# Uso: Mejora la legibilidad del código y ayuda a herramientas de desarrollo a 
# detectar errores antes de ejecutar el programa.
# Nota: Son solo sugerencias, Python no las "obliga" en tiempo de ejecución.

def multiplicar(a: int, b: int) -> int:
    """Multiplica dos números enteros y devuelve el resultado."""
    return a * b

resultado_mult = multiplicar(4, 5)
print(f"4 * 5 = {resultado_mult}")

# Puedes pasar tipos incorrectos, pero las herramientas de análisis de código te advertirían
# resultado_incorrecto = multiplicar("hola", 2) # Esto generaría un error de tipo en tiempo de ejecución
```
```python showLineNumbers
def conversion(valor):
    """ calcula la conversion de una moneda a otra pesos a dolares"""
    valor_fijo = 890
    return valor / valor_fijo

# uso con varios valores

for valorpeso in (234500, 278900, 275600, 329800):
    print(f"{valorpeso} pesos son {conversion(valorpeso):.2f} dólares")
```
```raw
--salida:
234500 pesos son 263.48 dólares
278900 pesos son 313.37 dólares
275600 pesos son 309.66 dólares
329800 pesos son 370.56 dólares
```

---

### Argumentos Posicionales vs. Argumentos por Nombre (Keyword Arguments)

Es fundamental entender cómo se pasan los valores a las funciones. En Python, hay dos formas principales:

#### Argumentos Posicionales

Son los argumentos que se pasan a una función basándose en su **posición** u orden. La función asigna los valores a los parámetros en el mismo orden en que se reciben.

**Características:**
*   El orden importa. Si cambias el orden, la función puede interpretar los valores de forma diferente o incluso generar un error.
*   Son la forma más común y sencilla de pasar argumentos.


```python showLineNumbers
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


```python showLineNumbers
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

### Argumentos arbitrarios

En situaciones donde se desconoce a priori el numero exacto de parametros se establece el último parámetro con nombre precedido por (*).

```python
def media(*valores):
    """ Calcula la media de una serie de un numero arbitrario de valores """
    return float(sum(valores)) / len(valores)
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


```python showLineNumbers
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



## Ejercicios

### (A):
Crea un notebook (.ipynb) que contenga las 4 funciones que se mencionan abajo, con las siguientes características:

#### 1. Función sin argumentos
Esta función no requiere información externa para realizar su tarea. En Python, aunque no reciba parámetros, es obligatorio incluir los paréntesis en su definición y llamada.

```python
def mostrar_mensaje():
    """
    Muestra un mensaje de bienvenida al sistema.
    Esta función no recibe argumentos y no retorna ningún valor 
    (devuelve None por defecto).
    """
    
```

#### 2. Función con argumentos (sin retorno explícito)
Las funciones pueden aceptar **parámetros**, que son nombres que actúan como variables locales dentro de la función y reciben los valores (**argumentos**) al ser llamadas.

```python
def saludar():
    """
    Imprime un saludo personalizado para el estudiante

    Argumentos:
    nombre (str): El nombre del alumno que se desea saludar.
    """
    
```

#### 3. Función con argumentos y un resultado de retorno
Para que una función envíe un dato de vuelta al programa principal, se utiliza la palabra clave **`return`**. Una vez que se ejecuta un `return`, la función termina inmediatamente.

```python
def calcular_cuadrado():
    """
    Calcula el cuadrado de un número dado.

    Argumentos:
    numero (int o float): El valor numérico a elevar.

    Retorna:
    float: El resultado del número multiplicado por sí mismo.
    """
    

def perimetro():
    """
    Calcula el perimetro de un rectangulo. 

    Argumentos:
    a (int o float): primer lado de un rectangulo.
    b (int o float): segundo lado de un rectangulo.
    """

```

#### 4. Función con argumentos y múltiples resultados
En Python, una función puede devolver más de un valor separándolos por comas en la sentencia `return`. Técnicamente, Python empaqueta estos valores en una **tupla** que luego puede ser desempaquetada por el usuario.

```python
def obtener_estadisticas_basicas():
    """
    Calcula la suma y el producto de dos números.
    
    Argumentos:
    a (int o float): Primer número.
    b (int o float): Segundo número.
    
    Retorna:
    tuple: Una tupla que contiene (suma, producto).
    """

```

#### Ejemplo de uso de las funciones
Para probar estas funciones, se puede utilizar el siguiente bloque de código:

```python
# 1. Llamada a función sin argumentos


# 2. Llamada a función con argumento


# 3. Almacenar el resultado de una función que retorna un valor


# 4. Desempaquetar múltiples resultados

```

**Nota sobre los Docstrings:** Es una convención en Python insertar estas cadenas de texto inmediatamente después de la línea `def`. Sirven para que herramientas como `help()` muestren la ayuda de la función al usuario.

---
### (B):
Crea una funcion 'limpiar_rut' que acepte un 'texto' y devuelva un rut limpio:
- **ingrese:** limpiar_rut(' 10. 789 . 300-k')
- **devuelve:** '10789300-K'


## Docstring

Los **docstrings** (o cadenas de documentación) son literales de cadena que se insertan como la primera sentencia en la definición de un módulo, función, clase o método en Python. A diferencia de los comentarios comunes (usando `#`), los docstrings se conservan en el código compilado y son accesibles en tiempo de ejecución.

#### Cómo se usan los docstrings

1.  **Ubicación:** Deben aparecer inmediatamente después de la línea de encabezado del objeto (por ejemplo, justo debajo de la línea `def` o `class`) y antes de cualquier otra sentencia de código.
2.  **Delimitadores:** La convención estándar es encerrarlos entre **triples comillas dobles (`"""..."""`)**, lo cual permite que la cadena abarque múltiples líneas.
3.  **Acceso:** Se pueden consultar de dos maneras principales:
    *   A través del atributo especial **`__doc__`** del objeto (ej. `func_nombre.__doc__`).
    *   Utilizando la función integrada **`help()`**, que genera una página de documentación basada en el docstring.

#### Mejores recomendaciones y convenciones

Para escribir docstrings profesionales, las fuentes sugieren seguir las pautas de la **PEP 257** y adoptar las siguientes prácticas:

*   **Docstrings de una sola línea:** Se utilizan para funciones muy simples. Deben indicar el propósito del objeto de forma concisa y terminar con un punto (ej. `"""Convierte grados Celsius a Fahrenheit."""`). No deben simplemente repetir la firma de la función.

*   **Estructura multilínea:** Para objetos complejos, se recomienda incluir:
    *   Un **resumen corto** en la primera línea seguido de una línea en blanco.
    *   Una descripción detallada de los **argumentos** (parámetros) y los **valores de retorno**.
    *   Menciones sobre posibles **efectos secundarios** o excepciones que se puedan lanzar.
*   **Inclusión de ejemplos (Doctests):** Una de las mejores prácticas es incluir ejemplos de sesiones interactivas de Python (comenzando con `>>>`) dentro del docstring. Herramientas como el módulo `doctest` pueden ejecutar estos ejemplos automáticamente para asegurar que la documentación y el código coincidan y funcionen correctamente.
*   **Legibilidad y Estilo:**
    *   Mantener la longitud de las líneas por debajo de los **80 caracteres**.
    *   No dejar líneas en blanco inmediatamente antes ni después del docstring dentro del cuerpo de la función.
    *   En las clases, el docstring debe resumir el comportamiento de la categoría y sus atributos principales.
    *   En los módulos, el docstring debe ir al principio del archivo para explicar su propósito y uso general.

#### Estándares de estilo más comunes

Existen varios formatos reconocidos por la comunidad, pero los más utilizados son:Estilo Google: Es muy legible y divide la información en secciones claras.

#### 1. Estilo Google
Es muy legible y divide la información en secciones claras.
```python
def calcular_area(base, altura):
    """
    Calcula el área de un rectángulo.

    Args:
        base (float): La longitud de la base del rectángulo.
        altura (float): La longitud de la altura del rectángulo.

    Returns:
        float: El área calculada del rectángulo.
    """

    return base * altura
```

#### 2. Estilo NumPy/SciPy
Muy usado en ciencia de datos, detalla ampliamente los parámetros y el tipo de dato.
```python
def calcular_area(base, altura):
    """
    Calcula el área de un rectángulo.

    Parameters
    ----------
    base : float
        La longitud de la base del rectángulo.
    altura : float
        La longitud de la altura del rectángulo.

    Returns
    -------
    float
        El área calculada del rectángulo.
    """

    return base * altura
```

#### Cómo acceder a la documentación
Puedes visualizar el docstring de cualquier objeto, módulo o función de dos maneras principales en Python:
- 1. Usando la función help()
Es la forma nativa de consultar la documentación desde tu terminal o script
- 2. Usando el atributo __doc__ de la funcion
print(calcular_area.__doc__)