---
id: kivy
title: "Kivy"
sidebar_label: "🖥️ Kivy"
description: "Kivy"
---

## **Kivy UI**

**Kivy** es un *framework* o biblioteca de terceros de código abierto en Python diseñado para el desarrollo de **interfaces gráficas de usuario (GUI)** e **interfaces naturales de usuario (NUI)** con capacidades multitáctiles. 

A diferencia de librerías como Tkinter o PyQt (pensadas principalmente para escritorios tradicionales), Kivy fue concebido bajo el principio de **"escribir una vez y ejecutar en todas partes"**, permitiendo que una misma base de código funcione sin cambios tanto en sistemas operativos de escritorio (Windows, macOS, Linux) como en dispositivos móviles (Android e iOS).

---

### Características Clave

* **Soporte Multiplataforma y Móvil:** Permite compilar y empaquetar aplicaciones en archivos ejecutables nativos para escritorio o en paquetes para dispositivos móviles (`.apk` en Android y `.ipa` en iOS) utilizando herramientas como *Buildozer* o *Briefcase*.
* **Aceleración por Hardware:** Utiliza OpenGL ES 2 para renderizar gráficos de forma fluida y rápida en pantallas táctiles y monitores.
* **Lenguaje KV (Kv Design Language):** Dispone de un lenguaje declarativo propio para separar el diseño de la interfaz visual de la lógica de programación en Python.
* **Manejo de Eventos y Táctil:** Orientado a eventos de usuario complejos, como gestos táctiles, giroscopio, acelerómetro y entradas compuestas.

---

### Casos de Uso y Ejemplos

1. **Aplicaciones Móviles para Android e iOS:**
   Permite construir herramientas y utilidades completas instalables directamente desde la Play Store o App Store (como sincronizadores de archivos, gestores de tareas o paneles de control).

2. **Desarrollo de Videojuegos 2D:**
   Es una opción popular en la industria del videojuego en Python junto a paquetes como *Pygame* y *Panda3D* para crear juegos interactivos con animaciones.

3. **Quioscos y Pantallas Táctiles Interactivas:**
   Ideal para aplicaciones industriales, cajeros, terminales de punto de venta (POS) o proyectos con Raspberry Pi que requieran pantallas táctiles dedicadas.
4. **Procesamiento de Imágenes y Gráficos:**

   Se emplea en herramientas científicas y visualizadores interactivos que combinan procesamiento gráfico con la pila de bibliotecas como *Pillow* u *OpenCV*.

---

### Ejemplo Básico

Para ejecutar una aplicación mínima en Kivy se define una clase que hereda de `App` y un método `build()` que retorna la jerarquía de componentes visuales (*widgets*):

```python showLineNumbers
from kivy.app import App
from kivy.uix.button import Button

class MiAplicacion(App):
    def build(self):
        # Retorna un botón interactivo como widget principal
        return Button(
            text="¡Hola desde Kivy!",
            font_size=24,
            background_color=(0.1, 0.5, 0.8, 1)
        )

if __name__ == "__main__":
    MiAplicacion().run()
```

---
## **Uso de clases**

En **Kivy**, la arquitectura orientada a objetos se estructura combinando **clases de Python** para la lógica de control y datos con el **lenguaje declarativo KV (`.kv`)** para la capa de diseño gráfico.

---

### Componentes Jerárquicos Principales

1. **Clase de la Aplicación (`kivy.app.App`)**:
   Es la clase raíz que gestiona el ciclo de vida del programa. Hereda de `App` y debe implementar el método **`build()`**, el cual retorna el widget principal que se mostrará en pantalla.

2. **Clases de Contenedores o Layouts (`BoxLayout`, `GridLayout`, `FloatLayout`)**:
   Estructuran la posición y dimensión de los elementos visuales. Se suelen heredar para crear pantallas o secciones compuestas.

3. **Clases de Widgets (`Button`, `Label`, `TextInput`)**:
   Elementos interactivos individuales. Kivy incluye **propiedades especiales** (`StringProperty`, `NumericProperty`, `BooleanProperty`, `ObjectProperty`) que crean un enlace de datos automático (*Data Binding*) entre el código Python y la interfaz.



### Estructuración Típica
**Python + Lenguaje KV**

La buena práctica en Kivy es aislar la lógica en Python y el diseño visual en un archivo con extensión `.kv`.

#### **Paso A: Lógica de Clases en Python (`main.py`)**

```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

# 1. Clase contenedora personalizada (Layout / Pantalla)
class FormularioLogin(BoxLayout):
    # Propiedad reactiva de Kivy para Data Binding automático
    mensaje_estado = StringProperty("Ingresa tus credenciales")

    def validar_ingreso(self, usuario, clave):
        if usuario.strip() and clave.strip():
            self.mensaje_estado = f"¡Bienvenido, {usuario}!"
        else:
            self.mensaje_estado = "Error: Campos incompletos"

# 2. Clase Principal de la Aplicación
class LoginApp(App):
    def build(self):
        return FormularioLogin()

if __name__ == "__main__":
    LoginApp().run()
```

