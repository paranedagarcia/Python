---
id: decoradores
title: "Decoradores"
sidebar_label: "​⚙️ Decoradores"
sidebar_position: 1
---

La función principal de los **decoradores** en Python es alterar o añadir funcionalidades a una función o clase de manera dinámica, sin necesidad de modificar directamente su código fuente. Se consideran una forma de **"azúcar sintáctico"** (*syntax sugar*), ya que proporcionan una sintaxis más limpia y legible para realizar una tarea que, de otro modo, sería más laboriosa de implementar.

A continuación se detallan sus características y ejemplos de uso:

## Funcionamiento y Propósitos
*   **Mecanismo de envoltura:** Un decorador es, en esencia, una función que recibe otra función como argumento y devuelve una nueva función (llamada habitualmente *wrapper* o envoltorio) que encapsula la lógica original junto con el nuevo comportamiento.
*   **Encapsulamiento y Reutilización:** Permiten separar responsabilidades y evitar la duplicación de código. Son ideales para tareas transversales como **depuración, registro de eventos (logging), validación de datos, gestión de permisos o medición de tiempos de ejecución**.
*   **Sintaxis `@`:** Aunque se pueden aplicar manualmente reasignando la función (`func = decorador(func)`), Python introdujo desde su versión 2.4 la sintaxis especial con el símbolo **`@`** colocado justo antes de la definición de la función.

## Ejemplos de uso

#### 1. Medición de tiempo (Profiling)
Un uso común es crear un decorador para medir cuánto tarda en ejecutarse una función sin tener que añadir código de cronómetro dentro de cada una:

```python showLineNumbers
import time

def measure(func):
    def wrapper(*args, **kwargs):
        t = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} tomó: {time.time() - t} segundos")
        return result
    return wrapper

@measure
def tarea_pesada():
    time.sleep(1)

# Al llamar a tarea_pesada(), se ejecutará la lógica de medida automáticamente.
```


#### 2. Decorador con argumentos (Factoría de decoradores)
Es posible pasar parámetros al propio decorador para personalizar su comportamiento. Por ejemplo, un decorador que verifique si el resultado de una función excede un umbral definido dinámicamente:

```python showLineNumbers
def max_result(threshold):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(f"Resultado demasiado grande ({result}). Máximo: {threshold}")
            return result
        return wrapper
    return decorator

@max_result(100)
def suma(a, b):
    return a + b
```
*(Fuente:)*

#### 3. Uso en Frameworks Reales
Los decoradores son fundamentales en muchas bibliotecas populares:
*   **Django:** Utiliza `@login_required` para restringir el acceso a vistas solo a usuarios autenticados.
*   **FastAPI:** Emplea decoradores como `@app.get("/")` para mapear funciones a rutas HTTP específicas y generar documentación automáticamente.
*   **Pytest:** Usa `@pytest.fixture` para definir funciones que configuran el entorno necesario para las pruebas de unidad.

### Consideraciones importantes
*   **Preservación de metadatos:** Al envolver una función, se pueden perder sus atributos originales (como su nombre o docstring). Para evitarlo, se recomienda usar el decorador **`@functools.wraps`** dentro del decorador personalizado.
*   **Orden de aplicación:** Se pueden aplicar múltiples decoradores a una misma función apilándolos. El decorador más cercano a la definición de la función es el que se aplica primero.

## Multiples decoradores

Para aplicar varios decoradores a una misma función en Python, simplemente se deben **apilar las sentencias `@nombre_del_decorador`** una encima de otra, inmediatamente antes de la definición de la función objetivo.

A continuación, se detallan los aspectos clave sobre su funcionamiento y orden de ejecución:

### 1. Orden de Aplicación
El orden en que se colocan los decoradores es fundamental, ya que Python los aplica de **abajo hacia arriba** (desde el más cercano a la función hacia afuera). 

Por ejemplo, si tienes la siguiente estructura:
```python showLineNumbers
@decorador_uno
@decorador_dos
def mi_funcion():
    pass
```
En este caso, `decorador_dos` se aplica primero a la función original, y el resultado de esa operación es luego procesado por `decorador_uno`.

### 2. Equivalencia Lógica
Aplicar múltiples decoradores mediante la sintaxis `@` es equivalente a realizar una **asignación anidada** de funciones manualmente. La estructura anterior es exactamente igual a escribir:
`mi_funcion = decorador_uno(decorador_dos(mi_funcion))`.

### 3. Ejemplo Práctico
Supongamos que queremos medir el tiempo de ejecución de una función y, al mismo tiempo, verificar que su resultado no exceda un límite. Podemos apilar ambos decoradores de la siguiente manera:

```python showLineNumbers
@measure      # Se aplica al final
@max_result(100) # Se aplica primero
def calcular_cubo(n):
    return n ** 3
```
Al llamar a `calcular_cubo(5)`, primero se ejecutará la lógica de `max_result` para validar el resultado (125) y luego `measure` informará cuánto tiempo tomó todo el proceso combinado.

### Consideraciones adicionales
*   **Encadenamiento:** Dado que cada decorador devuelve un objeto función (normalmente un *wrapper*), puedes encadenar tantos como sean necesarios para añadir capas de funcionalidad como registro de eventos, validación o caché.
*   **Legibilidad:** El uso de la sintaxis `@` permite identificar rápidamente todas las modificaciones que se han aplicado a una función sin tener que leer el código interno de la misma.

## En caso de error

El manejo de excepciones en un decorador se realiza envolviendo la ejecución de la función original dentro de un bloque **`try-except`** ubicado en la función interna o envoltorio (*wrapper*). Cuando la función decorada falla y lanza una excepción, el flujo normal se interrumpe y el control se transfiere inmediatamente al bloque **`except`** definido dentro del decorador.

