---
# 10 Ejemplos Prácticos de Herencia en Python: De Simple a Avanzado

Este documento contiene **10 ejemplos completos e independientes** sobre el uso de herencia en la Programación Orientada a Objetos (POO) con Python, organizados en una progresión didáctica de menor a mayor complejidad.


## Índice
1. [Ejemplo 1: Herencia Básica de Atributos y Métodos (Videojuego RPG)](#ejemplo-1-herencia-básica-de-atributos-y-métodos-videojuego-rpg)
2. [Ejemplo 2: Sobrescritura y Extensión de `__str__` (Biblioteca)](#ejemplo-2-sobrescritura-y-extensión-de-__str__-biblioteca)
3. [Ejemplo 3: Herencia de Estructuras Nativas de Python (Lista Tipada)](#ejemplo-3-herencia-de-estructuras-nativas-de-python-lista-tipada)
4. [Ejemplo 4: Herencia Jerárquica (Sistema de Notificaciones)](#ejemplo-4-herencia-jerárquica-sistema-de-notificaciones)
5. [Ejemplo 5: Herencia Multinivel y Tarifación Encascada (Envíos)](#ejemplo-5-herencia-multinivel-y-tarifación-encascada-envíos)
6. [Ejemplo 6: Herencia Múltiple y Patrón Mixin (Serialización y Auditoría)](#ejemplo-6-herencia-múltiple-y-patrón-mixin-serialización-y-auditoría)
7. [Ejemplo 7: Patrón Template Method (Pipeline ETL de Datos)](#ejemplo-7-patrón-template-method-pipeline-etl-de-datos)
8. [Ejemplo 8: Patrón Factory Method (Generación de Reportes)](#ejemplo-8-patrón-factory-method-generación-de-reportes)
9. [Ejemplo 9: Optimización de Memoria con `__slots__` en Herencia](#ejemplo-9-optimización-de-memoria-con-__slots__-en-herencia)
10. [Ejemplo 10: Registro Automático de Plugins con `__init_subclass__`](#ejemplo-10-registro-automático-de-plugins-con-__init_subclass__)

jupyter:
  jupytext:
    cell_metadata_filter: -all
    custom_cell_magics: kql
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.2
  kernelspec:
    display_name: Python (3.13.5)
    language: python
    name: python3
---

## Ejemplo 1: Herencia Básica de Atributos y Métodos (Videojuego RPG)

### Enunciado
Crea una clase base `Personaje` con los atributos `nombre` y `vida`, y el método `atacar()`. Luego, define la subclase `Mago` que herede de `Personaje`, agregue el atributo `mana` y el método especializado `lanzar_hechizo()`.

### Código en Python
```python
class Personaje:
    def __init__(self, nombre: str, vida: int):
        self.nombre = nombre
        self.vida = vida

    def atacar(self) -> str:
        return f"⚔️ {self.nombre} realiza un ataque básico de cuerpo a cuerpo."


class Mago(Personaje):
    def __init__(self, nombre: str, vida: int, mana: int):
        super().__init__(nombre, vida)  # Inicializa atributos heredados del padre
        self.mana = mana

    def lanzar_hechizo(self, nombre_hechizo: str, costo_mana: int) -> str:
        if self.mana >= costo_mana:
            self.mana -= costo_mana
            return f"🔮 {self.nombre} lanza '{nombre_hechizo}'! (Mana restante: {self.mana})"
        return f"❌ {self.nombre} no tiene suficiente mana para lanzar '{nombre_hechizo}'."


# --- Prueba ---
gandalf = Mago("Gandalf", vida=100, mana=50)
print(gandalf.atacar())                             # Método heredado de Personaje
print(gandalf.lanzar_hechizo("Bola de Fuego", 30))  # Método propio de Mago
print(gandalf.lanzar_hechizo("Rayo Hielo", 30))     # Intento con mana insuficiente
```

### Explicación
* **`class Mago(Personaje):`** Establece que `Mago` deriva de `Personaje`.
* **`super().__init__(nombre, vida)`**: Delega la inicialización de los atributos comunes a la clase base, evitando duplicación de código.
* **Extensión de comportamiento:** La subclase añade un atributo específico (`mana`) y un método exclusivo (`lanzar_hechizo()`) sin alterar la clase padre.

---

## Ejemplo 2: Sobrescritura y Extensión de `__str__` (Biblioteca)

### Enunciado
Crea una clase `Publicacion` con atributos `titulo` y `autor`, e implementa el método mágico `__str__()`. Construye la subclase `Libro` que añada `num_paginas` e `isbn`, y sobrescriba `__str__()` para extender la representación en texto aprovechando `super().__str__()`.

### Código en Python
```python
class Publicacion:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

    def __str__(self) -> str:
        return f"📖 '{self.titulo}' por {self.autor}"


class Libro(Publicacion):
    def __init__(self, titulo: str, autor: str, num_paginas: int, isbn: str):
        super().__init__(titulo, autor)
        self.num_paginas = num_paginas
        self.isbn = isbn

    def __str__(self) -> str:
        # Reutiliza el formato base de Publicacion y le anexa la información técnica
        info_base = super().__str__()
        return f"{info_base} [{self.num_paginas} págs, ISBN: {self.isbn}]"


# --- Prueba ---
pub = Publicacion("Artículos de Ciencia", "Varios Autores")
libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 471, "978-0307474728")

print(pub)    # Llama a Publicacion.__str__()
print(libro)  # Llama a Libro.__str__() que extiende el comportamiento del padre
```

### Explicación
* **Sobrescritura de método dunder:** `Libro` define su propia versión de `__str__()`.
* **`super().__str__()`**: Permite reutilizar la lógica de representación de la clase padre en lugar de reimplementarla desde cero.

---

## Ejemplo 3: Herencia de Estructuras Nativas de Python (Lista Tipada)

### Enunciado
Crea una clase `ListaTipada` que herede de la clase nativa `list`. La nueva clase debe restringir la inserción de elementos para que solo se admitan objetos de un tipo homogéneo (por ejemplo, solo enteros), lanzando un `TypeError` en caso contrario.

### Código en Python
```python
class ListaTipada(list):
    def __init__(self, tipo_permitido: type, *args):
        self.tipo_permitido = tipo_permitido
        # Validar elementos iniciales antes de pasarlos a la lista nativa
        for item in args:
            self._validar(item)
        super().__init__(args)

    def _validar(self, elemento):
        if not isinstance(elemento, self.tipo_permitido):
            raise TypeError(
                f"Solo se permiten elementos de tipo '{self.tipo_permitido.__name__}'. "
                f"Se intentó agregar '{type(elemento).__name__}'."
            )

    def append(self, elemento):
        self._validar(elemento)
        super().append(elemento)  # Llama a list.append() nativo

    def extend(self, iterable):
        for item in iterable:
            self._validar(item)
        super().extend(iterable)


# --- Prueba ---
lista_enteros = ListaTipada(int, 10, 20, 30)
lista_enteros.append(40)
print(f"Lista de enteros: {lista_enteros}")

try:
    lista_enteros.append("Texto no permitido")  # Provoca error de validación
except TypeError as error:
    print(f"❌ Excepción capturada con éxito: {error}")
```

### Explicación
* En Python, se puede heredar directamente de tipos nativos como `list`, `dict` o `str`.
* Al sobrescribir métodos como `append()` y `extend()`, se intercepta la modificación de la colección para aplicar validaciones de negocio antes de llamar al método heredado con `super()`.

---

## Ejemplo 4: Herencia Jerárquica (Sistema de Notificaciones)

### Enunciado
Diseña una estructura jerárquica con una clase base `Notificacion` y dos subclases hijas, `NotificacionEmail` y `NotificacionSMS`. Ambas deben implementar el método `enviar()` adaptado a su canal de comunicación.

### Código en Python
```python
class Notificacion:
    def __init__(self, destinatario: str, mensaje: str):
        self.destinatario = destinatario
        self.mensaje = mensaje

    def enviar(self) -> str:
        raise NotImplementedError("Cada subclase debe definir su método de envío.")


class NotificacionEmail(Notificacion):
    def __init__(self, destinatario: str, mensaje: str, asunto: str):
        super().__init__(destinatario, mensaje)
        self.asunto = asunto

    def enviar(self) -> str:
        return f"📧 [EMAIL a {self.destinatario}] Asunto: '{self.asunto}' | Mensaje: {self.mensaje}"


class NotificacionSMS(Notificacion):
    def enviar(self) -> str:
        return f"📱 [SMS a {self.destinatario}] {self.mensaje}"


# --- Prueba ---
canales: list[Notificacion] = [
    NotificacionEmail("cliente@empresa.com", "Su factura está lista.", "Facturación Mensual"),
    NotificacionSMS("+5215551234567", "Su código de verificación es 49201")
]

for canal in canales:
    print(canal.enviar())
```

### Explicación
* **Herencia Jerárquica:** Múltiples clases derivadas dependen de un único ancestro común.
* **Polimorfismo:** La lista `canales` contiene diferentes tipos de notificaciones, pero el cliente las invoca unificadamente llamando a `.enviar()`.

---

## Ejemplo 5: Herencia Multinivel y Tarifación Encascada (Envíos)

### Enunciado
Construye una cadena de tres niveles: `Paquete` (base) -> `PaqueteExpress` (nivel 2) -> `PaqueteInternacional` (nivel 3). Cada nivel debe sobreescribir el cálculo de costo sumando sus propios recargos de forma encadenada.

### Código en Python
```python
class Paquete:
    def __init__(self, peso_kg: float, tarifa_base_per_kg: float = 5.0):
        self.peso_kg = peso_kg
        self.tarifa_base_per_kg = tarifa_base_per_kg

    def calcular_costo(self) -> float:
        return self.peso_kg * self.tarifa_base_per_kg


class PaqueteExpress(Paquete):
    def __init__(self, peso_kg: float, recargo_urgencia: float = 15.0):
        super().__init__(peso_kg)
        self.recargo_urgencia = recargo_urgencia

    def calcular_costo(self) -> float:
        # Suma el costo base + recargo por urgencia
        return super().calcular_costo() + self.recargo_urgencia


class PaqueteInternacional(PaqueteExpress):
    def __init__(self, peso_kg: float, impuesto_aduana_pct: float = 0.16):
        super().__init__(peso_kg)
        self.impuesto_aduana_pct = impuesto_aduana_pct

    def calcular_costo(self) -> float:
        # Recupera el costo express y le aplica los impuestos de aduana
        costo_express = super().calcular_costo()
        return costo_express * (1 + self.impuesto_aduana_pct)


# --- Prueba ---
p1 = Paquete(10)
p2 = PaqueteExpress(10)
p3 = PaqueteInternacional(10)

print(f"📦 Paquete Estándar (10kg): ${p1.calcular_costo():.2f}")
print(f"🚀 Paquete Express (10kg):  ${p2.calcular_costo():.2f}")
print(f"✈️ Paquete Intl Express (10kg + 16% aduana): ${p3.calcular_costo():.2f}")
```

### Explicación
* En la herencia multinivel, `super()` en `PaqueteInternacional` llama a `PaqueteExpress`, la cual a su vez llama a `Paquete`.
* Permite crear reglas de negocio acumulativas donde cada subnivel añade su propia capa de cálculo.

---

## Ejemplo 6: Herencia Múltiple y Patrón Mixin (Serialización y Auditoría)

### Enunciado
Define dos clases *Mixin* independientes: `JsonSerializableMixin` (convierte el objeto a JSON) y `AuditableMixin` (añade marca de tiempo de creación). Luego, combina ambos *Mixins* con la clase `Documento` para crear `DocumentoOficial`.

### Código en Python
```python
import json
from datetime import datetime

class JsonSerializableMixin:
    def a_json(self) -> str:
        """Convierte los atributos del objeto a formato JSON."""
        return json.dumps(self.__dict__, default=str, indent=2, ensure_ascii=False)


class AuditableMixin:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.creado_en = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Documento:
    def __init__(self, titulo: str, contenido: str, **kwargs):
        super().__init__(**kwargs)
        self.titulo = titulo
        self.contenido = contenido


# Herencia múltiple combinando los dos Mixins con la clase base
class DocumentoOficial(AuditableMixin, JsonSerializableMixin, Documento):
    def __init__(self, titulo: str, contenido: str, autor: str):
        super().__init__(titulo=titulo, contenido=contenido)
        self.autor = autor


# --- Prueba ---
doc = DocumentoOficial("Estatutos de la Empresa", "Contenido legal confidencial...", "Lic. Pérez")

print(f"📅 Fecha de creación automatizada por AuditableMixin: {doc.creado_en}")
print("\n📄 Exportación JSON provista por JsonSerializableMixin:")
print(doc.a_json())
```

### Explicación
* Los **Mixins** son clases pequeñas enfocadas en proveer una única funcionalidad reutilizable.
* Al usar `super().__init__(**kwargs)` con argumentos nombrados, la inicialización cooperativa fluye correctamente a través del MRO (*Method Resolution Order*).

---

## Ejemplo 7: Patrón Template Method (Pipeline ETL de Datos)

### Enunciado
Implementa el patrón de diseño *Template Method* usando una clase abstracta `ProcesadorPipeline`. La clase base debe definir el esqueleto del proceso en el método `ejecutar()` y delegar las etapas específicas (`extraer()` y `transformar()`) a las subclases `ProcesadorCSV` y `ProcesadorJSON`.

### Código en Python
```python
from abc import ABC, abstractmethod

class ProcesadorPipeline(ABC):
    def ejecutar(self):
        """Método plantilla que define la secuencia fija del algoritmo."""
        print("--- 🚀 Iniciando Pipeline ---")
        self.extraer()
        self.transformar()
        self.cargar()
        print("--- ✅ Pipeline Completado ---\n")

    @abstractmethod
    def extraer(self):
        pass

    @abstractmethod
    def transformar(self):
        pass

    def cargar(self):
        """Paso común por defecto para todos los pipelines."""
        print("💾 Guardando datos procesados en la base de datos central...")


class ProcesadorCSV(ProcesadorPipeline):
    def extraer(self):
        print("📂 [CSV] Leyendo archivo .csv y parseando filas...")

    def transformar(self):
        print("🧹 [CSV] Limpiando valores nulos y formateando fechas...")


class ProcesadorJSON(ProcesadorPipeline):
    def extraer(self):
        print("📦 [JSON] Consumiendo API REST y decodificando payload JSON...")

    def transformar(self):
        print("🔄 [JSON] Aplanando estructuras anidadas de diccionarios...")


# --- Prueba ---
pipeline_csv = ProcesadorCSV()
pipeline_csv.ejecutar()

pipeline_json = ProcesadorJSON()
pipeline_json.ejecutar()
```

### Explicación
* La clase base controla el **orden de ejecución** de los pasos (*Inversión de Control*).
* Las subclases garantizan la personalización de cada etapa sin cambiar la estructura general del proceso.

---

## Ejemplo 8: Patrón Factory Method (Generación de Reportes)

### Enunciado
Implementa un patrón de fábrica mediante herencia. Crea la clase abstracta `GeneradorReporte` con un método abstracto `crear_documento()`, e implementa dos generadores concretos: `GeneradorReportePDF` y `GeneradorReporteExcel`.

### Código en Python
```python
from abc import ABC, abstractmethod

# Producto Abstracto
class DocumentoReporte(ABC):
    @abstractmethod
    def renderizar(self) -> str:
        pass

# Productos Concretos
class ReportePDF(DocumentoReporte):
    def renderizar(self) -> str:
        return "📄 Documento renderizado en formato PDF vectorial."

class ReporteExcel(DocumentoReporte):
    def renderizar(self) -> str:
        return "📊 Libro de hojas de cálculo exportado en formato .XLSX."


# Creador Abstracto (Fábrica)
class GeneradorReporte(ABC):
    @abstractmethod
    def crear_documento(self) -> DocumentoReporte:
        pass

    def procesar_envio(self) -> str:
        doc = self.crear_documento()
        return f"Procesando envío: {doc.renderizar()}"


# Creadores Concretos
class GeneradorReportePDF(GeneradorReporte):
    def crear_documento(self) -> DocumentoReporte:
        return ReportePDF()

class GeneradorReporteExcel(GeneradorReporte):
    def crear_documento(self) -> DocumentoReporte:
        return ReporteExcel()


# --- Prueba ---
fabricas = [GeneradorReportePDF(), GeneradorReporteExcel()]
for f in fabricas:
    print(f.procesar_envio())
```

### Explicación
* Desacopla la lógica de creación de objetos de la lógica que los utiliza.
* Añadir un nuevo formato (por ejemplo, `ReporteHTML`) requiere solo crear una nueva subclase sin tocar el código existente.

---

## Ejemplo 9: Optimización de Memoria con `__slots__` en Herencia

### Enunciado
Demuestra la optimización de memoria en herencia usando `__slots__`. Crea `Punto2D` especificando sus ranuras de memoria y la subclase `Punto3D` agregando su propia coordenada sin generar un diccionario dinámico `__dict__`.

### Código en Python
```python
class Punto2D:
    __slots__ = ('x', 'y')  # Restringe los atributos e impide la creación de __dict__

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Punto2D(x={self.x}, y={self.y})"


class Punto3D(Punto2D):
    __slots__ = ('z',)  # Declara ÚNICAMENTE las nuevas ranuras de la subclase

    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y)
        self.z = z

    def __repr__(self) -> str:
        return f"Punto3D(x={self.x}, y={self.y}, z={self.z})"


# --- Prueba ---
p2 = Punto2D(10.0, 20.0)
p3 = Punto3D(10.0, 20.0, 30.0)

print(f"Instancia 2D: {p2}")
print(f"Instancia 3D: {p3}")

print(f"¿Tiene p3 diccionario __dict__?: {hasattr(p3, '__dict__')}")

try:
    p3.color = "Rojo"  # Intento de agregar atributo dinámico no declarado en __slots__
except AttributeError as error:
    print(f"❌ Error al intentar agregar atributo dinámico: {error}")
```

### Explicación
* `__slots__` elimina la sobrecarga de memoria del diccionario dinámico `__dict__` por cada objeto.
* En herencia, la subclase debe declarar solo los campos nuevos en su propia tupla `__slots__`.

---

## Ejemplo 10: Registro Automático de Plugins con `__init_subclass__`

### Enunciado
Implementa un registro de plugins dinámico. Crea una clase base `PluginBase` que utilice el método dunder `__init_subclass__()` para inscribir automáticamente cualquier subclase que se defina en un registro global.

### Código en Python
```python
class PluginBase:
    # Diccionario central de registro de plugins
    REGISTRO_PLUGINS = {}

    def __init_subclass__(cls, clave_plugin: str = None, **kwargs):
        super().__init_subclass__(**kwargs)
        if clave_plugin:
            cls.REGISTRO_PLUGINS[clave_plugin] = cls
            print(f"🔌 [REGISTRO] Plugin registrado automáticamente: '{clave_plugin}' -> {cls.__name__}")

    def ejecutar(self) -> str:
        raise NotImplementedError()


# Subclases que se registran automáticamente al momento de ser definidas
class PluginFiltroBlur(PluginBase, clave_plugin="blur"):
    def ejecutar(self) -> str:
        return "Aplicando filtro de desenfoque Gaussiano."


class PluginFiltroGris(PluginBase, clave_plugin="escala_grises"):
    def ejecutar(self) -> str:
        return "Convirtiendo imagen a escala de grises."


# --- Prueba ---
print("\n--- Estado del Registro Central de Plugins ---")
for clave, clase_plugin in PluginBase.REGISTRO_PLUGINS.items():
    instancia = clase_plugin()
    print(f"Clave: '{clave}' | Resultado: {instancia.ejecutar()}")
```

### Explicación
* **`__init_subclass__`**: Es una alternativa moderna y limpia a las metaclases. Se ejecuta automáticamente cada vez que se define una nueva subclase de `PluginBase`.
* Permite crear sistemas totalmente extensibles donde nuevos módulos se autorregistran sin requerir configuración manual.

---
