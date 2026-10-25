import tkinter as tk
from tkinter import messagebox, ttk


class AppGestionTkinter(tk.Tk):
    """Formulario de registro y lista de usuarios con widgets estándar de Tkinter."""

    def __init__(self):
        super().__init__()

        self.title("Sistema de Registro y Lista de Resultados - Tkinter")
        self.geometry("1000x600")
        self.minsize(850, 500)

        self.registros = [
            {"id": 1, "nombre": "Ana Martínez", "email": "ana.martinez@email.com", "rol": "Administrador", "estado": "Activo"},
            {"id": 2, "nombre": "Carlos López", "email": "carlos.lopez@email.com", "rol": "Desarrollador", "estado": "Activo"},
            {"id": 3, "nombre": "Sofía Torres", "email": "sofia.torres@email.com", "rol": "Diseñador UX", "estado": "Inactivo"},
        ]
        self.contador_id = 4
        self.estilo = ttk.Style(self)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        self._crear_panel_formulario()
        self._crear_panel_tabla()
        self._cargar_datos_tabla()
        self._cambiar_apariencia("Claro")

    def _crear_panel_formulario(self):
        self.frame_form = ttk.LabelFrame(self, text="Ingreso de Datos", padding=15)
        self.frame_form.grid(row=0, column=0, padx=(15, 10), pady=15, sticky="nsew")
        self.frame_form.columnconfigure(0, weight=1)

        ttk.Label(self.frame_form, text="Nombre Completo:").grid(row=0, column=0, sticky="w", pady=(5, 2))
        self.ent_nombre = ttk.Entry(self.frame_form)
        self.ent_nombre.grid(row=1, column=0, sticky="ew", pady=(0, 10))

        ttk.Label(self.frame_form, text="Correo Electrónico:").grid(row=2, column=0, sticky="w", pady=(5, 2))
        self.ent_email = ttk.Entry(self.frame_form)
        self.ent_email.grid(row=3, column=0, sticky="ew", pady=(0, 10))

        ttk.Label(self.frame_form, text="Rol Profesional:").grid(row=4, column=0, sticky="w", pady=(5, 2))
        self.opt_rol = ttk.Combobox(
            self.frame_form,
            values=["Desarrollador", "Administrador", "Diseñador UX", "Analista de Datos"],
            state="readonly",
        )
        self.opt_rol.current(0)
        self.opt_rol.grid(row=5, column=0, sticky="ew", pady=(0, 10))

        self.estado_activo = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            self.frame_form,
            text="Usuario Activo",
            variable=self.estado_activo,
        ).grid(row=6, column=0, sticky="w", pady=(10, 15))

        ttk.Button(
            self.frame_form,
            text="Registrar Usuario",
            command=self._agregar_registro,
        ).grid(row=7, column=0, sticky="ew", pady=(5, 10))

        ttk.Label(self.frame_form, text="Apariencia de la Interfaz:").grid(
            row=8, column=0, sticky="w", pady=(25, 2)
        )
        self.opt_tema = ttk.Combobox(
            self.frame_form,
            values=["Claro", "Oscuro"],
            state="readonly",
        )
        self.opt_tema.set("Claro")
        self.opt_tema.bind("<<ComboboxSelected>>", self._cambiar_apariencia)
        self.opt_tema.grid(row=9, column=0, sticky="ew", pady=(0, 15))

    def _crear_panel_tabla(self):
        self.frame_tabla = ttk.LabelFrame(self, text="Lista de Resultados", padding=15)
        self.frame_tabla.grid(row=0, column=1, padx=(10, 15), pady=15, sticky="nsew")
        self.frame_tabla.columnconfigure(0, weight=1)
        self.frame_tabla.rowconfigure(0, weight=1)

        columnas = ("id", "nombre", "email", "rol", "estado")
        self.tabla = ttk.Treeview(
            self.frame_tabla,
            columns=columnas,
            show="headings",
            selectmode="browse",
        )
        titulos = {
            "id": "ID",
            "nombre": "Nombre",
            "email": "Email",
            "rol": "Rol",
            "estado": "Estado",
        }
        anchos = {"id": 45, "nombre": 150, "email": 190, "rol": 130, "estado": 85}
        for columna in columnas:
            self.tabla.heading(columna, text=titulos[columna])
            self.tabla.column(columna, width=anchos[columna], minwidth=50, anchor="w")

        self.tabla.tag_configure("activo", foreground="#15803d")
        self.tabla.tag_configure("inactivo", foreground="#dc2626")
        self.tabla.grid(row=0, column=0, sticky="nsew")

        barra = ttk.Scrollbar(self.frame_tabla, orient="vertical", command=self.tabla.yview)
        barra.grid(row=0, column=1, sticky="ns")
        self.tabla.configure(yscrollcommand=barra.set)

        ttk.Button(
            self.frame_tabla,
            text="Eliminar seleccionado",
            command=self._eliminar_registro_seleccionado,
        ).grid(row=1, column=0, sticky="e", pady=(10, 0))

    def _cargar_datos_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for item in self.registros:
            etiqueta = "activo" if item["estado"] == "Activo" else "inactivo"
            self.tabla.insert(
                "",
                "end",
                iid=str(item["id"]),
                values=(item["id"], item["nombre"], item["email"], item["rol"], item["estado"]),
                tags=(etiqueta,),
            )

    def _agregar_registro(self):
        nombre = self.ent_nombre.get().strip()
        email = self.ent_email.get().strip()

        if not nombre or not email:
            messagebox.showwarning("Campos Incompletos", "Por favor completa el nombre y el correo.")
            return

        self.registros.append({
            "id": self.contador_id,
            "nombre": nombre,
            "email": email,
            "rol": self.opt_rol.get(),
            "estado": "Activo" if self.estado_activo.get() else "Inactivo",
        })
        self.contador_id += 1

        self._cargar_datos_tabla()
        self.ent_nombre.delete(0, tk.END)
        self.ent_email.delete(0, tk.END)
        messagebox.showinfo("Éxito", f"Usuario '{nombre}' registrado correctamente.")

    def _eliminar_registro_seleccionado(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Sin selección", "Selecciona un usuario para eliminarlo.")
            return

        id_registro = int(seleccion[0])
        self.registros = [registro for registro in self.registros if registro["id"] != id_registro]
        self._cargar_datos_tabla()

    def _cambiar_apariencia(self, evento=None):
        oscuro = self.opt_tema.get() == "Oscuro"
        fondo = "#252525" if oscuro else "#f0f0f0"
        texto = "#f5f5f5" if oscuro else "#202020"
        campo = "#333333" if oscuro else "#ffffff"

        self.configure(bg=fondo)
        self.estilo.configure("TFrame", background=fondo)
        self.estilo.configure("TLabelframe", background=fondo, foreground=texto)
        self.estilo.configure("TLabelframe.Label", background=fondo, foreground=texto)
        self.estilo.configure("TLabel", background=fondo, foreground=texto)
        self.estilo.configure("TCheckbutton", background=fondo, foreground=texto)
        self.estilo.map("TCheckbutton", background=[("active", fondo)])
        self.estilo.configure("TEntry", fieldbackground=campo, foreground=texto)
        self.estilo.configure("TCombobox", fieldbackground=campo, foreground=texto)
        self.estilo.configure(
            "Treeview",
            background=campo,
            fieldbackground=campo,
            foreground=texto,
        )
        self.estilo.configure("Treeview.Heading", background=fondo, foreground=texto)
        self.estilo.map(
            "Treeview",
            background=[("selected", "#2563eb")],
            foreground=[("selected", "#ffffff")],
        )


if __name__ == "__main__":
    app = AppGestionTkinter()
    app.mainloop()