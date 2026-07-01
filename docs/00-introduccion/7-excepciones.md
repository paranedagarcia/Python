---
id: excepciones
title: "Excepciones"
sidebar_label: "🗂️​ Excepciones"
description: "Manejo de excepciones y errores"
sidebar_position: 12
---

El manejo de excepciones en Python es un mecanismo fundamental para gestionar errores que ocurren durante la ejecución de un programa, permitiendo que este responda a situaciones inesperadas de manera controlada en lugar de detenerse abruptamente.

### Estructura del Manejo de Excepciones

La herramienta principal para gestionar estos eventos es el bloque **`try-except`**, que puede extenderse con las cláusulas **`else`** y **`finally`**:

1.  **`try`**: Contiene el código que se desea supervisar y que podría generar un error.
2.  **`except`**: Define el bloque de código que se ejecutará si ocurre una excepción específica en el bloque `try`. Es una buena práctica capturar solo las excepciones que se esperan (por ejemplo, `ZeroDivisionError`) en lugar de usar un `except` genérico.
3.  **`else`**: Se ejecuta únicamente si el código dentro del bloque `try` no lanzó ninguna excepción.
4.  **`finally`**: Contiene tareas de limpieza (como cerrar un archivo) que se ejecutarán **siempre**, independientemente de si ocurrió un error o no.

### Ejemplos de Uso

*   **Manejo de divisiones por cero:**
    ```python showLineNumbers
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("¡Error! No se puede dividir por cero.")
    ```

*   **Lectura segura de archivos:**
    ```python showLineNumbers
    from pathlib import Path
    path = Path('datos.txt')
    try:
        contenido = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Lo siento, el archivo {path} no existe.")
    ```

*   **Conversión de datos del usuario:**
    ```python showLineNumbers
    try:
        numero = int(input("Introduce un número: "))
    except ValueError:
        print("Eso no es un número válido.")
    ```

### Levantando y Definiendo Excepciones

Los programadores pueden forzar la aparición de una excepción usando la palabra clave **`raise`** seguida del tipo de error y un mensaje descriptivo. Además, es posible crear **excepciones personalizadas** definiendo una clase que herede de `Exception`:

```python showLineNumbers
class ErrorDeRango(ValueError):
    """Excepción para valores fuera de los límites permitidos."""
    pass

def validar_edad(edad):
    if edad < 0:
        raise ErrorDeRango("La edad no puede ser negativa")
```

### Excepciones Disponibles por Defecto

A continuación se listan algunas de las excepciones más comunes integradas en Python:

| Excepción | Descripción |
| :--- | :--- |
| **`BaseException`** | Clase raíz de la que heredan todas las demás excepciones. |
| **`Exception`** | Superclase para casi todos los errores que no son de salida del sistema. |
| **`ArithmeticError`** | Clase base para errores aritméticos como `OverflowError`. |
| **`ZeroDivisionError`** | Se lanza al intentar dividir o realizar módulo por cero. |
| **`ValueError`** | Ocurre cuando una función recibe un argumento del tipo correcto pero con un valor inapropiado. |
| **`TypeError`** | Se lanza cuando se aplica una operación a un objeto de tipo incorrecto. |
| **`IndexError`** | Ocurre cuando un índice de una secuencia (lista, tupla, etc.) está fuera de rango. |
| **`KeyError`** | Se lanza cuando no se encuentra una clave en un diccionario. |
| **`FileNotFoundError`**| Variante de `IOError` que ocurre cuando un archivo solicitado no existe. |
| **`NameError`** | Ocurre cuando se intenta acceder a una variable o nombre no definido. |
| **`SyntaxError`** | Se produce cuando Python encuentra un error en la gramática del código. |
| **`KeyboardInterrupt`**| Lanzada cuando el usuario interrumpe la ejecución (usualmente con Ctrl+C). |
| **`StopIteration`** | Indica que un iterador no tiene más elementos que entregar. |



Aunque la estructura **`try-finally`** es la base para garantizar que el código de limpieza se ejecute sin importar si ocurre un error, el uso de la sentencia **`with`** (basada en administradores de contexto) se considera la forma más "pitónica" y eficiente de manejar recursos externos.

Las principales ventajas de usar **`with`** frente a **`try-finally`** son:

