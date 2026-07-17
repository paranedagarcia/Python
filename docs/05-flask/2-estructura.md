---
id: flask-estructura
title: "Estructura"
sidebar_label: "Estructura"
sidebar_position: 2
---

Para manejar aplicaciones de alta complejidad, Flask utiliza una estructura modular basada en **paquetes de Python** y **Blueprints**. Esta organización permite que el proyecto escale de manera predecible y que varios desarrolladores trabajen en distintas áreas sin interferir entre sí.

### Componentes Clave de la Estructura Modular

1.  **Patrón de Fábrica de Aplicaciones (`Application Factory`):** En lugar de crear una instancia global de Flask, se define una función (usualmente `create_app`) que configura e instancia la aplicación. Esto facilita el uso de diferentes configuraciones (desarrollo, pruebas, producción) y mejora la testabilidad.

2.  **Blueprints:** Actúan como controladores que agrupan rutas, plantillas y archivos estáticos por funcionalidad (por ejemplo: `auth`, `blog`, `api`). Cada Blueprint se registra en la aplicación central dentro de la fábrica de aplicaciones.

3.  **Separación de Responsabilidades:** Dentro de cada módulo funcional, se deben separar los componentes para mantener el código limpio:
    *   `models.py`: Definiciones de la base de datos específicas del módulo.
    *   `forms.py`: Formularios de usuario y validaciones.
    *   `controllers.py` (o `views.py`): Lógica de las rutas asociada al Blueprint.


### Organización de un proyecto

En una aplicación Flask de alta complejidad, la organización de carpetas sigue un patrón modular para asegurar que el código sea predecible y escalable. Basándonos en las mejores prácticas, la estructura se vería así:

### Estructura de un Proyecto Modular
*   **`/flask_project`**: Raíz del proyecto que contiene archivos de configuración como `config.py`, el script de ejecución `manage.py` y la lista de dependencias `requirements.txt`.

*   **`/app` (o `/webapp`)**: Paquete principal de la aplicación.
    *   **`__init__.py`**: Contiene la **Application Factory** (`create_app`), donde se inicializan las extensiones y se registran los Blueprints.

    *   **`/main`, `/auth`, `/api`**: Subcarpetas para cada Blueprint (característica).
        *   **`__init__.py`**: Crea la instancia del `Blueprint`.

        *   **`views.py` (o `controllers.py`)**: Define las rutas y la lógica de control específica de ese módulo.

        *   **`models.py` y `forms.py`**: Definen las tablas de la base de datos y los formularios asociados únicamente a ese módulo.

    *   **`/templates`**: Carpeta global de plantillas, pero organizada internamente en subcarpetas con el nombre de cada Blueprint (ej. `/templates/auth/login.html`) para evitar colisiones de nombres.

    *   **`/static`**: Archivos CSS, JavaScript e imágenes.

#### Ejemplo de estructura

Siguiendo las mejores prácticas para aplicaciones escalables y el patrón de **Fábrica de Aplicaciones**, esta es la estructura de carpetas recomendada para un proyecto conteniendo:

```text
/proyecto_flask
│
├── manage.py              # Script para ejecutar la app y comandos
├── config.py              # Configuraciones (Desarrollo, Producción)
├── requirements.txt       # Dependencias del proyecto
│
└── /webapp                # Paquete principal de la aplicación
    ├── __init__.py        # Fábrica de aplicaciones (create_app)
    │
    ├── /admin             # Módulo de Administración
    │   ├── __init__.py    # Creación del Blueprint 'admin'
    │   ├── controllers.py # Rutas y lógica de vistas
    │   ├── models.py      # Modelos de base de datos del módulo
    │   └── forms.py       # Formularios WTForms
    │
    ├── /clientes          # Módulo de Clientes
    │   ├── __init__.py    # Creación del Blueprint 'clientes'
    │   ├── controllers.py
    │   ├── models.py
    │   └── forms.py
    │
    ├── /ventas            # Módulo de Ventas
    │   ├── __init__.py    # Creación del Blueprint 'ventas'
    │   ├── controllers.py
    │   ├── models.py
    │   └── forms.py
    │
    ├── /compras           # Módulo de Compras
    │   ├── __init__.py    # Creación del Blueprint 'compras'
    │   ├── controllers.py
    │   ├── models.py
    │   └── forms.py
    │
    ├── /templates         # Plantillas HTML organizadas por módulo
    │   ├── /admin
    │   ├── /clientes
    │   ├── /ventas
    │   └── /compras
    │
    └── /static            # Archivos CSS, JS e imágenes
```

