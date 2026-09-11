La diferencia principal entre **`@classmethod`** y **`@staticmethod`** radica en qué tipo de referencia reciben implícitamente como primer parámetro y para qué propósito de diseño se utilizan dentro de una clase:

* **`@classmethod` (Método de clase):** Recibe automáticamente la **propia clase (`cls`)** como primer argumento. Puede acceder y modificar el estado de la clase, y su uso más común es como **método fábrica** (*factory method*) para crear instancias de formas alternativas.
* **`@staticmethod` (Método estático):** **No recibe ningún argumento automático** (ni la instancia `self` ni la clase `cls`). Funciona como una función ordinaria empaquetada dentro del espacio de nombres de la clase por razones de organización y coherencia lógica.

---

### Ejemplo Práctico Integrado: Clase `Fecha`

El siguiente ejemplo muestra ambos decoradores trabajando juntos en una misma clase:

```python
class Fecha:
    def __init__(self, dia: int, mes: int, anio: int):
        # Método de instancia tradicional
        self.dia = dia
        self.mes = mes
        self.anio = anio

    # 1. @classmethod: Método Fábrica
    @classmethod
    def desde_cadena(cls, texto_fecha: str):
        """
        Toma un texto como '10-09-2026', procesa los datos
        y crea una nueva instancia de la clase usando 'cls'.
        """
        dia, mes, anio = map(int, texto_fecha.split("-"))
        return cls(dia, mes, anio)  # Equivale a llamar a Fecha(dia, mes, anio)

    # 2. @staticmethod: Función de Utilidad
    @staticmethod
    def es_cadena_valida(texto_fecha: str) -> bool:
        """
        Verifica el formato del texto de entrada.
        No necesita conocer los atributos de ninguna instancia ni de la clase.
        """
        partes = texto_fecha.split("-")
        if len(partes) != 3:
            return False
        d, m, a = partes
        return d.isdigit() and m.isdigit() and a.isdigit()

    def mostrar(self):
        print(f"Fecha: {self.dia:02d}/{self.mes:02d}/{self.anio}")
```

---

### ¿Cómo se utilizan en la práctica?

```python
# A. Uso del @staticmethod (Validación autónoma sin crear objetos)
texto = "10-09-2026"

if Fecha.es_cadena_valida(texto):
    print("El formato de fecha es correcto.")

# B. Uso del @classmethod (Creación alternativa de instancias)
fecha_objeto = Fecha.desde_cadena(texto)

# C. Uso del método de instancia normal
fecha_objeto.mostrar()  # Salida: Fecha: 10/09/2026
```

---

### ¿Por qué elegir uno u otro?

1. **Usa `@classmethod` cuando:**
   * Necesites crear **constructores alternativos** (por ejemplo, instanciar un objeto a partir de un archivo JSON, una cadena de texto o un diccionario).
   * Necesites modificar un atributo de clase compartido por todas las instancias.
   * Quieras asegurar que el método funcione correctamente al ser heredado por subclases (ya que `cls` apuntará automáticamente a la subclase hija que lo invoque).

2. **Usa `@staticmethod` cuando:**
   * Necesites una **función auxiliar o utilitaria** que realice una tarea lógica vinculada al concepto de la clase, pero que no requiera leer ni alterar datos de las instancias o de la clase.
   * Quieras mantener el código ordenado dentro del espacio de nombres de la clase en lugar de dejar la función "suelta" como función global en el módulo.

---

### Tabla Comparativa de Resumen

| Característica | Método de Instancia Normal | `@classmethod` | `@staticmethod` |
| :--- | :--- | :--- | :--- |
| **Primer parámetro implícito** | `self` (la instancia concreta) | `cls` (la clase misma) | **Ninguno** |
| **Acceso al estado de la instancia** | Sí (`self.atributo`) | No directo | No |
| **Acceso al estado de la clase** | Sí (`self.__class__`) | Sí (`cls.atributo`) | No directo |
| **Caso de uso principal** | Operaciones sobre un objeto específico | Métodos fábrica y constructores alternativos | Funciones utilitarias independientes |

