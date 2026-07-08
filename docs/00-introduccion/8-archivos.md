---
id: archivos
title: "Archivos y sistema operativo"
sidebar_label: "🗂️​ Manejo de archivos"
description: "Ingesta de datos y procesos de carga"
sidebar_position: 14
---

El manejo de archivos en Python es una habilidad fundamental. Para trabajar de manera correcta y segura, la mejor práctica en Python moderno es usar un **administrador de contexto** mediante la palabra clave `with`. Esto garantiza que los archivos se cierren automáticamente al terminar, evitando fugas de memoria o corrupción de datos.

A continuación, se presentan tres ejemplos prácticos organizados según las necesidades:

---

### Captura de datos por consola

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

### Creación y Lectura de Archivos Estructurados (`.json`)

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

### Descarga de Archivos desde la Web

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
## Modo lectura y escritura

La diferencia fundamental entre el modo de lectura y el de escritura en Python radica en cómo interactúan con el archivo y qué sucede si este ya existe o no en el sistema de almacenamiento.

A continuación se detallan las disparidades principales según las fuentes:

#### 1. Comportamiento según la existencia del archivo
*   **Modo Lectura (`'r'`):** Es el modo por defecto. Requiere obligatoriamente que el archivo **exista previamente** en la ruta especificada. Si el archivo no se encuentra, Python lanzará una excepción de tipo `FileNotFoundError` o `IOError`.
*   **Modo Escritura (`'w'`):** Si el archivo **no existe**, Python lo **creará automáticamente**.

#### 2. Efecto sobre el contenido (Truncamiento)
*   **Modo Lectura (`'r'`):** Solo permite visualizar o extraer la información. No altera en absoluto el contenido original del archivo.
*   **Modo Escritura (`'w'`):** Si el archivo ya existe, este modo **borra todo su contenido anterior** (proceso conocido como truncamiento) y lo sobreescribe con la nueva información. Esto significa que los datos originales se pierden de forma irreversible al abrir el archivo en este modo.

#### 3. Operaciones y métodos permitidos
*   **Lectura:** Se utilizan métodos como `read()` (lee todo el contenido), `readline()` (lee una sola línea) o `readlines()` (devuelve una lista con todas las líneas).
*   **Escritura:** Se emplean métodos como `write(cadena)` o `writelines(lista_de_cadenas)`. Cabe destacar que `write()` no añade automáticamente saltos de línea, por lo que es necesario incluirlos manualmente con `\n`.

### Resumen comparativo

| Característica | Modo Lectura (`'r'`) | Modo Escritura (`'w'`) |
| :--- | :--- | :--- |
| **Si el archivo existe** | Lo abre para leer | **Sobreescribe/Borra** el contenido |
| **Si el archivo NO existe** | Lanza un error (`FileNotFoundError`) | **Crea** un archivo nuevo |
| **Permisos** | Solo lectura | Solo escritura |
| **Puntero inicial** | Al inicio del archivo | Al inicio (tras borrar el contenido) |

#### Modos relacionados para mayor control
Existen otros modos que resuelven limitaciones de los anteriores:
*   **Modo Anexar (`'a'`):** Abre el archivo para escribir pero, a diferencia de `'w'`, mantiene el contenido existente y **añade los nuevos datos al final** del archivo.
*   **Modo Creación Exclusiva (`'x'`):** Permite escribir pero **falla si el archivo ya existe**, evitando así sobreescrituras accidentales.
*   **Modo Binario (`'b'`):** Se añade a los anteriores (ej. `'rb'` o `'wb'`) para trabajar con archivos que no son de texto plano, como imágenes o ejecutables.


#### Resumen de los Modos de Apertura utilizados:

* **`'w'` (Write):** Abre un archivo de texto exclusivamente para escribir. Si el archivo ya existe, borra su contenido anterior. Si no existe, lo crea.
* **`'r'` (Read):** Abre un archivo de texto para lectura. Lanza un error (`FileNotFoundError`) si el archivo no existe.
* **`'wb'` (Write Binary):** Abre un archivo en formato binario para escribir (imágenes, PDFs, ejecutables).

