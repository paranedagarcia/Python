"""
Ejemplo Práctico Profesional: Estructura de Ventana con PySide6 / PyQt
---------------------------------------------------------------------
Implementa:
1. Herencia de QMainWindow con Widget Central y Menú.
2. Mecanismo de Señales y Slots (Signals & Slots).
3. Formulario de ingreso de datos con QFormLayout.
4. Tabla de datos interactiva con QTableWidget y cabeceras ajustables.
5. Barra de estado (QStatusBar) y cuadros de diálogo modales (QMessageBox).
6. Hoja de estilos Qt (QSS) para una apariencia limpia y contemporánea.
"""

import sys

# Intentar importar PySide6; si no está disponible, permitir PyQt6 o PyQt5 como alternativa
try:
    from PySide6.QtWidgets import (
        QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
        QComboBox, QCheckBox, QPushButton, QTableWidget, QTableWidgetItem,
        QVBoxLayout, QHBoxLayout, QFormLayout, QHeaderView, QMessageBox,
        QAbstractItemView, QFrame
    )
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QAction, QFont
except ImportError:
    try:
        from PyQt6.QtWidgets import (
            QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
            QComboBox, QCheckBox, QPushButton, QTableWidget, QTableWidgetItem,
            QVBoxLayout, QHBoxLayout, QFormLayout, QHeaderView, QMessageBox,
            QAbstractItemView, QFrame
        )
        from PyQt6.QtCore import Qt
        from PyQt6.QtGui import QAction, QFont
    except ImportError:
        from PyQt5.QtWidgets import (
            QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
            QComboBox, QCheckBox, QPushButton, QTableWidget, QTableWidgetItem,
            QVBoxLayout, QHBoxLayout, QFormLayout, QHeaderView, QMessageBox,
            QAbstractItemView, QFrame
        )
        from PyQt5.QtCore import Qt
        from PyQt5.QtGui import QAction, QFont


