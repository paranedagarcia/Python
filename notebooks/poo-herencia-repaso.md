Estos ejercicios están diseñados sin la solución completa, incluyendo únicamente los **enunciados**, **tips guiados** y una **plantilla de código inicial** lista para que los alumnos la completen.

---

### Ejercicios Prácticos

#### **Ejercicio 1: Animales y Sonidos (`Mascota` -> `Perro`)**
* **Enunciado:** Crea una clase base `Mascota` que reciba el atributo `nombre` en su constructor y tenga un método `emitir_sonido()` con un mensaje genérico. Luego, crea la subclase `Perro` que herede de `Mascota` e implemente su propio método `emitir_sonido()` que retorne `'¡Guau guau!'`.
* **Tips de solución:**
  1. Define `__init__(self, nombre)` en `Mascota` para guardar el nombre.
  2. En `Perro`, al no agregar atributos nuevos, heredará automáticamente el constructor de la clase base.

---

#### **Ejercicio 2: Electrodomésticos y Consumo (`Electrodomestico` -> `Lavadora`)**
* **Enunciado:** Diseña una clase base `Electrodomestico` con atributos `marca` y `potencia_watts`. Crea la subclase `Lavadora` que agregue `carga_kg` y el método `calcular_consumo_diario(horas)` que devuelva el consumo en kWh usando la fórmula: \\(\frac{\text{potencia\_watts} \cdot \text{horas}}{1000}\\).
* **Tips de solución:**
  1. Usa `super().__init__(marca, potencia_watts)` dentro del constructor de `Lavadora`.
  2. Asegúrate de dividir entre 1000 para convertir Watts a KiloWatts (kWh).

---

#### **Ejercicio 3: Permisos de Usuario (`Usuario` -> `UsuarioAdministrador`)**
* **Enunciado:** Crea una clase `Usuario` con `nombre_usuario` y `email`. Luego, crea la subclase `UsuarioAdministrador` con una lista de `permisos` (ej. `['crear', 'eliminar', 'editar']`) y un método `tiene_permiso(permiso)` que devuelva `True` o `False`.
* **Tips de solución:**
  1. Utiliza el operador `in` de Python (`permiso in self.permisos`) para verificar la existencia del permiso.
  2. En el constructor del administrador, permite recibir la lista o asigna una por defecto.

---

#### **Ejercicio 4: Registro Escolar (`PersonaEscolar` -> `Estudiante`)**
* **Enunciado:** Modela `PersonaEscolar` con `nombre` e `id_identificacion`. Crea la subclase `Estudiante` con una lista de `calificaciones` y los métodos `agregar_calificacion(nota)` y `calcular_promedio()`. Si no hay calificaciones, debe retornar `0.0`.
* **Tips de solución:**
  1. Inicializa `self.calificaciones = []` en el constructor de `Estudiante`.
  2. Usa `sum(self.calificaciones)` y `len(self.calificaciones)`, verificando antes que la lista no esté vacía para evitar errores de división por cero (`ZeroDivisionError`).

---

#### **Ejercicio 5: Sensor de Temperatura (`Sensor` -> `SensorTemperatura`)**
* **Enunciado:** Diseña la clase `Sensor` con `ubicacion` y `lectura_actual`. Crea la subclase `SensorTemperatura` con el umbral `temperatura_maxima` y el método `evaluar_alerta()` que devuelva `'⚠️ ¡ALERTA: Temperatura crítica!'` si la lectura supera el límite, o `'✅ Temperatura dentro del rango normal.'` en caso contrario.
* **Tips de solución:**
  1. Crea un método `actualizar_lectura(nuevo_valor)` en la clase base.
  2. Usa un condicional `if / else` dentro de `evaluar_alerta()` comparando `self.lectura_actual > self.temperatura_maxima`.

---

#### **Ejercicio 6: Tienda Online (`Producto` -> `ProductoEnOferta`)**
* **Enunciado:** Crea la clase `Producto` con `nombre` y `precio_base`, y el método `obtener_precio_final()`. Crea la subclase `ProductoEnOferta` con `porcentaje_descuento` (ej. 20 para 20%) y sobrescribe `obtener_precio_final()` aplicando la rebaja.
* **Tips de solución:**
  1. Aplica la fórmula: \\(\text{precio\_base} \cdot \left(1 - \frac{\text{porcentaje\_descuento}}{100}\right)\\).
  2. Conserva el mismo nombre del método (`obtener_precio_final`) para mantener el comportamiento polimórfico.

---

#### **Ejercicio 7: Geometría 3D (`Circulo` -> `Cilindro`)**
* **Enunciado:** Desarrolla la clase `Circulo` con el atributo `radio` y el método `area()` (\\(\pi \cdot r^2\\)). Crea la subclase `Cilindro` que agregue `altura` e implemente el método `volumen()` reutilizando el método `area()` del padre (\\(\text{volumen} = \text{area\_base} \cdot \text{altura}\\)).
* **Tips de solución:**
  1. Importa `math` y utiliza la constante `math.pi`.
  2. Dentro de `volumen()`, invoca `self.area()` o `super().area()` para obtener la superficie de la base circular sin repetir la fórmula.

