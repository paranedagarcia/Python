Para los estudiantes que se están iniciando en el paradigma de la Programación Orientada a Objetos (POO), es fundamental entender la analogía de que una **clase** es como un plano de construcción o molde, una **instancia** es el objeto real construido con ese molde, y un **método** es una acción o comportamiento que ese objeto puede realizar.

A continuación, se presentan **3 ejemplos progresivos y muy sencillos**, diseñados específicamente para asentar estos conceptos básicos sin abrumar con sintaxis compleja:

---

### Ejercicio 1: El Objeto Perro (El clásico del mundo real)
*   **Enunciado:** Imagina que vas a diseñar un sistema para una clínica veterinaria. Necesitas crear un "molde" (clase) para representar perros. Cada perro individual debe tener un **nombre** y una **raza** (atributos). Además, todos los perros deben ser capaces de realizar una acción: **ladrar** (un método que muestre un mensaje en pantalla indicando su nombre y un "¡Guau!").
*   **Conceptos a observar:** Cómo el inicializador `__init__` recibe los datos iniciales y cómo la variable `self` hace referencia al perro en específico que está realizando la acción.

#### Solución en Python:
```python
# 1. Definición de la CLASE (El molde)
class Perro:
    # El método especial __init__ (constructor) define qué datos necesita cada perro al nacer
    def __init__(self, nombre, raza):
        self.nombre = nombre  # Atributo
        self.raza = raza      # Atributo

    # Definición de un MÉTODO (La acción que el objeto puede realizar)
    def ladrar(self):
        # Usamos 'self.nombre' para referirnos al nombre del perro específico que ladra
        print(f"{self.nombre} ({self.raza}) dice: ¡Guau, guau!")


# 2. Creación de las INSTANCIAS (Los objetos reales creados con el molde)
perro_uno = Perro("Fido", "Labrador")
perro_dos = Perro("Toby", "Pug")

# 3. Llamada a los MÉTODOS (Ejecución de las acciones de cada objeto)
perro_uno.ladrar()  # Salida: Fido (Labrador) dice: ¡Guau, guau!
perro_dos.ladrar()  # Salida: Toby (Pug) dice: ¡Guau, guau!
```

---

### Ejercicio 2: La Alcancía Digital (Manipulación de estados)
*   **Enunciado:** Diseña una clase llamada `Alcancia` que permita a los niños aprender a ahorrar de forma digital. Cada alcancía debe comenzar vacía (con un **saldo** inicial de `0`). Debe tener un método para **guardar_dinero** (añadiendo una cantidad al saldo) y otro método llamado **ver_saldo** que muestre en pantalla cuánto dinero lleva acumulado el objeto en ese momento.
*   **Conceptos a observar:** Cómo los métodos pueden modificar directamente el valor de los atributos internos de un objeto a lo largo del tiempo.

#### Solución en Python:
```python
# 1. Definición de la CLASE
class Alcancia:
    def __init__(self):
        self.saldo = 0.0  # El atributo inicia automáticamente en cero

    # MÉTODO para modificar el estado (guardar dinero)
    def guardar_dinero(self, cantidad):
        if cantidad > 0:
            self.saldo = self.saldo + cantidad
            print(f"¡Has guardado ${cantidad}! Saldo actual: ${self.saldo}")
        else:
            print("Error: No puedes guardar cantidades negativas o vacías.")

    # MÉTODO para consultar el estado actual
    def ver_saldo(self):
        print(f"Saldo total acumulado: ${self.saldo}")


# 2. Creación de la INSTANCIA
mi_hucha = Alcancia()

# 3. Uso de los métodos de la instancia
mi_hucha.ver_saldo()          # Salida: Saldo total acumulado: $0.0
mi_hucha.guardar_dinero(50)   # Salida: ¡Has guardado $50! Saldo actual: $50.0
mi_hucha.guardar_dinero(20.5) # Salida: ¡Has guardado $20.5! Saldo actual: $70.5
mi_hucha.ver_saldo()          # Salida: Saldo total acumulado: $70.5
```

---

### Ejercicio 3: El Catálogo de Biblioteca (Formatear información)
*   **Enunciado:** Escribe un programa que ayude a organizar una biblioteca escolar. Crea una clase `Libro` donde cada ejemplar guarde su **titulo** y su **autor**. Define un método llamado `obtener_informacion` que devuelva una cadena de texto formal formateada con los datos del libro (por ejemplo: `"'Don Quijote de la Mancha', escrito por Miguel de Cervantes"`).
*   **Conceptos a observar:** Cómo un método puede procesar la información interna del objeto y **retornar** un valor de texto estructurado para que el programa principal decida cómo mostrarlo.

#### Solución en Python:
```python
# 1. Definición de la CLASE
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo  # Atributo de texto
        self.autor = autor    # Atributo de texto

    # MÉTODO que procesa y retorna un valor estructurado
    def obtener_informacion(self):
        # En lugar de imprimir directamente, devolvemos el texto formateado con 'return'
        return f"'{self.titulo}', escrito por {self.autor}"


# 2. Creación de las INSTANCIAS (Dos libros diferentes en nuestra base de datos)
libro_favorito = Libro("Cien años de soledad", "Gabriel García Márquez")
libro_estudio = Libro("Curso Intensivo de Python", "Eric Matthes")

# 3. Llamada e impresión del resultado retornado
info_uno = libro_favorito.obtener_informacion()
info_dos = libro_estudio.obtener_informacion()

print("Fichas bibliográficas generadas:")
print(info_uno)  # Salida: 'Cien años de soledad', escrito por Gabriel García Márquez
print(info_dos)  # Salida: 'Curso Intensivo de Python', escrito por Eric Matthes
```

---

### Resumen para compartir con tus estudiantes:
*   **La Clase (`Perro`, `Alcancia`, `Libro`):** Es la plantilla general escrita en el código. No almacena datos reales de un perro o libro específico, sino la estructura que todos compartirán.
*   **La Instancia (`perro_uno`, `mi_hucha`, `libro_favorito`):** Es el objeto físico e independiente creado en la memoria de la computadora mediante la llamada a la clase. Tienen sus propios datos aislados de otros objetos.
*   **Los Métodos (`ladrar()`, `guardar_dinero()`, `obtener_informacion()`):** Son las funciones que viven dentro de la clase y que solo los objetos creados a partir de ella pueden ejecutar.

---
💡 Como tienes disponible la aplicación **`Python Cuestionario`** en tu panel de Studio, ¿te gustaría que agreguemos un set de preguntas de opción múltiple diseñado específicamente para evaluar si los alumnos logran diferenciar correctamente entre clases, instancias y atributos en código de Python?