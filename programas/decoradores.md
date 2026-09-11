Un **decorador** en Python es una función que recibe otra función (o clase) como argumento y retorna una nueva función con funcionalidad extendida, sin modificar el código fuente de la función original.

---

### 1. El Concepto y la Sintaxis (`@`)

La sintaxis con el símbolo `@` es lo que en programación se conoce como **azúcar sintáctico** (*syntactic sugar*). Permite aplicar una transformación de forma legible y elegante.

Cuando escribes:

```python
@mi_decorador
def saludar():
    print("¡Hola!")
```

Es exactamente equivalente a definir la función y luego reasignar su nombre pasando la función original al decorador:

```python
def saludar():
    print("¡Hola!")

saludar = mi_decorador(saludar)
```

---

### 2. Estructura de un Decorador (Patrón *Wrapper*)

Un decorador típicamente define una función interna (comúnmente llamada `wrapper` o `envoltura`) que intercepta la llamada, añade lógica antes o después, y finalmente ejecuta la función original pasándole sus argumentos mediante `*args` y `**kwargs`.

Para evitar que la función decorada pierda sus metadatos originales (como su nombre `__name__` o su documentación), se utiliza habitualmente el decorador `@wraps` del módulo estándar `functools`.

#### Ejemplo 1: Decorador para medir tiempo o registrar llamadas (*Logger*)

```python
import time
from functools import wraps

def auditoria_ejecucion(func):
    """Decorador que registra la entrada, salida y tiempo de ejecución de una función."""
    @wraps(func)  # Conserva el __name__ y docstring original de la función
    def wrapper(*args, **kwargs):
        print(f"--> [INICIO] Ejecutando '{func.__name__}' con args={args}, kwargs={kwargs}")
        inicio = time.time()
        
        # Ejecución de la función original
        resultado = func(*args, **kwargs)
        
        duracion = time.time() - inicio
        print(f"<-- [FIN] '{func.__name__}' finalizó en {duracion:.4f} segundos. Resultado: {resultado}")
        return resultado
    return wrapper

# --- Uso del decorador ---
@auditoria_ejecucion
def calcular_potencia(base, exponente):
    time.sleep(0.1)  # Simulación de carga
    return base ** exponente

# Llamada normal a la función
res = calcular_potencia(2, 10)
```

**Salida en consola:**
```text
--> [INICIO] Ejecutando 'calcular_potencia' con args=(2, 10), kwargs={}
<-- [FIN] 'calcular_potencia' finalizó en 0.1002 segundos. Resultado: 1024
```

---

### 3. Decoradores Integrados de Uso Frecuente

Python incluye varios decoradores nativos en su biblioteca estándar que se utilizan a diario en programación orientada a objetos y optimización:

* **En Clases (POO):**
  * **`@property`**: Transforma un método de lectura en un atributo de solo lectura o protegido mediante *getters* y *setters*.
  * **`@classmethod`**: Define un método que recibe la clase (`cls`) como primer parámetro en lugar de la instancia (`self`), muy usado para constructores alternativos.
  * **`@staticmethod`**: Define un método utilitario dentro del espacio de nombres de la clase que no recibe ni `self` ni `cls`.

* **En Optimización:**
  * **`@functools.lru_cache`**: Implementa una memoria caché (*Last Recently Used*) para guardar automáticamente los resultados de funciones costosas en función de sus argumentos.

---

### 4. Caso de Uso: Control de Acceso o Autenticación

Los decoradores son ampliamente utilizados en frameworks como Flask, Django o FastAPI para validar permisos o rutas web antes de ejecutar la lógica principal:

```python
def requiere_autenticacion(func):
    @wraps(func)
    def wrapper(usuario, *args, **kwargs):
        if not usuario.get("es_admin", False):
            raise PermissionError("Acceso denegado: Se requieren permisos de administrador.")
        return func(usuario, *args, **kwargs)
    return wrapper

@requiere_autenticacion
def eliminar_usuario(usuario, id_eliminar):
    print(f"Usuario {id_eliminar} eliminado con éxito.")

# Prueba
user_normal = {"nombre": "Carlos", "es_admin": False}
user_admin = {"nombre": "Ana", "es_admin": True}

# eliminar_usuario(user_normal, 42)  # Lanza PermissionError
eliminar_usuario(user_admin, 42)    # Imprime: Usuario 42 eliminado con éxito.
```

---

⚙️ ¿Te gustaría que exploremos cómo crear **decoradores que acepten sus propios parámetros** (como `@timer(label="TEST")`) o prefieres ver cómo aplicar decoradores directamente a **clases completas**?

---

## Ejemplos

Aquí tienes **4 ejemplos prácticos y avanzados de decoradores** en Python, que muestran patrones ampliamente utilizados en el desarrollo de software real:

---

