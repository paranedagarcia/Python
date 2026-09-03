---
id: composicion
title: "Composición"
sidebar_label: "Composición"
description: "Combinar u organizar múltiples objetos simples para construir un objeto más complejo"
---

La **composición** es un principio de diseño fundamental en la programación orientada a objetos que consiste en **combinar u organizar múltiples objetos simples para construir un objeto más complejo que actúa como el "todo"**. 

A diferencia de la herencia (que representa una relación de especialización *"Es-Un"*), la composición modela relaciones de componentes o partes de un todo, conocidas técnicamente como relaciones **"Tiene-Un" (*Has-A*)**.

---

### ¿Cómo funciona la composición en la práctica?

Desde la perspectiva del programador, la composición se logra **declarando instancias de otras clases dentro de los atributos de una clase contenedora (o compuesto)**. En lugar de heredar los métodos de otra clase de forma invisible, el objeto compuesto proporciona una interfaz propia y la implementa **dirigiendo y delegando llamadas** a los objetos internos que tiene encapsulados.

Un ejemplo clásico del mundo real es un coche: un coche no *es un* motor, sino que un coche **tiene un** motor, una transmisión y faros. 

En código Python, la descomposición de una clase grande en partes más pequeñas que cooperan entre sí se vería así:

```python showLineNumbers
class Bateria:
    """Clase que representa un componente especializado."""
    def __init__(self, capacidad=40):
        self.capacidad = capacity

    def describir(self):
        return f"Batería de {self.capacidad} kWh"

class CocheElectrico:
    """Clase compuesta que encapsula el componente en sus atributos."""
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        # COMPOSICIÓN: Creamos e introducemos el objeto Bateria dentro del coche
        self.bateria = Bateria(62) 

    def mostrar_especificaciones(self):
        # Delegamos la descripción en el objeto interno batería
        print(f"Vehículo: {self.marca} | {self.bateria.describir()}")
```
*(Estructura técnica y ejemplos basados en las explicaciones de las fuentes)*

---

### La sutil diferencia: Composición vs. Agregación

Las fuentes señalan que el diseño con clases a veces distingue entre dos formas de composición según el **ciclo de vida (*lifespan*)** de los objetos involucrados:

1.  **Composición Estricta:** Existe una dependencia de vida absoluta. El objeto contenedor (externo) controla por completo la creación y destrucción de los objetos internos. Si destruyes el compuesto, las partes se destruyen con él.
    *   *Ejemplo:* Un tablero de ajedrez y sus casillas. Si eliminas el tablero de la memoria, las casillas dejan de existir porque no tienen sentido fuera de él.
2.  **Agregación (o Composición Débil):** Los objetos relacionados se crean de forma independiente y pueden existir fuera del objeto contenedor, sobreviviendo a su destrucción.
    *   *Ejemplo:* Un cliente o un servidor en una tienda de pizzas. Los clientes van y vienen (se crean y se destruyen para cada orden), pero la tienda o el mesero siguen existiendo independientemente.

A pesar de esta distinción teórica en el modelado, en la práctica y al momento de escribir el código de implementación en Python, ambas relaciones se estructuran exactamente de la misma manera (guardando referencias a otros objetos en los atributos de una instancia).

---

### ¿Por qué es altamente recomendada frente a la herencia?

Existe un famoso lema en la arquitectura de software: *"Favorece la composición sobre la herencia"*. Esto se debe a varias razones que las fuentes destacan:

*   **Evita el acoplamiento fuerte:** La herencia acopla fuertemente a las subclases con sus padres; si cambias el constructor o un método de la clase base, puedes romper accidentalmente todo el árbol de herencia. En la composición, las clases componentes son independientes y autónomas, lo que facilita enormemente el mantenimiento y las pruebas aisladas.
*   **Flexibilidad en tiempo de ejecución:** La herencia es estática (se define al escribir el código). Con composición, puedes cambiar dinámicamente un componente interno por otro diferente en tiempo de ejecución siempre que cumpla con la misma interfaz.
*   **Simplifica taxonomías confusas:** Tratar de clasificar el mundo exclusivamente mediante herencia estricta puede llevar a contradicciones complejas (como decidir si una `Manzana` debe heredar de `Fruta` o de `Postre`). La composición resuelve esto de manera limpia al permitir que una clase simplemente "tenga" diferentes componentes según el contexto.

---

## **Ejercicio práctico: Videojuego**

La **explosión de clases por abuso de herencia** (herencia profunda), y cómo resolverlo de manera elegante mediante **composición**.


### El Escenario: Un Sistema de Personajes de Videojuego

Imagina que estamos diseñando un juego de rol (RPG). 
*   Tenemos personajes básicos (`Personaje`).
*   Queremos personajes que puedan pelear con espada (`Guerrero`).
*   Queremos que algunos puedan volar (`GuerreroVolador`).

