---
id: instalacion
title: "Instalación y configuración"
sidebar_label: "Instalación"
sidebar_position: 2
---

##

### Windows
```bash
https://www.python.org/ftp/python/3.13.14/python-3.13.14-amd64.exe
```

### MacOS
```bash
https://www.python.org/ftp/python/3.13.14/python-3.13.14-macos11.pkg
```
### Linux
```bash
# debian Ubuntu
sudo apt update
sudo apt install python3.13 python3.13-venv python3.13-dev -y

# confirm
python3.13 --version

```

## UV
UV es un gestor de paquetes y proyectos de Python de última generación diseñado para reemplazar herramientas como pip, virtualenv, poetry y pyenv. Creado para ofrecer velocidad y eficiencia, UV proporciona una interfaz unificada para gestionar entornos, dependencias e incluso versiones de Python. Está escrito en `Rust`, lo que lo hace significativamente más rápido que las herramientas tradicionales.

Instalar uv
```bash
# linux / Mac
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Verificar
```bash
uv --version
```
Crear entorno
```bash
uv venv --python 3.11
```
Activar entorno virtual
```bash
source .venv/bin/activate  # For Linux/Mac
.venv\Scripts\activate     # For Windows
```
Instalar dependencias
```bash
uv pip install requests
```
Listar dependencias
```bash
uv pip freeze > requirements.txt
```
 Para proyectos usando `pyproject.toml`, UV automaticamente gestiona las dependencias y crea un archivo `uv.lock` para bloquear las versiones.

 Desactivar el entorno
 ```bash
 uv deactivate
 ```
 ### Migración
 Para migrar un entorno ya creado hacia uv
 ```bash
 uv init
 ```
 Convertir las dependencias
 ```bash
 uv add -r requirements.txt
 ```
 Lo que recrea pyproject.toml and uv.lock haciendo el proyecto compatible con `uv`

### Avanzado
Gestiona versiones de Python
```bash
uv python install 3.10
uv python use 3.10
```
Reproducibilidad
```bash
uv pip compile pyproject.toml -o requirements.txt
```
Bloquea dependencias en `requirements.txt`
```bash
uv pip compile requirements.in -o requirements.txt
```
Bloquea las dependencias declaradas en varios archivos
```bash
uv pip compile pyproject.toml requirements-dev.in -o requirements-dev.txt
```

## Visual Studio Code

https://code.visualstudio.com/

### Extensiones
- Python Debuger
- Python
- Pylance
- Python Environments
- Jupyter
- Jupyter Cell tags
- Jupyter Keymap
- Live Preview
- Rainbow CSV (mechatroner)
- vscode-pdf (tomokit1207)


## Colab Google

https://colab.research.google.com/
