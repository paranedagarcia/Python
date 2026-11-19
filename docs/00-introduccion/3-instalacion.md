---
id: instalacion
title: "Instalación"
sidebar_label: "🖥️ Instalación"
description: "Núcleo y entornos de programación"
sidebar_position: 3
---

## **Pyhton**

Una ventaja importante es que Python es multiplataforma, y por tanto funciona perfectamente en todos los sistemas operativos más populares. Y los programas que produce se ejecutan sin alteraciones en cada sistema.

Solo varían las formas de instalación, propias de cada sistema:

### Windows
```bash
https://www.python.org/ftp/python/3.14.7/python-3.14.7-amd64.exe
```

### MacOS
```bash
https://www.python.org/ftp/python/3.14.7/python-3.14.7-macos11.pkg
```
### Linux
```bash
# debian Ubuntu
sudo apt update
sudo apt install python3.14 python3.14-venv python3.14-dev -y

# confirm
python3.14 --version

```

***
## **uv**

UV es un gestor de paquetes y proyectos de Python de última generación diseñado para reemplazar herramientas como pip, virtualenv, poetry y pyenv. Creado para ofrecer velocidad y eficiencia, UV proporciona una interfaz unificada para gestionar entornos, dependencias e incluso versiones de Python. Está escrito en `Rust`, lo que lo hace significativamente más rápido que las herramientas tradicionales.

**Documentación:**

https://docs.astral.sh/uv/getting-started/features

Instalar uv
```bash
# linux / Mac
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Windows con permiso para uso de directorios
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Verificar la instalación (Terminal / PowerShell)
```bash
uv --version
```
**Crear un entorno**

cambia al directorio de trabajo
```bash
cd directorio
```
crea el nuevo entorno
```bash
uv venv --python 3.14
```
Activar entorno virtual
```bash
source .venv/bin/activate  # For Linux/Mac
.venv\Scripts\activate     # For Windows
```
**Crea un proyecto** o inicializa el actual
```bash
uv init
```
**Gestión de dependencias**
```bash
uv add # instala dependencias
uv remove # elimina dependencias
uv sync # sincroniza las dependencias con el ambiente
uv lock # crea un archivo de bloqueo de las dependencias
uv pip install # instala dependencias con pip
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
**Eliminar un entorno**

Eliminar un entorno en Linux/Mac
```
rm -rf .venv
```
En Windows (PowerShell)
```
Remove-Item -Recurse -Force .venv
```

 ### Entornos centralizados

 Se puede crear un entorno virtual dentro de una carpeta centralizada (ej: `~/.venvs/`). Nombras cada entorno (ej: datascience) y lo activas desde cualquier proyecto.

 Crea la carpeta central y el entorno:
```bash
uv venv --python 3.14 ~/.venvs/datascience
```
Para Windows
```bash
uv venv -- python 3.14 %USERPROFILE%\.venvs\datascience
```
Instala los paquetes directamente en el nuevo entorno sin activarlo:
```bash
uv pip install --python 3.14 ~/.venvs/datascience pandas requests 
```
Activalo desde cualquier carpeta de trabajo
```bash
# linux / Mac
source ~/.venvs/datascience/bin/activate
# Windows
~\.venvs\datascience\Scripts\Activate.ps1
```
:::info
Si la versión 3.14 aún no la tienes descargada o gestionada por uv, este intentará descargarla automáticamente o puedes asegurarte de instalarla primero ejecutando:
```
uv python install 3.14
```
:::

**Eliminar un entorno centralizado**

Eliminar entornos centralizados en una ruta específica, borra la carpeta

Eliminar un entorno en Linux/Mac
```
rm -rf ~/.venvs/nombre_del_entorno
```
En Windows (PowerShell)
```
Remove-Item -Recurse -Force %USERPROFILE%\.venvs\nombre_del_entorno
```

### Sin entornos

Para crear un script sin requerir la creación de un nuevo entorno y solo utilizar uno previamente existente (no armas un proyecto), declara las dependencias dentro del mismo archivo Python .`.py`. 

`uv` creará en entorno temporal en la cache central, instalará las librerias y se utilizará automáticamente cada vez que se ejecute el script, sin agregar carpetas.

Agrega el encabezado siguiente en el archivo `simple.py`:
```python
# /// script
# dependencies = [
#   "requests",
#   "rich",
# ]
# ///

import requests
from rich import print

print("¡Ejecutando con dependencias aisladas y cacheadas!")
```
y se ejecuta directamente desde la terminal
```bash
uv run simple.py
```

#### Cuál elegir?


| Objetivo	| Solución con uv |	Ventaja principal|
|--- |--- |--- |
| Varios proyectos con las mismas librerías | uv venv ~/.venvs/nombre |	Los activas por nombre desde cualquier ruta. |
| Un solo entorno para toda la PC |	Variable<br/>UV_PROJECT_ENVIRONMENT | Nunca se crean carpetas .venv locales. |
| Scripts sueltos y automatizaciones | Dependencias inline + uv run | Cero configuración manual y reutilización automática. |


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
uv python install 3.14
uv python use 3.14
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

Este es un entorno de fácil uso y orientado principalmente al aprendizaje y la academia. No requiere instalación de versión alguna de Python o de librerias adicicionales, ya que posee las esenciales.

https://colab.research.google.com/
