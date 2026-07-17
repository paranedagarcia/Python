---
id: flask-blueprint
title: "Blueprint"
sidebar_label: "Blueprint"
sidebar_position: 3
---

Un **Blueprint** es un objeto de Flask diseñado para organizar y modularizar aplicaciones al permitir la división de estas en componentes independientes y reutilizables. 

A continuación, te detallo el concepto completo:

*   **Naturaleza modular:** Funcionan como "planos" que agrupan rutas, manejadores de errores, plantillas y archivos estáticos bajo una misma funcionalidad lógica (por ejemplo: autenticación, blog o API).

*   **Estado latente:** A diferencia de la aplicación principal (`app`), un Blueprint permanece en un estado "inactivo" o latente tras su definición; solo se integra y cobra vida cuando se registra formalmente en la aplicación, usualmente dentro de una **Application Factory**.

*   **Gestión de nombres:** Aplican un **espacio de nombres (namespace)** a todos sus endpoints, lo que permite que varios Blueprints definan funciones con el mismo nombre (como `index`) sin que existan colisiones, siempre que se referencien con el prefijo del Blueprint (ej. `auth.login`).

*   **Estructura y rutas:** Cada uno puede tener su propio **prefijo de URL** (como `/auth` o `/api`) y sus propios directorios independientes para archivos estáticos y plantillas, lo que facilita que diferentes equipos trabajen en módulos separados sin interferencias.

*   **Arquitectura MVC:** En aplicaciones empresariales, los Blueprints actúan como los **controladores** en un modelo Vista-Controlador (MVC), separando la lógica de las rutas de la definición de los modelos de datos.



### Ventajas de esta organización
1.  **Separación de responsabilidades**: Cada módulo es independiente, facilitando que varios desarrolladores trabajen en distintas áreas sin interferir entre sí.
2.  **Espacios de nombres (Namespaces)**: Flask aplica el nombre del Blueprint a todos los endpoints, permitiendo tener funciones llamadas `index` en diferentes módulos (ej. `auth.index` y `blog.index`).
3.  **Mantenibilidad**: Si detectas un error en la autenticación, sabes exactamente que debes buscar en la carpeta `/auth`.

¿Te gustaría ver un ejemplo de cómo configurar el archivo `__init__.py` dentro de un Blueprint para que Flask lo reconozca correctamente? He creado un informe técnico detallado que cubre los fundamentos de Flask, sus principales diferencias con Django y las ventajas que ofrece este microframework para el desarrollo moderno. El documento está disponible en la pestaña de Estudio.

### Registro de init

Para que Flask reconozca un **Blueprint** correctamente, el archivo `__init__.py` dentro de la carpeta del módulo debe instanciar el objeto `Blueprint` e importar las rutas (vistas) para registrarlas.

Aquí tienes un ejemplo técnico basado en un módulo de autenticación:

```python showLineNumbers
# app/auth/__init__.py
from flask import Blueprint

# 1. Se crea la instancia del Blueprint
# 'auth' es el nombre del blueprint para url_for
# __name__ ayuda a Flask a localizar recursos como plantillas
auth = Blueprint('auth', __name__)

# 2. IMPORTANTE: Importar las vistas al final para evitar importaciones circulares.
# Esto asegura que el objeto 'auth' ya esté definido cuando views intente usarlo.
from . import views
```


En el archivo `views.py`, se utiliza el objeto `auth` que se importa desde el paquete actual para definir las rutas. Aquí se vería:

```python showLineNumbers
# app/auth/views.py
from flask import render_template, redirect, url_for
from . import auth  # Importamos la instancia del Blueprint

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Lógica para mostrar o procesar el formulario de inicio de sesión
    return render_template('auth/login.html')

@auth.route('/logout')
def logout():
    # Lógica para cerrar sesión
    return redirect(url_for('main.index'))
```


#### Detalles importantes:
*   **Decorador:** Usas `@auth.route` en lugar de `@app.route`.
*   **Nombres de puntos finales:** Al estar dentro de un Blueprint, Flask aplica un espacio de nombres. Para referirte a la función `login` desde fuera del módulo, usarías `url_for('auth.login')`.
*   **Puntos relativos:** Dentro del mismo Blueprint, puedes usar un punto como atajo: `url_for('.login')`.




### Puntos clave para la configuración:
*   **Nombre del Blueprint:** El primer argumento (ej. `'auth'`) se utiliza como prefijo para los nombres de los endpoints (ej. `auth.login`).
*   **Importación de vistas:** Siempre debe ir después de la definición del objeto `auth` para evitar que el intérprete de Python falle por dependencias circulares.
*   **Registro:** Recuerda que este Blueprint permanecerá inactivo hasta que lo registres en tu función de fábrica `create_app` usando `app.register_blueprint(auth)`.

¿Te gustaría ver cómo se escribiría el archivo `views.py` para que utilice este objeto `auth` que acabamos de crear?

## Registro de Blueprint

Para registrar un **Blueprint** dentro de la función de fábrica `create_app`, debes seguir un proceso sencillo que integra los módulos en la aplicación principal en tiempo de ejecución:

1.  **Importar el Blueprint:** Realiza la importación de la instancia del Blueprint directamente dentro de la función `create_app`. Esto se hace habitualmente para evitar problemas de dependencias circulares entre los archivos del proyecto.
2.  **Usar `app.register_blueprint`:** Llama a este método pasando la instancia del Blueprint importado como argumento.
3.  **Configurar parámetros opcionales:** Puedes usar el argumento `url_prefix` para que todas las rutas definidas en ese Blueprint comiencen con un prefijo específico (por ejemplo, `/auth` o `/api`).

### Ejemplo técnico de registro
Siguiendo la estructura modular, el código dentro de `create_app` se vería así:

```python showLineNumbers
def create_app(config_name):
    app = Flask(__name__)
    # ... inicialización de configuraciones y extensiones ...

    # Registro del Blueprint principal
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Registro de un Blueprint con prefijo de URL
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
```
(Fuentes)

Este patrón permite que los Blueprints permanezcan "inactivos" hasta que se inyectan en la aplicación real al llamar a la fábrica.

### Manejo de errores

El manejo de errores en los **Blueprints** de Flask se diferencia principalmente en el alcance que desees darle al controlador:

*   **Alcance Local (`@blueprint.errorhandler`):** Si usas este decorador, el manejador solo se activará para los errores que se originen dentro de las rutas definidas en ese Blueprint específico.
*   **Alcance Global (`@blueprint.app_errorhandler`):** Para registrar manejadores de errores que funcionen en toda la aplicación (independientemente de qué Blueprint genere el fallo), debes usar este decorador.

#### Ejemplo de implementación
Dentro de un archivo como `errors.py` asociado a tu Blueprint:

```python showLineNumbers
from flask import render_template
from . import main_blueprint

# Solo para errores dentro de este Blueprint
@main_blueprint.errorhandler(404)
def local_not_found(e):
    return render_template('404_especifico.html'), 404

# Para errores en toda la aplicación
@main_blueprint.app_errorhandler(500)
def global_internal_error(e):
    return render_template('500.html'), 500
```


Este enfoque es ideal para aplicaciones grandes porque permite que cada módulo gestione sus propios fallos lógicos sin contaminar el código central.

La diferencia principal entre estos dos decoradores radica en su **alcance** (scope) cuando se utilizan dentro de un **Blueprint**:

*   **`@blueprint.errorhandler` (Local):** El manejador solo se activará para los errores que se originen específicamente dentro de las rutas definidas en ese Blueprint,.
*   **`@blueprint.app_errorhandler` (Global):** Permite registrar manejadores de errores que funcionen para **toda la aplicación**. Independientemente de qué parte del código o qué Blueprint genere el fallo, este manejador interceptará el error,.

**¿Cuándo usar cada uno?**
*   Usa `errorhandler` si quieres que un módulo (como un blog) tenga su propio diseño de página de error 404, distinto al del resto del sitio.
*   Usa `app_errorhandler` para errores genéricos de la aplicación o si estás construyendo una API y quieres que todos los errores 404 devuelvan un objeto JSON en lugar de HTML, sin importar la ruta solicitada.

#### Respuestas JSON

Para que tus manejadores de errores respondan con **JSON**, debes sustituir la función `render_template` por `jsonify` y asegurarte de devolver el código de estado HTTP correspondiente.

Aquí tienes las dos formas de implementarlo según tus necesidades:

**1. Respuesta JSON Directa (Exclusivo para APIs)**

Si tu aplicación es puramente una API, simplemente defines el manejador para que devuelva un objeto JSON:

```python showLineNumbers
from flask import jsonify

@main_blueprint.app_errorhandler(404)
def not_found_json(e):
    # Retorna un diccionario convertido a JSON y el código 404
    return jsonify({'error': 'Not found', 'message': str(e)}), 404
```

**2. Negociación de Contenido (Híbrido: HTML o JSON)**

Si quieres que el mismo manejador responda con JSON a un cliente de API y con HTML a un navegador, debes usar **negociación de contenido** revisando el encabezado `Accept` de la solicitud:

```python showLineNumbers
from flask import request, jsonify, render_template

@main_blueprint.app_errorhandler(404)
def page_not_found(e):
    # Verifica si el cliente prefiere JSON antes que HTML
    if request.accept_mimetypes.accept_json and \
       not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    
    # Respuesta por defecto para navegadores
    return render_template('404.html'), 404
```

**Puntos clave:**
*   **`jsonify`**: Convierte diccionarios de Python en respuestas con formato JSON y establece automáticamente el tipo de contenido como `application/json`.
*   **Códigos de estado**: Es vital incluirlos manualmente al final del `return` (201, 400, 404, etc.) para que el cliente sepa qué ocurrió sin procesar el texto.


Para implementar una respuesta JSON global en una API de Flask, la mejor estrategia es utilizar **negociación de contenido** dentro de los manejadores de error globales. Esto permite que la aplicación responda con JSON a los clientes de la API y con HTML a los navegadores convencionales.

