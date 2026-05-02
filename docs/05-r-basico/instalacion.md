---
id: r-instalar
title: Instalación
sidebar_label: Instalación
sidebar_position: 2
---

## Instalación de R

### Windows
1. Descarga el instalador desde [CRAN Windows](https://cran.r-project.org/bin/windows/base/)
2. Ejecuta el archivo `.exe` descargado
3. Sigue el asistente de instalación con opciones predeterminadas
4. Verifica la instalación abriendo CMD y ejecutando: `R --version`

### macOS
1. Descarga el instalador `.pkg` desde [CRAN macOS](https://cran.r-project.org/bin/macos/)
2. Selecciona la versión compatible con tu procesador (Apple Silicon o Intel)
3. Abre el instalador y sigue las instrucciones
4. Verifica desde Terminal: `R --version`

### Linux
**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install r-base r-base-dev
```

**Fedora/RHEL:**
```bash
sudo dnf install R
```

**Arch Linux:**
```bash
sudo pacman -S r
```

Verifica: `R --version`

### IDE Recomendado
Instala [RStudio](https://posit.co/download/rstudio-desktop/) para una experiencia mejorada con editor, consola y visualización integrados.

