# **Guía de Práctica: Polimorfismo Dinámico y Duck Typing en Python**

Como ingenieros de software, uno de los saltos cualitativos más importantes en nuestra carrera es pasar de entender el código como una serie de jerarquías rígidas a visualizarlo como un ecosistema de comportamientos. En Python, esta transición se fundamenta en el concepto de **Duck Typing**, una filosofía que prioriza la capacidad de un objeto para realizar una acción por encima de su linaje o clase base.

## **1. Fundamentos: La Filosofía del Duck Typing**

El término proviene de la máxima de James Whitcomb Riley: *"Si camina como un pato y grazna como un pato, entonces debe ser un pato"*. En el desarrollo "Pythonic", esto significa que si un objeto implementa los métodos requeridos por una función, Python lo aceptará sin cuestionar si el objeto hereda de una clase específica o implementa formalmente una interfaz.

A diferencia del **tipado nominal** (común en Java o C++), donde la validez de un objeto se decide por su nombre y posición en el árbol de herencia, el **Duck Typing** se basa en el **tipado estructural dinámico**.

### **Comparativa de Modelos de Tipado**

| Característica | Tipado Nominal (Java/C++) | Duck Typing (Python) |
| :---- | :---- | :---- |
| **Validación** | Tiempo de compilación (estática). | Tiempo de ejecución (dinámica). |
| **Requisito** | Herencia explícita o interfaces. | Presencia de atributos/métodos. |
| **Acoplamiento** | Alto (dependencia de jerarquías). | Bajo (dependencia de contratos). |
| **Extensibilidad** | Requiere modificar la base de clases. | Natural; basta cumplir el protocolo. |

**Insight Arquitectónico:** El Duck Typing es una herramienta poderosa para el desacoplamiento. Permite que el código sea extensible "hacia el futuro": podemos diseñar un sistema hoy que acepte objetos de clases que ni siquiera han sido escritas todavía, siempre que respeten el contrato de comportamiento.

## **2. Ejercicio 1 (Intermedio): El Procesador de Flujos (Streams)**

Imaginemos un orquestador de datos que debe leer información de una fuente y enviarla a un destino. En otros lenguajes, definiríamos interfaces como `IReadable` e `IWritable`. En Python, simplemente confiamos en que los objetos "sepan" leer y escribir.

### **Configuración del Esqueleto**

Definiremos diversas fuentes y destinos sin ninguna relación de herencia entre sí:
```python
class FileReader:

    def readline(self):

        return "Datos persistidos en disco"

class StringReader:

    def readline(self):

        return "Datos en memoria"

class ConsoleWriter:

    def write(self, data):

        print(f"[Salida Estándar]: {data}")

class HTMLWriter:

    def write(self, data):

        print(f"<div><p>{data}</p></div>")
```
### **Implementación del Orquestador: De LBYL a EAFP**

Como catedráticos, debemos distinguir dos enfoques pedagógicos. El primero es **LBYL** (*Look Before You Leap*), donde validamos la existencia del método antes de llamar. El segundo, preferido por los desarrolladores senior, es **EAFP** (*Easier to Ask for Forgiveness than Permission*), que asume que el objeto cumplirá el contrato y maneja la excepción si falla.

```pyhton
class Processor:
    """Orquestador que procesa flujos de datos mediante Duck Typing."""

    def process(self, source, dest):

        # Enfoque LBYL (Pedagógico): Verificamos antes de actuar

        if not hasattr(source, 'readline') or not hasattr(dest, 'write'):

            raise TypeError("Los objetos no cumplen con el protocolo Reader/Writer")

        # Enfoque EAFP (Pythonic): Operamos y capturamos fallos de contrato

        try:

            data = source.readline()

            dest.write(data)

        except AttributeError as e:

            print(f"Error de protocolo: El objeto no se comporta como se esperaba. {e}")

# Ejemplo de uso

proc = Processor()

proc.process(StringReader(), HTMLWriter())
```
Este polimorfismo dinámico no se limita a métodos nombrados; se extiende orgánicamente a los operadores matemáticos de Python.

## **3. Ejercicio 2 (Avanzado): Operadores Conmutativos y Vectores**

Basándonos en la implementación técnica de la clase `Vector` (donde los componentes se almacenan en una tupla, según el *Source Context*), implementaremos una suma dinámica que acepte tanto otros vectores como escalares.

También introduciremos la clase `Doc` para demostrar cómo el Duck Typing permite la comparación y suma de objetos de texto de forma similar a los vectores.

