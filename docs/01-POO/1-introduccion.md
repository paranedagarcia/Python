---
id: poo
title: "Fundamentos de POO"
sidebar_label: "Fundamentos"
sidebar_position: 1
description: "Fundamentos del POO"
---

<center>
![](img/poo.png)
</center>

La programación orientada a objetos (POO) es un paradigma fundamental que permite modelar entidades del mundo real mediante estructuras de datos llamadas **objetos**, los cuales agrupan tanto un estado (datos) como un comportamiento (funcionalidad). Python es un lenguaje **multiparadigma** donde todo es considerado un objeto, desde los números básicos hasta las funciones y módulos.

La Programación Orientada a Objetos te permite crear código más organizado, reutilizable y fácil de mantener, modelando el mundo real con clases y objetos. Aunque suena técnico, en el fondo es como construir con bloques de LEGO: defines piezas (clases) y luego las ensamblas (objetos) para crear algo funcional.

![](img/poo-info.webp)

La **Programación Orientada a Objetos (POO)** es una forma de organizar el código pensando en **objetos del mundo real**. En lugar de escribir instrucciones sueltas, creamos "plantillas" (llamadas **clases**) que definen cómo son y cómo se comportan esos objetos.

**Ejemplo cotidiano**:  
Piensa en un **auto**. Todos los autos tienen características (color, marca, velocidad) y pueden hacer cosas (acelerar, frenar). En POO, modelamos eso con clases y objetos.

<center>
![](img/poo-objeto.jpg)
</center>

## **Clases y objetos**
- **Clase**: Es como un **molde** o **receta** para crear objetos. Define qué atributos y comportamientos tendrán.
- **Objeto**: Es una **instancia** de una clase. Es decir, un objeto real creado a partir de esa receta.

```python showLineNumbers
# Definimos una clase llamada "Perro"
class Perro:
    pass

# Creamos un objeto (instancia) de la clase Perro
mi_perro = Perro()

# Aquí, `Perro` es la clase (el molde), y `mi_perro` es un objeto real basado en ese molde.
```

### Fundamentos de la POO

*   **Clase (Class):** Es la "plantilla" o plano general que define los atributos y métodos comunes a una categoría de objetos. Se define con la palabra clave `class`.

*   **Objeto o Instancia:** Es una realización específica de una clase. La creación de un objeto se llama **instanciación**.

*   **Atributos:** Son variables que almacenan el estado o las características de un objeto.

*   **Métodos:** Son funciones definidas dentro de una clase que determinan qué acciones puede realizar el objeto.

*   **El método `__init__`:** Conocido como **constructor** o inicializador, es un método especial que Python ejecuta automáticamente al crear una nueva instancia para establecer sus valores iniciales.

*   **El parámetro `self`:** Es el primer argumento obligatorio en los métodos de una instancia y representa al objeto específico que está llamando al método, permitiendo acceder a sus propios atributos y otros métodos.

