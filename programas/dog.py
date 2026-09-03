
class Dog:
    """Un intento sencillo de modelar un perro."""

    def __init__(self, name, age):
        """Inicializa los atributos de nombre y edad."""
        self.name = name  # Atributo de instancia para el nombre
        self.age = age    # Atributo de instancia para la edad

    def sit(self):
        """Simula un perro sentándose en respuesta a una orden."""
        print(f"{self.name} is now sitting.")

    def rueda(self):
        """Simula hacer la croqueta en respuesta a una orden."""
        print(f"{self.name} rolled over!")

    # ejercicio 1:
    # agrega más métodos según sea necesario: 
    # saltar, ladrar, correr, detenerse
    # agrega los métodos aquí:

# --- Demostración de Uso del Programa ---

# 1. Creamos una instancia específica de la clase Dog
my_dog = Dog('Willie', 6)

# 2. Accedemos e imprimimos sus atributos
print(f"Mi perro se llama {my_dog.name}.")
print(f"Mi perro tiene {my_dog.age} años.")

# 3. Llamamos a los métodos del objeto
my_dog.sit()
my_dog.rueda()

# 4. Creación de una segunda instancia independiente
your_dog = Dog('Lucy', 3)
print(f"\nMi otro perro se llama {your_dog.name}.")
print(f"Mi otro perro tiene {your_dog.age} años.")
your_dog.sit()
your_dog.rueda()