Los pasos clave para su implementación:

1.  **Uso de `app_errorhandler`**: Para que un manejador dentro de un Blueprint capture errores en toda la aplicación, debes usar el decorador `@blueprint.app_errorhandler` en lugar del local.

2.  **Negociación de Contenido**: Dentro de la función, verifica el encabezado `Accept` de la solicitud mediante `request.accept_mimetypes`. Si el cliente solicita JSON y no prefiere HTML, genera la respuesta estructurada.

3.  **Respuesta JSON**: Utiliza la función `jsonify()` para convertir un diccionario de Python en el cuerpo de la respuesta y establece manualmente el código de estado HTTP (como 404 o 500).

4.  **Manejo de Excepciones Personalizadas**: Puedes registrar manejadores para clases de excepción específicas, como un `ValidationError`. Esto permite capturar errores de lógica de negocio en cualquier parte del código y devolver siempre un error 400 en formato JSON de manera automática.

Este enfoque mantiene las funciones de vista (view functions) limpias y concisas, ya que no necesitan incluir lógica de captura de errores repetitiva.


Para implementar la negociación de contenido, se utiliza el objeto `request.accept_mimetypes` de Flask para determinar qué formato prefiere el cliente (habitualmente a través de la cabecera `Accept`). 

Aquí tienes un ejemplo práctico aplicado a un manejador de errores:

```python showLineNumbers
from flask import request, jsonify, render_template

@app.errorhandler(404)
def page_not_found(e):
    # Si el cliente solicita JSON y no prefiere HTML
    if request.accept_mimetypes.accept_json and \
       not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    
    # Respuesta por defecto (HTML para navegadores)
    return render_template('404.html'), 404
```


**Puntos clave:**
*   **API vs Navegador:** Los navegadores generalmente no imponen restricciones estrictas, por lo que recibirán el HTML, mientras que los clientes de API suelen solicitar JSON específicamente.

*   **jsonify:** Esta función no solo convierte los datos, sino que establece automáticamente el `Content-Type` como `application/json`.

#### Excepcion personalizada

Para estructurar una clase de excepción personalizada en una API de Flask, el primer paso es definir una clase que herede de una excepción estándar de Python, como `ValueError`. Esta clase puede ser extremadamente sencilla, actuando simplemente como un marcador para errores de lógica de negocio o validación:

```python showLineNumbers
class ValidationError(ValueError):
    pass
```

Una vez definida, puedes registrar un controlador global para esta excepción específica utilizando el decorador `@api.errorhandler(ValidationError)`. Este controlador interceptará cualquier instancia de la excepción que se lance dentro del Blueprint y transformará el mensaje de error en una respuesta estructurada. Por ejemplo, se puede utilizar una función auxiliar para devolver un JSON con el código de estado 400 (Bad Request):

```python showLineNumbers
@api.errorhandler(ValidationError)
def validation_error(e):
    # e.args contiene el mensaje pasado al levantar la excepción
    return bad_request(e.args)

def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response
```

Este patrón permite que la lógica de tus modelos o funciones de vista se mantenga limpia. En lugar de incluir bloques repetitivos de comprobación de errores, simplemente levantas la excepción cuando los datos no cumplen con los requisitos:

```python showLineNumbers
if body is None or body == '':
    raise ValidationError('El post no tiene contenido.')
```

¿Te parece útil este enfoque para centralizar errores o prefieres que veamos cómo implementar **autenticación basada en tokens (JWT)** para proteger estas mismas rutas?

#### Excepción para validacion de datos

Para crear una excepción personalizada para la validación de datos en una API de Flask, se sigue un patrón de tres pasos que permite mantener el código de las rutas limpio y centralizado.

**1. Definir la clase de excepción**

Primero, se crea una clase que herede de una excepción estándar de Python, como `ValueError`. Esta clase actúa como un marcador específico para errores de validación:

```python showLineNumbers
class ValidationError(ValueError):
    pass
```

**2. Registrar el manejador de errores global**

Para evitar el uso repetitivo de bloques `try-except` en cada ruta, se utiliza el decorador `@api.errorhandler` (asociado a tu aplicación o Blueprint). Este capturará cualquier instancia de `ValidationError` que se lance y devolverá una respuesta JSON estructurada:

```python showLineNumbers
@api.errorhandler(ValidationError)
def validation_error(e):
    # e.args contiene el mensaje pasado al levantar la excepción
    return bad_request(e.args)

def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response
```

**3. Lanzar la excepción en la lógica**

Ahora, en tus modelos o funciones de procesamiento, simplemente lanzas la excepción cuando los datos no cumplen con los requisitos. Flask se encargará automáticamente de enviarla al manejador definido arriba:

```python showLineNumbers
def from_json(json_post):
    body = json_post.get('body')
    if body is None or body == '':
        raise ValidationError('El post no tiene contenido.')
    return Post(body=body)
```

Este enfoque garantiza que tu API siempre responda con el mismo formato de error ante fallos de entrada de datos.