#### ❌ El Anti-patrón: La Rigidez de la Herencia Profunda

Si abordamos esto usando únicamente herencia, el árbol de clases rápidamente se vuelve inmanejable:

```python showLineNumbers
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

class Guerrero(Personaje):
    def atacar(self):
        return f"{self.nombre} ataca ferozmente con su espada."

class GuerreroVolador(Guerrero):
    def desplazar(self):
        return f"{self.nombre} vuela majestuosamente por los cielos."
```

#### El gran problema de este diseño:
¿Qué ocurre si ahora queremos un **Mago** que también pueda volar (`MagoVolador`)? 
*   No podemos heredar de `GuerreroVolador` porque los magos no atacan con espada.
*   Si heredamos de `Personaje`, nos vemos obligados a **duplicar el código** del método `desplazar()` (vuelo) dentro de la clase `MagoVolador`.
*   Esto nos lleva a una explosión de clases redundantes (`MagoVolador`, `GuerreroVolador`, `MagoNadador`, `GuerreroNadador`, etc.). El código se vuelve rígido y sumamente difícil de mantener.


###  La Solución: Refactorización usando Composición

En lugar de definir lo que un personaje **es** mediante herencia rígida, definiremos lo que un personaje **tiene** (sus comportamientos) usando **composición**. 

Separamos los comportamientos cambiantes (ataque y movimiento) en sus propias clases independientes y se las inyectamos al personaje.

#### 1. Definimos los componentes de Comportamiento:

```python showLineNumbers
# --- Comportamientos de Movimiento ---
class Caminar:
    def mover(self, nombre):
        return f"{nombre} avanza caminando por el suelo."

class Volar:
    def mover(self, nombre):
        return f"{nombre} vuela majestuosamente por los cielos."


# --- Comportamientos de Ataque ---
class AtaqueEspada:
    def atacar(self, nombre):
        return f"{nombre} lanza un tajo feroz con su espada."

class AtaqueHechizo:
    def atacar(self, nombre):
        return f"{nombre} lanza una poderosa bola de fuego."
```

#### 2. Creamos la clase compuesta (`Personaje`):
Ahora, el personaje no tiene métodos de combate o movimiento fijos. En su lugar, **tiene** referencias a sus comportamientos y delega las tareas en ellos.

```python showLineNumbers
class Personaje:
    def __init__(self, nombre, motor_movimiento, motor_ataque):
        self.nombre = nombre
        # COMPOSICIÓN: El personaje tiene un comportamiento de movimiento y ataque
        self.movimiento = motor_movimiento
        self.ataque = motor_ataque

    def desplazar(self):
        # Delegamos la responsabilidad al objeto componente
        return self.movimiento.mover(self.nombre)

    def combatir(self):
        # Delegamos la responsabilidad al objeto componente
        return self.ataque.atacar(self.nombre)
```


### 3. La recompensa: Flexibilidad absoluta y cambios dinámicos

Al usar composición, crear combinaciones de personajes es asombrosamente sencillo y **no requiere crear nuevas clases**. Además, podemos alterar el comportamiento de un personaje en tiempo de ejecución.

```python showLineNumbers
# Creamos un Guerrero Volador combinando componentes
arthur = Personaje("Arthur", Volar(), AtaqueEspada())
print(arthur.desplazar())  # Salida: Arthur vuela majestuosamente por los cielos.
print(arthur.combatir())   # Salida: Arthur lanza un tajo feroz con su espada.

# Creamos un Mago Terrestre combinando componentes
gandalf = Personaje("Gandalf", Caminar(), AtaqueHechizo())
print(gandalf.desplazar())  # Salida: Gandalf avanza caminando por el suelo.
print(gandalf.combatir())   # Salida: Gandalf lanza una poderosa bola de fuego.

# --- ¡CAMBIO DINÁMICO EN TIEMPO DE EJECUCIÓN! ---
# Imagina que Gandalf aprende un hechizo para volar a mitad de la partida:
gandalf.movimiento = Volar()

print(gandalf.desplazar())  # Salida: Gandalf vuela majestuosamente por los cielos.
```

### ¿Por qué este diseño es superior?
1.  **Cero duplicación de código:** El código para "volar" o "atacar con espada" se escribe exactamente una sola vez.

2.  **Bajo acoplamiento:** Si en el futuro necesitas modificar cómo funciona el vuelo (`Volar`), solo editas esa clase. No corres el riesgo de romper la lógica de ataque de tus personajes.

3.  **Flexibilidad dinámica:** Puedes cambiar el equipamiento o las habilidades de un personaje simplemente reasignando sus atributos (`personaje.ataque = AtaqueArco()`), algo imposible de lograr si usaras herencia estricta.

