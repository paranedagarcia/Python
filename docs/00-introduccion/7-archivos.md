---
id: archivos
title: "Archivos y sistema operativo"
sidebar_label: "🗂️​ Manejo de archivos"
description: "Ingesta de datos y procesos de carga"
sidebar_position: 12
---

El manejo de archivos en Python es una habilidad fundamental. Para trabajar de manera correcta y segura, la mejor práctica en Python moderno es usar un **administrador de contexto** mediante la palabra clave `with`. Esto garantiza que los archivos se cierren automáticamente al terminar, evitando fugas de memoria o corrupción de datos.

A continuación, se presentan tres ejemplos prácticos organizados según las necesidades:

---

### Captura de datos por consola y Creación de un Archivo Local (`.txt`)

Este ejemplo captura información ingresada por un usuario en la terminal y la guarda de forma interactiva en un archivo de texto local.

```python showLineNumbers title="Guardar datos en un archivo local"
def capturar_y_guardar_datos():
    print("--- Captura de Datos para Archivo Local ---")
    
    # Capturar datos desde la terminal
    nombre = input("Introduce tu nombre: ")
    edad = input("Introduce tu edad: ")
    ciudad = input("Introduce tu ciudad: ")
    
    nombre_archivo = "datos_usuario.txt"
    
    # El modo 'w' crea el archivo (o lo sobrescribe si ya existe)
    # encoding='utf-8' asegura soporte para tildes y eñes
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(f"Registro de Usuario\n")
        archivo.write(f"-------------------\n")
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Edad: {edad}\n")
        archivo.write(f"Ciudad: {ciudad}\n")
        
    print(f"\n¡Éxito! Los datos han sido guardados localmente en '{nombre_archivo}'.")

if __name__ == "__main__":
    capturar_y_guardar_datos()

```

---

### Creación y Lectura de Archivos Locales Estructurados (`.json`)

Para almacenar datos complejos recopilados del sistema o del usuario, se suele preferir el formato JSON (JavaScript Object Notation), ya que mantiene la estructura nativa de los diccionarios y listas de Python.

```python showLineNumbers
import json

def gestionar_archivo_json():
    print("\n--- Generación de Archivo Estructurado JSON ---")
    
    # Datos capturados en una estructura de diccionario
    productos_capturados = [
        {"id": 1, "nombre": "Teclado Mecánico", "precio": 85.50},
        {"id": 2, "nombre": "Ratón Inalámbrico", "precio": 45.00},
        {"id": 3, "nombre": "Monitor 4K", "precio": 320.00}
    ]
    
    nombre_json = "inventario.json"
    
    # Guardar estructura en el archivo local
    with open(nombre_json, "w", encoding="utf-8") as archivo:
        # json.dump convierte el objeto Python a texto JSON estructurado
        json.dump(productos_capturados, archivo, indent=4, ensure_ascii=False)
    print(f"Archivo '{nombre_json}' creado con éxito.")
    
    # Leer el archivo local para verificar el contenido escrito
    print("\nLeyendo el contenido guardado...")
    with open(nombre_json, "r", encoding="utf-8") as archivo:
        datos_leidos = json.load(archivo)
        for producto in datos_leidos:
            print(f"- {producto['nombre']}: ${producto['precio']}")

if __name__ == "__main__":
    gestionar_archivo_json()

```

---

### Descarga de Archivos desde la Web y Creación de Réplica Local

Para trabajar con archivos en la web, se utiliza comúnmente la biblioteca externa `requests` (debe ser instalada previamente ejecutando `pip install requests`). Este script realiza una petición HTTP a un servidor web para descargar un archivo (en este caso, un logo o imagen) y guardarlo en el disco duro local.

```python showLineNumbers title="Manejo de archivos desde Internet"
import requests

def descargar_archivo_web():
    print("\n--- Captura y Creación de Archivos desde la Web ---")
    
    # URL de un recurso público en la web (una imagen de ejemplo)
    url_web = "https://www.python.org/static/img/python-logo.png"
    nombre_local = "logo_python_descargado.png"
    
    try:
        # Realizar la petición GET para descargar el contenido web
        print(f"Conectando con {url_web}...")
        respuesta = requests.get(url_web, timeout=10)
        
        # Verificar que la conexión web fue exitosa (Código HTTP 200)
        if respuesta.status_code == 200:
            # Se usa el modo 'wb' (Write Binary) porque es un elemento binario (imagen)
            with open(nombre_local, "wb") as archivo_binario:
                archivo_binario.write(respuesta.content)
            print(f"¡Éxito! El archivo web ha sido guardado localmente como '{nombre_local}'.")
        else:
            print(f"Error en la web: El servidor respondió con el código {respuesta.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Ocurrió un error al intentar acceder al archivo web: {e}")

if __name__ == "__main__":
    descargar_archivo_web()

```

