---
id: dycktyping
title: "Duck Typing"
sidebar_label: "Duck Typing"
description: "Duck Typing (tipado de pato)"
---

**Duck Typing** (o **tipado de pato**) es un estilo de tipado dinámico en el que la clase o el tipo de un objeto es menos importante que los métodos y atributos que este define. Bajo este principio, para determinar si un objeto se puede utilizar en un bloque de código, Python no evalúa si el objeto hereda de una clase específica; en su lugar, se enfoca únicamente en si el objeto se comporta como se espera en ese contexto.

El término proviene del conocido dicho popular: 

> *"Si camina como un pato, nada como un pato y grazna como un pato, entonces es un pato"*.

### Filosofía: "Lo que hace importa más que lo que es"
En lenguajes de programación con tipado estático (como Java, C# o C++), si deseas que una función acepte diferentes objetos de manera intercambiable, debes declarar explícitamente relaciones de herencia (*is-a*) o interfaces formales para asegurar la compatibilidad en tiempo de compilación.

En Python, gracias al polimorfismo generalizado (*pervasive polymorphism*), lo que define a un objeto son sus capacidades reales en tiempo de ejecución. Si un objeto proporciona los métodos o propiedades requeridos por una función, se acepta su uso independientemente de su origen o jerarquía. Esto da lugar a una flexibilidad enorme de **polimorfismo dinámico e implícito**.

### Un ejemplo clásico en Python
Imagina que estás diseñando un sistema de juego. Si deseas mover una pieza, no necesitas heredar de una clase base común `PiezaJuego`. Solo requieres que el objeto que pases tenga un método llamado `mover()`.

```python
class Alfil:
    def mover(self):
        print("El Alfil se mueve en diagonal.")

class Auto:
    def mover(self):
        print("El Auto avanza por la carretera.")

class Pato:
    def mover(self):
        print("El Pato vuela o nada en el estanque.")

# Esta función no valida tipos; solo invoca el método esperado
def realizar_movimiento(objeto):
    # No nos importa la identidad del objeto, solo que "sepa" moverse
    objeto.mover()

# Uso intercambiable sin herencia formal
realizar_movimiento(Alfil())  # "El Alfil se mueve en diagonal."
realizar_movimiento(Auto())   # "El Auto avanza por la carretera."
realizar_movimiento(Pato())   # "El Pato vuela o nada en el estanque."
```
*(Código conceptual estructurado a partir del comportamiento de chess/move de las fuentes)*

### Ventajas del Duck Typing
1. **Extensión fácil y acoplamiento débil:** Permite a futuros diseñadores crear nuevos comportamientos "drop-in" que se acoplen con sistemas existentes sin tener que adherirse formalmente a jerarquías rígidas.

2. **Cumplimiento parcial de interfaces:** El objeto que pases solo necesita proporcionar aquellos métodos y atributos que realmente van a ser accedidos. Por ejemplo, si creas un objeto de tipo archivo ficticio para lectura, basta con implementar el método `read()`; no es obligatorio escribir un método `write()` si el programa no va a escribir nada.

3. **Simplicidad sin sobrecarga:** Evita la necesidad de escribir código repetitivo dedicado únicamente a configurar herencias pesadas o jerarquías complejas.

### ¿Cuándo formalizar este comportamiento?
Aunque el Duck Typing ofrece una libertad inmensa, en proyectos grandes o de tipo corporativo puede ser útil tener contratos validados para prevenir errores tontos en tiempo de ejecución. En Python, esto se puede resolver de dos formas:
* **`typing.Protocol` (Static Duck-Typing):** Permite definir interfaces de manera implícita para que herramientas como `mypy` comprueben la compatibilidad de los tipos en estático, conservando la flexibilidad en tiempo de ejecución.
* **Clases Base Abstractas (ABCs):** Útiles para validaciones explícitas de jerarquías y la definición estricta de plantillas mediante herencia.

## **Caso ejemplo**

En Python, el tipado de pato (*duck typing*) es por naturaleza dinámico y se basa en la premisa "comprobar en tiempo de ejecución si falla". Sin embargo, a partir de Python 3.8, podemos formalizar este comportamiento de forma estática utilizando **`typing.Protocol`**. 

Esto nos permite implementar el **subtipado estructural** (o *static duck typing*): definimos un contrato (interfaz) para que herramientas como `mypy` o nuestro IDE validen el código antes de ejecutarlo, pero **sin obligar** a que nuestras clases hereden explícitamente de una clase base común.


<br />
<Tabs>
<TabItem value="mnp" label="Caso" default>
<div class="alert alert--primary">
**El Escenario: Un Reproductor de Medios Multiformato**

Imagina que estás diseñando un reproductor de medios. Queremos que pueda reproducir cualquier objeto que se pueda "reproducir". 
*   Definiremos el protocolo **`Playable`**.
*   Cualquier clase que implemente un método `.play()` será considerada compatible de forma automática, sin necesidad de usar herencia formal.
</div>
</TabItem>
<TabItem value="mnp-python" label="💻 Código" >

```python showLineNumbers
from typing import Protocol, runtime_checkable

# 1. Definimos el Protocolo (La Interfaz Implícita)
# Usamos el decorador @runtime_checkable para que también funcione con isinstance() en ejecución.
@runtime_checkable
class Playable(Protocol):
    """
    Define el contrato para cualquier objeto que pueda ser reproducido.
    Cualquier clase con un método 'play' que no reciba argumentos adicionales 
    cumple implícitamente con este protocolo.
    """
    def play(self) -> None:
        ...  # Elipsis (...) es sintaxis válida de Python para indicar un cuerpo vacío


# 2. Implementamos dos clases completamente independientes
# ¡Observa que ninguna de las dos hereda de 'Playable'!
class AudioFile:
    def __init__(self, title: str):
        self.title = title

    def play(self) -> None:
        print(f"🎶 Reproduciendo archivo de audio: {self.title}")


class VideoStream:
    def __init__(self, url: str):
        self.url = url

    def play(self) -> None:
        print(f"🎬 Transmitiendo video desde: {self.url}")


# 3. Esta clase NO cumple el protocolo porque le falta el método 'play()'
class Photo:
    def __init__(self, filename: str):
        self.filename = filename


# 4. Función cliente que consume el protocolo
# Indicamos que el parámetro 'media_item' debe cumplir con el protocolo 'Playable'
def start_playback(media_item: Playable) -> None:
    # Mypy y tu IDE sabrán que 'media_item' tiene garantizado el método '.play()'
    media_item.play()


# --- Demostración en ejecución ---

cancion = AudioFile("Imagine - John Lennon")
pelicula = VideoStream("https://streaming.com/movie1")
foto = Photo("vacaciones.jpg")

# Pruebas de compatibilidad estática (y ejecución exitosa):
start_playback(cancion)   # Salida: 🎶 Reproduciendo archivo de audio...
start_playback(pelicula)  # Salida: 🎬 Transmitiendo video desde...

# Comprobación en tiempo de ejecución usando isinstance() gracias a @runtime_checkable:
print(f"¿Es la canción reproducible?: {isinstance(cancion, Playable)}")  # True
print(f"¿Es la foto reproducible?: {isinstance(foto, Playable)}")        # False

# Esto fallaría estáticamente si ejecutamos 'mypy':
# start_playback(foto)  # Error de Mypy: "Photo" no es compatible con "Playable"
```
</TabItem>
</Tabs>



### La potencia de este enfoque

1.  **Acoplamiento débil:** Si en el futuro otro desarrollador crea una clase `Podcast` o `RadioStream`, solo necesita escribir un método `.play()`. No necesita importar tu módulo ni heredar de tu clase para que tu reproductor lo acepte.

2.  **Seguridad estática:** Si accidentalmente intentas pasar un objeto `Photo` a la función `start_playback()`, tu analizador estático (`mypy`) te avisará del error inmediatamente antes de que lances el código a producción.

3.  **Cumplimiento parcial:** El objeto solo necesita implementar el método que realmente vas a usar (en este caso, `.play()`), eliminando la necesidad de reescribir plantillas de interfaces gigantescas.

Este balance entre la libertad dinámica de Python y el rigor del tipado estático de lenguajes como Java o Go es lo que hace a las bibliotecas modernas de Python extremadamente limpias y fáciles de mantener.
