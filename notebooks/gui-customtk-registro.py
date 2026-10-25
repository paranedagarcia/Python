import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

# Configuración global del tema y la apariencia
ctk.set_appearance_mode("System")  # Opciones: "System", "Dark", "Light"
ctk.set_default_color_theme("blue") # Opciones: "blue", "green", "dark-blue"

class AppGestionCustomTkinter(ctk.CTk):
    """
    Aplicación de escritorio desarrollada con CustomTkinter que integra:
    1. Formulario de ingreso de datos (Data Entry) estilizado.
    2. Tabla de resultados/registros utilizando CTkScrollableFrame.
    """

    def __init__(self):
        super().__init__()

        # 1. Configuración de la ventana principal
        self.title("Sistema de Registro y Lista de Resultados - CustomTkinter")
        self.geometry("1000x600")
        self.minsize(850, 500)

        # Datos en memoria
        self.registros = [
            {"id": 1, "nombre": "Ana Martínez", "email": "ana.martinez@email.com", "rol": "Administrador", "estado": "Activo"},
            {"id": 2, "nombre": "Carlos López", "email": "carlos.lopez@email.com", "rol": "Desarrollador", "estado": "Activo"},
            {"id": 3, "nombre": "Sofía Torres", "email": "sofia.torres@email.com", "rol": "Diseñador UX", "estado": "Inactivo"},
        ]
        self.contador_id = 4

        # 2. Estructura del Layout principal (Grid de 2 columnas)
        self.grid_columnconfigure(0, weight=1)  # Columna 0: Formulario (Panel Izquierdo)
        self.grid_columnconfigure(1, weight=2)  # Columna 1: Tabla de Resultados (Panel Derecho)
        self.grid_rowconfigure(0, weight=1)

        # 3. Construcción de los paneles
        self._crear_panel_formulario()
        self._crear_panel_tabla()
        self._cargar_datos_tabla()

    def _crear_panel_formulario(self):
        """Crea el panel izquierdo para el ingreso de datos (Data Entry)."""
        self.frame_form = ctk.CTkFrame(self, corner_radius=12)
        self.frame_form.grid(row=0, column=0, padx=(15, 10), pady=15, sticky="nsew")

        # Título del Formulario
        lbl_titulo = ctk.CTkLabel(
            self.frame_form,
            text="Ingreso de Datos",
            font=ctk.CTkFont(family="Roboto", size=18, weight="bold")
        )
        lbl_titulo.pack(padx=15, pady=(20, 15), anchor="w")

        # Campo: Nombre Completo
        lbl_nombre = ctk.CTkLabel(self.frame_form, text="Nombre Completo:", font=ctk.CTkFont(size=12))
        lbl_nombre.pack(padx=15, pady=(5, 2), anchor="w")

        self.ent_nombre = ctk.CTkEntry(
            self.frame_form,
            placeholder_text="Ej. Laura Gómez",
            height=35
        )
        self.ent_nombre.pack(padx=15, pady=(0, 10), fill="x")

        # Campo: Correo Electrónico
        lbl_email = ctk.CTkLabel(self.frame_form, text="Correo Electrónico:", font=ctk.CTkFont(size=12))
        lbl_email.pack(padx=15, pady=(5, 2), anchor="w")

        self.ent_email = ctk.CTkEntry(
            self.frame_form,
            placeholder_text="ejemplo@correo.com",
            height=35
        )
        self.ent_email.pack(padx=15, pady=(0, 10), fill="x")

        # Campo: Rol Profesional (Dropdown Menu)
        lbl_rol = ctk.CTkLabel(self.frame_form, text="Rol Profesional:", font=ctk.CTkFont(size=12))
        lbl_rol.pack(padx=15, pady=(5, 2), anchor="w")

        self.opt_rol = ctk.CTkOptionMenu(
            self.frame_form,
            values=["Desarrollador", "Administrador", "Diseñador UX", "Analista de Datos"],
            height=35
        )
        self.opt_rol.pack(padx=15, pady=(0, 10), fill="x")

        # Campo: Estado (Switch de CustomTkinter)
        self.switch_estado = ctk.CTkSwitch(
            self.frame_form,
            text="Usuario Activo",
            font=ctk.CTkFont(size=12)
        )
        self.switch_estado.select()
        self.switch_estado.pack(padx=15, pady=(10, 15), anchor="w")

        # Botón de Guardar Registro
        btn_guardar = ctk.CTkButton(
            self.frame_form,
            text="➕ Registrar Usuario",
            font=ctk.CTkFont(size=13, weight="bold"),
            height=40,
            command=self._agregar_registro
        )
        btn_guardar.pack(padx=15, pady=(10, 10), fill="x")

        # Selector de Apariencia (Modo Claro / Oscuro / Sistema)
        lbl_tema = ctk.CTkLabel(self.frame_form, text="Apariencia de la Interfaz:", font=ctk.CTkFont(size=11))
        lbl_tema.pack(padx=15, pady=(25, 2), anchor="w")

        self.opt_tema = ctk.CTkOptionMenu(
            self.frame_form,
            values=["System", "Dark", "Light"],
            command=self._cambiar_apariencia,
            height=30,
            fg_color="gray30",
            button_color="gray25"
        )
        self.opt_tema.pack(padx=15, pady=(0, 15), fill="x")

    def _crear_panel_tabla(self):
        """Crea el panel derecho para visualizar la lista de resultados en formato Tabla."""
        self.frame_tabla = ctk.CTkFrame(self, corner_radius=12)
        self.frame_tabla.grid(row=0, column=1, padx=(10, 15), pady=15, sticky="nsew")

        self.frame_tabla.grid_columnconfigure(0, weight=1)
        self.frame_tabla.grid_rowconfigure(1, weight=1)

        # Encabezado del Panel
        lbl_titulo_tabla = ctk.CTkLabel(
            self.frame_tabla,
            text="Lista de Resultados",
            font=ctk.CTkFont(family="Roboto", size=18, weight="bold")
        )
        lbl_titulo_tabla.grid(row=0, column=0, padx=15, pady=(20, 10), sticky="w")

        # Tabla Nativa con CTkScrollableFrame
        self.scroll_tabla = ctk.CTkScrollableFrame(self.frame_tabla, corner_radius=8)
        self.scroll_tabla.grid(row=1, column=0, padx=15, pady=(0, 15), sticky="nsew")

        # Configurar proporciones de las columnas
        self.scroll_tabla.grid_columnconfigure(0, weight=1)  # ID
        self.scroll_tabla.grid_columnconfigure(1, weight=3)  # Nombre
        self.scroll_tabla.grid_columnconfigure(2, weight=4)  # Email
        self.scroll_tabla.grid_columnconfigure(3, weight=3)  # Rol
        self.scroll_tabla.grid_columnconfigure(4, weight=2)  # Estado
        self.scroll_tabla.grid_columnconfigure(5, weight=1)  # Acción

        # Cabeceras de la Tabla
        cabeceras = ["ID", "Nombre", "Email", "Rol", "Estado", "Acción"]
        for col_idx, texto in enumerate(cabeceras):
            lbl_cabecera = ctk.CTkLabel(
                self.scroll_tabla,
                text=texto,
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color="gray70"
            )
            lbl_cabecera.grid(row=0, column=col_idx, padx=5, pady=8, sticky="w")

        # Línea divisoria
        sep = ctk.CTkFrame(self.scroll_tabla, height=2, fg_color="gray40")
        sep.grid(row=1, column=0, columnspan=6, sticky="ew", pady=(0, 10))

    def _cargar_datos_tabla(self):
        """Renderiza dinámicamente las filas dentro de la tabla."""
        # Limpiar filas existentes
        for widget in self.scroll_tabla.winfo_children():
            if widget.grid_info().get("row", 0) > 1:
                widget.destroy()

        # Insertar registros
        for idx, item in enumerate(self.registros, start=2):
            lbl_id = ctk.CTkLabel(self.scroll_tabla, text=str(item["id"]), font=ctk.CTkFont(size=12))
            lbl_id.grid(row=idx, column=0, padx=5, pady=6, sticky="w")

            lbl_nom = ctk.CTkLabel(self.scroll_tabla, text=item["nombre"], font=ctk.CTkFont(size=12, weight="bold"))
            lbl_nom.grid(row=idx, column=1, padx=5, pady=6, sticky="w")

            lbl_email = ctk.CTkLabel(self.scroll_tabla, text=item["email"], font=ctk.CTkFont(size=12))
            lbl_email.grid(row=idx, column=2, padx=5, pady=6, sticky="w")

            lbl_rol = ctk.CTkLabel(self.scroll_tabla, text=item["rol"], font=ctk.CTkFont(size=12))
            lbl_rol.grid(row=idx, column=3, padx=5, pady=6, sticky="w")

            color_estado = "#22c55e" if item["estado"] == "Activo" else "#ef4444"
            lbl_est = ctk.CTkLabel(self.scroll_tabla, text=item["estado"], font=ctk.CTkFont(size=11, weight="bold"), text_color=color_estado)
            lbl_est.grid(row=idx, column=4, padx=5, pady=6, sticky="w")

            # Botón eliminar
            btn_borrar = ctk.CTkButton(
                self.scroll_tabla,
                text="🗑️",
                width=30,
                height=25,
                fg_color="#dc2626",
                hover_color="#991b1b",
                command=lambda id_reg=item["id"]: self._eliminar_registro(id_reg)
            )
            btn_borrar.grid(row=idx, column=5, padx=5, pady=6)

    def _agregar_registro(self):
        """Procesa y valida el ingreso de un nuevo registro."""
        nombre = self.ent_nombre.get().strip()
        email = self.ent_email.get().strip()
        rol = self.opt_rol.get()
        estado = "Activo" if self.switch_estado.get() == 1 else "Inactivo"

        if not nombre or not email:
            messagebox.showwarning("Campos Incompletos", "Por favor completa el nombre y el correo.")
            return

        nuevo_registro = {
            "id": self.contador_id,
            "nombre": nombre,
            "email": email,
            "rol": rol,
            "estado": estado
        }

        self.registros.append(nuevo_registro)
        self.contador_id += 1

        self._cargar_datos_tabla()
        self.ent_nombre.delete(0, tk.END)
        self.ent_email.delete(0, tk.END)
        messagebox.showinfo("Éxito", f"Usuario '{nombre}' registrado correctamente.")

    def _eliminar_registro(self, id_registro):
        """Elimina un registro de la lista de resultados."""
        self.registros = [r for r in self.registros if r["id"] != id_registro]
        self._cargar_datos_tabla()

    def _cambiar_apariencia(self, nuevo_modo):
        """Cambia el modo claro / oscuro en tiempo de ejecución."""
        ctk.set_appearance_mode(nuevo_modo)

if __name__ == "__main__":
    app = AppGestionCustomTkinter()
    app.mainloop()