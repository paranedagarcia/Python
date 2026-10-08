A continuación tienes **5 ejercicios progresivos de composición en Python**, pensados para estudiantes que ya conocen clases, atributos, métodos y creación de objetos, pero que todavía están comenzando con POO.

La idea central que se practica en todos es:

> **Composición:** una clase contiene objetos de otra clase y los utiliza para cumplir su responsabilidad.
> Se puede pensar como una relación **“tiene un” (has-a)**.

Por ejemplo:

```text
Computador
 ├── Procesador
 └── Memoria
```

Un `Computador` **tiene un** `Procesador` y **tiene una** `Memoria`.

---

# Ejemplo 1: Una casa tiene habitaciones

### Nivel: ⭐ Básico

### Objetivo

Comprender la idea más simple de composición: una clase `Casa` contiene objetos de la clase `Habitacion`.

### Enunciado

Crea un programa que modele una casa.

Cada habitación debe tener:

* un nombre, por ejemplo `"Dormitorio"`
* una superficie en metros cuadrados.

La clase `Casa` debe:

* tener una dirección;
* contener varias habitaciones;
* permitir agregar habitaciones;
* mostrar las habitaciones de la casa;
* calcular la superficie total.

El programa debe crear una casa y agregar tres habitaciones.

### Código

```python
class Habitacion:
    def __init__(self, nombre, superficie):
        self.nombre = nombre
        self.superficie = superficie

    def mostrar(self):
        print(f"{self.nombre}: {self.superficie} m²")


class Casa:
    def __init__(self, direccion):
        self.direccion = direccion
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        print(f"Casa ubicada en: {self.direccion}")

        for habitacion in self.habitaciones:
            habitacion.mostrar()

    def superficie_total(self):
        total = 0

        for habitacion in self.habitaciones:
            total += habitacion.superficie

        return total


# Crear habitaciones
dormitorio = Habitacion("Dormitorio", 15)
cocina = Habitacion("Cocina", 12)
living = Habitacion("Living", 25)

# Crear casa
casa = Casa("Av. Los Pinos 123")

# Agregar habitaciones
casa.agregar_habitacion(dormitorio)
casa.agregar_habitacion(cocina)
casa.agregar_habitacion(living)

# Mostrar información
casa.mostrar_habitaciones()

print(f"Superficie total: {casa.superficie_total()} m²")
```

### ¿Dónde está la composición?

En esta línea:

```python
self.habitaciones = []
```

La clase `Casa` mantiene una colección de objetos `Habitacion`.

Posteriormente:

```python
casa.agregar_habitacion(dormitorio)
```

hace que un objeto `Casa` contenga un objeto `Habitacion`.

### Concepto que debe aprender el alumno

```text
Casa
 ├── Habitacion
 ├── Habitacion
 └── Habitacion
```

La clase `Casa` **usa y contiene objetos de otra clase**.

---

# Ejemplo 2: Un automóvil tiene un motor

### Nivel: ⭐⭐ Básico

### Objetivo

Introducir una composición más directa: un objeto es creado **dentro de otro objeto**.

### Enunciado

Crea un programa para representar un automóvil.

El automóvil debe tener:

* marca;
* modelo;
* un motor.

El motor debe tener:

* tipo de combustible;
* potencia.

La clase `Automovil` debe tener métodos para:

* mostrar sus características;
* arrancar el motor.

El motor debe tener un método `arrancar()`.

### Código

```python
class Motor:
    def __init__(self, combustible, potencia):
        self.combustible = combustible
        self.potencia = potencia

    def arrancar(self):
        print("El motor está funcionando.")


class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

        # Composición
        self.motor = Motor("Gasolina", 120)

    def mostrar(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Combustible: {self.motor.combustible}")
        print(f"Potencia: {self.motor.potencia} HP")

    def arrancar(self):
        print(f"El automóvil {self.marca} {self.modelo} está arrancando.")
        self.motor.arrancar()


# Crear automóvil
auto = Automovil("Toyota", "Yaris")

# Mostrar información
auto.mostrar()

print()

# Arrancar automóvil
auto.arrancar()
```

### ¿Qué está ocurriendo?

Cuando hacemos:

```python
auto = Automovil("Toyota", "Yaris")
```

el constructor de `Automovil` ejecuta:

```python
self.motor = Motor("Gasolina", 120)
```

Por lo tanto, el automóvil crea y contiene su propio motor.

La estructura conceptual es:

```text
Automovil
   │
   └── Motor
```

### Una característica importante

El usuario del programa **no necesita crear directamente el motor**:

```python
auto = Automovil("Toyota", "Yaris")
```

El automóvil se encarga de construirlo.

Esto permite mostrar una forma muy intuitiva de composición:

> Un automóvil **está compuesto por** un motor.

---

# Ejemplo 3: Un computador tiene procesador y memoria

### Nivel: ⭐⭐ Básico-intermedio

### Objetivo

Aprender que una clase puede estar compuesta por **varios objetos de diferentes clases**.

### Enunciado

Desarrolla un programa que represente un computador.

Debe existir una clase `Procesador` con:

* marca;
* modelo.

Debe existir una clase `Memoria` con:

* capacidad en GB.

La clase `Computador` debe tener:

* marca;
* procesador;
* memoria.

Debe permitir:

* mostrar las características;
* encender el computador.

### Código

```python
class Procesador:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar(self):
        print(f"Procesador: {self.marca} {self.modelo}")


class Memoria:
    def __init__(self, capacidad):
        self.capacidad = capacidad

    def mostrar(self):
        print(f"Memoria RAM: {self.capacidad} GB")


class Computador:
    def __init__(self, marca, procesador, memoria):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria

    def mostrar(self):
        print(f"Computador: {self.marca}")
        self.procesador.mostrar()
        self.memoria.mostrar()

    def encender(self):
        print("El computador se está encendiendo...")
        print("Sistema iniciado.")


# Crear componentes
procesador = Procesador("Intel", "Core i5")
memoria = Memoria(16)

# Crear computador
computador = Computador(
    "Dell",
    procesador,
    memoria
)

# Mostrar información
computador.mostrar()

print()

# Encender
computador.encender()
```

### ¿Dónde está la composición?

Aquí:

```python
class Computador:
    def __init__(self, marca, procesador, memoria):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
```

El objeto `Computador` contiene:

```text
Computador
 ├── Procesador
 └── Memoria
```

Una característica interesante es que los componentes se crean antes:

```python
procesador = Procesador("Intel", "Core i5")
memoria = Memoria(16)
```

y luego se entregan al computador:

```python
computador = Computador(
    "Dell",
    procesador,
    memoria
)
```

Esto permite introducir una idea importante:

> La composición no significa necesariamente que el objeto componente deba ser creado dentro del constructor de la clase principal.

---

# Ejemplo 4: Una biblioteca contiene libros

### Nivel: ⭐⭐⭐ Intermedio

### Objetivo

Practicar composición utilizando **listas de objetos** y métodos que trabajan sobre esos objetos.

### Enunciado

Desarrolla un sistema simple para administrar una biblioteca.

Cada `Libro` debe tener:

* título;
* autor;
* año de publicación.

La clase `Biblioteca` debe:

* tener un nombre;
* contener una lista de libros;
* permitir agregar libros;
* mostrar todos los libros;
* buscar libros por autor.

El programa debe crear una biblioteca y agregar al menos cuatro libros.

### Código

```python
class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar(self):
        print(
            f"{self.titulo} - "
            f"{self.autor} - "
            f"{self.anio}"
        )


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        print(f"Biblioteca: {self.nombre}")
        print("Libros disponibles:")

        for libro in self.libros:
            libro.mostrar()

    def buscar_por_autor(self, autor):
        print(f"\nLibros de {autor}:")

        for libro in self.libros:
            if libro.autor == autor:
                libro.mostrar()


# Crear libros
libro1 = Libro(
    "Cien años de soledad",
    "Gabriel García Márquez",
    1967
)

libro2 = Libro(
    "El amor en los tiempos del cólera",
    "Gabriel García Márquez",
    1985
)

libro3 = Libro(
    "1984",
    "George Orwell",
    1949
)

libro4 = Libro(
    "Rebelión en la granja",
    "George Orwell",
    1945
)

# Crear biblioteca
biblioteca = Biblioteca("Biblioteca Central")

# Agregar libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)

# Mostrar libros
biblioteca.mostrar_libros()

# Buscar por autor
biblioteca.buscar_por_autor("George Orwell")
```

### ¿Qué aprende aquí el estudiante?

La clase:

```python
Biblioteca
```

contiene una colección:

```python
self.libros = []
```

y esa colección contiene objetos:

```python
Libro
```

Visualmente:

```text
Biblioteca
    │
    ├── Libro
    ├── Libro
    ├── Libro
    └── Libro
```