```pyhton
class Vector:

    def __init__(self, *components):

        # Los componentes se almacenan como tupla (Referencia: Source Ex 12)

        self.components = components

    def __repr__(self):

        return f"Vector{self.components}"

    def __add__(self, other):

        """

        Suma dinámica con Duck Typing.

        Intenta operar con .components; si falla, intenta como escalar.

        """

        try:

            # Caso 1: 'other' se comporta como un Vector (tiene .components)

            new_coords = tuple(x + y for x, y in zip(self.components, other.components))

            return Vector(*new_coords)

        except AttributeError:

            # Caso 2: 'other' se comporta como un número (escalar)

            try:

                new_coords = tuple(x + other for x in self.components)

                return Vector(*new_coords)

            except TypeError:

                return NotImplemented

    def __radd__(self, other):

        # Garantiza conmutatividad: permite 2 + Vector(1, 2)

        return self.__add__(other)

class Doc:

    def __init__(self, string):

        self.string = string

    

    def __add__(self, other):

        # Suma de documentos con espacio (Referencia: Source Ex 23)

        return Doc(self.string + ' ' + other.string)

    def __repr__(self):

        return f"Doc(string='{self.string}')"

# Pruebas de ejecución

v1 = Vector(4, 2)

v2 = Vector(-1, 3)

print(f"Suma Vectorial: {v1 + v2}")  # Vector(3, 5)

print(f"Suma Escalar: {v1 + 10}")    # Vector(14, 12)

print(f"Conmutatividad: {5 + v1}")   # Vector(9, 7)
```

La clave aquí es `NotImplemented`. Al devolverlo, Python sabe que `Vector` no sabe sumar ese objeto y le da la oportunidad al objeto de la izquierda de intentar la operación, o falla con un `TypeError` descriptivo.

## **4. Ejercicio 3 (Moderno): Protocolos Estáticos con `typing.Protocol`**

En versiones modernas (Python 3.8+), podemos formalizar estos "contratos de comportamiento" sin perder la flexibilidad del Duck Typing. Esto se conoce como **Subtipado Estructural**. A diferencia de las Clases Abstractas (ABC), que requieren herencia nominal, los `Protocols` permiten validación estática (vía MyPy) basándose únicamente en la estructura del objeto.

### **Beneficios del uso de `Protocol`**

1. **Validación sin Herencia:** Las clases no necesitan importar el protocolo; MyPy verifica el cumplimiento solo por la firma de los métodos.  
2. **Documentación Ejecutable:** Define claramente qué se espera de un objeto para los demás desarrolladores.

### **Implementación de un Protocolo `Renderable`**

```pyhton
from typing import Protocol, runtime_checkable

@runtime_checkable

class Renderable(Protocol):

    """Define el contrato estructural para objetos que pueden representarse."""

    def render(self) -> str:

        ...

class Boton:

    def render(self) -> str:

        return "[ Aceptar ]"

class Enlace:

    def render(self) -> str:

        return "<a href='#'>Click aquí</a>"

def imprimir_componente(obj: Renderable):

    # Gracias a @runtime_checkable, podemos usar isinstance en tiempo de ejecución

    if isinstance(obj, Renderable):

        print(obj.render())

    else:

        print("El objeto no cumple con el protocolo Renderable")

# Uso dinámico y estático

imprimir_componente(Boton())

imprimir_componente(Enlace())
```

## **5. Conclusiones y Mejores Prácticas**

El polimorfismo dinámico es la columna vertebral de la elegancia de Python. Nos permite escribir código que se enfoca en la **esencia funcional** de los objetos, reduciendo la fricción arquitectónica y promoviendo la reutilización.

### **Los 3 Mandamientos del Programador Pythonic**

1. **Priorizarás el comportamiento sobre el linaje:** Diseña tus funciones para que operen sobre protocolos (lo que el objeto hace), no sobre clases específicas (lo que el objeto es).  
2. **Abrazarás la filosofía EAFP:** Confía en que los objetos cumplen el contrato y utiliza bloques `try/except` para manejar las excepciones de manera limpia, evitando el exceso de comprobaciones `isinstance()`.  
3. **Documentarás mediante Protocolos:** Para sistemas complejos, utiliza `typing.Protocol`. Esto ofrece lo mejor de ambos mundos: la libertad del Duck Typing y la seguridad del análisis estático de tipos.

La verdadera maestría en Python se alcanza cuando dejamos de forzar a los objetos a ser algo que no son, y empezamos a celebrar lo que son capaces de hacer.