class VentanaPrincipal(QMainWindow):
    """
    Ventana principal de la aplicación.
    Hereda de QMainWindow para disponer de Barra de Menús, Widget Central
    y Barra de Estado integradas.
    """
    def __init__(self):
        super().__init__()

        # 1. Configuración de la ventana principal
        self.setWindowTitle("Sistema de Gestión de Usuarios - PySide6 / PyQt")
        self.resize(950, 580)
        self.setMinimumSize(800, 480)

        # Estructura de datos en memoria para el ejemplo
        self.usuarios = [
            {"id": "1", "nombre": "Camila Soto", "email": "camila.soto@empresa.com", "rol": "Administrador", "activo": True},
            {"id": "2", "nombre": "Rodrigo Morales", "email": "rodrigo.m@empresa.com", "rol": "Desarrollador", "activo": True},
            {"id": "3", "nombre": "Valentina Silva", "email": "v.silva@empresa.com", "rol": "Diseñador UX", "activo": False},
        ]
        self.contador_id = 4

        # 2. Inicializar componentes de la arquitectura Qt
        self._aplicar_estilos_qss()
        self._crear_barra_menus()
        self._crear_barra_estado()
        self._construir_interfaz_central()
        self._cargar_datos_tabla()

    def _aplicar_estilos_qss(self):
        """Aplica una hoja de estilos Qt (QSS) para modernizar la interfaz."""
        estilo = """
        QMainWindow {
            background-color: #f8fafc;
        }
        QFrame#panelFormulario, QFrame#panelTabla {
            background-color: #ffffff;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            padding: 12px;
        }
        QLabel {
            color: #334155;
            font-size: 13px;
        }
        QLabel#tituloSeccion {
            font-size: 16px;
            font-weight: bold;
            color: #0f172a;
            padding-bottom: 6px;
        }
        QLineEdit, QComboBox {
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            padding: 6px 10px;
            font-size: 13px;
            background-color: #ffffff;
        }
        QLineEdit:focus, QComboBox:focus {
            border: 1px solid #2563eb;
        }
        QPushButton {
            border-radius: 6px;
            padding: 8px 16px;
            font-size: 13px;
            font-weight: bold;
        }
        QPushButton#btnPrimario {
            background-color: #2563eb;
            color: white;
            border: none;
        }
        QPushButton#btnPrimario:hover {
            background-color: #1d4ed8;
        }
        QPushButton#btnSecundario {
            background-color: #e2e8f0;
            color: #1e293b;
            border: none;
        }
        QPushButton#btnSecundario:hover {
            background-color: #cbd5e1;
        }
        QTableWidget {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            gridline-color: #f1f5f9;
            font-size: 12px;
        }
        QHeaderView::section {
            background-color: #0f172a;
            color: #ffffff;
            font-weight: bold;
            padding: 6px;
            border: none;
        }
        QStatusBar {
            background-color: #ffffff;
            color: #64748b;
            border-top: 1px solid #e2e8f0;
        }
        """
        self.setStyleSheet(estilo)

    def _crear_barra_menus(self):
        """Configura la barra de menú superior."""
        barra_menu = self.menuBar()

        # Menú Archivo
        menu_archivo = barra_menu.addMenu("&Archivo")
        accion_salir = QAction("&Salir", self)
        accion_salir.setShortcut("Ctrl+Q")
        accion_salir.setStatusTip("Cerrar la aplicación")
        accion_salir.triggered.connect(self.close)
        menu_archivo.addAction(accion_salir)

        # Menú Ayuda
        menu_ayuda = barra_menu.addMenu("A&yuda")
        accion_acerca = QAction("&Acerca de Qt", self)
        accion_acerca.triggered.connect(lambda: QMessageBox.aboutQt(self, "Acerca del framework Qt"))
        menu_ayuda.addAction(accion_acerca)

    def _crear_barra_estado(self):
        """Crea la barra de estado inferior para retroalimentación."""
        self.barra_estado = self.statusBar()
        self.barra_estado.showMessage("Aplicación lista para operar", 4000)

    def _construir_interfaz_central(self):
        """Configura el QWidget central y distribuye los paneles principales."""
        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        # Layout horizontal principal: Izquierda (Formulario) | Derecha (Tabla)
        layout_principal = QHBoxLayout(widget_central)
        layout_principal.setContentsMargins(16, 16, 16, 16)
        layout_principal.setSpacing(16)

        # -------------------------------------------------------------
        # PANEL IZQUIERDO: Formulario de Ingreso de Datos
        # -------------------------------------------------------------
        panel_izquierdo = QFrame()
        panel_izquierdo.setObjectName("panelFormulario")
        layout_izquierdo = QVBoxLayout(panel_izquierdo)

        lbl_titulo_form = QLabel("Registrar Usuario")
        lbl_titulo_form.setObjectName("tituloSeccion")
        layout_izquierdo.addWidget(lbl_titulo_form)

        # Form Layout para alinear etiquetas y campos de entrada limpiamente
        form_layout = QFormLayout()
        form_layout.setSpacing(10)

        self.txt_nombre = QLineEdit()
        self.txt_nombre.setPlaceholderText("Ej. Javiera Pérez")
        form_layout.addRow("Nombre Completo:", self.txt_nombre)

        self.txt_email = QLineEdit()
        self.txt_email.setPlaceholderText("javiera@empresa.com")
        form_layout.addRow("Correo Electrónico:", self.txt_email)

        self.cmb_rol = QComboBox()
        self.cmb_rol.addItems(["Desarrollador", "Administrador", "Diseñador UX", "Analista de Datos"])
        form_layout.addRow("Rol / Cargo:", self.cmb_rol)

        self.chk_activo = QCheckBox("Usuario activo en el sistema")
        self.chk_activo.setChecked(True)
        form_layout.addRow("Estado:", self.chk_activo)

        layout_izquierdo.addLayout(form_layout)

        # Botones de acción
        layout_botones = QHBoxLayout()
        self.btn_limpiar = QPushButton("Limpiar")
        self.btn_limpiar.setObjectName("btnSecundario")
        # Conexión Signal -> Slot
        self.btn_limpiar.clicked.connect(self._limpiar_formulario)

        self.btn_guardar = QPushButton("Registrar")
        self.btn_guardar.setObjectName("btnPrimario")
        # Conexión Signal -> Slot
        self.btn_guardar.clicked.connect(self._agregar_usuario)

        layout_botones.addWidget(self.btn_limpiar)
        layout_botones.addWidget(self.btn_guardar)
        layout_izquierdo.addLayout(layout_botones)

        # Espacio expandible para mantener los campos arriba
        layout_izquierdo.addStretch()

        # -------------------------------------------------------------
        # PANEL DERECHO: Tabla de Registros
        # -------------------------------------------------------------
        panel_derecho = QFrame()
        panel_derecho.setObjectName("panelTabla")
        layout_derecho = QVBoxLayout(panel_derecho)

        lbl_titulo_tabla = QLabel("Usuarios Registrados")
        lbl_titulo_tabla.setObjectName("tituloSeccion")
        layout_derecho.addWidget(lbl_titulo_tabla)

        # Creación y configuración de la tabla
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Email", "Rol", "Estado"])
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabla.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tabla.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        # Ajuste de tamaño de columnas
        cabecera = self.tabla.horizontalHeader()
        cabecera.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        cabecera.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        cabecera.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        cabecera.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        cabecera.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)

        # Conectar selección de fila con Slot
        self.tabla.itemSelectionChanged.connect(self._fila_seleccionada)
        layout_derecho.addWidget(self.tabla)

        # Botón inferior para eliminar registro seleccionado
        self.btn_eliminar = QPushButton("Eliminar Fila Seleccionada")
        self.btn_eliminar.setObjectName("btnSecundario")
        self.btn_eliminar.clicked.connect(self._eliminar_usuario_seleccionado)
        layout_derecho.addWidget(self.btn_eliminar)

        # Asignar proporción de ancho horizontal (1 a 2)
        layout_principal.addWidget(panel_izquierdo, 1)
        layout_principal.addWidget(panel_derecho, 2)

    # -----------------------------------------------------------------
    # SLOTS (Manejadores de Eventos y Lógica de Negocio)
    # -----------------------------------------------------------------
    def _cargar_datos_tabla(self):
        """Carga y renderiza los elementos en el QTableWidget."""
        self.tabla.setRowCount(len(self.usuarios))
        for fila, u in enumerate(self.usuarios):
            item_id = QTableWidgetItem(str(u["id"]))
            item_id.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_nombre = QTableWidgetItem(u["nombre"])
            item_email = QTableWidgetItem(u["email"])
            item_rol = QTableWidgetItem(u["rol"])

            estado_txt = "Activo" if u["activo"] else "Inactivo"
            item_estado = QTableWidgetItem(estado_txt)
            item_estado.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.tabla.setItem(fila, 0, item_id)
            self.tabla.setItem(fila, 1, item_nombre)
            self.tabla.setItem(fila, 2, item_email)
            self.tabla.setItem(fila, 3, item_rol)
            self.tabla.setItem(fila, 4, item_estado)

    def _agregar_usuario(self):
        """Valida y registra un nuevo usuario."""
        nombre = self.txt_nombre.text().strip()
        email = self.txt_email.text().strip()
        rol = self.cmb_rol.currentText()
        activo = self.chk_activo.isChecked()

        if not nombre or not email:
            QMessageBox.warning(
                self,
                "Campos Incompletos",
                "Por favor, completa el nombre y el correo electrónico."
            )
            return

        nuevo_registro = {
            "id": str(self.contador_id),
            "nombre": nombre,
            "email": email,
            "rol": rol,
            "activo": activo
        }
        self.usuarios.append(nuevo_registro)
        self.contador_id += 1

        self._cargar_datos_tabla()
        self._limpiar_formulario()
        self.barra_estado.showMessage(f"Usuario '{nombre}' registrado con éxito", 5000)

    def _limpiar_formulario(self):
        """Restablece los campos de captura."""
        self.txt_nombre.clear()
        self.txt_email.clear()
        self.cmb_rol.setCurrentIndex(0)
        self.chk_activo.setChecked(True)
        self.txt_nombre.setFocus()

    def _fila_seleccionada(self):
        """Invocado cuando cambia la fila seleccionada en la tabla."""
        filas = self.tabla.selectedItems()
        if filas:
            fila_idx = self.tabla.currentRow()
            nombre = self.tabla.item(fila_idx, 1).text()
            self.barra_estado.showMessage(f"Fila activa: {nombre}")

    def _eliminar_usuario_seleccionado(self):
        """Elimina la fila seleccionada tras confirmar con diálogo modal."""
        fila_actual = self.tabla.currentRow()
        if fila_actual < 0:
            QMessageBox.information(self, "Aviso", "Selecciona una fila de la tabla primero.")
            return

        nombre_usuario = self.tabla.item(fila_actual, 1).text()
        id_usuario = self.tabla.item(fila_actual, 0).text()

        respuesta = QMessageBox.question(
            self,
            "Confirmar Eliminación",
            f"¿Estás seguro de que deseas eliminar al usuario '{nombre_usuario}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if respuesta == QMessageBox.StandardButton.Yes:
            self.usuarios = [u for u in self.usuarios if u["id"] != id_usuario]
            self._cargar_datos_tabla()
            self.barra_estado.showMessage(f"Usuario '{nombre_usuario}' eliminado", 4000)


def main():
    """Punto de entrada de la aplicación."""
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
