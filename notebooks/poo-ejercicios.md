---
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

<!-- #region -->



### Ejercicios

#### 1. Herencia Simple e Inicialización con `super()`


<!-- #endregion -->

```python
class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, carrera: str):
        # TODO: Llama al constructor de la clase base
        ___(nombre, edad)
        self.carrera = carrera

# * **Solución:** `super().__init__(nombre, edad)`


#### 2. Sobrescritura de Métodos (*Method Overriding*) y Extensión

class Empleado:
    def __init__(self, nombre: str, salario_base: float):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_pago(self) -> float:
        return self.salario_base

class Vendedor(Empleado):
    def __init__(self, nombre: str, salario_base: float, ventas: float, comision_pct: float):
        super().__init__(nombre, salario_base)
        self.ventas = ventas
        self.comision_pct = comision_pct

    def calcular_pago(self) -> float:
        # TODO: Obtén el salario base invocando el método del padre
        pago_base = ___.calcular_pago()
        return pago_base + (self.ventas * (self.comision_pct / 100))

```

<!-- #raw -->
* **Solución:** `super()`

---
<!-- #endraw -->

#### 3. Herencia Múltiple Cooperativa con `**kwargs`
```python
class Dispositivo:
    def __init__(self, id_codigo: str, **kwargs):
        super().__init__(**kwargs)
        self.id_codigo = id_codigo

class Pantalla(Dispositivo):
    def __init__(self, pulgadas: int, **kwargs):
        # TODO: Delegación cooperativa en el MRO
        ___(____)
        self.pulgadas = pulgadas

class SmartTV(Pantalla, Conectividad):
    def __init__(self, id_codigo: str, pulgadas: int, tiene_wifi: bool):
        # TODO: Llama a super().__init__() pasando los argumentos nombrados
        ___(id_codigo=id_codigo, pulgadas=pulgadas, tiene_wifi=tiene_wifi)
```
* **Solución:** `super().__init__(**kwargs)` en `Pantalla` y `super().__init__(id_codigo=id_codigo, pulgadas=pulgadas, tiene_wifi=tiene_wifi)` en `SmartTV`.

---

#### 4. Clases Abstractas Base (`ABC`)
```python
from abc import ABC, abstractmethod

class SensorBase(___):  # TODO: Heredar de la clase base abstracta
    def __init__(self, ubicacion: str):
        self.ubicacion = ubicacion

    @___  # TODO: Aplicar el decorador de método abstracto
    def leer_dato(self) -> float:
        pass
```
* **Solución:** `class SensorBase(ABC):` y `@abstractmethod`.

---

#### 5. Herencia y Propiedades Encapsuladas (`@property`)
```python
class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self.saldo = saldo_inicial

    @property
    def saldo(self) -> float:
        return self._saldo

    @___.setter  # TODO: Decorador del setter
    def saldo(self, monto: float):
        if monto < 0: raise ValueError("El saldo no puede ser negativo.")
        self._saldo = monto

class CuentaInversion(CuentaBancaria):
    def __init__(self, titular: str, saldo_inicial: float, tasa_retorno: float):
        ___(titular, saldo_inicial)  # TODO: Invocación al constructor padre
        self.tasa_retorno = tasa_retorno
```
* **Solución:** `@saldo.setter` y `super().__init__(titular, saldo_inicial)`.

---

💡 ¿Te gustaría que preparemos una **guía sobre polimorfismo y Duck Typing en Python** para complementar el tema de herencia en tus clases?