#### Manejo de los bytes y Unicode

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

#### 1. Interpretación del contenido
*   **Modo Texto (`'t'` o `'r'`):** Trata el contenido del archivo como caracteres Unicode (**strings**). Python decodifica automáticamente los bytes del disco utilizando una codificación específica (usualmente UTF-8) para que el programador reciba texto legible.
*   **Modo Binario (`'b'`):** Accede a los datos en su forma **cruda o pura**, tal como están grabados en el dispositivo de almacenamiento. No se realiza ninguna interpretación ni decodificación de los datos.

#### 2. Tipos de objetos devueltos
*   En el modo texto, las operaciones de lectura devuelven objetos de tipo **`str`**.
*   En el modo binario, las operaciones de lectura devuelven objetos de tipo **`bytes`**. Si intentas escribir un objeto de texto en un archivo abierto en modo binario, o viceversa, Python lanzará un error.

#### 3. Manejo de saltos de línea (EOL)
*   **Modo Texto:** Python suele realizar una **traducción automática** de los caracteres de fin de línea según la plataforma. Por ejemplo, en Windows, puede convertir la secuencia `\r\n` del disco en un simple `\n` al leerlo en el programa.
*   **Modo Binario:** No existe ninguna traducción. Los bytes que representan el salto de línea se leen exactamente como están, lo cual es crítico para archivos que no son texto (donde un byte con el valor de un salto de línea podría representar en realidad un píxel o una muestra de audio).

#### 4. Casos de uso
*   **Modo Texto:** Es el modo predeterminado y se utiliza para archivos que contienen información que las personas pueden leer, como archivos **.txt**, scripts de **.py**, archivos **CSV** o **JSON**.
*   **Modo Binario:** Es imprescindible para archivos multimedia o formatos propietarios que contienen datos estructurados no textuales, tales como **imágenes (JPEG, PNG)**, archivos de **audio**, **PDFs**, **ejecutables** o bases de datos como **SQLite**.

#### Resumen de diferencias clave
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

#### Estructura y Funcionamiento

1.  **`try`**: En este bloque se coloca el código que podría generar una excepción, como abrir un archivo que no existe o procesar datos mal formados. Por seguridad, se recomienda que este bloque sea lo más corto posible.
2.  **`except`**: Se ejecuta únicamente si surge una excepción dentro del bloque `try`. Permite al programador capturar errores específicos (como `FileNotFoundError` si el archivo no se encuentra) y dar un mensaje amigable o una solución en lugar de permitir que el programa falle estrepitosamente.
3.  **`else` (opcional)**: Este código se ejecuta solo si el bloque `try` tuvo éxito y no se lanzó ninguna excepción. Es útil para colocar la lógica que depende totalmente de que el archivo se haya leído correctamente.
4.  **`finally`**: Es el bloque de **limpieza**. Se ejecuta **siempre**, independientemente de si ocurrió un error o no, e incluso si el bloque `try` terminó con una sentencia como `return` o `break`. 

#### Aplicación en la Limpieza de Archivos
La tarea de limpieza más crítica al trabajar con archivos es **cerrarlos** mediante el método `.close()`. No cerrar un archivo puede provocar fugas de memoria, corrupción de datos o errores del sistema operativo que informan que el archivo sigue en uso por otro software.

Al envolver la operación en un `finally`, el programador garantiza que los recursos del sistema se liberen correctamente incluso si se produce un error a mitad de la lectura.