### 1. Decorador con Parámetros (*Decorator Factory*): `@reintentar`

Cuando necesitas que un decorador reciba configuraciones (como el número de reintentos o el tiempo de espera), se utiliza una función externa que retorna el decorador real. Esto crea una estructura de 3 niveles de funciones anidadas basada en *closures*.

* **Caso de uso:** Reintentar automáticamente llamadas a APIs o conexiones de red inestables que pueden fallar por problemas temporales.

```python
import time
from functools import wraps

def reintentar(intentos=3, espera_segundos=1):
    """Fábrica de decoradores que recibe parámetros de configuración."""
    def decorador(func):
        @wraps(func)  # Conserva el nombre y docstring original
        def wrapper(*args, **kwargs):
            intentos_restantes = intentos
            while intentos_restantes > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    intentos_restantes -= 1
                    print(f"⚠️ Error en '{func.__name__}': {e}. Reintentos restantes: {intentos_restantes}")
                    if intentos_restantes == 0:
                        raise e
                    time.sleep(espera_segundos)
        return wrapper
    return decorador

# --- Uso del decorador ---
intento_conexion = 0

@reintentar(intentos=3, espera_segundos=0.5)
def conectar_servidor():
    global intento_conexion
    intento_conexion += 1
    if intento_conexion < 3:
        raise ConnectionError("Servidor ocupado")
    return "✅ Conexión establecida con éxito"

print(conectar_servidor())
```

---

### 2. Decorador de Caché / Memorización Personalizada

Consiste en almacenar los resultados de llamadas costosas en un diccionario interno dentro del ámbito de la función (*scope closure*).

* **Caso de uso:** Optimizar algoritmos recursivos pesados o consultas repetitivas a bases de datos sin modificar la función original.

```python
from functools import wraps

def memorizar(func):
    cache = {}  # Memoria persistente para la función decorada
    
    @wraps(func)
    def wrapper(*args):
        # Si el argumento ya fue procesado, devuelve el resultado guardado
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    wrapper.cache = cache  # Permite inspeccionar la caché desde fuera
    return wrapper

@memorizar
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci(35): {fibonacci(35)}")
print(f"Llamadas almacenadas en caché: {len(fibonacci.cache)}")
```

---

### 3. Decorador de Validación de Argumentos: `@validar_positivos`

Intercepta los argumentos pasados a la función **antes** de que esta se ejecute, verificando que cumplan con reglas de negocio específicas.

* **Caso de uso:** Garantizar la integridad de los datos de entrada sin llenar el cuerpo de la función con condicionales `if` repetitivos.

```python
from functools import wraps

def validar_positivos(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Inspecciona todos los argumentos numéricos recibidos
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"Error en {func.__name__}: El argumento {arg} debe ser mayor a cero.")
        return func(*args, **kwargs)
    return wrapper

@validar_positivos
def calcular_interes_compuesto(capital, tasa, tiempo):
    return capital * ((1 + tasa) ** tiempo)

# Prueba válida
print(f"Monto final: ${calcular_interes_compuesto(1000, 0.05, 3):.2f}")

# Intento inválido (lanza ValueError)
# calcular_interes_compuesto(-500, 0.05, 3)
```

---

### 4. Decorador de Depuración y Traza: `@traza`

Permite inspeccionar en consola el flujo de ejecución, registrando qué argumentos recibe una función y qué valor retorna exactamente.

* **Caso de uso:** Rastrear fallos o entender la secuencia de ejecución en sistemas complejos durante la fase de desarrollo.

```python
from functools import wraps

def traza(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Formatea los argumentos para la consola
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        firma = ", ".join(args_repr + kwargs_repr)
        
        print(f"🔍 [CALL] {func.__name__}({firma})")
        resultado = func(*args, **kwargs)
        print(f"✨ [RETURN] {func.__name__} -> {resultado!r}")
        
        return resultado
    return wrapper

@traza
def procesar_usuario(nombre, edad, es_vip=False):
    return {"usuario": nombre.lower(), "status": "VIP" if es_vip else "Standard"}

procesar_usuario("Carlos", 28, es_vip=True)
```

---

### Resumen de la Estructura Interna

| Tipo de Decorador | Estructura | Ámbito de Estado |
| :--- | :--- | :--- |
| **Sencillo** | 2 Funciones (`decorador` -> `wrapper`) | Captura `func`. |
| **Con parámetros** | 3 Funciones (`fábrica` -> `decorador` -> `wrapper`) | Captura los argumentos de configuración y `func`. |
| **Con estado (Caché)** | 2 Funciones con diccionario/variable local | Mantiene el estado en la clausura (`closure`). |

---

🛠️ ¿Te gustaría que apliquemos estos decoradores a la arquitectura de algún proyecto de ejemplo (como un servicio web con Flask/FastAPI o un pipeline de procesado de datos en Pandas)?