#### **Paso B: Definición Visual en Lenguaje KV (`login.kv`)**

Kivy asocia automáticamente el archivo `.kv` con la clase de la aplicación si sigue la convención de nombres: para `LoginApp(App)`, busca un archivo llamado `login.kv` (remueve la palabra "App" y convierte a minúsculas).

```kv
<FormularioLogin>:
    orientation: 'vertical'
    padding: 20
    spacing: 12

    Label:
        text: 'Inicio de Sesión'
        font_size: 22
        size_hint_y: None
        height: 40

    TextInput:
        id: txt_usuario
        hint_text: 'Nombre de usuario'
        multiline: False
        size_hint_y: None
        height: 40

    TextInput:
        id: txt_clave
        hint_text: 'Contraseña'
        password: True
        multiline: False
        size_hint_y: None
        height: 40

    Button:
        text: 'Ingresar'
        size_hint_y: None
        height: 45
        on_press: root.validar_ingreso(txt_usuario.text, txt_clave.text)

    Label:
        text: root.mensaje_estado
        font_size: 14
        color: 0.2, 0.8, 0.2, 1
```



### Elementos Clave del Diseño de Clases

* **Palabra clave `root`**: En el archivo `.kv`, `root` hace referencia a la instancia de la clase Python contenedora (`FormularioLogin`).

* **Palabra clave `app`**: Hace referencia a la instancia activa de la clase `App` (`LoginApp`).

* **Acceso mediante `id`**: Al definir un `id` en el archivo KV (como `id: txt_usuario`), Python puede acceder a ese widget mediante el diccionario `self.ids.txt_usuario`.

* **Propiedades Reactivas (`Property`)**: Cuando modificas el valor de `self.mensaje_estado` en Python, la etiqueta visual asociada en el archivo `.kv` se actualiza inmediatamente en pantalla sin llamar a métodos de refresco manuales.

---


## **Ejemplo registro de usuarios**

Para construir una interfaz en **Kivy** que integre un **formulario de ingreso de datos** y una **tabla de resultados en la misma ventana**, la arquitectura recomendada combina un `BoxLayout` horizontal principal dividido en dos secciones:

1. **Panel Izquierdo (Formulario de Ingreso / Data Entry):** Utiliza campos `TextInput` para capturar el nombre, correo y rol del usuario, junto con un `Button` para procesar la acción.
2. **Panel Derecho (Tabla Dinámica de Resultados):** Combina un `ScrollView` con un `GridLayout` interno para permitir el desplazamiento vertical de las filas de usuarios a medida que se agregan nuevos registros.

He generado el archivo ejecutable **`kivy_registro_tabla.py`** (disponible en tu panel Studio), el cual utiliza el **lenguaje declarativo KV** integrado directamente en el script mediante `Builder.load_string`.


<details>
<summary>🖥️ Código de ejemplo</summary>