**Ejemplo de implementación:**
```python showLineNumbers
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
Aunque `try-except-finally` es la base del manejo de recursos, se debe destacar que el uso de un **administrador de contexto** (*context manager*) para gestionar los recursos de forma automática. Con la palabra clave **`with`** es la forma más limpia y "pitónica" de lograr el mismo resultado. El bloque `with` asegura automáticamente que el archivo se cierre al finalizar el bloque de código, simplificando la estructura y evitando que el programador olvide la limpieza manual.


A continuación se detalla su funcionamiento y ventajas:

#### Funcionamiento y Sintaxis
La sentencia `with` crea un bloque de código delimitado donde el archivo permanece abierto. Al finalizar dicho bloque, Python se encarga de realizar las tareas de limpieza necesarias.

*   **Estructura básica:** `with open('archivo.txt', 'r') as fh:`.
*   **Apertura:** La función `open()` genera un objeto de archivo que el administrador de contexto vincula a la variable indicada después de la palabra clave `as`.
*   **Cierre automático:** La mayor ventaja es que el método `.close()` se invoca **automáticamente** al salir del bloque, incluso si ocurre una excepción o error durante la ejecución.

#### Ventajas sobre el bloque `try-finally`
Antes del uso extendido de `with`, los programadores debían usar estructuras `try-finally` para asegurar que un archivo se cerrara (llamando a `.close()` en el bloque `finally`).
*   **Legibilidad:** `with` simplifica el código, haciéndolo más conciso y fácil de leer al evitar la gestión manual de cierres.
*   **Seguridad:** Previene errores comunes como fugas de memoria o que el sistema operativo informe que un archivo sigue en uso por otro software porque se olvidó cerrarlo.

#### El protocolo interno del administrador de contexto
Técnicamente, un objeto que funciona con `with` debe implementar dos métodos especiales o "mágicos":
*   **`__enter__()`**: Se ejecuta justo antes de entrar al cuerpo del bloque `with`. Generalmente abre el recurso y lo devuelve para ser usado.
*   **`__exit__()`**: Se ejecuta al salir del bloque. Recibe información sobre cualquier excepción que haya ocurrido (`tipo`, `valor` y `traceback`) y se encarga de cerrar el recurso.

#### Usos avanzados
*   **Múltiples archivos:** Es posible abrir varios archivos en una sola sentencia `with` separándolos por comas, lo cual es muy útil para leer de un origen y escribir en un destino simultáneamente.
*   **Diferentes tipos de recursos:** Además de archivos físicos, este protocolo se usa para **bloqueos de hilos** (*locks*), sesiones de bases de datos, sockets de red y flujos en memoria como `io.StringIO()`.
*   **Integración con `pathlib`:** El módulo moderno para rutas, `pathlib`, también permite usar sus objetos `Path` directamente con `with` mediante el método `.open()`.

**Ejemplo de lectura segura:**
```python showLineNumbers
from pathlib import Path
path = Path('datos.txt')

with path.open(encoding='utf-8') as f:
    for linea in f:
        print(linea.strip())
