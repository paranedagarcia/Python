---
id: poo
title: "Fundamentos de POO"
sidebar_label: "Fundamentos POO"
sidebar_position: 2
description: "Fundamentos del POO"
---

La programación orientada a objetos (POO) en Python es un paradigma fundamental que permite modelar entidades del mundo real mediante estructuras de datos llamadas **objetos**, los cuales agrupan tanto un estado (datos) como un comportamiento (funcionalidad). Python es un lenguaje **multiparadigma** donde todo es considerado un objeto, desde los números básicos hasta las funciones y módulos.

### Fundamentos de la POO en Python

*   **Clase (Class):** Es la "plantilla" o plano general que define los atributos y métodos comunes a una categoría de objetos. Se define con la palabra clave `class`.
*   **Objeto o Instancia:** Es una realización específica de una clase. La creación de un objeto se llama **instanciación**.
*   **Atributos:** Son variables que almacenan el estado o las características de un objeto.
*   **Métodos:** Son funciones definidas dentro de una clase que determinan qué acciones puede realizar el objeto.
*   **El método `__init__`:** Conocido como **constructor** o inicializador, es un método especial que Python ejecuta automáticamente al crear una nueva instancia para establecer sus valores iniciales.
*   **El parámetro `self`:** Es el primer argumento obligatorio en los métodos de una instancia y representa al objeto específico que está llamando al método, permitiendo acceder a sus propios atributos y otros métodos.

### Características Principales

1.  **Herencia (Inheritance):** Permite crear una nueva clase (subclase) a partir de una existente (superclase), heredando todos sus atributos y métodos. Esto facilita la reutilización de código y la especialización de funciones.
2.  **Polimorfismo:** Es la capacidad de objetos de distintas clases de responder al mismo mensaje o nombre de método. Python lo implementa principalmente a través del **Duck Typing**: "si camina como un pato y grazna como un pato, entonces es un pato", priorizando lo que el objeto puede hacer sobre su tipo estricto.
3.  **Encapsulamiento:** Se refiere a ocultar los detalles internos de un objeto y exponer solo una interfaz pública. A diferencia de otros lenguajes, Python no impone restricciones técnicas estrictas (como `private`), sino que utiliza convenciones de nombres (como un guion bajo inicial `_variable`) para indicar que un atributo es de uso interno.
4.  **Composición (Composition):** Consiste en construir clases complejas utilizando instancias de otras clases como atributos (relación "tiene un" o *has-a*).
5.  **Métodos Especiales (Dunder Methods):** Métodos que comienzan y terminan con doble guion bajo (como `__str__` o `__len__`) y permiten que los objetos se integren con la sintaxis nativa de Python, como el uso de operadores matemáticos o la función `len()`.

### Ejercicios Sugeridos por las Fuentes

Los materiales proporcionan diversos ejemplos prácticos para asentar estos conceptos:

*   **Modelado básico:** Crear una clase `Dog` con atributos `name` y `age`, y métodos como `sit()` y `roll_over()`.
*   **Gestión bancaria:** Implementar una clase `Account` que maneje depósitos, retiros y muestre el balance actual de forma controlada.
*   **Geometría:** Desarrollar clases para figuras como `Circle`, `Rectangle` o `Triangle` que incluyan métodos para calcular el área y la circunferencia basándose en sus dimensiones.
*   **Herencia aplicada:** Crear una clase `Line` (línea recta) y luego una clase `Parabola` que herede de `Line` para extender su funcionalidad matemática.
*   **Uso de `super()`:** Modificar una clase derivada para que llame explícitamente al inicializador de su clase base mediante `super().__init__()`.
*   **Refactorización:** Tomar un programa procedimental (como un simulador de crecimiento logístico o un lector de archivos CSV) y reorganizar su lógica dentro de una estructura de clases.

## Polimorfismo con 'Duck Typing' 

El **Duck Typing** (tipado de pato) es la base del polimorfismo en Python y se resume en el principio: "si camina como un pato y grazna como un pato, entonces es un pato". En este paradigma, lo que importa es **qué puede hacer un objeto** (sus métodos y comportamientos) y no qué tipo de objeto es estrictamente o de qué clase hereda.

A continuación, se presentan los ejemplos más destacados de polimorfismo mediante *Duck Typing* en Python según las fuentes:

### 1. Objetos "tipo archivo" (File-like objects)
Es el ejemplo más común y práctico de *Duck Typing*. Muchas funciones esperan un objeto sobre el cual puedan llamar a métodos como `.read()`, `.write()` o `.seek()`.
*   **Polimorfismo en acción:** No importa si el objeto es un archivo real en el disco, una cadena en memoria (`io.StringIO`), una respuesta de una red (`urllib`) o un archivo comprimido (`zipfile`).
*   **Ejemplo:** Una función que procesa XML puede aceptar cualquier objeto que tenga un método `.read()`, sin necesidad de que ese objeto herede de una clase base `File` específica.

### 2. Iterables y Contenedores
Cualquier objeto que implemente el "protocolo iterador" (métodos mágicos como `__iter__` o `__getitem__`) puede ser tratado como un iterable.
*   **Polimorfismo en acción:** Las estructuras como `for`, y funciones como `sum()`, `len()` o `max()`, funcionan con listas, tuplas, diccionarios, conjuntos e incluso archivos de texto, simplemente porque todos ellos saben cómo devolver sus elementos uno a uno cuando se les solicita.
*   **Verificación:** En lugar de comprobar si un objeto es de tipo `list`, un programador "pitónico" intentará usar `iter(obj)` y manejará la excepción si falla, permitiendo que cualquier clase personalizada actúe como una colección.

