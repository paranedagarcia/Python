Una **estructura de datos** es una forma organizada y sistemática de almacenar, gestionar y acceder a colecciones de datos en la memoria de un computador para poder operar sobre ellos de manera eficiente. 

En Python, todos los elementos se representan como objetos. El lenguaje ofrece un conjunto central de **estructuras de datos integradas** (*built-in*) que cubren la mayoría de las necesidades de programación, además de módulos especializados y soporte para definir estructuras complejas personalizadas mediante clases.

---

### **1. Estructuras de Datos Integradas (*Built-in*)**

Las estructuras nativas de Python se clasifican fundamentalmente según dos criterios: si conservan un orden posicional (**secuencias**) o acceden mediante asociaciones (**mapeos/conjuntos**), y si pueden modificarse tras su creación (**mutables** vs. **inmutables**).

#### **A. Listas (`list`)**
* **Definición:** Secuencias ordenadas, dinámicas y **mutables** que pueden contener objetos de tipos homogéneos o heterogéneos.
* **Representación interna:** En CPython se implementan como arrays de punteros a objetos en memoria con asignación dinámica previa (*overallocation*). El acceso por índice es de tiempo constante \\(O(1)\\).
* **Sintaxis y métodos comunes:**
  ```python
  numeros =
  numeros.append(40)         # Agrega al final - O(1)
  numeros.insert(0, 5)       # Inserta al inicio desplazando elementos - O(n)
  numeros = 15            # Modificación en el lugar por índice
  ultimo = numeros.pop()     # Extrae y remueve el último elemento - O(1)
  ```
* **Operaciones clave:** Indexación posicional comenzando en 0, rebanado (*slicing* `lista[inicio:fin:paso]`), concatenación (`+`) y extensión in-place (`.extend()`).

#### **B. Tuplas (`tuple`)**
* **Definición:** Secuencias ordenadas y heterogéneas, pero estrictamente **inmutables** y de longitud fija.
* **Uso y ventajas:** Al no poder modificarse tras su creación, ofrecen integridad de datos, consumen menos memoria que las listas y, dado que sus componentes son inmutables, son objetos con función de resumen (*hashables*), lo que les permite actuar como claves en diccionarios o miembros de conjuntos.
* **Sintaxis y manejo:**
  ```python
  punto = (4, 5, 6)          # Paréntesis o delimitadas por comas
  x, y, z = punto            # Desempaquetado de tuplas (tuple unpacking)
  ```

#### **C. Diccionarios (`dict`)**
* **Definición:** La estructura de mapeo (*mapping*) central de Python. Almacena pares `clave: valor`, donde cada clave debe ser un objeto inmutable y *hashable*, mientras que el valor puede ser de cualquier tipo.
* **Representación interna:** Implementados mediante **tablas hash** (*hash tables*) altamente optimizadas. La búsqueda, inserción y eliminación se ejecutan en tiempo promedio \\(O(1)\\). Desde Python 3.7 preservan de forma garantizada el orden de inserción de las claves.
* **Sintaxis y manejo:**
  ```python
  usuario = {"id": 101, "nombre": "Pat", "activo": True}
  usuario["rol"] = "admin"           # Asignación o creación dinámica
  nombre = usuario.get("nombre")     # Búsqueda segura evitando KeyError si la clave no existe
  claves = usuario.keys()            # Vista dinámica de claves
  valores = usuario.values()         # Vista dinámica de valores
  items = usuario.items()            # Pares (clave, valor) para iterar en bucles for
  ```

#### **D. Conjuntos (`set` y `frozenset`)**
* **Definición:** Colecciones desordenadas de elementos únicos. La versión `set` es mutable, mientras que `frozenset` es inmutable.
* **Propiedades:** No permiten elementos duplicados y operan mediante el hash de sus miembros, haciendo que las pruebas de pertenencia (`x in s`) tomen tiempo \\(O(1)\\) frente a la búsqueda lineal \\(O(n)\\) de las listas.
* **Sintaxis y operaciones de teoría de conjuntos:**
  ```python
  lenguajes = {"Python", "C++", "Java"}
  lenguajes.add("Rust")
  
  # Operaciones de álgebra de conjuntos
  a = {1, 2, 3}
  b = {3, 4, 5}
  union = a | b             # {1, 2, 3, 4, 5}
  interseccion = a & b      # {3}
  diferencia = a - b        # {1, 2}
  ```

