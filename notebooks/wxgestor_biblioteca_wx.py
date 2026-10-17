#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Administración de Biblioteca
=========================================
Demostración de Composición en Programación Orientada a Objetos (POO)
con Persistencia en SQLite3 e Interfaz Gráfica wxPython.

Conceptos Clave de POO Aplicados:
---------------------------------
1. Composición ("Tiene-Un"):
   - La clase `Biblioteca` posee una lista de instancias de la clase `Libro`.
   - La vida útil y gestión del conjunto de libros es coordinada por la biblioteca.
2. Encapsulamiento:
   - La interacción con la base de datos y la colección en memoria se realiza
     a través de métodos públicos de la `Biblioteca`.
"""

import sqlite3
from typing import List, Optional

# Intentamos importar wxPython
try:
    import wx
    WX_DISPONIBLE = True
except ImportError:
    WX_DISPONIBLE = False


# ==============================================================================
# MODELO DE DOMINIO Y COMPOSICIÓN (POO)
# ==============================================================================

class Libro:
    """
    Representa la entidad Libro.
    """
    def __init__(self, titulo: str, autor: str, anio_publicacion: int, id_libro: Optional[int] = None):
        self.id = id_libro
        self.titulo = titulo.strip()
        self.autor = autor.strip()
        self.anio_publicacion = int(anio_publicacion)

    def __repr__(self) -> str:
        return f"Libro(id={self.id}, titulo='{self.titulo}', autor='{self.autor}', anio={self.anio_publicacion})"


class Biblioteca:
    """
    Clase compuesta que administra una colección de objetos `Libro` ("Tiene-Un").
    Gestiona la persistencia en una base de datos SQLite v3 local.
    """
    def __init__(self, nombre: str, db_path: str = "biblioteca.db"):
        self.nombre = nombre
        self.db_path = db_path
        
        # ATRIBUTO DE COMPOSICIÓN: Lista de objetos Libro
        self.libros: List[Libro] = []
        
        self._inicializar_base_datos()
        self.cargar_libros_desde_db()
        self._asegurar_libros_iniciales()

    def _inicializar_base_datos(self):
        """Crea la tabla de libros en SQLite3 si aún no existe."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS libros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    anio_publicacion INTEGER NOT NULL,
                    biblioteca_nombre TEXT NOT NULL
                )
            """)
            conn.commit()

    def cargar_libros_desde_db(self):
        """
        Carga los libros desde SQLite3 y puebla la lista compuesta `self.libros`.
        """
        self.libros.clear()
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, titulo, autor, anio_publicacion FROM libros WHERE biblioteca_nombre = ?",
                (self.nombre,)
            )
            filas = cursor.fetchall()
            for fila in filas:
                libro = Libro(
                    id_libro=fila[0],
                    titulo=fila[1],
                    autor=fila[2],
                    anio_publicacion=fila[3]
                )
                self.libros.append(libro)

    def _asegurar_libros_iniciales(self):
        """Agrega al menos 4 libros por defecto si la base de datos está vacía."""
        if len(self.libros) == 0:
            libros_defecto = [
                Libro("Cien años de soledad", "Gabriel García Márquez", 1967),
                Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985),
                Libro("Ficciones", "Jorge Luis Borges", 1944),
                Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605),
                Libro("La ciudad y los perros", "Mario Vargas Llosa", 1963)
            ]
            for lib in libros_defecto:
                self.agregar_libro(lib)

    def agregar_libro(self, libro: Libro) -> bool:
        """
        Agrega una nueva instancia de `Libro` a la lista interna y la persiste en SQLite3.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO libros (titulo, autor, anio_publicacion, biblioteca_nombre) VALUES (?, ?, ?, ?)",
                (libro.titulo, libro.autor, libro.anio_publicacion, self.nombre)
            )
            conn.commit()
            libro.id = cursor.lastrowid
        
        # Agregar a la lista compuesta
        self.libros.append(libro)
        return True

    def mostrar_libros(self) -> List[Libro]:
        """Devuelve la lista completa de libros pertenecientes a la biblioteca."""
        return self.libros

    def buscar_por_autor(self, autor_busqueda: str) -> List[Libro]:
        """
        Filtra la lista de libros buscando coincidencias por nombre del autor.
        """
        termino = autor_busqueda.strip().lower()
        if not termino:
            return self.mostrar_libros()
            
        return [
            libro for libro in self.libros
            if termino in libro.autor.lower()
        ]


# ==============================================================================
# INTERFAZ GRÁFICA DE USUARIO (wxPython)
# ==============================================================================

