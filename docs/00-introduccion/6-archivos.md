---
id: archivos
title: "Archivos y sistema operativo"
sidebar_label: "Archivos"
description: "Ingesta de datos y procesos de carga"
sidebar_position: 11
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