Esto es especialmente importante porque permite pasar desde una composición simple:

```text
Automovil → Motor
```

a una composición:

```text
Biblioteca → muchos Libro
```

---

# Ejemplo 5: Un pedido tiene productos

### Nivel: ⭐⭐⭐ Intermedio

### Objetivo

Integrar composición, listas, métodos y cálculo de información.

Este ejercicio puede ser muy útil para que los alumnos comprendan una aplicación cercana a sistemas informáticos reales.

### Enunciado

Desarrolla un pequeño sistema para representar un pedido de una tienda.

Debe existir una clase `Producto` con:

* nombre;
* precio.

Debe existir una clase `Pedido` con:

* número de pedido;
* cliente;
* lista de productos.

El pedido debe permitir:

1. agregar productos;
2. mostrar los productos;
3. calcular el total;
4. mostrar un resumen del pedido.

### Código

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f"{self.nombre}: ${self.precio}")


class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0

        for producto in self.productos:
            total += producto.precio

        return total

    def mostrar(self):
        print("===== PEDIDO =====")
        print(f"Número: {self.numero}")
        print(f"Cliente: {self.cliente}")
        print("\nProductos:")

        for producto in self.productos:
            producto.mostrar()

        print("------------------")
        print(f"Total: ${self.calcular_total()}")


# Crear productos
producto1 = Producto("Teclado", 25000)
producto2 = Producto("Mouse", 15000)
producto3 = Producto("Audífonos", 30000)

# Crear pedido
pedido = Pedido(1001, "Juan Pérez")

# Agregar productos
pedido.agregar_producto(producto1)
pedido.agregar_producto(producto2)
pedido.agregar_producto(producto3)

# Mostrar pedido
pedido.mostrar()
```

### Resultado esperado

Conceptualmente:

```text
===== PEDIDO =====
Número: 1001
Cliente: Juan Pérez

Productos:
Teclado: $25000
Mouse: $15000
Audífonos: $30000
------------------
Total: $70000
```

### ¿Dónde está la composición?

El objeto:

```python
pedido
```

contiene:

```python
self.productos
```

que es una lista de objetos `Producto`.

Por lo tanto:

```text
Pedido
 ├── Producto
 ├── Producto
 └── Producto
```

El método:

```python
def calcular_total(self):
```

también demuestra una ventaja importante de la POO: el `Pedido` sabe cómo trabajar con los objetos `Producto` que contiene.

---

# Progresión didáctica

Los cinco ejercicios pueden utilizarse como una pequeña secuencia de aprendizaje:

| Ejercicio     | Composición                         | Concepto principal              |
| ------------- | ----------------------------------- | ------------------------------- |
| 1. Casa       | `Casa → Habitacion`                 | Lista de objetos                |
| 2. Automóvil  | `Automovil → Motor`                 | Objeto contenido                |
| 3. Computador | `Computador → Procesador + Memoria` | Varios componentes              |
| 4. Biblioteca | `Biblioteca → Libro*`               | Colección de objetos            |
| 5. Pedido     | `Pedido → Producto*`                | Composición + lógica de negocio |

La progresión sería:

```text
Objeto
   ↓
Objeto que contiene otro objeto
   ↓
Objeto que contiene varios objetos
   ↓
Objeto que contiene una colección
   ↓
Objeto que utiliza sus componentes para realizar operaciones
```

## Una distinción conceptual importante para los alumnos

Conviene introducir desde el principio la pregunta:

> **¿Qué relación existe entre las clases?**

Por ejemplo:

```text
Automóvil ───── tiene un ───── Motor
Computador ──── tiene un ───── Procesador
Biblioteca ──── tiene muchos ─ Libro
Pedido ──────── tiene muchos ─ Producto
```

Esto ayuda a diferenciar **composición** de **herencia**.

### Composición

```python
class Automovil:
    def __init__(self):
        self.motor = Motor()
```

Se expresa como:

**Automóvil tiene un Motor.**

### Herencia

```python
class Vehiculo:
    pass


class Automovil(Vehiculo):
    pass
```

Se expresa como:

**Automóvil es un Vehículo.**

Una regla sencilla para principiantes es:

> **“Es un” → pensar en herencia.**
> **“Tiene un / contiene un” → pensar en composición.**

Esta distinción constituye una muy buena base para posteriormente introducir **agregación, composición fuerte, encapsulamiento y principios SOLID**.
