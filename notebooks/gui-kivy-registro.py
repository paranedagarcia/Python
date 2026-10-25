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