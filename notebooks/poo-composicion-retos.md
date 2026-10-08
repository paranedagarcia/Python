Aquí tienes 3 retos prácticos adicionales pensados para evaluar la comprensión de la composición en alumnos principiantes. Las consignas plantean requisitos funcionales claros y las soluciones completas están al final para facilitar la corrección.

---

### Reto 1: Jugador y Arma (Videojuego básico)

**Consigna:**

Diseña un sistema para un juego por turnos:

1. Crea una clase `Arma` con los atributos `nombre` y `danio`. Debe tener un método `atacar()` que devuelva el string: `f"{self.nombre} causa {self.danio} puntos de daño."`.
2. Crea una clase `Guerrero` con los atributos `nombre` y `puntos_vida`. Un guerrero se crea sin arma (`self.arma = None`).
3. Agrega al `Guerrero` los métodos:
* `equipar_arma(arma)`: asigna un objeto `Arma` al guerrero.
* `realizar_ataque()`: si tiene un arma equipada, imprime `f"{self.nombre} ataca: "` seguido del resultado de `arma.atacar()`. Si no tiene arma, imprime `f"{self.nombre} ataca con los puños (1 punto de daño)."`.



---

### Reto 2: Biblioteca y Libros (Colección de objetos)

**Consigna:**

Modela el catálogo de una biblioteca pequeña:

1. Crea una clase `Libro` con los atributos `titulo` y `autor`. Agrega un método `descripcion()` que retorne: `f"'{self.titulo}' por {self.autor}"`.
2. Crea una clase `Biblioteca` con un nombre y una lista vacía para almacenar libros.
3. Agrega a `Biblioteca` los métodos:
* `agregar_libro(libro)`: añade una instancia de `Libro` a la lista interna.
* `mostrar_catalogo()`: recorre la lista e imprime cada libro usando el método `descripcion()` de cada uno. Si la lista está vacía, debe avisar que no hay libros registrados.



---

### Reto 3: Factura e Ítems con Cantidad (Cálculo acumulativo)

**Consigna:**

Modela la emisión de un comprobante de venta simple:

1. Crea una clase `ItemFactura` con los atributos `descripcion`, `precio_unitario` y `cantidad`. Debe tener un método `calcular_subtotal()` que retorne el total del ítem (`precio_unitario * cantidad`).
2. Crea una clase `Factura` con el atributo `numero_factura` y una lista de ítems.
3. Agrega a `Factura` los métodos:
* `agregar_item(descripcion, precio_unitario, cantidad)`: crea la instancia de `ItemFactura` dentro del método y la añade a la lista interna.
* `calcular_total()`: suma los subtotales de todos los ítems de la lista.
* `imprimir_resumen()`: muestra el número de factura, el desglose de cada ítem (descripción, cantidad y subtotal) y el total final.



---

### Soluciones de Referencia

#### Solución Reto 1

```python
class Arma:
    def __init__(self, nombre, danio):
        self.nombre = nombre
        self.danio = danio

    def atacar(self):
        return f"{self.nombre} causa {self.danio} puntos de daño."


class Guerrero:
    def __init__(self, nombre, puntos_vida):
        self.nombre = nombre
        self.puntos_vida = puntos_vida
        self.arma = None  # Composición opcional / agregación

    def equipar_arma(self, arma):
        self.arma = arma
        print(f"{self.nombre} equipó {arma.nombre}.")

    def realizar_ataque(self):
        if self.arma:
            print(f"{self.nombre} ataca: {self.arma.atacar()}")
        else:
            print(f"{self.nombre} ataca con los puños (1 punto de daño).")


# Prueba
heroe = Guerrero("Conan", 100)
heroe.realizar_ataque()

espada = Arma("Espada Vorpal", 35)
heroe.equipar_arma(espada)
heroe.realizar_ataque()

```

---

#### Solución Reto 2

```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descripcion(self):
        return f"'{self.titulo}' por {self.autor}"


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def mostrar_catalogo(self):
        print(f"--- Catálogo de {self.nombre} ---")
        if not self.catalogo:
            print("No hay libros registrados.")
            return

        for libro in self.catalogo:
            print(f"- {libro.descripcion()}")


# Prueba
biblio = Biblioteca("Biblioteca Central")
b1 = Libro("Cien años de soledad", "Gabriel García Márquez")
b2 = Libro("Ficciones", "Jorge Luis Borges")

biblio.agregar_libro(b1)
biblio.agregar_libro(b2)
biblio.mostrar_catalogo()

```

---

#### Solución Reto 3

```python
class ItemFactura:
    def __init__(self, descripcion, precio_unitario, cantidad):
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.precio_unitario * self.cantidad


class Factura:
    def __init__(self, numero_factura):
        self.numero_factura = numero_factura
        self.items = []

    def agregar_item(self, descripcion, precio_unitario, cantidad):
        # Composición directa: Factura instancia y gestiona el ciclo de vida del Item
        nuevo_item = ItemFactura(descripcion, precio_unitario, cantidad)
        self.items.append(nuevo_item)

    def calcular_total(self):
        return sum(item.calcular_subtotal() for item in self.items)

    def imprimir_resumen(self):
        print(f"Factura N°: {self.numero_factura}")
        print("-" * 35)
        for item in self.items:
            subtotal = item.calcular_subtotal()
            print(f"{item.descripcion} x{item.cantidad}: ${subtotal:.2f}")
        print("-" * 35)
        print(f"Total: ${self.calcular_total():.2f}")


# Prueba
factura = Factura("FAC-001")
factura.agregar_item("Teclado Mecánico", 45.0, 1)
factura.agregar_item("Cable USB-C", 5.5, 2)
factura.imprimir_resumen()

```