### Resumen de los Modos de Apertura utilizados:

* **`'w'` (Write):** Abre un archivo de texto exclusivamente para escribir. Si el archivo ya existe, borra su contenido anterior. Si no existe, lo crea.
* **`'r'` (Read):** Abre un archivo de texto para lectura. Lanza un error (`FileNotFoundError`) si el archivo no existe.
* **`'wb'` (Write Binary):** Abre un archivo en formato binario para escribir (imágenes, PDFs, ejecutables).

### manejan los bytes y Unicode al leer archivos

El manejo de archivos en Python distingue fundamentalmente entre datos de texto (**Unicode**) y datos binarios (**bytes**). Aunque físicamente todos los archivos son secuencias de bytes almacenados en disco, la forma en que Python los interpreta depende del modo en que se abran.

A continuación se detalla cómo se gestionan estos conceptos:

#### Modos de lectura: Texto vs. Binario
*   **Modo Texto (`'rt'` o `'r'`):** Es el comportamiento predeterminado. Python lee los bytes del archivo y los decodifica automáticamente a una cadena de caracteres Unicode (`str`).
*   **Modo Binario (`'rb'`):** Se utiliza para archivos que no son texto plano, como imágenes, audios o ejecutables. En este modo, Python devuelve objetos de tipo `bytes` sin realizar ninguna decodificación ni traducción de saltos de línea.

#### La importancia de la codificación (Encoding)
Al leer archivos en modo texto, es fundamental especificar el parámetro **`encoding`** (usualmente `'utf-8'`).
*   **Dependencia de la plataforma:** Si no se indica, Python utiliza la codificación predeterminada del sistema, que varía según el sistema operativo y puede causar errores al mover el código entre máquinas.
*   **Errores de decodificación:** Si se intenta leer un archivo con una codificación incorrecta (por ejemplo, intentar leer bytes no-ASCII como si fueran ASCII), Python lanzará una excepción **`UnicodeDecodeError`**.

#### La lógica de conversión: Encode y Decode
Python utiliza un modelo claro para transformar datos:
*   **Decoding (Decodificación):** Es el proceso de convertir **bytes en texto** Unicode. Se usa el método `.decode()` sobre un objeto de bytes.
*   **Encoding (Codificación):** Es el proceso inverso, convertir **texto Unicode en bytes** para guardarlos o enviarlos por red. Se usa el método `.encode()` sobre una cadena.
*   **Regla mnemotécnica:** "Codificamos el texto plano para crear bytes; decodificamos bytes para recuperar el texto".

#### Manejo de bytes específicos
Al trabajar en binario, Python maneja bytes individuales como números enteros entre 0 y 255.
*   **Representación canónica:** Python muestra los bytes que coinciden con caracteres ASCII como letras (ej. `b'A'`) y los demás como códigos hexadecimales (ej. `\xc3\xb1` para la 'ñ' en UTF-8).
*   **Interpretación de estructuras:** Para archivos binarios con formatos fijos (como encabezados de imágenes), se utiliza el módulo **`struct`** y su función `unpack` para interpretar secuencias de bytes como números enteros o de punto flotante, considerando el orden de los bytes (*Big-endian* o *Little-endian*).

#### Herramientas modernas y eficiencia
*   **`pathlib`:** Este módulo ofrece métodos simplificados como `read_text(encoding='utf-8')` para obtener directamente el texto decodificado, o `read_bytes()` para obtener el contenido binario sin abrir manualmente el archivo.
*   **Lectura iterativa:** Para archivos grandes, es más eficiente leer el archivo **línea por línea** (en modo texto) o en **bloques de tamaño fijo** (en modo binario) para evitar saturar la memoria RAM del sistema.

La diferencia fundamental entre el modo texto y el modo binario al manejar archivos en Python radica en cómo el lenguaje interpreta y transforma los bytes almacenados en el disco para entregarlos al programador. Aunque físicamente **todos los archivos son secuencias de bytes**, Python ofrece el modo texto como una abstracción para facilitar el trabajo con caracteres legibles.

A continuación se detallan las principales diferencias según las fuentes:

### 1. Interpretación del contenido
*   **Modo Texto (`'t'` o `'r'`):** Trata el contenido del archivo como caracteres Unicode (**strings**). Python decodifica automáticamente los bytes del disco utilizando una codificación específica (usualmente UTF-8) para que el programador reciba texto legible.
*   **Modo Binario (`'b'`):** Accede a los datos en su forma **cruda o pura**, tal como están grabados en el dispositivo de almacenamiento. No se realiza ninguna interpretación ni decodificación de los datos.