### 1. Legibilidad y Concisión
La sentencia `with` permite escribir código mucho más limpio y corto. Mientras que un bloque `try-finally` para cerrar un archivo requiere varias líneas y una llamada explícita a `.close()`, el bloque `with` realiza la misma tarea de forma implícita en una sola línea de encabezado. Las fuentes señalan que el uso repetitivo de `try-finally` puede hacer que el código se vuelva "bastante feo" y difícil de seguir.

### 2. Gestión Automática de Recursos
La ventaja técnica más crítica es que `with` garantiza que los recursos (como archivos, sockets de red o bloqueos de bases de datos) se cierren o liberen **automáticamente** al salir del bloque, incluso si se lanza una excepción. Esto evita errores comunes, como olvidar cerrar un archivo manualmente, lo que podría causar fugas de memoria o corrupción de datos.

### 3. Encapsulación de la Lógica de Limpieza
El uso de `with` delega la responsabilidad de la preparación y la limpieza al **administrador de contexto**. Esto significa que el programador no necesita conocer los detalles internos de cómo liberar un recurso; solo necesita saber cómo entrar en el contexto. Por ejemplo:
*   En archivos, asegura el cierre del manejador.
*   En hilos, permite adquirir y liberar bloqueos (*locks*) de forma segura.
*   En transacciones de bases de datos, puede realizar un *commit* si todo sale bien o un *rollback* si ocurre un error.

### 4. Soporte para Múltiples Recursos
Python permite combinar múltiples administradores de contexto en una sola sentencia `with`, lo cual es mucho más sencillo que anidar múltiples bloques `try-finally`.

