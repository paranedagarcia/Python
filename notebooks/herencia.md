---
He generado y publicado el Jupyter Notebook interactivo **`herencia_ejemplos_python.ipynb`** en tu panel de Studio. 

A continuación tienes los **8 ejemplos de uso de herencia en Python**, ordenados en una progresión didáctica de menor a mayor complejidad, con sus respectivos enunciados, códigos ejecutables y explicaciones técnicas:


### 1. Herencia Simple (Nivel Básico)
**Enunciado:** Crea una clase base `Vehiculo` con atributos `marca` y `modelo`, y un método `describir()`. Luego, crea una subclase `Coche` que herede de `Vehiculo` e incorpore el atributo `num_puertas` y el método `abrir_maletero()`.

```python
class Vehiculo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def describir(self) -> str:
        return f"Vehículo: {self.marca} {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca: str, modelo: str, num_puertas: int):
        super().__init__(marca, modelo)  # Inicializa atributos heredados
        self.num_puertas = num_puertas

    def abrir_maletero(self) -> str:
        return f"Abriendo maletero del {self.marca} {self.modelo} ({self.num_puertas} puertas)."

# Ejemplo de uso
mi_coche = Coche("Toyota", "Corolla", 4)
print(mi_coche.describir())       # Método heredado de Vehiculo
print(mi_coche.abrir_maletero())  # Método propio de Coche
```
* **Explicación:** La sintaxis `class Coche(Vehiculo):` establece la relación de herencia. Con `super().__init__()` se delega la construcción de los atributos del padre a la clase base sin duplicar código.

jupyter:
  jupytext:
    cell_metadata_filter: -all
    custom_cell_magics: kql
    main_language: python
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.2
---

### 2. Sobrescritura de Métodos (*Method Overriding*) y Extensiones
**Enunciado:** Diseña una clase base `Empleado` con un método `calcular_salario()`. Crea una subclase `Gerente` que modifique (sobrescriba) la forma en que se calcula el salario sumando un bono especial, reutilizando el cálculo base.

```python
class Empleado:
    def __init__(self, nombre: str, salario_base: float):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self) -> float:
        return self.salario_base

class Gerente(Empleado):
    def __init__(self, nombre: str, salario_base: float, bono: float):
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_salario(self) -> float:
        # Reutiliza la lógica del padre y extiende la responsabilidad
        return super().calcular_salario() + self.bono

gerente = Gerente("Ana", 3500.0, 1000.0)
print(f"Salario de {gerente.nombre}: ${gerente.calcular_salario():,.2f}")
```
* **Explicación:** La subclase reemplaza la implementación del método heredado. Mediante `super().calcular_salario()`, invoca el cálculo base del padre y le añade la lógica específica del bono.

---

### 3. Herencia Jerárquica y Polimorfismo
**Enunciado:** Construye una clase base `FiguraGeometrica` y dos subclases derivadas, `Circulo` y `Rectangulo`. Cada subclase debe calcular su propia área según su fórmula matemática.

```python
import math

class FiguraGeometrica:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def calcular_area(self) -> float:
        raise NotImplementedError("Las subclases deben implementar este método.")

class Circulo(FiguraGeometrica):
    def __init__(self, radio: float):
        super().__init__("Círculo")
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * (self.radio ** 2)

class Rectangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

# Uso polimórfico
figuras = [Circulo(5.0), Rectangulo(4.0, 6.0)]
for f in figuras:
    print(f"Área de {f.nombre}: {f.calcular_area():.2f}")
```
* **Explicación:** Un solo padre sirve de plantilla para múltiples subclases hermanas. El bucle procesa los objetos de forma polimórfica llamando a `.calcular_area()` sin importar la clase concreta.

---

### 4. Herencia Multinivel (Cadenas de Herencia)
**Enunciado:** Modela una cadena de tres niveles: `DispositivoElectronico` (abuelo) \\(\rightarrow\\) `Computadora` (padre) \\(\rightarrow\\) `Laptop` (hijo). Cada nivel agrega atributos y responsabilidades más específicas.

```python
class DispositivoElectronico:
    def __init__(self, marca: str):
        self.marca = marca

    def encender(self) -> str:
        return f"[{self.marca}] Dispositivo encendido."

class Computadora(DispositivoElectronico):
    def __init__(self, marca: str, procesador: str, ram_gb: int):
        super().__init__(marca)
        self.procesador = procesador
        self.ram_gb = ram_gb

    def ejecutar_programa(self, programa: str) -> str:
        return f"Ejecutando '{programa}' ({self.ram_gb} GB RAM)."

class Laptop(Computadora):
    def __init__(self, marca: str, procesador: str, ram_gb: int, peso_kg: float):
        super().__init__(marca, procesador, ram_gb)
        self.peso_kg = peso_kg

    def verificar_portabilidad(self) -> str:
        return f"Laptop {self.marca} ultraligera ({self.peso_kg} kg)."

laptop = Laptop("Apple", "M3 Pro", 18, 1.6)
print(laptop.encender())                  # Método heredado del abuelo
print(laptop.ejecutar_programa("VS Code")) # Método heredado del padre
print(laptop.verificar_portabilidad())     # Método propio de la subclase
```
* **Explicación:** La clase `Laptop` acumula las capacidades y atributos de toda la cadena jerárquica. Las llamadas a `super().__init__()` se propagan hacia arriba a través de cada nivel.