```python
"""
Ejemplo de Aplicación en Kivy: Registro de Usuarios y Tabla de Resultados
Integra el ingreso de datos (formulario) y la visualización tabular
desplazable en la misma ventana.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder

# Diseño declarativo de la interfaz gráfica en Lenguaje KV
KV_DESIGN = """
<MainWidget>:
    orientation: 'horizontal'
    padding: 15
    spacing: 15

    # -------------------------------------------------------------
    # PANEL IZQUIERDO: Formulario de Ingreso de Datos (Data Entry)
    # -------------------------------------------------------------
    BoxLayout:
        orientation: 'vertical'
        size_hint_x: 0.38
        spacing: 10
        padding: 12
        canvas.before:
            Color:
                rgba: 0.15, 0.18, 0.24, 1
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: 'Ingreso de Usuario'
            font_size: '18sp'
            bold: True
            size_hint_y: None
            height: '35dp'
            color: 0.3, 0.7, 1, 1

        Label:
            text: 'Nombre Completo:'
            size_hint_y: None
            height: '25dp'
            halign: 'left'
            text_size: self.size

        TextInput:
            id: txt_nombre
            hint_text: 'Ej. María Silva'
            multiline: False
            size_hint_y: None
            height: '38dp'

        Label:
            text: 'Correo Electrónico:'
            size_hint_y: None
            height: '25dp'
            halign: 'left'
            text_size: self.size

        TextInput:
            id: txt_email
            hint_text: 'maria@ejemplo.com'
            multiline: False
            size_hint_y: None
            height: '38dp'

        Label:
            text: 'Rol / Cargo:'
            size_hint_y: None
            height: '25dp'
            halign: 'left'
            text_size: self.size

        TextInput:
            id: txt_rol
            hint_text: 'Ej. Desarrolladora'
            multiline: False
            size_hint_y: None
            height: '38dp'

        Button:
            text: 'Registrar Usuario'
            bold: True
            size_hint_y: None
            height: '45dp'
            background_normal: ''
            background_color: 0.15, 0.55, 0.9, 1
            on_press: root.agregar_usuario()

        Label:
            id: lbl_mensaje
            text: ''
            color: 0.4, 0.9, 0.5, 1
            size_hint_y: None
            height: '30dp'

        Widget:
            # Espaciador flexible para mantener alineados los campos arriba
            size_hint_y: 1

    # -------------------------------------------------------------
    # PANEL DERECHO: Tabla de Resultados (ScrollView + GridLayout)
    # -------------------------------------------------------------
    BoxLayout:
        orientation: 'vertical'
        size_hint_x: 0.62
        spacing: 10
        padding: 12
        canvas.before:
            Color:
                rgba: 0.11, 0.13, 0.17, 1
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: 'Lista de Usuarios Registrados'
            font_size: '18sp'
            bold: True
            size_hint_y: None
            height: '35dp'
            color: 1, 1, 1, 1

        # Encabezados de la Tabla
        GridLayout:
            cols: 4
            size_hint_y: None
            height: '38dp'
            spacing: 2
            canvas.before:
                Color:
                    rgba: 0.22, 0.28, 0.38, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

            Label:
                text: 'ID'
                bold: True
                size_hint_x: 0.15
            Label:
                text: 'Nombre'
                bold: True
                size_hint_x: 0.35
            Label:
                text: 'Correo'
                bold: True
                size_hint_x: 0.30
            Label:
                text: 'Rol'
                bold: True
                size_hint_x: 0.20

        # Áreas con desplazamiento vertical (Tabla con Scroll)
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True

            GridLayout:
                id: tabla_grid
                cols: 4
                size_hint_y: None
                height: self.minimum_height
                spacing: 2
                row_default_height: '36dp'
                row_force_default: True
"""

class MainWidget(BoxLayout):
    contador_id = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Registros iniciales de muestra
        self.agregar_registro_muestra("Ana Martínez", "ana@empresa.com", "Administradora")
        self.agregar_registro_muestra("Carlos López", "carlos@empresa.com", "Desarrollador")
        self.agregar_registro_muestra("Sofia Torres", "sofia@empresa.com", "Diseñadora UX")

    def agregar_registro_muestra(self, nombre, email, rol):
        self._insertar_fila_tabla(self.contador_id, nombre, email, rol)
        self.contador_id += 1

    def agregar_usuario(self):
        nombre = self.ids.txt_nombre.text.strip()
        email = self.ids.txt_email.text.strip()
        rol = self.ids.txt_rol.text.strip()

        # Validación básica de campos vacíos
        if not nombre or not email or not rol:
            self.ids.lbl_mensaje.color = (1, 0.4, 0.4, 1)
            self.ids.lbl_mensaje.text = "Por favor completa todos los campos."
            return

        self._insertar_fila_tabla(self.contador_id, nombre, email, rol)
        self.contador_id += 1

        # Limpiar formulario
        self.ids.txt_nombre.text = ""
        self.ids.txt_email.text = ""
        self.ids.txt_rol.text = ""
        self.ids.lbl_mensaje.color = (0.4, 0.9, 0.5, 1)
        self.ids.lbl_mensaje.text = "¡Usuario registrado con éxito!"

    def _insertar_fila_tabla(self, user_id, nombre, email, rol):
        tabla = self.ids.tabla_grid

        # Creación de celdas simples para la fila
        cell_id = Label(text=str(user_id), size_hint_x=0.15, color=(0.8, 0.8, 0.8, 1))
        cell_nombre = Label(text=nombre, size_hint_x=0.35, color=(1, 1, 1, 1))
        cell_email = Label(text=email, size_hint_x=0.30, color=(0.8, 0.9, 1, 1))
        cell_rol = Label(text=rol, size_hint_x=0.20, color=(0.9, 0.9, 0.9, 1))

        # Insertar etiquetas en el GridLayout de la tabla
        tabla.add_widget(cell_id)
        tabla.add_widget(cell_nombre)
        tabla.add_widget(cell_email)
        tabla.add_widget(cell_rol)

class KivyTablaApp(App):
    def build(self):
        self.title = "Kivy - Ingreso de Datos y Tabla de Resultados"
        Builder.load_string(KV_DESIGN)
        return MainWidget()

if __name__ == "__main__":
    KivyTablaApp().run()
```
</details>


#### Puntos Clave del Diseño

1. **Lectura directa mediante identificadores (`self.ids`):**
   Al definir `id: txt_nombre` en el código KV, Python puede leer o modificar el valor ingresado mediante `self.ids.txt_nombre.text`.

2. **Tablas ajustables con `ScrollView` + `GridLayout`:**
   Al asignar `height: self.minimum_height` al `GridLayout` interno, Kivy expande automáticamente la altura del contenedor a medida que se insertan nuevas filas, permitiendo un desplazamiento fluido cuando la lista supera el alto de la ventana.

3. **Control del tamaño relativo (`size_hint_x`):**
   Garantiza que las columnas de ID, Nombre, Correo y Rol mantengan proporciones armónicas tanto en la cabecera como en las filas insertadas.

---