---

### **2. Técnicas Avanzadas de Manejo en Python**

Python provee construcciones sintácticas idiomáticas para manipular estas estructuras de manera concisa y eficiente:

1. **Comprensiones (*Comprehensions*):**
   Sustituyen bucles acumuladores tradicionales por expresiones compactas de una sola línea:
   ```python
   # Comprensión de lista
   cuadrados = [x**2 for x in range(10) if x % 2 == 0]
   
   # Comprensión de diccionario
   cuadrados_dict = {x: x**2 for x in range(5)}
   
   # Comprensión de conjunto (elimina duplicados automáticamente)
   longitudes = {len(palabra) for palabra in ["sol", "luna", "sol"]}
   ```
2. **Anidación (*Nesting*):**
   Las estructuras pueden contenerse unas dentro de otras sin restricciones de profundidad (por ejemplo, listas de diccionarios, diccionarios cuyos valores son listas o tablas bidimensionales de listas de listas).
3. **Módulo `collections` (Estructuras de Contenedor Especializadas):**
   * **`deque`:** Cola de doble extremo basada en listas doblemente enlazadas; permite inserciones y extracciones rápidas en ambos extremos (\\(O(1)\\)) a diferencia de la lista común.
   * **`defaultdict`:** Diccionario que llama a una fábrica de valores predeterminados cuando se consulta una clave inexistente.
   * **`Counter`:** Subclase de diccionario diseñada para calcular frecuencias y conteos de elementos en iterables.
   * **`namedtuple`:** Generador de clases tupla que permite acceder a los campos tanto por índice como por nombre de atributo, consumiendo menos memoria que un diccionario.

---

### **3. Estructuras No Lineales y Definidas por el Usuario**

Cuando las necesidades del software van más allá de las colecciones básicas (como al trabajar con pilas LIFO, colas FIFO, árboles binarios o grafos), Python permite estructurarlas mediante **clases y programación orientada a objetos**:

* **Pilas (*Stacks*) y Colas (*Queues*):** Se pueden implementar fácilmente utilizando `list` (con `.append()` y `.pop()`) o mediante `collections.deque`.
* **Árboles y Grafos:** Se modelan vinculando instancias de nodos donde cada objeto contiene referencias a sus nodos hijos o adyacentes, o mediante diccionarios de relaciones.
* **Protocolos e Integración con Métodos Dunder:**
  Al definir una clase propia, se pueden sobrecargar métodos especiales para que responda a la sintaxis nativa de Python:
  * `__len__(self)`: Para responder a `len(objeto)`.
  * `__getitem__(self, key)` y `__setitem__(self, key, value)`: Para permitir indexación y acceso como `objeto[clave]`.
  * `__iter__(self)`: Para permitir recorrer la estructura en un bucle `for`.
  * `__contains__(self, item)`: Para responder a comprobaciones de pertenencia con `in`.

---

### **Resumen Comparativo de las Estructuras Nativas**

| Estructura | Sintaxis literal | ¿Ordenada? | ¿Mutable? | ¿Duplicados? | Acceso / Búsqueda |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Lista (`list`)** | `` | Sí | Sí | Sí | Por índice numérico `L[i]` (\\(O(1)\\)); búsqueda lineal con `in` (\\(O(n)\\)). |
| **Tupla (`tuple`)** | `(1, 2, 3)` | Sí | No | Sí | Por índice numérico `T[i]` (\\(O(1)\\)); almacenamiento inmutable de tamaño fijo. |
| **Diccionario (`dict`)** | `{"a": 1, "b": 2}` | Sí (por inserción) | Sí | Claves no, valores sí | Por clave única `D[k]` (\\(O(1)\\) promedio gracias a tabla hash). |
| **Conjunto (`set`)** | `{1, 2, 3}` | No | Sí (`frozenset` no) | No | Comprobación de pertenencia directa `x in S` (\\(O(1)\\) promedio vía hash). |

---

💡 ¿Te gustaría que profundicemos en la implementación práctica de alguna estructura de datos específica (como pilas, colas, árboles binarios) o en el análisis de complejidad algorítmica (\\(O\\) grande) de sus operaciones?