# Al llegar aquí, el archivo ya está cerrado automáticamente.
```
### Manejo de error

Si intentas abrir o leer un archivo que no existe dentro de un bloque **`try`**, Python genera automáticamente una excepción denominada **`FileNotFoundError`**. 

Lo que sucede a continuación depende de si has definido un bloque `except` para capturar ese error específico:

#### 1. Si la excepción es capturada (`except FileNotFoundError`)
*   **Interrupción inmediata**: En el momento exacto en que Python detecta que el archivo no está, la ejecución de las líneas restantes dentro del bloque `try` se detiene.
*   **Salto al bloque except**: El flujo del programa salta directamente al bloque `except FileNotFoundError`.
*   **Recuperación**: Dentro de este bloque, puedes programar una respuesta controlada, como mostrar un mensaje amigable al usuario indicando que el archivo no se encontró, en lugar de permitir que el programa falle estrepitosamente.
*   **Continuidad**: Una vez ejecutado el código del bloque `except`, el programa puede seguir funcionando normalmente con las instrucciones que sigan después de la estructura `try-except`.

#### 2. Si la excepción NO es capturada
*   **Finalización del programa**: Si no hay un bloque `except` compatible con `FileNotFoundError`, Python detiene la ejecución del programa por completo.
*   **Traceback**: Se mostrará un informe de error detallado o **traceback**, que termina con el mensaje: `FileNotFoundError: [Errno 2] No such file or directory` seguido del nombre del archivo.

#### 3. Otras posibilidades de manejo
*   **Fallos silenciosos**: Puedes usar la sentencia **`pass`** en el bloque `except` si prefieres que el programa simplemente ignore el error y continúe sin notificar al usuario.
*   **Bloque else**: Si el archivo **sí existiera** y se leyera correctamente, el código dentro de un bloque **`else`** (si se incluye) se ejecutaría justo después del `try`, saltándose todos los bloques `except`.
*   **Uso de pathlib**: Una alternativa recomendada es verificar la existencia del archivo antes de intentar abrirlo usando el método **`path.exists()`**, lo que puede evitar lanzar la excepción en primer lugar.

## Ejemplos

Python ofrece múltiples herramientas para trabajar con archivos de datos, desde el módulo estándar `csv` para tareas básicas hasta la biblioteca **Pandas**, que es el estándar para el análisis y manipulación de datos a gran escala.

A continuación, se presentan ejemplos de código organizados por tipo de archivo y operación:

#### 1. Uso del módulo estándar `csv`
Este módulo es ideal para procesar archivos CSV fila por fila sin necesidad de instalar bibliotecas adicionales.

*   **Lectura básica como lista:**
```python showLineNumbers
import csv
with open('presupuesto.csv', 'r') as f:
    lector = csv.reader(f)
    tabla = [fila for row in lector] # Almacena cada fila como una lista
```
*   **Lectura como diccionario (mejor legibilidad):**
El uso de `DictReader` permite acceder a cada columna por su nombre definido en el encabezado.
```python showLineNumbers
with open('datos.csv', 'rt') as f:
    lector_dict = csv.DictReader(f)
    for fila in lector_dict:
        print(f"Usuario: {fila['nombre']}, Edad: {fila['edad']}")
```
*   **Escritura de archivos:**
```python showLineNumbers
datos = [["nombre", "edad"], ["Alice", 30], ["Bob", 25]]
with open('salida.csv', 'w', newline='') as f:
    escritor = csv.writer(f)
    escritor.writerows(datos)
```

#### 2. Carga de datos con Pandas (CSV y Excel)
Pandas simplifica la carga al convertir automáticamente los archivos en un objeto **DataFrame**, permitiendo inferir tipos de datos y manejar encabezados de forma inteligente.

*   **Carga de CSV:**
```python showLineNumbers
import pandas as pd
# Carga básica e inspección de las primeras 5 filas
df = pd.read_csv("archivo.csv")
print(df.head())

# Carga con manejo de errores si el archivo no existe
try:
    df_v = pd.read_csv("datos/ventas.csv")
except FileNotFoundError:
    print("Error: El archivo no fue encontrado.")
```
*   **Carga de Excel:**
Para leer archivos `.xlsx` o `.xls`, Pandas utiliza motores internos como `openpyxl` o `xlrd`, que deben estar instalados.
```python showLineNumbers
# Leer una hoja específica de un libro de Excel
df_excel = pd.read_excel("informe.xlsx", sheet_name="Hoja1")
```

#### 3. Manipulación y limpieza de datos con Pandas
Una vez cargados, los datos a menudo requieren limpieza (limpiar valores nulos o duplicados) antes de ser analizados.

*   **Limpieza de valores nulos y duplicados:**
```python showLineNumbers
# Rellenar valores faltantes con el promedio de la columna
df['monto'].fillna(df['monto'].mean(), inplace=True)

# Eliminar filas que tengan datos duplicados
df_limpio = df.drop_duplicates()
```
*   **Filtrado y selección:**
```python showLineNumbers
# Seleccionar filas basadas en una condición (ej. valores mayores a 10)
filtrado = df[df['valor'] > 10]