#### Puntos clave:
*   **Separación de responsabilidades:** Cada carpeta de módulo es independiente, conteniendo sus propios modelos, formularios y rutas.

*   **Evitar colisiones:** Organizar los `templates` en subcarpetas permite usar nombres comunes (como `index.html`) sin que Flask se confunda, siempre que se referencien como `admin/index.html`.

*   **Registro central:** Todos estos Blueprints se importan y registran dentro de `create_app` en `webapp/__init__.py`.


#### Configuracion  ```__init__```

Para registrar automáticamente tus módulos (`admin`, `clientes`, `ventas`, `compras`) utilizando el patrón de **Fábrica de Aplicaciones**, se debe configurar el archivo `webapp/__init__.py` importando cada Blueprint y llamando a `app.register_blueprint()`.

Un ejemplo técnico de cómo se vería ese archivo:

```python
from flask import Flask
from .admin.controllers import admin_blueprint
from .clientes.controllers import clientes_blueprint
from .ventas.controllers import ventas_blueprint
from .compras.controllers import compras_blueprint

def create_app(config_name):
    app = Flask(__name__)
    # ... configuraciones adicionales ...

    # Registro de Blueprints
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.register_blueprint(clientes_blueprint, url_prefix='/clientes')
    app.register_blueprint(ventas_blueprint, url_prefix='/ventas')
    app.register_blueprint(compras_blueprint, url_prefix='/compras')

    return app
```


#### Puntos clave:
*   **Separación de rutas:** Al usar `url_prefix`, aseguras que las rutas de cada módulo no colisionen (ej. `/admin/index` vs `/ventas/index`).

*   **Importación dentro de la fábrica:** En aplicaciones con muchas dependencias circulares, es común realizar las importaciones de los Blueprints directamente dentro de la función `create_app` para evitar errores de ejecución.

*   **Flexibilidad:** Este patrón permite crear múltiples instancias de la aplicación con diferentes configuraciones (desarrollo, pruebas, producción) de manera sencilla.

#### Conexión personalizada a base de datos

Para manejar conexiones independientes en una estructura modular, tienes dos caminos principales según el nivel de aislamiento que busques:

**1. Aplicación Modular con Múltiples Bases de Datos (Binds)**

Si mantienes una sola aplicación Flask pero quieres que cada módulo (`admin`, `clientes`, etc.) apunte a una base de datos distinta, utilizas una característica de Flask-SQLAlchemy llamada **Binds**:

*   **Configuración:** En tu `config.py`, defines un diccionario `SQLALCHEMY_BINDS` donde asignas una URI diferente a cada módulo.

*   **Asignación en Modelos:** En el archivo `models.py` de cada módulo, añades la propiedad `__bind_key__` a tus clases. Por ejemplo, en `webapp/ventas/models.py`:

    ```python
    class Venta(db.Model):
        __bind_key__ = 'ventas' # Indica que este modelo usa la BD de ventas
        id = db.Column(db.Integer, primary_key=True)
    ```
*   **Gestión Centralizada:** Sigues usando un único objeto `db` inicializado en la fábrica de aplicaciones, pero Flask sabe a qué base de datos enviar cada consulta según el modelo.

**2. Arquitectura de Microservicios (Independencia Total)**

Si se necesita que la independencia sea absoluta (por ejemplo, que el módulo de `compras` use MySQL y el de `clientes` use Postgres), debe evolucionar hacia **Microservicios**:

*   **Aislamiento de Datos:** Cada módulo se convierte en una aplicación Flask independiente que corre en su propio contenedor (Docker).

*   **Configuración propia:** Cada servicio tiene su propio archivo de entorno (`.env`) con su `DATABASE_URL` específica.

*   **Comunicación:** Los módulos ya no comparten el objeto `db`; se comunican entre sí mediante solicitudes HTTP a sus respectivas APIs RESTful.