Dentro de este bloque de captura, el decorador puede ejecutar diversas estrategias de gestión:

*   **Registro y Notificación:** El decorador puede imprimir un mensaje de error o registrar el incidente en un sistema de *logging* detallando qué función falló y por qué.
*   **Propagación del Error:** Es una práctica común que, tras registrar el error, el decorador utilice la palabra clave **`raise`** (sin argumentos) para re-lanzar la excepción original, permitiendo que esta siga subiendo por la pila de llamadas hasta ser manejada en otro nivel superior del programa.
*   **Gestión de Resultados Alternativos:** El decorador podría capturar la excepción y optar por no propagarla, devolviendo en su lugar un valor por defecto o un objeto que indique la ausencia de un resultado válido, como **`None`**.
*   **Limpieza de Recursos:** Si el decorador está gestionando recursos externos, puede incluir una cláusula **`finally`** para asegurar que tareas críticas, como cerrar un archivo o liberar un bloqueo (*lock*), se ejecuten independientemente de si la función falló o tuvo éxito.

Un ejemplo técnico muestra un decorador de registro que utiliza la estructura `try...except Exception as ex:`. En el bloque `except`, calcula el tiempo transcurrido hasta el fallo, registra el error y finalmente usa `raise` para no ocultar el problema al resto de la aplicación. Esta capacidad de supervisión permite que los decoradores actúen como una capa defensiva robusta en el diseño de software.

### Ejemplo de código

**Decorador de supervisión de errores**

El siguiente ejemplo muestra un decorador que intenta ejecutar una función, y si esta falla, imprime los detalles del error y lo vuelve a lanzar para no ocultar el problema al sistema.

```python showLineNumbers
import functools
import time

def monitor_de_errores(func):
    @functools.wraps(func) # Preserva los metadatos de la función original
    def wrapper(*args, **kwargs):
        try:
            # Supervisamos la ejecución de la función original
            return func(*args, **kwargs)
        except Exception as e:
            # Capturamos el error y reportamos información útil
            print(f"¡ERROR DETECTADO en la función '{func.__name__}'!")
            print(f"Argumentos recibidos: {args} {kwargs}")
            print(f"Tipo de excepción: {type(e).__name__}")
            print(f"Mensaje del error: {e}")
            
            # Re-levantamos la excepción original para que siga su curso
            raise 
    return wrapper

# --- Ejemplo de uso ---

@monitor_de_errores
def dividir_numeros(a, b):
    return a / b

try:
    # Esta llamada provocará un ZeroDivisionError
    print(dividir_numeros(10, 0))
except ZeroDivisionError:
    print("El programa principal manejó el error después del decorador.")
```

En este diseño, el decorador funciona como una **herramienta de diagnóstico** que no altera la lógica de negocio de la función, pero añade una capa de transparencia sobre por qué y cómo falló el código.


## EJEMPLO

Para crear un decorador que valide tipos de datos, se debe utilizar el patrón de **factoría de decoradores** (un decorador que acepta argumentos). Este mecanismo permite definir dinámicamente qué tipo de dato esperamos antes de que se ejecute la función original.

A continuación, se presenta un ejemplo basado en los conceptos de **envoltorios (wrappers)**, el uso de **`isinstance`** para la verificación y la gestión de excepciones de tipo **`TypeError`**.

### Ejemplo de Decorador: `validate_types`

Este decorador verificará que todos los argumentos posicionales pasados a una función coincidan con el tipo especificado.

```python showLineNumbers
import functools

def validate_types(expected_type):
    """Factoría de decoradores que recibe el tipo esperado."""
    def decorator(func):
        @functools.wraps(func) # Preserva los metadatos de la función original
        def wrapper(*args, **kwargs):
            # Verificamos cada argumento posicional recibido [*args]
            for arg in args:
                if not isinstance(arg, expected_type):
                    # Lanzamos TypeError si el tipo es incorrecto
                    raise TypeError(f"El argumento '{arg}' no es de tipo {expected_type.__name__}")
            
            # Si todo es correcto, ejecutamos la función original
            return func(*args, **kwargs)
        return wrapper
    return decorator

# --- Ejemplo de uso ---

@validate_types(int) # Solo permitiremos enteros
def sumar_numeros(a, b):
    return a + b

try:
    print(sumar_numeros(10, 20))    # Funciona correctamente
    print(sumar_numeros(10, "20"))  # Lanzará un TypeError
except TypeError as e:
    print(f"Error de validación: {e}")
```

### Análisis técnico:

1.  **Estructura de tres niveles:** Para que el decorador acepte argumentos (como `int`), es necesario anidar tres funciones: la factoría, el decorador real y el envoltorio (*wrapper*).
2.  **Uso de `isinstance`:** Se recomienda usar `isinstance(objeto, tipo)` en lugar de comparar tipos directamente (como `type(x) == int`), ya que es más flexible y compatible con la herencia.
3.  **Preservación de metadatos:** Se utiliza `@functools.wraps(func)` para asegurar que la función decorada no pierda su nombre (`__name__`) ni su cadena de documentación (*docstring*) al ser reemplazada por el *wrapper*.
4.  **Manejo de argumentos variables:** El uso de `*args` permite que el decorador sea genérico y pueda procesar cualquier cantidad de parámetros de entrada sin conocerlos de antemano.
5.  **Validación en tiempo de ejecución:** A diferencia de las "sugerencias de tipo" (*type hints*) de Python que son informativas, un decorador como este **fuerza** la validación durante la ejecución del programa, deteniéndolo si los datos son incorrectos mediante una excepción.


¿Cómo se usan los decoradores en clases de Python?