# Selección por etiquetas de fila y columna
subconjunto = df.loc[0:10, ['nombre', 'fecha']]
```

#### 4. Agregación y Exportación
La manipulación final suele implicar resumir los datos y guardarlos en un nuevo formato.

*   **Agrupamiento (GroupBy):**
```python showLineNumbers
# Calcular el promedio de propinas agrupado por día y fumadores
resumen = df.groupby(['dia', 'fumador'])['propina'].mean()
```
*   **Exportación de resultados:**
```python showLineNumbers
# Guardar el DataFrame procesado a un nuevo CSV sin el índice automático
df.to_csv("resultados.csv", index=False)

# Guardar a Excel (requiere openpyxl)
df.to_excel("resultados.xlsx", sheet_name="Final")
```

**Nota técnica:** Al exportar a Excel desde Pandas, es importante asegurar que las fechas no tengan información de zona horaria, ya que el formato de Excel no siempre las soporta directamente.


#### 💻 Código:
<Tabs>
<TabItem value="file" label="Antecedentes" default>
<div class="alert alert--primary">
**EJEMPLO:**<br />
Cargar un archivo 'csv' con información de covid a nivel regional, sumar los totales de cada region y crear un nuevo archivo resumen 'csv' con esta información.

**Descarga el archivo csv**: [datos-covid-por-region.csv](/data/datos-covid-por-region.csv)

</div>
</TabItem>
<TabItem value="file-csv" label="CSV" default>
```python showLineNumbers
# Implementación en Python con csv
import csv

# Diccionario para almacenar la suma por región
totales_por_region = {}

# 1. Leer el archivo original
with open('datos-covid-por-region.csv', mode='r', encoding='utf-8') as archivo_entrada:
    lector_csv = csv.DictReader(archivo_entrada)
    
    for fila in lector_csv:
        region = fila['Region']
        
        # Evitamos sumar las filas que correspondan al gran total del archivo original
        if region.lower() == 'total':
            continue
            
        # Convertir el valor a flotante (o entero si estás seguro de que no hay decimales)
        total_casos = float(fila['Total'])
        
        # Acumular el total por región
        if region in totales_por_region:
            totales_por_region[region] += total_casos
        else:
            totales_por_region[region] = total_casos

# 2. Ordenar las regiones por el valor total de forma descendente
regiones_ordenadas = sorted(totales_por_region.items(), key=lambda x: x[1], reverse=True)

# 3. Crear y escribir el nuevo archivo de resumen
with open('resumen-covid.csv', mode='w', newline='', encoding='utf-8') as archivo_salida:
    escritor_csv = csv.writer(archivo_salida)
    
    # Escribir los encabezados
    escritor_csv.writerow(['Region', 'Total'])
    
    # Escribir los datos ordenados
    for region, total in regiones_ordenadas:
        escritor_csv.writerow([region, total])

print("El archivo 'resumen-covid.csv' ha sido creado exitosamente.")
```
</TabItem>
<TabItem value="file-pandas" label="Pandas" default>
```python showLineNumbers
# Implementación en Python con Pandas
import pandas as pd

# 1. Leer el archivo CSV adjunto
df = pd.read_csv('datos-covid-por-region.csv')

# Opcional: Filtrar la fila 'Total' si el archivo original ya incluye una fila de suma global
df = df[df['Region'] != 'Total']

# 2. Agrupar por 'Region', sumar la columna 'Total' y ordenar de forma descendente
resumen = df.groupby('Region')['Total'].sum().reset_index()
resumen = resumen.sort_values(by='Total', ascending=False)

# 3. Guardar el resultado en un nuevo archivo CSV
resumen.to_csv('resumen-covid.csv', index=False)

print("El archivo 'resumen-covid.csv' ha sido creado exitosamente.")
```
</TabItem>
</Tabs>


