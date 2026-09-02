---
id: herencia
title: "Herencia"
sidebar_label: "Herencia"
description: "Crear una nueva clase a partir de una existente"
---

![](img/herencia.webp)

La **herencia** es un mecanismo fundamental de la programación orientada a objetos que permite crear una clase nueva (llamada **clase derivada** o **subclase**) basándose en una clase existente (llamada **clase base** o **superclase**). Al hacer esto, la subclase adopta automáticamente los atributos y métodos de la clase original, lo que facilita la reutilización de código y evita la redundancia.

A continuación, se presenta un ejemplo didáctico y sencillo basado en el modelado de vehículos:

```python
class Vehiculo:
    """Clase base que representa un vehículo genérico."""
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def obtener_nombre_descriptivo(self):
        """Devuelve un nombre descriptivo formateado."""
        return f"{self.marca.title()} {self.modelo.title()}"


class CocheElectrico(Vehiculo):
    """Clase derivada que representa un coche eléctrico."""
    
    def __init__(self, marca, modelo, capacidad_bateria=40):
        # La función super() permite llamar al constructor de la clase base
        super().__init__(marca, modelo)
        # Atributo exclusivo de la subclase coche eléctrico
        self.capacidad_bateria = capacidad_bateria
        
    def describir_bateria(self):
        """Muestra información sobre el tamaño de la batería."""
        print(f"Este coche tiene una batería de {self.capacidad_bateria} kWh.")
```

### Explicación del funcionamiento:
1. **Definición de la jerarquía:** Para indicar que `CocheElectrico` hereda de `Vehiculo`, colocamos el nombre de la clase base entre paréntesis al definir la subclase (`class CocheElectrico(Vehiculo)`).
2. **Uso de `super()`:** En el constructor (`__init__`) de `CocheElectrico`, llamamos a `super().__init__(marca, modelo)`. Esto le dice a Python que invoque el método de inicialización de la clase base `Vehiculo` para configurar de inmediato los atributos comunes (`marca` y `modelo`), evitando la duplicación de código.
3. **Especialización:** Una vez que la clase base está inicializada, podemos añadir nuevos atributos específicos (como `capacidad_bateria`) y métodos especializados (como `describir_bateria`) que solo tienen sentido para los coches eléctricos.

### Demostración de uso:
```python
# Crear una instancia de la clase derivada
mi_coche = CocheElectrico('nissan', 'leaf', 62)

# 1. Acceso al método heredado de la clase base:
print(mi_coche.obtener_nombre_descriptivo())  # Salida: Nissan Leaf

# 2. Acceso al método propio de la clase derivada:
mi_coche.describir_bateria()  # Salida: Este coche tiene una batería de 62 kWh.
```

🚙 ¿Te gustaría que hagamos un ejercicio para ver cómo anular (sobrescribir) un método heredado de la clase base, o prefieres revisar cómo funciona la herencia múltiple en Python?