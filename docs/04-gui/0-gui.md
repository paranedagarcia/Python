---
id: tkinter
title: "GUI en Python"
sidebar_label: "🖥️ GUI en Python"
description: "Desarrollo GUI e Python"
---

En el ecosistema de Python existen varias herramientas y bibliotecas consolidadas para el desarrollo de interfaces gráficas de usuario (GUI) a nivel profesional, cada una orientada a diferentes requisitos de arquitectura, rendimiento, plataforma y estética:

---

### **1. PyQt / PySide (Qt para Python) — El estándar de la industria**
Es el conjunto de herramientas más potente y utilizado en entornos empresariales, aplicaciones de ingeniería, diseño asistido (CAD) y software científico de alto rendimiento.
* **Qué es:** Enlaces en Python (*bindings*) para el framework **Qt** en C++. Existen dos versiones principales:
  * **PySide (oficial de The Qt Company):** Licencia LGPL, muy favorable para proyectos comerciales cerrados sin costo de licencia si se enlaza dinámicamente.
  * **PyQt (de Riverbank Computing):** Licencia GPL / Comercial.
* **Ventajas:**
  * Rendimiento nativo muy elevado y aceleración por hardware.
  * Colección inmensa de widgets complejos (gráficos vectoriales, docks acoplables, tablas avanzadas con arquitectura Modelo-Vista-Controlador).
  * Incluye **Qt Designer** (herramienta visual de arrastrar y soltar para diseñar interfaces) y soporte para **QML / Qt Quick** (interfaces animadas y fluidas tipo móvil).
* **Ideal para:** Aplicaciones de escritorio complejas de nivel corporativo o comercial multiplataforma (Windows, Linux, macOS).

---

### **2. wxPython — Aspecto y comportamiento 100% nativo**
* **Qué es:** Es una envoltura sobre la biblioteca C++ **wxWidgets**.
* **Ventajas:**
  * A diferencia de Qt (que dibuja sus propios controles con gran precisión imitando al sistema), wxPython **utiliza los controles nativos reales del sistema operativo** subyacente (Win32 en Windows, Cocoa en macOS, GTK en Linux).
  * La aplicación se siente y comporta exactamente como cualquier otro programa nativo del sistema en el que se ejecuta.
* **Ideal para:** Software de escritorio donde la integración visual y el respeto estricto a las guías de diseño de cada sistema operativo sean prioritarios.

---

### **3. Kivy — Multiplataforma con soporte móvil (Android / iOS)**
* **Qué es:** Framework enfocado en interfaces táctiles (*NUI*) y multitáctiles con renderizado directo sobre OpenGL ES 2.
* **Ventajas:**
  * Una sola base de código para escritorio y plataformas móviles.
  * Gran flexibilidad gráfica y soporte para gestos táctiles complejos.
* **Ideal para:** Aplicaciones táctiles industriales, quioscos interactivos, pantallas táctiles en dispositivos embebidos (como Raspberry Pi) y aplicaciones móviles en Python.

---

### **4. Flet (Basado en Flutter) — La alternativa moderna y reactiva**
* **Qué es:** Un framework reciente y de rápido crecimiento que permite construir interfaces de Python utilizando el motor de renderizado de **Flutter (de Google)**.
* **Ventajas:**
  * Estética moderna basada en **Material Design 3** sin esfuerzo.
  * Soporta modo claro/oscuro automático, animaciones fluidas y reactividad en el estado.
  * La misma aplicación puede empaquetarse para escritorio (Windows, Mac, Linux), móviles (iOS, Android) o ejecutarse directamente como una aplicación web en el navegador.
* **Ideal para:** Desarrolladores que buscan interfaces contemporáneas de manera rápida con una arquitectura moderna orientada a componentes.

---

### **5. CustomTkinter y ttkbootstrap — Modernización ligera sobre Tkinter**
* **Qué son:** Extensiones que eliminan la estética clásica de Tkinter sin la complejidad de aprender C++ o frameworks pesados:
  * **`CustomTkinter`:** Estilo plano contemporáneo (*Flat Design*), bordes redondeados y soporte nativo de modo oscuro/claro.
  * **`ttkbootstrap`:** Estilos y temas inspirados en Bootstrap (versiones 4 y 5) aplicables sobre `ttk`.
* **Ventajas:** No requieren dependencias complejas, son muy fáciles de distribuir y mantienen un consumo de memoria mínimo.
* **Ideal para:** Herramientas internas de empresa, paneles de administración ligeros, utilidades y prototipado rápido.

---

### **Resumen Comparativo Rápido**

| Framework | Integración Visual | Complejidad | Plataformas | Caso de uso principal |
| :--- | :--- | :---: | :--- | :--- |
| **PySide / PyQt** | Motor Qt personalizable | Alta | Win, Mac, Linux | Software corporativo, suites profesionales y herramientas científicas. |
| **wxPython** | Controles nativos del S.O. | Media-Alta | Win, Mac, Linux | Programas que deben integrarse como software del sistema. |
| **Flet** | Flutter (Material Design) | Media | Escritorio, Móvil, Web | Apps modernas multiplataforma con estética web/móvil. |
| **Kivy** | Gráficos OpenGL propios | Media | Escritorio, Móvil (Android/iOS) | Pantallas táctiles, quioscos y aplicaciones móviles. |
| **CustomTkinter** | Moderna sobre Tkinter | Baja | Win, Mac, Linux | Herramientas de escritorio ligeras y paneles de gestión. |

---

💡 ¿Te gustaría ver un ejemplo práctico de cómo se estructura una ventana con **PySide6 / PyQt** o prefieres explorar cómo funciona **Flet** para interfaces multiplataforma?