### 3. Sobrecarga de Operadores Matemáticos
Python permite que objetos de clases totalmente distintas interactúen mediante operadores estándar como `+` o `*` si implementan los métodos especiales correspondientes (como `__add__` o `__mul__`).
*   **Polimorfismo en acción:** Puedes sumar un entero con un flotante, o incluso definir que un objeto de una clase personalizada `Dice` (dados) se sume a un número entero.
*   **Ejemplo:** En una operación `a + b`, Python no verifica los tipos de forma rígida; simplemente comprueba si `a` tiene un método `__add__` que sepa manejar a `b`, o si `b` tiene un método `__radd__` para manejar a `a`.

### 4. Sistemas de Juegos y Multimedia
El *Duck Typing* permite extender diseños originales con nuevos comportamientos sin alterar la jerarquía de clases existente.
*   **Piezas de Ajedrez:** Un tablero puede llamar al método `.move()` de cualquier objeto que reciba, ya sea un `Alfil`, un `Caballo` o incluso un objeto `Coche` o `Pato` que no tenga nada que ver con el ajedrez, siempre que posea dicho método.
*   **Archivos de Audio:** Un reproductor puede procesar una clase `FlacFile` con la misma interfaz que una jerarquía de `AudioFile`, aunque la clase `FlacFile` sea independiente y no herede de la base común, siempre que tenga un método `.play()`.

### 5. El patrón "Strategy" y Callables
En Python, el patrón de diseño *Strategy* se simplifica enormemente gracias al *Duck Typing*.
*   **Polimorfismo en acción:** En lugar de crear complejas jerarquías de clases abstractas para diferentes algoritmos (como tipos de ordenamiento), Python permite pasar simplemente funciones o cualquier **objeto ejecutable** (que implemente `__call__`).
*   **Ejemplo:** Una función que requiere un algoritmo de cálculo puede recibir una función normal, una función lambda o una instancia de una clase con el método `__call__`, ya que todos se comportan de la misma manera al ser invocados.

### Formalización con Protocolos
Aunque el *Duck Typing* es dinámico por naturaleza, versiones modernas de Python permiten formalizar estas expectativas mediante `typing.Protocol`. Esto permite que herramientas como `mypy` verifiquen el polimorfismo en tiempo de desarrollo (comprobando si el objeto "camina y grazna" correctamente) sin obligar a usar herencia formal en tiempo de ejecución.


Para aplicar la herencia al crear una clase `Parabola`, se utiliza una clase base preexistente (como una clase para líneas rectas) para evitar la duplicación de código y extender su funcionalidad. Matemáticamente, una parábola definida como $y = c_0 + c_1x + c_2x^2$ puede verse como una extensión de una línea recta $y = c_0 + c_1x$, donde simplemente se añade un término cuadrático.

A continuación se detalla el proceso paso a paso según las fuentes:

### 1. Definición de la clase base
Primero se debe tener una clase base, por ejemplo, **`Line`**, que gestione los coeficientes constantes y lineales ($c_0$ y $c_1$) y proporcione métodos generales como la evaluación de la función (`__call__`) o la creación de tablas de valores (`table`).

### 2. Sintaxis de herencia
Para que la clase `Parabola` herede de `Line`, se debe incluir el nombre de la clase madre entre paréntesis en la definición de la clase hija: **`class Parabola(Line):`**. Con esto, `Parabola` adquiere automáticamente todos los atributos y métodos de `Line` de forma invisible.

### 3. El constructor (`__init__`) y el uso de `super()`
La clase `Parabola` necesita almacenar un coeficiente adicional, $c_2$. Para inicializar correctamente el objeto sin repetir el código de la clase base, el constructor de `Parabola` debe llamar al constructor de `Line`. 
*   Se puede llamar directamente usando el nombre de la clase: `Line.__init__(self, c0, c1)`.
*   La forma recomendada y más flexible es utilizar la función integrada **`super()`**, que localiza automáticamente la clase base: **`super().__init__(c0, c1)`**.
*   Tras llamar a la base, se asigna el nuevo atributo específico: `self.c2 = c2`.

### 4. Especialización de métodos
La clase `Parabola` debe "anular" o **sobrescribir** el método de evaluación para incluir el término cuadrático. Un principio importante es evitar repetir la lógica; por ello, el método `__call__` de la parábola puede llamar al de la línea para obtener la parte lineal y luego sumarle el resto:
```python
def __call__(self, x):
    return super().__call__(x) + self.c2*x**2  # Reutiliza el cálculo de c0 + c1*x
```

### 5. Ventajas del flujo de trabajo
*   **Reutilización de código:** Métodos como `table`, que genera una tabla de puntos $(x, y)$, no necesitan ser reescritos en la clase `Parabola`; se heredan tal cual de `Line` y funcionan correctamente porque internamente llaman a `self(x)`, que en una instancia de parábola ejecutará la versión cuadrática.
*   **Polimorfismo:** Un objeto de tipo `Parabola` es reconocido por Python también como una instancia de `Line` (usando `isinstance(p, Line)`), lo que permite que cualquier parte del programa que espere una línea pueda trabajar con una parábola sin notar la diferencia.

En resumen, la herencia permite que la clase `Parabola` sea mucho más pequeña y fácil de mantener, ya que solo contiene el código que la hace diferente de una línea recta.