---

### 5. Herencia Múltiple Básica
**Enunciado:** Define una clase `RelojCalendario` que combine las funciones de dos clases totalmente independientes: `Reloj` (manejo de hora) y `Calendario` (manejo de fecha).

```python
class Reloj:
    def __init__(self, hora: str):
        self.hora = hora

    def mostrar_hora(self) -> str:
        return f"⏰ Hora: {self.hora}"

class Calendario:
    def __init__(self, fecha: str):
        self.fecha = fecha

    def mostrar_fecha(self) -> str:
        return f"📅 Fecha: {self.fecha}"

class RelojCalendario(Reloj, Calendario):
    def __init__(self, hora: str, fecha: str):
        Reloj.__init__(self, hora)
        Calendario.__init__(self, fecha)

    def mostrar_estado(self) -> str:
        return f"{self.mostrar_fecha()} | {self.mostrar_hora()}"

widget = RelojCalendario("14:30:00", "2026-09-22")
print(widget.mostrar_estado())
```
* **Explicación:** Permite fusionar comportamientos de dos o más clases independientes en una sola subclase.

---

### 6. El Problema del Diamante y Resolución con MRO
**Enunciado:** Construye una estructura en forma de diamante donde `Smartphone` herede de `Telefono` y `Camara`, y ambas deriven de `Dispositivo`. Usa `super()` para garantizar que la base común se inicialice solo una vez.

```python
class Dispositivo:
    def __init__(self, id_dispositivo: str, **kwargs):
        super().__init__(**kwargs)
        self.id_dispositivo = id_dispositivo

class Telefono(Dispositivo):
    def __init__(self, numero: str, **kwargs):
        super().__init__(**kwargs)
        self.numero = numero

class Camara(Dispositivo):
    def __init__(self, megapixeles: int, **kwargs):
        super().__init__(**kwargs)
        self.megapixeles = megapixeles

class Smartphone(Telefono, Camara):
    def __init__(self, id_dispositivo: str, numero: str, megapixeles: int, modelo: str):
        super().__init__(id_dispositivo=id_dispositivo, numero=numero, megapixeles=megapixeles)
        self.modelo = modelo

sp = Smartphone("DEV-99", "+12345678", 48, "Galaxy Pro")
print(f"Smartphone ID={sp.id_dispositivo}, Num={sp.numero}, Cámara={sp.megapixeles}MP")
```
* **Explicación:** Al usar `super()` con `**kwargs`, la llamada sigue el orden linealizado C3 del MRO (`Smartphone` \\(\rightarrow\\) `Telefono` \\(\rightarrow\\) `Camara` \\(\rightarrow\\) `Dispositivo`). Esto evita la ejecución duplicada del constructor base.

---

### 7. Clases Abstractas Base (ABC) e Interfaces
**Enunciado:** Utiliza el módulo `abc` para definir un contrato formal `ProcesadorPago` con métodos obligatorios `@abstractmethod`. Implementa la subclase concreta `PagoTarjeta`.

```python
from abc import ABC, abstractmethod

class ProcesadorPago(ABC):
    @abstractmethod
    def validar_monto(self, monto: float) -> bool:
        pass

    @abstractmethod
    def procesar(self, monto: float) -> str:
        pass

class PagoTarjeta(ProcesadorPago):
    def __init__(self, tarjeta: str):
        self.tarjeta = tarjeta

    def validar_monto(self, monto: float) -> bool:
        return monto > 0 and monto <= 10000.0

    def procesar(self, monto: float) -> str:
        if self.validar_monto(monto):
            return f"💳 Pago de ${monto:,.2f} procesado con tarjeta ****-{self.tarjeta[-4:]}."
        return "❌ Transacción rechazada."

pago = PagoTarjeta("4532890123456789")
print(pago.procesar(1500.0))
```
* **Explicación:** Heredar de `ABC` e incluir `@abstractmethod` impide la creación de instancias incompletas. Si una subclase no implementa todos los métodos obligatorios, Python lanzará un `TypeError`.

---

### 8. Herencia Avanzada con Validaciones (`@property`)
**Enunciado:** Crea una clase `CuentaBancaria` que proteja su saldo con propiedades `@property`. Luego, crea la subclase `CuentaAhorros` que herede las reglas de validación y agregue cálculo de intereses.

```python
class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self.saldo = saldo_inicial  # Llama al setter para validar

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, monto: float):
        if monto < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self._saldo = monto

class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular: str, saldo_inicial: float, tasa_interes_anual: float):
        super().__init__(titular, saldo_inicial)
        self.tasa_interes_anual = tasa_interes_anual

    @property
    def rendimiento_anual_estimado(self) -> float:
        return self.saldo * (self.tasa_interes_anual / 100)

cuenta = CuentaAhorros("Laura Méndez", 5000.0, 6.0)
print(f"Titular: {cuenta.titular} | Saldo: ${cuenta.saldo:,.2f}")
print(f"Rendimiento estimado a 1 año: ${cuenta.rendimiento_anual_estimado:,.2f}")
```
* **Explicación:** La subclase hereda las propiedades encapsuladas de la clase base. Cualquier modificación del saldo en `CuentaAhorros` pasará obligatoriamente por el `@saldo.setter` definido en `CuentaBancaria`.

