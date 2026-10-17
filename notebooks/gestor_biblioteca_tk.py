"""
Sistema de Gestión de Biblioteca (POO con Composición, SQLite3 y Tkinter)

Enunciado:
Desarrolla un sistema simple para administrar una biblioteca.

Cada Libro debe tener:
- título
- autor
- año de publicación

La clase Biblioteca debe:
- tener un nombre
- contener una lista de libros (Composición: "Tiene-Un")
- permitir agregar libros
- mostrar todos los libros
- buscar libros por autor

Utiliza una interfaz gráfica con Tkinter para crear y agregar libros a la biblioteca
sobre una base de datos local (SQLite v3).
"""

import sqlite3
import sys
from typing import List, Optional


# ==========================================
# 1. CLASE COMPONENTE: LIBRO
# ==========================================
class Libro:
    def __init__(self, titulo: str, autor: str, anio_publicacion: int, id_libro: Optional[int] = None):
        self.id = id_libro
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def __repr__(self) -> str:
        return f"Libro(id={self.id}, titulo='{self.titulo}', autor='{self.autor}', anio={self.anio_publicacion})"


# ==========================================
# 2. CLASE CONTENEDORA COMPUESTA: BIBLIOTECA
# ==========================================
class Biblioteca:
    def __init__(self, nombre: str, db_path: str = "biblioteca.db"):
        self.nombre = nombre
        self.db_path = db_path
        # COMPOSICIÓN: La biblioteca administra su propia lista de objetos Libro ("Tiene-Un")
        self.libros: List[Libro] = []
        self._inicializar_base_datos()
        self.cargar_libros_desde_db()

    def _inicializar_base_datos(self):
        """Crea la tabla en SQLite3 e inserta registros iniciales si está vacía."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS libros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    anio_publicacion INTEGER NOT NULL
                )
            """)
            conn.commit()

            cursor.execute("SELECT COUNT(*) FROM libros")
            if cursor.fetchone()[0] == 0:
                libros_semilla = [
                    ("Cien años de soledad", "Gabriel García Márquez", 1967),
                    ("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985),
                    ("Ficciones", "Jorge Luis Borges", 1944),
                    ("Don Quijote de la Mancha", "Miguel de Cervantes", 1605),
                    ("La ciudad y los perros", "Mario Vargas Llosa", 1963)
                ]
                cursor.executemany("""
                    INSERT INTO libros (titulo, autor, anio_publicacion)
                    VALUES (?, ?, ?)
                """, libros_semilla)
                conn.commit()

    def cargar_libros_desde_db(self):
        """Carga los registros de SQLite y los convierte en instancias de Libro en memoria."""
        self.libros.clear()
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, titulo, autor, anio_publicacion FROM libros ORDER BY id DESC")
            registros = cursor.fetchall()
            for id_lib, tit, aut, anio in registros:
                self.libros.append(Libro(tit, aut, anio, id_lib))

    def agregar_libro(self, titulo: str, autor: str, anio_publicacion: int) -> Libro:
        """Agrega un libro a la base de datos y a la lista compuesta en memoria."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO libros (titulo, autor, anio_publicacion)
                VALUES (?, ?, ?)
            """, (titulo, autor, anio_publicacion))
            id_nuevo = cursor.lastrowid
            conn.commit()

        nuevo_libro = Libro(titulo, autor, anio_publicacion, id_nuevo)
        self.libros.insert(0, nuevo_libro)
        return nuevo_libro

    def mostrar_todos_los_libros(self) -> List[Libro]:
        """Devuelve la lista completa de objetos Libro."""
        return self.libros

    def buscar_libros_por_autor(self, autor_busqueda: str) -> List[Libro]:
        """Filtra y retorna objetos Libro cuyo autor coincida parcialmente."""
        termino = autor_busqueda.lower().strip()
        if not termino:
            return self.libros
        return [libro for libro in self.libros if termino in libro.autor.lower()]