### 5. Manejo Avanzado de Excepciones
A través del método especial `__exit__`, un administrador de contexto puede decidir si **suprime** una excepción o permite que se propague. Esto permite reutilizar la lógica de manejo de errores en diferentes partes del programa, aplicando el principio **DRY** (*Don't Repeat Yourself*) de forma más efectiva que con bloques `except` e `if` dispersos.

En resumen, se recomienda utilizar `with` siempre que se trabaje con objetos que soporten el protocolo de administración de contexto, reservando `try-finally` solo para situaciones muy específicas donde no exista un administrador de contexto disponible.

## Excepción personalizada

Para definir una excepción personalizada en Python, debes crear una **clase que herede de una clase de excepción existente**, preferiblemente de la clase base **`Exception`**.

A continuación se detallan los pasos y variantes según las fuentes:

#### 1. Definición básica
La forma más sencilla de crear una excepción propia es definir una clase con el nombre deseado y usar la sentencia `pass` para no agregar lógica adicional.
```python
class MiErrorPersonalizado (Exception):
    """Descripción de la excepción."""
    pass
```

#### 2. Elección de la clase base
Aunque todas las excepciones derivan técnicamente de `BaseException`, las fuentes recomiendan **heredar siempre de `Exception`** para excepciones de usuario. También es una buena práctica heredar de una excepción incorporada que sea **semánticamente similar** al problema que deseas reportar. Por ejemplo:
*   Si el error es sobre un valor inválido, hereda de **`ValueError`**.
*   Si es un error de entrada/salida, hereda de **`IOError`**.

#### 3. Personalización con `__init__` y métodos
Si necesitas que la excepción transporte información específica o realice cálculos, puedes definir su propio método **`__init__`** y otros métodos adicionales.
*   **Constructor:** Puedes pasar argumentos adicionales (como saldos, códigos de error o nombres de archivo) que se guardarán en el atributo **`args`** de la instancia.
*   **Métodos propios:** Puedes incluir lógica para procesar los datos del error, como un método para calcular la diferencia en un retiro bancario inválido.
#### 4. Uso de la excepción personalizada
Una vez definida, puedes lanzarla en tu código utilizando la palabra clave **`raise`**.
```python
# Ejemplo de uso
if valor < 0:
    raise MiErrorPersonalizado("El valor no puede ser negativo")
```

#### 5. Captura y manejo
Para gestionar estas excepciones, se utilizan los bloques **`try-except`**, donde puedes capturar específicamente tu clase personalizada o cualquier clase padre de la que esta herede. Al capturarla, puedes usar la palabra clave **`as`** para asignar el objeto de la excepción a una variable y acceder a sus atributos o métodos.


Un ejemplo real y robusto de una excepción personalizada en Python es la gestión de transacciones bancarias, como un retiro de dinero inválido. Este caso permite demostrar cómo una excepción puede no solo informar de un error, sino también **transportar datos útiles** y ofrecer métodos para procesarlos.

A continuación, se presenta una implementación basada en los principios de diseño de las fuentes:

### Definición de la excepción personalizada
En este caso, heredamos de `ValueError` porque el error se debe a un valor inapropiado (intentar sacar más dinero del disponible).

```python showLineNumbers title="utils.py"
from decimal import Decimal

class InvalidRetiro(ValueError):
    """Excepción lanzada cuando el saldo es insuficiente para el retiro."""
    def __init__(self, balance: Decimal, amount: Decimal) -> None:
        # Llamamos al constructor de la clase padre con un mensaje descriptivo
        super().__init__(f"La cuenta no tiene fondos suficientes para retirar ${amount}")
        self.amount = amount
        self.balance = balance

    def overage(self) -> Decimal:
        """Calcula cuánto dinero falta para completar la operación."""
        return self.amount - self.balance
```

### Uso y captura en el programa
Para manejar esta situación, se utiliza el bloque **`try-except`** y la palabra clave **`as`** para acceder a la instancia de la excepción y sus métodos específicos.

```python showLineNumbers
# Supongamos estos valores iniciales
balance = Decimal('25.00')
retiro_amount = Decimal('50.00')

try:
    if retiro_amount > balance:
        # Lanzamos nuestra excepción personalizada con los datos reales
        raise InvalidRetiro(balance, retiro_amount)
except InvalidRetiro as ex:
    # Informamos al usuario usando el método personalizado .overage()
    print(f"Lo sentimos, su retiro excede su saldo por ${ex.overage()}")
```

### ¿Por qué es un "ejemplo real" efectivo?
*   **Encapsulación:** Al definir `InvalidRetiro`, separas la lógica de errores bancarios de los errores genéricos de Python.
*   **Tratamiento de datos sensibles:** Las fuentes señalan que es una buena práctica no incluir datos sensibles (como números de cuenta) directamente en el mensaje de la excepción para evitar que aparezcan en los registros de errores (*logs*) o rastreos (*tracebacks*).
*   **Uso de `Decimal`:** Para aplicaciones financieras, se utiliza la clase `Decimal` de la biblioteca estándar en lugar de `float` para evitar errores de redondeo binario.
*   **Control de flujo:** Este diseño permite que el programa no se detenga bruscamente (*crash*), sino que tome una ruta alternativa para informar al usuario de forma amigable.

## Multiples excepciones

Para capturar múltiples excepciones en un mismo bloque `try-except` y darles el mismo tratamiento, debes agrupar los tipos de excepción en una **tupla** (dentro de paréntesis) separada por comas.

### Sintaxis para capturar varias excepciones
La estructura recomendada es la siguiente:

```python
try:
    # Código que puede lanzar errores
    resultado = 10 / variable_entrada
except (ZeroDivisionError, TypeError, ValueError) as e:
    # Este bloque maneja cualquiera de las tres excepciones anteriores
    print(f"Ocurrió un error esperado: {e}")
```

### Detalles técnicos importantes
*   **Uso de paréntesis:** Al listar más de una excepción en una sola cláusula `except`, **los paréntesis son obligatorios**. Si se omiten, Python podría interpretar el segundo nombre como una variable donde guardar el objeto de la excepción (sintaxis antigua) en lugar de un segundo tipo de error a capturar.
*   **Acceso al objeto de la excepción:** Puedes usar la palabra clave **`as`** después de la tupla para asignar la excepción capturada a una variable (comúnmente `e`, `ex` o `err`) y así acceder a sus argumentos o mensajes de error.
*   **Mismo tratamiento:** Esta técnica es útil únicamente cuando deseas que la respuesta del programa sea **idéntica** para todos los errores listados.

### Alternativa: Bloques except múltiples
Si necesitas realizar acciones diferentes según el tipo de error, lo correcto es apilar bloques `except` individuales:

```python
try:
    # Código supervisado
except ZeroDivisionError:
    print("No se puede dividir por cero")
except TypeError:
    print("Tipo de dato inválido para la operación")
except Exception:
    print("Cualquier otro error no especificado anteriormente")
```

**Nota sobre el orden:** Cuando se usan múltiples cláusulas `except`, Python ejecuta solo la **primera que coincida** con la excepción lanzada. Por ello, debes colocar las excepciones más específicas al principio y las más genéricas (como `Exception`) al final.