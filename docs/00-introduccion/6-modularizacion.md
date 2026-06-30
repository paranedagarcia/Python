---
id: modularizacion
title: "Modularización"
sidebar_label: "​​📦 Modularización"
sidebar_position: 11
description: "Modularización y reutilización de código"
---

En Python, la **modularización y reutilización de código** se gestionan mediante una jerarquía de estructuras que permiten organizar el software en unidades lógicas, evitando la redundancia y facilitando el mantenimiento. Este enfoque se basa en el principio fundamental **DRY (Don't Repeat Yourself)**, que establece que cada pieza de conocimiento debe tener una representación única e inequívoca dentro de un sistema.

A continuación se detallan los mecanismos principales para lograrlo:

### Funciones: La unidad básica de reutilización
Las funciones son bloques de código con nombre diseñados para realizar tareas específicas. Son la forma más sencilla de encapsular código para ser ejecutado múltiples veces en diferentes puntos de un programa.
*   **Ventajas:** Reducen la duplicación de código, permiten dividir tareas complejas en bloques manejables y mejoran la legibilidad y trazabilidad del programa.
*   **Flexibilidad:** Pueden recibir parámetros para influir en su cómputo y devolver nuevos objetos como resultado.

### Clases y Programación Orientada a Objetos (POO)
Las clases permiten encapsular tanto el código (métodos) como los datos (atributos) sobre los cuales opera ese código.
*   **Herencia:** Permite crear una relación "es-un" (is-a), donde una clase hija adquiere automáticamente los atributos y métodos de una clase padre, pudiendo extenderlos o especializarlos. Esto evita copiar y pegar código entre clases similares.
*   **Composición:** Crea una relación "tiene-un" (has-a), donde un objeto complejo se construye a partir de otros objetos más simples. Es a menudo una alternativa más flexible que la herencia para combinar comportamientos.
*   **Polimorfismo:** Permite que diferentes clases respondan al mismo nombre de método, permitiendo que una sola pieza de código trabaje con diversos tipos de objetos de manera unificada.

### Módulos y Paquetes: Organización a gran escala
*   **Módulos:** Son simplemente archivos con extensión `.py` que contienen definiciones de funciones, clases y variables. Permiten agrupar elementos relacionados y ocultar detalles de implementación para concentrarse en la lógica de nivel superior.
*   **Paquetes:** Son colecciones de módulos organizados en directorios. Para que Python reconozca un directorio como un paquete, este debe contener tradicionalmente un archivo llamado `__init__.py`. Esto permite crear jerarquías anidadas de código.

### Bibliotecas y el Ecosistema Python
Python se describe como un lenguaje con **"pilas incluidas"** debido a su extensa **biblioteca estándar**, que ofrece módulos listos para usar en tareas comunes (matemáticas, fechas, archivos, etc.). 
*   **Módulos de terceros:** A través de herramientas como **pip** o **uv**, los desarrolladores pueden instalar y reutilizar miles de paquetes creados por la comunidad alojados en el **PyPI (Python Package Index)**.

### Gestión del entorno: Entornos Virtuales
Para evitar conflictos entre las versiones de las bibliotecas que utilizan diferentes proyectos, se emplean **entornos virtuales** (`venv`, `pipenv`, `conda`). Estos crean espacios aislados donde se pueden instalar dependencias específicas para cada aplicación, garantizando que el entorno de ejecución sea repetible y controlado.

### Otros mecanismos de reutilización
*   **Decoradores:** Permiten alterar o extender el comportamiento de funciones o clases de forma dinámica y elegante.
*   **Generadores:** Optimizan el uso de memoria al generar elementos sobre la marcha en lugar de almacenarlos todos en una lista.
*   **Administradores de contexto (`with`):** Formalizan la preparación y limpieza de recursos, asegurando que tareas como cerrar archivos se realicen correctamente siempre.

## Creación y uso de modulos de funciones

Para crear y usar un módulo de funciones en un proyecto de Python, se deben seguir una serie de pasos que permiten organizar el código en unidades lógicas, facilitando su mantenimiento y reutilización.

### Creación del módulo
Un módulo es simplemente un archivo de texto con extensión **`.py`** que contiene definiciones de funciones, clases o variables.

*   **Nombre del archivo:** El nombre del archivo (sin la extensión) será el nombre del módulo. Por ejemplo, un archivo llamado `perimetros.py` se convierte en el módulo `perimetros`. 
*   **Contenido:** Se deben agrupar funciones relacionadas. Es una buena práctica incluir un **docstring** (cadena de documentación) al inicio del archivo para explicar su propósito.
*   **Funciones internas:** Si se desea que una función sea de uso interno y no se importe automáticamente con `from modulo import *`, su nombre debe comenzar con un **guion bajo** (ej. `_funcion_privada`).
*   **Restricciones de nombre:** Se deben evitar nombres que coincidan con palabras clave de Python o módulos de la biblioteca estándar (como `math.py` o `random.py`) para evitar conflictos.

### El bloque de prueba (`if __name__ == '__main__':`)
Es fundamental incluir un bloque de código al final del módulo que solo se ejecute cuando el archivo se inicie como un programa independiente, pero que se ignore cuando el módulo sea importado por otro script.
*   La variable especial `__name__` se establece automáticamente como `'__main__'` si el archivo se ejecuta directamente.
*   Si el archivo se importa, `__name__` toma el nombre del módulo, evitando que se ejecuten las pruebas o ejemplos incluidos en dicho bloque.

### Uso del módulo (Importación)
Existen diversas formas de incorporar la funcionalidad de un módulo en otro archivo del proyecto:

*   **`import modulo`:** Importa el módulo completo. Para acceder a sus funciones se utiliza la "notación de punto": `modulo.nombre_funcion()`.
*   **`from modulo import funcion`:** Importa solo una función específica, permitiendo llamarla directamente por su nombre sin el prefijo del módulo.
*   **`import modulo as alias`:** Permite asignar un nombre más corto o conveniente al módulo (ej. `import math as m`).
*   **`from modulo import *`:** Importa todos los nombres del módulo. Se desaconseja su uso frecuente porque puede "ensuciar" el espacio de nombres local y causar conflictos con funciones que tengan el mismo nombre en diferentes archivos.

### Rutas de búsqueda y paquetes
*   **Ubicación:** Para que Python encuentre el módulo, este debe residir en el mismo directorio que el programa que lo llama o en una de las carpetas listadas en `sys.path`. Se puede añadir una carpeta a esta lista mediante la variable de entorno `PYTHONPATH`.
*   **Paquetes:** Si el proyecto crece, se pueden agrupar varios módulos en directorios llamados **paquetes**. Para que un directorio sea reconocido como tal, tradicionalmente debe contener un archivo llamado **`__init__.py`**. La importación de un módulo dentro de un paquete se hace mediante la ruta jerárquica: `import paquete.subpaquete.modulo`.

### Organización en Paquetes

Cuando un proyecto tiene muchos módulos, estos pueden agruparse en directorios llamados paquetes. Para que Python reconozca una carpeta como un paquete, tradicionalmente esta debe contener un archivo llamado __init__.py (que puede estar vacío). La importación se realiza entonces indicando la ruta jerárquica: import paquete.subpaquete.módulo

#### Validacion de un rut chileno

Para validar si un RUT es matemáticamente correcto, se aplica el algoritmo denominado **Módulo 11**. Este procedimiento permite determinar si el dígito verificador (DV) es el resultado exacto de una serie de operaciones sobre los dígitos precedentes.

Utilizando las funciones y conceptos de Python detallados en las fuentes y en nuestra conversación previa, la validación se desglosa en los siguientes pasos técnicos:

1.  **Preparación de los datos**: Primero se debe extraer el "cuerpo" del RUT (los números antes del guion) y el DV. Es necesario convertir los caracteres de texto en números enteros mediante la función **`int()`** para poder realizar cálculos.
2.  **Inversión del número**: Los dígitos del cuerpo deben procesarse de derecha a izquierda. En Python, esto se logra de forma eficiente mediante **slicing** con un paso negativo (`[::-1]`), una técnica para rebanar secuencias desde el final.
3.  **Multiplicación por serie**: Se multiplica cada dígito por una secuencia numérica que va del 2 al 7, reiniciándose si el RUT tiene más de seis dígitos. Para recorrer esta secuencia se utiliza un **bucle `for`**.
4.  **Suma y resto**: Se suman todos los productos obtenidos y se aplica el **operador módulo (`%`)** para obtener el resto de la división por 11. El uso del módulo es fundamental en este algoritmo para encontrar el residuo entero.
5.  **Cálculo del dígito esperado**: Se resta el residuo obtenido al número 11. Para determinar el DV final, se aplica **lógica condicional (`if-elif-else`)** siguiendo estas reglas estándar:
    *   Si el resultado es 11, el DV esperado es **0**.
    *   Si el resultado es 10, el DV esperado es **'K'**.
    *   Para cualquier otro valor, el DV esperado es el número obtenido.

Finalmente, se utiliza el **operador de igualdad (`==`)** para comparar el DV calculado con el DV ingresado por el usuario y confirmar si el RUT es válido.

Este enfoque garantiza la precisión matemática al evitar errores de redondeo que podrían ocurrir con tipos **`float`**, los cuales son inherentemente inexactos para este tipo de validaciones exactas.

**EJERCICIO:**

```python title="rut_utils.py"
# modulo rut_utils.py
def rut_valido(rut_str):
    """
    valida que la cadena recibida sea un rut validado
    """
    def rut_valido(rut_str):
    # 1. Limpieza y separación
    limpio = rut_str.replace(".", "").replace("-", "").upper()
    cuerpo, dv_real = limpio[:-1], limpio[-1] #
    
    # 2. Algoritmo Módulo 11
    suma = 0
    multiplicador = 2
    for d in reversed(cuerpo): # Iteración
        suma += int(d) * multiplicador # Conversión int
        multiplicador = 2 if multiplicador == 7 else multiplicador + 1
    
    resto = suma % 11 # Operador módulo
    dv_esperado = 11 - resto
    
    # 3. Lógica de comparación
    if dv_esperado == 11: dv_esperado = "0"
    elif dv_esperado == 10: dv_esperado = "K"
    else: dv_esperado = str(dv_esperado)
    
    return dv_real == dv_esperado # Retorno booleano

def rut_print(rut_str):
    """
    Recibe una cadena de texto y devuelve el formato de RUT chileno. formato numerico
    Ejemplo: '9530872K' -> '9.530.872-K'
    """
    # desafío ...

    return f"{cuerpo}-{dv}"

def rut_formato(rut_str):
    """
    Recibe una cadena de texto y devuelve el formato de RUT chileno.
    Ejemplo: '9530872K' -> '9530872-K'
    """
    # Limpieza básica: eliminamos puntos y guiones existentes
    limpio = rut_str.replace(".", "").replace("-", "")
    
    # Separamos el cuerpo del dígito verificador usando slicing
    cuerpo = limpio[:-1]
    dv = limpio[-1].upper() # Aseguramos que el DV esté en mayúscula
    
    # Retornamos la cadena formateada usando una f-string
    return f"{cuerpo}-{dv}"

# Bloque de prueba
if __name__ == '__main__':
    ejemplo = "9530872K"
    print(f"Prueba interna del módulo: {rut_formato(ejemplo)}")
```
Para utilizar la función desde otro archivo del proyecto, se debe emplear la sentencia **import** o **from ... import**. Esto permite acceder a la lógica definida en el módulo sin tener que duplicar el código.

```python title="main.py"
# programa principal
# Importamos la función específica del módulo
from rut_utils import rut_formato

def ejecutar_programa():
    # Supongamos que recibimos una entrada de usuario
    entrada = "16320890k"
    
    # Llamada a la función del módulo
    rut_listo = rut_formato(entrada)
    
    # Mostramos el resultado con un mensaje claro
    print(f"El RUT procesado es: {rut_listo}")

if __name__ == '__main__':
    ejecutar_programa()
```