# ==========================================
# 3. INTERFAZ GRÁFICA CON TKINTER / TTK
# ==========================================
def iniciar_gui(biblioteca: Biblioteca):
    import tkinter as tk
    from tkinter import ttk, messagebox

    class BibliotecaGUI(tk.Tk):
        def __init__(self, biblio: Biblioteca):
            super().__init__()
            self.biblio = biblio
            self.title(f"Gestión de Biblioteca - {self.biblio.nombre}")
            self.geometry("750x520")
            self.minsize(650, 450)

            # Estilo moderno
            self.style = ttk.Style(self)
            self.style.theme_use("clam")

            self._crear_widgets()
            self._actualizar_tabla(self.biblio.mostrar_todos_los_libros())

        def _crear_widgets(self):
            # Encabezado
            header_frame = ttk.Frame(self, padding=10)
            header_frame.pack(fill=tk.X)
            lbl_titulo = ttk.Label(
                header_frame,
                text=f"📚 {self.biblio.nombre}",
                font=("Helvetica", 16, "bold")
            )
            lbl_titulo.pack(anchor=tk.W)

            # Formulario de ingreso de libro
            form_frame = ttk.LabelFrame(self, text=" Agregar Nuevo Libro ", padding=10)
            form_frame.pack(fill=tk.X, padx=10, pady=5)

            ttk.Label(form_frame, text="Título:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
            self.ent_titulo = ttk.Entry(form_frame, width=25)
            self.ent_titulo.grid(row=0, column=1, padx=5, pady=5)

            ttk.Label(form_frame, text="Autor:").grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
            self.ent_autor = ttk.Entry(form_frame, width=25)
            self.ent_autor.grid(row=0, column=3, padx=5, pady=5)

            ttk.Label(form_frame, text="Año:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
            self.spn_anio = ttk.Spinbox(form_frame, from_=1000, to=2030, width=10)
            self.spn_anio.set(2024)
            self.spn_anio.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

            btn_agregar = ttk.Button(form_frame, text="➕ Agregar Libro", command=self._on_agregar)
            btn_agregar.grid(row=1, column=3, sticky=tk.E, padx=5, pady=5)

            # Buscador por autor
            search_frame = ttk.Frame(self, padding=10)
            search_frame.pack(fill=tk.X, padx=10)

            ttk.Label(search_frame, text="🔍 Buscar por Autor:").pack(side=tk.LEFT, padx=5)
            self.ent_buscar = ttk.Entry(search_frame, width=30)
            self.ent_buscar.pack(side=tk.LEFT, padx=5)
            self.ent_buscar.bind("<KeyRelease>", self._on_buscar)

            btn_limpiar = ttk.Button(search_frame, text="Mostrar Todos", command=self._on_mostrar_todos)
            btn_limpiar.pack(side=tk.LEFT, padx=5)

            # Tabla de libros (Treeview)
            tree_frame = ttk.Frame(self, padding=10)
            tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

            columnas = ("ID", "Título", "Autor", "Año")
            self.tree = ttk.Treeview(tree_frame, columns=columnas, show="headings", selectmode="browse")

            self.tree.heading("ID", text="ID")
            self.tree.heading("Título", text="Título")
            self.tree.heading("Autor", text="Autor")
            self.tree.heading("Año", text="Año Publicación")

            self.tree.column("ID", width=50, anchor=tk.CENTER)
            self.tree.column("Título", width=300, anchor=tk.W)
            self.tree.column("Autor", width=220, anchor=tk.W)
            self.tree.column("Año", width=100, anchor=tk.CENTER)

            scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
            self.tree.configure(yscrollcommand=scrollbar.set)

            self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        def _actualizar_tabla(self, lista_libros: List[Libro]):
            """Vuelve a cargar las filas de la tabla con la lista de objetos Libro."""
            for item in self.tree.get_children():
                self.tree.delete(item)

            for libro in lista_libros:
                self.tree.insert("", tk.END, values=(libro.id, libro.titulo, libro.autor, libro.anio_publicacion))

        def _on_agregar(self):
            tit = self.ent_titulo.get().strip()
            aut = self.ent_autor.get().strip()
            anio_str = self.spn_anio.get().strip()

            if not tit or not aut or not anio_str:
                messagebox.showwarning("Campos Incompletos", "Por favor completa el título, autor y año.")
                return

            try:
                anio = int(anio_str)
            except ValueError:
                messagebox.showerror("Error de Formato", "El año debe ser un número entero válido.")
                return

            # Agrega el libro usando la clase Biblioteca (Composición)
            libro_creado = self.biblio.agregar_libro(tit, aut, anio)

            self.ent_titulo.delete(0, tk.END)
            self.ent_autor.delete(0, tk.END)
            self.spn_anio.set(2024)
            self.ent_buscar.delete(0, tk.END)

            self._actualizar_tabla(self.biblio.mostrar_todos_los_libros())
            messagebox.showinfo("Éxito", f"Libro '{libro_creado.titulo}' registrado correctamente.")

        def _on_buscar(self, event=None):
            termino = self.ent_buscar.get()
            resultados = self.biblio.buscar_libros_por_autor(termino)
            self._actualizar_tabla(resultados)

        def _on_mostrar_todos(self):
            self.ent_buscar.delete(0, tk.END)
            self._actualizar_tabla(self.biblio.mostrar_todos_los_libros())

    app = BibliotecaGUI(biblioteca)
    app.mainloop()


# ==========================================
# 4. MODO CONSOLA DE RESPALDO (HEADLESS)
# ==========================================
def ejecutar_consola(biblioteca: Biblioteca):
    print("=" * 60)
    print(f"📚 DEMOSTRACIÓN EN CONSOLA: {biblioteca.nombre.upper()}")
    print("=" * 60)

    print(f"\n📋 Todos los libros registrados (Total: {len(biblioteca.mostrar_todos_los_libros())}):")
    for lib in biblioteca.mostrar_todos_los_libros():
        print(f"  • [ID {lib.id}] '{lib.titulo}' - Autor: {lib.autor} ({lib.anio_publicacion})")

    print("\n➕ Agregando un libro de prueba...")
    nuevo = biblioteca.agregar_libro("Rayuela", "Julio Cortázar", 1963)
    print(f"  ✨ ¡Agregado exitosamente!: {nuevo}")

    autor_query = "García Márquez"
    print(f"\n🔍 Buscando libros del autor '{autor_query}':")
    hallados = biblioteca.buscar_libros_por_autor(autor_query)
    for lib in hallados:
        print(f"  • '{lib.titulo}' ({lib.anio_publicacion})")

    print("\n" + "=" * 60)


# ==========================================
# PUNTO DE ENTRADA
# ==========================================
if __name__ == "__main__":
    biblioteca = Biblioteca("Biblioteca Central Municipal", db_path="biblioteca.db")

    try:
        import tkinter
        test_root = tkinter.Tk()
        test_root.destroy()
        iniciar_gui(biblioteca)
    except Exception as e:
        print(f"⚠️ No se pudo iniciar la interfaz gráfica Tkinter ({e}).")
        print("Ejecutando la demostración en modo consola:\n")
        ejecutar_consola(biblioteca)
