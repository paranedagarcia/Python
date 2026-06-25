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

    def deposit(self, amount):
        """Realiza un depósito controlado verificando que el monto sea positivo."""
        if amount > 0:
            self.__balance += amount
            print(f"Depósito exitoso: +${amount:.2f}")
            self.show_statement()
        else:
            print("Error: El monto a depositar debe ser mayor que cero.")

    def withdraw(self, amount):
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
    cuenta_juan.deposit(150.50)

    print("--- Prueba de Depósito Inválido ---")
    cuenta_juan.deposit(-20.0)

    print("--- Prueba de Retiro Válido ---")
    cuenta_juan.withdraw(200.0)

    print("--- Prueba de Retiro por Encima de los Fondos ---")
    cuenta_juan.withdraw(600.0)

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

**Conceptos de POO aplicados en este programa:**

1. **Abstracción:** Creamos la clase base `Shape` utilizando el decorador `@abstractmethod`. Esto define una interfaz obligatoria para todas las figuras, ocultando la complejidad y dictando las reglas que cada subclase debe seguir (no se puede instanciar directamente un `Shape`).
2. **Herencia:** Las clases `Circle`, `Rectangle` y `Triangle` heredan de `Shape` mediante la sintaxis `class NombreClase(Shape):`. Al hacer esto, adoptan el compromiso de implementar sus propios métodos de cálculo.
3. **Encapsulamiento:** Las dimensiones de cada figura (como `radius`, `width` o `side_a`) se agrupan de forma lógica dentro del objeto correspondiente a través del constructor `__init__`, asociando directamente los datos con los métodos que operan sobre ellos (`self`).
4. **Polimorfismo:** En el ciclo `for shape in shapes:`, ejecutamos `shape.area()` y `shape.perimeter()`. El programa no necesita saber de antemano si la figura actual es un círculo o un rectángulo; cada objeto sabe cómo resolver esa función según su propia naturaleza.

</div>
</TabItem>
<TabItem value="mnp-python" label="Pyhton" default>
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
<TabItem value="mnp-python" label="Pyhton">
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