if WX_DISPONIBLE:
    class VentanaBiblioteca(wx.Frame):
        """
        Ventana principal de la aplicación desarrollada con wxPython.
        """
        def __init__(self, biblioteca: Biblioteca):
            super().__init__(
                parent=None,
                title=f"🏛️ Administrador de Biblioteca - {biblioteca.nombre}",
                size=(850, 600)
            )
            self.biblioteca = biblioteca
            
            self._crear_interfaz()
            self.Center()
            self.actualizar_tabla(self.biblioteca.mostrar_libros())

        def _crear_interfaz(self):
            panel_principal = wx.Panel(self)
            sizer_principal = wx.BoxSizer(wx.VERTICAL)

            # --- Encabezado ---
            panel_header = wx.Panel(panel_principal)
            panel_header.SetBackgroundColour(wx.Colour(41, 128, 185))
            sizer_header = wx.BoxSizer(wx.VERTICAL)
            
            lbl_titulo_app = wx.StaticText(
                panel_header,
                label=f"Gestión de Biblioteca: {self.biblioteca.nombre}"
            )
            lbl_titulo_app.SetForegroundColour(wx.WHITE)
            lbl_subtitulo = wx.StaticText(
                panel_header,
                label="Demostración de Composición de Objetos (POO) + Persistencia SQLite3"
            )
            lbl_subtitulo.SetForegroundColour(wx.Colour(236, 240, 241))
            
            # Fuentes estilizadas
            font_title = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
            font_sub = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
            lbl_titulo_app.SetFont(font_title)
            lbl_subtitulo.SetFont(font_sub)

            sizer_header.Add(lbl_titulo_app, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
            sizer_header.Add(lbl_subtitulo, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 8)
            panel_header.SetSizer(sizer_header)
            sizer_principal.Add(panel_header, 0, wx.EXPAND)

            # --- Formulario de Ingreso (Agregar Libro) ---
            box_formulario = wx.StaticBox(panel_principal, label="➕ Agregar Nuevo Libro")
            sizer_form = wx.StaticBoxSizer(box_formulario, wx.HORIZONTAL)

            grid_inputs = wx.FlexGridSizer(rows=2, cols=3, vgap=8, hgap=10)

            grid_inputs.Add(wx.StaticText(panel_principal, label="Título del Libro:"), 0, wx.ALIGN_CENTER_VERTICAL)
            grid_inputs.Add(wx.StaticText(panel_principal, label="Autor:"), 0, wx.ALIGN_CENTER_VERTICAL)
            grid_inputs.Add(wx.StaticText(panel_principal, label="Año Publicación:"), 0, wx.ALIGN_CENTER_VERTICAL)

            self.txt_titulo = wx.TextCtrl(panel_principal, size=(250, -1))
            self.txt_autor = wx.TextCtrl(panel_principal, size=(200, -1))
            self.spn_anio = wx.SpinCtrl(panel_principal, min=1000, max=2030, initial=2024, size=(100, -1))

            grid_inputs.Add(self.txt_titulo, 1, wx.EXPAND)
            grid_inputs.Add(self.txt_autor, 1, wx.EXPAND)
            grid_inputs.Add(self.spn_anio, 0, wx.EXPAND)

            sizer_form.Add(grid_inputs, 1, wx.ALL | wx.EXPAND, 8)

            self.btn_agregar = wx.Button(panel_principal, label="Guardar Libro", size=(120, 45))
            self.btn_agregar.SetBackgroundColour(wx.Colour(46, 204, 113))
            self.btn_agregar.SetForegroundColour(wx.WHITE)
            self.btn_agregar.Bind(wx.EVT_BUTTON, self.on_agregar_libro)
            
            sizer_form.Add(self.btn_agregar, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
            sizer_principal.Add(sizer_form, 0, wx.ALL | wx.EXPAND, 10)

            # --- Sección de Búsqueda y Filtros ---
            sizer_busqueda = wx.BoxSizer(wx.HORIZONTAL)
            sizer_busqueda.Add(wx.StaticText(panel_principal, label="🔍 Buscar por Autor:"), 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 10)
            
            self.txt_buscar_autor = wx.TextCtrl(panel_principal, size=(220, -1))
            sizer_busqueda.Add(self.txt_buscar_autor, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 8)

            self.btn_buscar = wx.Button(panel_principal, label="Buscar")
            self.btn_buscar.Bind(wx.EVT_BUTTON, self.on_buscar_autor)
            sizer_busqueda.Add(self.btn_buscar, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

            self.btn_mostrar_todos = wx.Button(panel_principal, label="📋 Mostrar Todos")
            self.btn_mostrar_todos.Bind(wx.EVT_BUTTON, self.on_mostrar_todos)
            sizer_busqueda.Add(self.btn_mostrar_todos, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)

            sizer_principal.Add(sizer_busqueda, 0, wx.EXPAND | wx.BOTTOM, 8)

            # --- Tabla de Resultados (wx.ListCtrl) ---
            self.tabla_libros = wx.ListCtrl(
                panel_principal,
                style=wx.LC_REPORT | wx.BORDER_SUNKEN
            )
            self.tabla_libros.InsertColumn(0, "ID", width=60)
            self.tabla_libros.InsertColumn(1, "Título del Libro", width=340)
            self.tabla_libros.InsertColumn(2, "Autor", width=250)
            self.tabla_libros.InsertColumn(3, "Año", width=100)

            sizer_principal.Add(self.tabla_libros, 1, wx.ALL | wx.EXPAND, 10)

            # --- Barra de Estado ---
            self.statusbar = self.CreateStatusBar(1)
            panel_principal.SetSizer(sizer_principal)

        def actualizar_tabla(self, lista_libros: List[Libro]):
            """Repuebla la tabla de la interfaz con la lista de objetos `Libro` recibida."""
            self.tabla_libros.DeleteAllItems()
            for idx, libro in enumerate(lista_libros):
                index = self.tabla_libros.InsertItem(idx, str(libro.id))
                self.tabla_libros.SetItem(index, 1, libro.titulo)
                self.tabla_libros.SetItem(index, 2, libro.autor)
                self.tabla_libros.SetItem(index, 3, str(libro.anio_publicacion))

            total_registros = len(lista_libros)
            total_biblioteca = len(self.biblioteca.mostrar_libros())
            self.statusbar.SetStatusText(
                f"Mostrando {total_registros} de {total_biblioteca} libro(s) en la biblioteca '{self.biblioteca.nombre}'."
            )

        def on_agregar_libro(self, event):
            """Manejador del evento de clic en 'Guardar Libro'."""
            titulo = self.txt_titulo.GetValue().strip()
            autor = self.txt_autor.GetValue().strip()
            anio = self.spn_anio.GetValue()

            if not titulo or not autor:
                wx.MessageBox(
                    "Por favor complete tanto el Título como el Autor del libro.",
                    "Atención",
                    wx.OK | wx.ICON_WARNING
                )
                return

            nuevo_libro = Libro(titulo=titulo, autor=autor, anio_publicacion=anio)
            self.biblioteca.agregar_libro(nuevo_libro)

            self.txt_titulo.Clear()
            self.txt_autor.Clear()
            self.spn_anio.SetValue(2024)

            self.actualizar_tabla(self.biblioteca.mostrar_libros())
            wx.MessageBox(
                f"¡El libro '{titulo}' se ha agregado con éxito a la biblioteca!",
                "Éxito",
                wx.OK | wx.ICON_INFORMATION
            )

        def on_buscar_autor(self, event):
            """Manejador del evento de búsqueda por autor."""
            autor_busqueda = self.txt_buscar_autor.GetValue()
            resultados = self.biblioteca.buscar_por_autor(autor_busqueda)
            self.actualizar_tabla(resultados)
            
            if not resultados:
                wx.MessageBox(
                    f"No se encontraron libros para el autor '{autor_busqueda}'.",
                    "Sin resultados",
                    wx.OK | wx.ICON_INFORMATION
                )

        def on_mostrar_todos(self, event):
            """Manejador del evento para restablecer la vista completa."""
            self.txt_buscar_autor.Clear()
            self.actualizar_tabla(self.biblioteca.mostrar_libros())


# ==============================================================================
# PUNTO DE ENTRADA PRINCIPAL
# ==============================================================================

def main():
    biblioteca_central = Biblioteca(
        nombre="Biblioteca Central Municipal",
        db_path="biblioteca.db"
    )

    if WX_DISPONIBLE:
        app = wx.App(False)
        frame = VentanaBiblioteca(biblioteca_central)
        frame.Show(True)
        app.MainLoop()
    else:
        print("=== BIBLIOTECA CENTRAL MUNICIPAL ===")
        print(f"Total de libros registrados en SQLite: {len(biblioteca_central.mostrar_libros())}\n")
        
        print("📋 Lista de Libros en Memoria (Composición):")
        for lib in biblioteca_central.mostrar_libros():
            print(f"  • [ID {lib.id}] {lib.titulo} - Autor: {lib.autor} ({lib.anio_publicacion})")

        print("\n🔍 Búsqueda por Autor ('García Márquez'):")
        resultados = biblioteca_central.buscar_por_autor("García Márquez")
        for lib in resultados:
            print(f"  • {lib.titulo} ({lib.anio_publicacion})")


if __name__ == "__main__":
    main()