### 2. Tipos de objetos devueltos
*   En el modo texto, las operaciones de lectura devuelven objetos de tipo **`str`**.
*   En el modo binario, las operaciones de lectura devuelven objetos de tipo **`bytes`**. Si intentas escribir un objeto de texto en un archivo abierto en modo binario, o viceversa, Python lanzará un error.

### 3. Manejo de saltos de línea (EOL)
*   **Modo Texto:** Python suele realizar una **traducción automática** de los caracteres de fin de línea según la plataforma. Por ejemplo, en Windows, puede convertir la secuencia `\r\n` del disco en un simple `\n` al leerlo en el programa.
*   **Modo Binario:** No existe ninguna traducción. Los bytes que representan el salto de línea se leen exactamente como están, lo cual es crítico para archivos que no son texto (donde un byte con el valor de un salto de línea podría representar en realidad un píxel o una muestra de audio).

### 4. Casos de uso
*   **Modo Texto:** Es el modo predeterminado y se utiliza para archivos que contienen información que las personas pueden leer, como archivos **.txt**, scripts de **.py**, archivos **CSV** o **JSON**.
*   **Modo Binario:** Es imprescindible para archivos multimedia o formatos propietarios que contienen datos estructurados no textuales, tales como **imágenes (JPEG, PNG)**, archivos de **audio**, **PDFs**, **ejecutables** o bases de datos como **SQLite**.

### Resumen de diferencias clave
| Característica | Modo Texto (`'rt'`) | Modo Binario (`'rb'`) |
| :--- | :--- | :--- |
| **Tipo de dato** | `str` (Unicode) | `bytes` |
| **Codificación** | Automática (ej. UTF-8) | Ninguna (bytes crudos) |
| **Saltos de línea** | Se traducen (ej. `\r\n` a `\n`) | Se mantienen intactos |
| **Uso principal** | Documentos legibles y código | Imágenes, audio, ejecutables |

Como nota importante, las fuentes recomiendan usar siempre la sentencia **`with`** (administrador de contexto) independientemente del modo, para asegurar que los recursos se liberen y el archivo se cierre correctamente al finalizar la operación.

### Try-except para limpieza de archivos

El uso de la estructura **`try-except-finally`** en Python es una práctica esencial para garantizar la robustez de los programas, especialmente al interactuar con recursos externos como los archivos. Esta construcción permite manejar errores inesperados y asegurar que las tareas de limpieza, como cerrar un archivo, se realicen sin importar lo que ocurra durante la ejecución.

A continuación, se detalla la función de cada bloque en este contexto:

### Estructura y Funcionamiento

1.  **`try`**: En este bloque se coloca el código que podría generar una excepción, como abrir un archivo que no existe o procesar datos mal formados. Por seguridad, se recomienda que este bloque sea lo más corto posible.
2.  **`except`**: Se ejecuta únicamente si surge una excepción dentro del bloque `try`. Permite al programador capturar errores específicos (como `FileNotFoundError` si el archivo no se encuentra) y dar un mensaje amigable o una solución en lugar de permitir que el programa falle estrepitosamente.
3.  **`else` (opcional)**: Este código se ejecuta solo si el bloque `try` tuvo éxito y no se lanzó ninguna excepción. Es útil para colocar la lógica que depende totalmente de que el archivo se haya leído correctamente.
4.  **`finally`**: Es el bloque de **limpieza**. Se ejecuta **siempre**, independientemente de si ocurrió un error o no, e incluso si el bloque `try` terminó con una sentencia como `return` o `break`. 

### Aplicación en la Limpieza de Archivos
La tarea de limpieza más crítica al trabajar con archivos es **cerrarlos** mediante el método `.close()`. No cerrar un archivo puede provocar fugas de memoria, corrupción de datos o errores del sistema operativo que informan que el archivo sigue en uso por otro software.

Al envolver la operación en un `finally`, el programador garantiza que los recursos del sistema se liberen correctamente incluso si se produce un error a mitad de la lectura.

**Ejemplo de implementación:**
```python
f = open('datos.txt', 'r')
try:
    # Código para procesar el contenido del archivo
    contenido = f.read()
except IOError:
    print("Ocurrió un error al leer el archivo")
finally:
    # Esta línea se ejecuta pase lo que pase
    f.close() 
    print("Archivo cerrado correctamente")
```
**

### La Alternativa Moderna: `with`
Aunque `try-except-finally` es la base del manejo de recursos, las fuentes destacan que el uso de un **administrador de contexto** con la palabra clave **`with`** es la forma más limpia y "pitónica" de lograr el mismo resultado. El bloque `with` asegura automáticamente que el archivo se cierre al finalizar el bloque de código, simplificando la estructura y evitando que el programador olvide la limpieza manual.