Las clases se definen con la palabra clave `class` seguida con el nombre de la clase, dos puntos `:` y luego el cuerpo de la clase con todas sus definiciones. Incluya siempre un cadena de texto docstring """ para documentar la clase.

```python title="clase" showLineNumbers
class Auto:
    “””Abstraccion de los objetos auto.”””
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print “Tenemos”, gasolina, “litros”
    
    def arrancar(self):
        if self.gasolina > 0:
            print “Arranca”
        else:
            print “No arranca”

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
        print “Quedan”, self.gasolina, “litros”
            else:
        print “No se mueve”
 ```

## **Constructores**
El **constructor** es un método especial que se ejecuta **automáticamente** cuando creamos un nuevo objeto. En Python, se llama `__init__`.

```python showLineNumbers
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

# Creamos un perro con nombre y raza
mi_perro = Perro("Firulais", "Labrador")
print(mi_perro.nombre)  # Imprime: Firulais
```
El constructor permite **inicializar** los atributos del objeto al crearlo.

El primer método `__init__` es relevante porque es la instanciación inicial, realiza todo el proceso de inicialización que sea necesario.
El primer parámetro de este es `self`y que se refiere al objeto actual y permite acceder a todos los atributos y métodos del objeto.

### Función isinstance()
Esta función nos dice si un objeto **es una instancia** de una clase determinada.

```python
print(isinstance(mi_perro, Perro))   # True
print(isinstance(mi_perro, str))    # False
```


### Características Principales

1.  **Herencia (Inheritance):** Permite crear una nueva clase (subclase) a partir de una existente (superclase), heredando todos sus atributos y métodos. Esto facilita la reutilización de código y la especialización de funciones.

<center>
<figure>
![](img/poo-herencia.jpg)
<figcaption>**Herencia**. Las clases 'hijas' heredan los atributos y métodos del 'padre', pero añaden sus propios detalles exclusivos.</figcaption>
</figure>
</center>

2.  **Polimorfismo:** Es la capacidad de objetos de distintas clases de responder al mismo mensaje o nombre de método. Python lo implementa principalmente a través del **Duck Typing**: "si camina como un pato y grazna como un pato, entonces es un pato", priorizando lo que el objeto puede hacer sobre su tipo estricto.

3.  **Encapsulamiento:** Se refiere a ocultar los detalles internos de un objeto y exponer solo una interfaz pública. A diferencia de otros lenguajes, Python no impone restricciones técnicas estrictas (como `private`), sino que utiliza convenciones de nombres (como un guion bajo inicial `_variable`) para indicar que un atributo es de uso interno.

<center>
<figure>
![](img/poo-capsula.jpg)
<figcaption>**Encapsulamiento**. Oculta el estado interno. El acceso o modificación a lod datps privados (__saldo) solo se permite a través de métodos controlados (Getters/Setters). Esto evita accidentes.</figcaption>
</figure>
</center>

4. **Abstracción**: Consiste en el proceso de **separar una interfaz pública limpia de los detalles internos de implementación** de un objeto, permitiendo interactuar con el código al nivel de detalle más adecuado para cada tarea y omitiendo las complejidades que no son relevantes.

<center>
<figure>
![](img/poo-control.jpg)
<figcaption>**Abstracción**. Al igual que el control remoto, los objetos POO exponen métodos simples y esconden el código dificil.</figcaption>
</figure>
</center>

5.  **Composición (Composition):** Consiste en construir clases complejas utilizando instancias de otras clases como atributos (relación "tiene un" o *has-a*).

5.  **Métodos Especiales (Dunder Methods):** Métodos que comienzan y terminan con doble guion bajo (como `__str__` o `__len__`) y permiten que los objetos se integren con la sintaxis nativa de Python, como el uso de operadores matemáticos o la función `len()`.

### Ejercicios

Los ejemplos prácticos para asentar estos conceptos serían:
<br />
#### 💻 Código:
<Tabs>
<TabItem value="mnp" label="Antecedentes" default>
<div class="alert alert--primary">
**Modelado básico:** 
Crear una clase `Dog` con atributos `name` y `age`, y métodos como `sit()` y `roll_over()`.
</div>
</TabItem>
<TabItem value="mnp-python" label="Pyhton" >
```python showLineNumbers
# Implementación en Python
```
</TabItem>
</Tabs>


#### 💻 Código:
<Tabs>
<TabItem value="mnp" label="Antecedentes" default>
<div class="alert alert--primary">
**Gestión bancaria:** <br /> 
Implementar una clase `Account` que maneje depósitos, retiros y muestre el balance actual de forma controlada.

Concepto clave: Encapsulamiento.

En Python, podemos proteger los atributos internos (como el saldo) usando un doble guion bajo (__), lo que restringe el acceso directo desde fuera de la clase. De este modo, cualquier modificación o consulta del saldo debe pasar obligatoriamente por filtros de validación (métodos).

**Conceptos de POO aplicados en este ejemplo:**

1. **Atributos Privado**s (__balance): Al anteponer __, Python aplica una característica llamada Name Mangling (deformación del nombre). Esto impide que un desarrollador o un agente externo haga cosas como cuenta.__balance = 99999 desde fuera del objeto, forzando el uso seguro del software.

2. **Encapsulamiento y Métodos de Control**: El saldo solo se puede alterar mediante operaciones de negocio predefinidas y seguras (deposit y withdraw). Ambos métodos actúan como "guardias de seguridad" validando que las reglas del banco se cumplan (no dinero negativo, no sobregiros sin autorización).

3. **Métodos de Acceso (Getters)**: El método get_balance() proporciona una interfaz de "solo lectura" para conocer el saldo, separando la visualización de datos de la lógica de modificación.
</div>
</TabItem>
<TabItem value="mnp-python" label="Pyhton" >

```python showLineNumbers
# Implementación en Python
class Account:
    """Clase que representa una cuenta bancaria con saldo protegido (Encapsulamiento)."""

    def __init__(self, owner, initial_balance=0.0):
        self.owner = owner
        # Atributo privado utilizando doble guion bajo
        if initial_balance >= 0:
            self.__balance = float(initial_balance)
        else:
            print("Advertencia: El saldo inicial no puede ser negativo. Se fijará en 0.0.")
            self.__balance = 0.0

    # Getter controlado: Permite leer el saldo sin modificarlo directamente
    def get_balance(self):
        """Devuelve el balance actual de la cuenta."""
        return self.__balance

    def deposito(self, amount):
        """Realiza un depósito controlado verificando que el monto sea positivo."""
        if amount > 0:
            self.__balance += amount
            print(f"Depósito exitoso: +${amount:.2f}")
            self.show_statement()
        else:
            print("Error: El monto a depositar debe ser mayor que cero.")

    def retiro(self, amount):
        """Realiza un retiro controlado verificando fondos y montos válidos."""
        if amount <= 0:
            print("Error: El monto a retirar debe ser mayor que cero.")
        elif amount > self.__balance:
            print(f"Error: Fondos insuficientes. Intenta retirar ${amount:.2f} pero solo tiene ${self.__balance:.2f}.")
        else:
            self.__balance -= amount
            print(f"Retiro exitoso: -${amount:.2f}")
            self.show_statement()

    def show_statement(self):
        """Muestra de forma limpia el estado actual de la cuenta."""
        print(f"Titular: {self.owner} | Saldo Actual: ${self.__balance:.2f}\n")


# --- Demostración del comportamiento controlado ---
if __name__ == "__main__":
    print("--- Creación de la Cuenta ---")
    cuenta_juan = Account(owner="Juan Pérez", initial_balance=500.0)
    cuenta_juan.show_statement()

    print("--- Prueba de Depósito Válido ---")
    cuenta_juan.deposito(150.50)

    print("--- Prueba de Depósito Inválido ---")
    cuenta_juan.deposito(-20.0)

    print("--- Prueba de Retiro Válido ---")
    cuenta_juan.retiro(200.0)

    print("--- Prueba de Retiro por Encima de los Fondos ---")
    cuenta_juan.retiro(600.0)

    print("--- Demostración de Encapsulamiento (Protección) ---")
    # Si intentamos alterar el balance directamente desde fuera, Python lanzará un error 
    # o creará una variable diferente, protegiendo el verdadero saldo interno.
    try:
        cuenta_juan.__balance = 1000000.0  # Intento malicioso de alterar el saldo
        print("Intento de hackeo directo...")
    except AttributeError:
        pass

    # Verificamos que el saldo real sigue estando a salvo
    print("Resultado tras el intento de alteración directa:")
    cuenta_juan.show_statement()
```
</TabItem>
</Tabs>
<br />

#### 💻 Código:
<Tabs>
<TabItem value="mnp" label="Antecedentes" default>
<div class="alert alert--primary">
**Geometría:** <br /> 
Desarrollar clases para figuras como `Circle`, `Rectangle` o `Triangle` que incluyan métodos para calcular el área y la circunferencia basándose en sus dimensiones.

**Conceptos de POO aplicados:**

1. **Abstracción:** Creamos la clase base `Shape` utilizando el decorador `@abstractmethod`. Esto define una interfaz obligatoria para todas las figuras, ocultando la complejidad y dictando las reglas que cada subclase debe seguir (no se puede instanciar directamente un `Shape`).
2. **Herencia:** Las clases `Circle`, `Rectangle` y `Triangle` heredan de `Shape` mediante la sintaxis `class NombreClase(Shape):`. Al hacer esto, adoptan el compromiso de implementar sus propios métodos de cálculo.
3. **Encapsulamiento:** Las dimensiones de cada figura (como `radius`, `width` o `side_a`) se agrupan de forma lógica dentro del objeto correspondiente a través del constructor `__init__`, asociando directamente los datos con los métodos que operan sobre ellos (`self`).
4. **Polimorfismo:** En el ciclo `for shape in shapes:`, ejecutamos `shape.area()` y `shape.perimeter()`. El programa no necesita saber de antemano si la figura actual es un círculo o un rectángulo; cada objeto sabe cómo resolver esa función según su propia naturaleza.

</div>
</TabItem>
<TabItem value="mnp-python" label="💻 Pyhton" default>

```python showLineNumbers
# Implementación en Python
from abc import ABC, abstractmethod
import math

# 1. Definición de la Clase Base Abstracta (Forma)
class Shape(ABC):
    """Clase abstracta que sirve de plantilla para todas las figuras geométricas."""
    
    @abstractmethod
    def area(self):
        """Calcula y devuelve el área de la figura."""
        pass
        
    @abstractmethod
    def perimeter(self):
        """Calcula y devuelve el perímetro o circunferencia de la figura."""
        pass


# 2. Clase para el Círculo (Circle)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        # En el caso del círculo, el perímetro es su circunferencia
        return 2 * math.pi * self.radius


# 3. Clase para el Rectángulo (Rectangle)
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# 4. Clase para el Triángulo (Triangle)
class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        # Utiliza la Fórmula de Herón para calcular el área con base en los 3 lados
        s = self.perimeter() / 2  # Semiperímetro
        # Evitamos errores de redondeo que puedan dar números negativos muy pequeños
        arg = s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)
        return math.sqrt(max(0, arg))


# --- Demostración del uso de las clases ---
if __name__ == "__main__":
    # Creamos una lista con instancias de diferentes figuras
    shapes = [
        Circle(radius=5),
        Rectangle(width=4, height=7),
        Triangle(side_a=3, side_b=4, side_c=5)
    ]
    
    print("Demostración de POO en Python (Figuras Geométricas):\n")
    
    # Demostramos Polimorfismo: recorremos la lista y llamamos a los mismos 
    # métodos sin importar el tipo específico de objeto.
    for shape in shapes:
        # Obtenemos el nombre de la clase dinámicamente
        class_name = shape.__class__.__name__
        
        print(f"--- {class_name} ---")
        print(f"Área:          {shape.area():.2f}")
        print(f"Perímetro/Circ: {shape.perimeter():.2f}\n")
```
</TabItem>
</Tabs>


#### 💻 Código:
<Tabs>
<TabItem value="mnp" label="Antecedentes" default>
<div class="alert alert--primary">
**Herencia aplicada:**
Crear una clase `Line` (línea recta) y luego una clase `Parabola` que herede de `Line` para extender su funcionalidad matemática.

Para aplicar el concepto de **Herencia** en un entorno matemático, podemos ver una línea recta como un caso especial o un subconjunto de una función polinómica.

La ecuación de una línea es:

```math
y = c_1 x + c_0
```

Mientras que la ecuación de una parábola (función cuadrática) añade un término de segundo grado:

```math
y = c_2 x^2 + c_1 x + c_0
```

Al hacer que `Parabola` herede de `Line`, reutilizamos la lógica de los coeficientes lineales y la extendemos agregando el coeficiente cuadrático ($c_2$).

**Conceptos de POO:**

1. **Reutilización de código vía `super()`:** En el constructor (`__init__`) de `Parabola`, llamamos a `super().__init__(c1, c0)`. Esto evita repetir la asignación de variables que la clase `Line` ya sabe hacer perfectamente.
2. **Extensión de métodos (Polimorfismo / Sobrescritura):** El método `value(x)` en `Parabola` reemplaza (sobrescribe) al de `Line`. Sin embargo, en lugar de reescribir toda la fórmula desde cero, hace un llamado a `super.value(x)` para obtener la parte lineal y le añade la parte cuadrática.
3. **Mantenibilidad:** Si el día de mañana decides cambiar la forma en que se imprimen o calculan las funciones lineales básicas, cualquier cambio en `Line` se transmitirá automáticamente a `Parabola` sin necesidad de tocar su código.
</div>
</TabItem>
<TabItem value="mnp-python" label="💻 Pyhton">

```python showLineNumbers
# Implementación en Python
class Line:
    """Representa una línea recta basada en la ecuación y = c1*x + c0."""
    
    def __init__(self, c1, c0):
        self.c1 = c1  # Pendiente o coeficiente lineal
        self.c0 = c0  # Intersección con el eje Y o término independiente

    def value(self, x):
        """Calcula y devuelve el valor de 'y' para un 'x' dado."""
        return self.c1 * x + self.c0

    def __str__(self):
        """Devuelve la representación matemática en formato texto."""
        return f"y = {self.c1}*x + {self.c0}"


# Aplicación de Herencia: Parabola extiende a Line
class Parabola(Line):
    """Representa una parábola basada en la ecuación y = c2*x^2 + c1*x + c0."""
    
    def __init__(self, c2, c1, c0):
        # Usamos super() para inicializar los atributos que ya maneja la clase padre (Line)
        super().__init__(c1, c0)
        self.c2 = c2  # Coeficiente cuadrático nuevo

    def value(self, x):
        """Calcula 'y' extendiendo el método de la clase padre."""
        # Reutilizamos el cálculo de la línea recta (c1*x + c0) usando super()
        # y simplemente le sumamos el término cuadrático nuevo.
        return self.c2 * (x ** 2) + super().value(x)

    def __str__(self):
        """Sobrescribe la representación en texto incorporando el término cuadrático."""
        return f"y = {self.c2}*x^2 + {self.c1}*x + {self.c0}"


# --- Demostración del uso de la Herencia ---
if __name__ == "__main__":
    print("--- Probando la Clase Padre (Line) ---")
    # Creamos una recta: y = 3x + 5
    recta = Line(c1=3, c0=5)
    print(f"Ecuación: {recta}")
    print(f"Si x = 2 -> y = {recta.value(2)}")    # 3*(2) + 5 = 11
    print(f"Si x = 0 -> y = {recta.value(0)}\n")   # 3*(0) + 5 = 5

    print("--- Probando la Clase Hija (Parabola) ---")
    # Creamos una parábola: y = 2x^2 + 3x + 5
    # Nota cómo reutiliza internamente los coeficientes 3 y 5
    parabola = Parabola(c2=2, c1=3, c0=5)
    print(f"Ecuación: {parabola}")
    print(f"Si x = 2 -> y = {parabola.value(2)}")    # 2*(4) + 3*(2) + 5 = 8 + 6 + 5 = 19
    print(f"Si x = 0 -> y = {parabola.value(0)}")    # 2*(0) + 3*(0) + 5 = 5
```
</TabItem>
</Tabs>
<br />




*   **Uso de `super()`:** Modificar una clase derivada para que llame explícitamente al inicializador de su clase base mediante `super().__init__()`.
*   **Refactorización:** Tomar un programa procedimental (como un simulador de crecimiento logístico o un lector de archivos CSV) y reorganizar su lógica dentro de una estructura de clases.

---
## **Method Resolution Order**

**MRO** son las siglas de **Method Resolution Order** (u **Orden de Resolución de Métodos** en español). Es el mecanismo interno que utiliza Python para determinar de manera exacta y predecible el **orden en el que se deben buscar los atributos y métodos** en una jerarquía de clases. 

Aunque su nombre hace referencia a los "métodos", el MRO se aplica para la resolución de **cualquier tipo de atributo** (como variables de clase o propiedades) y no solo para funciones.

A continuación se detallan sus aspectos clave:

### ¿Por qué es necesario?
En la herencia simple, el orden de búsqueda es directo: Python busca en la clase del objeto, luego en su padre, luego en el abuelo, y así sucesivamente. Sin embargo, bajo **herencia múltiple**, la estructura puede volverse compleja. 

El caso más crítico es la **herencia en diamante** (cuando una clase hereda de dos padres que a su vez comparten un ancestro común). Sin una regla clara, Python podría buscar atributos de forma desordenada o resolver de manera contraintuitiva. El MRO resuelve esto asegurando que **cada clase en la jerarquía se visite una sola vez, y siempre después de todas sus subclases**.

### El algoritmo C3 Linearization
A partir de la versión 2.3, Python adoptó el algoritmo **C3 linearization** para calcular este orden de búsqueda. Este algoritmo (originalmente creado para el lenguaje de programación Dylan) genera una lista plana y ordenada de ancestros garantizando propiedades fundamentales:
*   **Monotonía:** Si una clase (`A`) precede a la clase (`B`) en el orden de búsqueda de una subclase, esa relación de precedencia debe mantenerse en cualquier otra subclase más compleja que herede de ellas.
*   **Preservación del orden local:** Se respeta rigurosamente el orden de izquierda a derecha en el que se declaran las clases base en la cabecera de la subclase.

### ¿Cómo se inspecciona en Python?
Cada vez que creas una clase, Python calcula su MRO en tiempo de definición y lo almacena. Puedes consultarlo de dos formas:
*   Accediendo al atributo especial de lectura de la clase: `Clase.__mro__` (que devuelve una tupla).
*   Llamando al método de clase: `Clase.mro()` (que devuelve una lista).

```python
print(MiClase.__mro__)
# Muestra el orden exacto de búsqueda, terminando siempre en la clase base 'object'
```

### Su relación con `super()`
La función integrada **`super()` no busca necesariamente en el padre directo de la clase actual**. Lo que realmente hace `super()` es localizar la clase donde se está ejecutando la llamada dentro del MRO del objeto original (`self.__class__.__mro__`) y delegar la llamada al **siguiente elemento en esa lista**. Esto es lo que permite la **inicialización cooperativa** a través de toda la jerarquía de herencia.


<Tabs>
<TabItem value="mro" label="Ejercicio" default>
<div class="alert alert--primary">
**Script interactivo:**

Construir una jerarquía con herencia múltiple compleja y mostrar exactamente cómo cambia su lista de MRO según el orden de declaración de sus padres.

Para este experimento, definiremos una jerarquía en diamante donde cambiaremos únicamente el **orden de declaración de los padres** en la subclase. Esto nos permitirá visualizar de manera directa el impacto en el **MRO** y en la ruta que sigue **`super()`**.
</div>
</TabItem>
<TabItem value="mro-python" label="💻 Pyhton" >

```python showLineNumbers
class Ancestro:
    def mensaje(self):
        print("   [Ancestro]  Método ejecutado.")


class ServicioLog(Ancestro):
    def mensaje(self):
        print("-> [ServicioLog] Iniciando...")
        super().mensaje()
        print("<- [ServicioLog] Finalizado.")


class ServicioSeguridad(Ancestro):
    def mensaje(self):
        print("-> [ServicioSeguridad] Verificando credenciales...")
        super().mensaje()
        print("<- [ServicioSeguridad] Verificación terminada.")


# =====================================================================
# EXPERIMENTO 1: ServicioLog va a la IZQUIERDA (tiene prioridad)
# =====================================================================
class GestorA(ServicioLog, ServicioSeguridad):
    def mensaje(self):
        print("\n=== EJECUTANDO GESTOR A (Log -> Seguridad) ===")
        super().mensaje()


# =====================================================================
# EXPERIMENTO 2: ServicioSeguridad va a la IZQUIERDA (tiene prioridad)
# =====================================================================
class GestorB(ServicioSeguridad, ServicioLog):
    def mensaje(self):
        print("\n=== EJECUTANDO GESTOR B (Seguridad -> Log) ===")
        super().mensaje()


# --- Bloque de ejecución e inspección del MRO ---
if __name__ == "__main__":
    # 1. Mostramos los MRO calculados por Python
    print("MRO de GestorA:")
    for i, clase in enumerate(GestorA.mro(), start=1):
        print(f"  {i}. {clase.__name__}")
        
    print("\nMRO de GestorB:")
    for i, clase in enumerate(GestorB.mro(), start=1):
        print(f"  {i}. {clase.__name__}")

    # 2. Ejecutamos los métodos para ver el orden de las llamadas
    obj_a = GestorA()
    obj_a.mensaje()

    obj_b = GestorB()
    obj_b.mensaje()
```
</TabItem>
<TabItem value="mro-res" label="Resultado" >
Cuando corras el script, la salida en tu terminal será exactamente esta:

```text
MRO de GestorA:
  1. GestorA
  2. ServicioLog
  3. ServicioSeguridad
  4. Ancestro
  5. object

MRO de GestorB:
  1. GestorB
  2. ServicioSeguridad
  3. ServicioLog
  4. Ancestro
  5. object

=== EJECUTANDO GESTOR A (Log -> Seguridad) ===
-> [ServicioLog] Iniciando...
-> [ServicioSeguridad] Verificando credenciales...
   [Ancestro]  Método ejecutado.
<- [ServicioSeguridad] Verificación terminada.
<- [ServicioLog] Finalizado.

=== EJECUTANDO GESTOR B (Seguridad -> Log) ===
-> [ServicioSeguridad] Verificando credenciales...
-> [ServicioLog] Iniciando...
   [Ancestro]  Método ejecutado.
<- [ServicioLog] Finalizado.
<- [ServicioSeguridad] Verificación terminada.
```
</TabItem>
</Tabs>
<br/>

### Tres observaciones clave

1.  **Prioridad de izquierda a derecha:** Python respeta estrictamente el orden en que declaras las clases base en la cabecera. En `GestorA(ServicioLog, ServicioSeguridad)`, el primer paso de búsqueda tras el propio gestor es `ServicioLog`. En `GestorB`, la prioridad se invierte.

2.  **`super()` como un hilo continuo:** Observa el comportamiento en `GestorA`. Cuando `ServicioLog.mensaje()` llama a `super().mensaje()`, el flujo no sube directamente a su padre `Ancestro`. En su lugar, el MRO del objeto le dice: *"el siguiente en la lista es tu hermano, ServicioSeguridad"*. De esta manera, el flujo "zigzaguea" de forma segura por todas las ramas del diamante antes de tocar el ancestro común.

3.  **El desenrollado de la pila:** Debido a que cada método ejecuta código *antes* y *después* de su llamada a `super()`, verás que el orden de entrada a los métodos es exactamente el inverso al orden de salida. Esto permite realizar operaciones de limpieza (como cerrar archivos o liberar transacciones de bases de datos) en el orden inverso en el que se abrieron.

