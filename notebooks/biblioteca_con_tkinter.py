import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os

class Libro:
    """Clase que representa un libro en la biblioteca."""
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = int(anio)

    def __str__(self):
        return f"'{self.titulo}' escrito por {self.autor} (Publicado en {self.anio})"

class Biblioteca:
    """Clase que representa una biblioteca, compuesta por una lista de objetos Libro."""
    def __init__(self, nombre, db_name="biblioteca_local.db"):
        self.nombre = nombre
        self.libros = []  # Composición: La biblioteca contiene una lista de libros
        self.db_name = db_name
        self.configurar_base_datos()
        self.cargar_libros_desde_db()
        self.inicializar_libros_por_defecto()

    def configurar_base_datos(self):
        """Crea la tabla de libros en SQLite si no existe."""
        conexion = sqlite3.connect(self.db_name)
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                anio INTEGER NOT NULL
            )
        ''')
        conexion.commit()
        conexion.close()

    def cargar_libros_desde_db(self):
        """Lee la base de datos y puebla la lista de objetos Libro."""
        self.libros.clear()
        conexion = sqlite3.connect(self.db_name)
        cursor = conexion.cursor()
        cursor.execute("SELECT titulo, autor, anio FROM libros")
        filas = cursor.fetchall()
        for fila in filas:
            libro = Libro(titulo=fila[0], autor=fila[1], anio=fila[2])
            self.libros.append(libro)
        conexion.close()

    def inicializar_libros_por_defecto(self):
        """Agrega 4 libros iniciales si la biblioteca está vacía para cumplir el enunciado."""
        if len(self.libros) == 0:
            libros_iniciales = [
                Libro("Cien años de soledad", "Gabriel García Márquez", 1967),
                Libro("1984", "George Orwell", 1949),
                Libro("El Señor de los Anillos", "J.R.R. Tolkien", 1954),
                Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)
            ]
            for libro in libros_iniciales:
                self.agregar_libro(libro)

    def agregar_libro(self, libro):
        """Agrega un libro a la lista en memoria y a la base de datos."""
        # Agregar a la lista de objetos (en memoria)
        self.libros.append(libro)
        
        # Guardar en SQLite
        conexion = sqlite3.connect(self.db_name)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO libros (titulo, autor, anio) VALUES (?, ?, ?)",
                       (libro.titulo, libro.autor, libro.anio))
        conexion.commit()
        conexion.close()

    def mostrar_libros(self):
        """Devuelve la lista de todos los libros."""
        return self.libros

    def buscar_por_autor(self, autor):
        """Devuelve una lista de libros cuyo autor coincida con la búsqueda."""
        libros_encontrados = []
        for libro in self.libros:
            if autor.lower() in libro.autor.lower():
                libros_encontrados.append(libro)
        return libros_encontrados

class AppBibliotecaGUI:
    """Clase principal para la interfaz gráfica de usuario en Tkinter."""
    def __init__(self, root, biblioteca):
        self.root = root
        self.biblioteca = biblioteca
        self.root.title(f"Sistema de Gestión: {self.biblioteca.nombre}")
        self.root.geometry("600x500")
        self.root.configure(padx=20, pady=20)

        # Variables de control para entradas de texto
        self.var_titulo = tk.StringVar()
        self.var_autor = tk.StringVar()
        self.var_anio = tk.StringVar()
        self.var_busqueda = tk.StringVar()

        self.crear_widgets()
        self.actualizar_pantalla(self.biblioteca.mostrar_libros())

    def crear_widgets(self):
        # --- Marco de Formulario para Añadir ---
        frame_formulario = tk.LabelFrame(self.root, text="Agregar Nuevo Libro", padx=10, pady=10)
        frame_formulario.pack(fill="x", pady=(0, 10))

        tk.Label(frame_formulario, text="Título:").grid(row=0, column=0, sticky="w", pady=2)
        tk.Entry(frame_formulario, textvariable=self.var_titulo, width=30).grid(row=0, column=1, pady=2, padx=5)

        tk.Label(frame_formulario, text="Autor:").grid(row=1, column=0, sticky="w", pady=2)
        tk.Entry(frame_formulario, textvariable=self.var_autor, width=30).grid(row=1, column=1, pady=2, padx=5)

        tk.Label(frame_formulario, text="Año:").grid(row=2, column=0, sticky="w", pady=2)
        tk.Entry(frame_formulario, textvariable=self.var_anio, width=10).grid(row=2, column=1, sticky="w", pady=2, padx=5)

        tk.Button(frame_formulario, text="Guardar Libro", command=self.accion_agregar_libro, bg="#4CAF50", fg="white").grid(row=0, column=2, rowspan=3, padx=20, ipadx=10, ipady=10)

        # --- Marco de Búsqueda ---
        frame_busqueda = tk.Frame(self.root)
        frame_busqueda.pack(fill="x", pady=(0, 10))

        tk.Label(frame_busqueda, text="Buscar por Autor:").pack(side="left")
        tk.Entry(frame_busqueda, textvariable=self.var_busqueda, width=25).pack(side="left", padx=5)
        tk.Button(frame_busqueda, text="Buscar", command=self.accion_buscar).pack(side="left", padx=2)
        tk.Button(frame_busqueda, text="Mostrar Todos", command=self.accion_mostrar_todos).pack(side="left", padx=2)

        # --- Área de Resultados (Tabla / Treeview) ---
        columnas = ("titulo", "autor", "anio")
        self.area_resultados = ttk.Treeview(self.root, columns=columnas, show="headings", height=12)
        
        # Definir los encabezados
        self.area_resultados.heading("titulo", text="Título")
        self.area_resultados.heading("autor", text="Autor")
        self.area_resultados.heading("anio", text="Publicación")
        
        # Configurar el ancho y alineación de las columnas
        self.area_resultados.column("titulo", width=250)
        self.area_resultados.column("autor", width=200)
        self.area_resultados.column("anio", width=100, anchor="center")
        
        self.area_resultados.pack(fill="both", expand=True)

    def accion_agregar_libro(self):
        titulo = self.var_titulo.get().strip()
        autor = self.var_autor.get().strip()
        anio_str = self.var_anio.get().strip()

        if not titulo or not autor or not anio_str:
            messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos para agregar un libro.")
            return

        if not anio_str.isdigit():
            messagebox.showerror("Error de formato", "El año debe ser un número entero.")
            return

        # Creamos el objeto libro
        nuevo_libro = Libro(titulo, autor, anio_str)
        # Usamos el método de la biblioteca para agregarlo
        self.biblioteca.agregar_libro(nuevo_libro)

        messagebox.showinfo("Éxito", f"Libro '{titulo}' agregado correctamente.")
        
        # Limpiar formulario
        self.var_titulo.set("")
        self.var_autor.set("")
        self.var_anio.set("")

        # Actualizar vista
        self.actualizar_pantalla(self.biblioteca.mostrar_libros())

    def accion_buscar(self):
        autor = self.var_busqueda.get().strip()
        if not autor:
            messagebox.showwarning("Búsqueda vacía", "Ingresa el nombre del autor a buscar.")
            return
            
        resultados = self.biblioteca.buscar_por_autor(autor)
        self.actualizar_pantalla(resultados)
        
        if not resultados:
            messagebox.showinfo("Resultados", "No se encontraron libros de ese autor.")

    def accion_mostrar_todos(self):
        self.var_busqueda.set("")
        self.actualizar_pantalla(self.biblioteca.mostrar_libros())

    def actualizar_pantalla(self, lista_libros):
        """Limpia la tabla y muestra los libros proveídos."""
        # Limpiar la tabla borrando todos los hijos
        for item in self.area_resultados.get_children():
            self.area_resultados.delete(item)
            
        # Insertar los libros en la tabla
        for libro in lista_libros:
            self.area_resultados.insert("", tk.END, values=(libro.titulo, libro.autor, libro.anio))

if __name__ == "__main__":
    # Creamos la instancia de nuestra clase principal, la cual inicializará la BD local.
    # El archivo de base de datos 'biblioteca_local.db' se creará en el directorio actual.
    mi_biblioteca = Biblioteca("Biblioteca Central")

    # Configuramos la ventana de Tkinter
    ventana_principal = tk.Tk()
    
    # Iniciamos la GUI enviándole la biblioteca instanciada
    app = AppBibliotecaGUI(ventana_principal, mi_biblioteca)
    
    # Bucle principal de eventos de la ventana
    ventana_principal.mainloop()