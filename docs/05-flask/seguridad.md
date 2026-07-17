---
id: flask-seguridad
title: "Gestión de la seguridad"
sidebar_label: "​Seguridad"
sidebar_position: 9
sidebar_custom_props:
    icon: '​🔒'
---

Flask, como trabaja con una filosofía de **microframework** (marco de trabajo minimalista), proporciona un núcleo sólido pero delega la mayoría de los aspectos de seguridad de alto nivel a extensiones externas y a las buenas prácticas que usted, como desarrollador, decida implementar. A continuación, se detallan los aspectos fundamentales de seguridad que maneja Flask, las alternativas para su implementación y ejemplos técnicos orientados a su formación académica.

### 1. Gestión de Sesiones y la Clave Secreta (SECRET_KEY)

El aspecto de seguridad más elemental que Flask maneja de forma nativa es la protección de la sesión del usuario. Flask utiliza **cookies** (pequeños archivos de datos almacenados en el navegador del cliente) que están firmadas criptográficamente.

*   **Fundamento:** Para evitar que un atacante modifique el contenido de su sesión, Flask utiliza una **Clave Secreta** o *SECRET_KEY*. Esta es una cadena de caracteres aleatoria que se utiliza para generar una firma **HMAC** (*Hash-based Message Authentication Code* o Código de Autenticación de Mensajes basado en Hash).

*   **Ejemplo de implementación:**
    Usted debe configurar esta clave en el objeto de configuración de su aplicación:
    ```python
    app.config['SECRET_KEY'] = 'una_cadena_muy_dificil_de_adivinar'
    ```
    Es imperativo que, en entornos de producción, esta clave se cargue desde una **variable de entorno** y nunca se incluya directamente en el código fuente para evitar fugas de seguridad.

### 2. Protección contra Falsificación de Petición en Sitios Cruzados (CSRF)

La **CSRF** (*Cross-Site Request Forgery*) es un ataque donde un sitio malicioso engaña al navegador de un usuario para que realice acciones no deseadas en su aplicación web mientras el usuario está autenticado.

*   **Alternativa de implementación:** La solución estándar en el ecosistema Flask es la extensión **Flask-WTF**, que integra el paquete **WTForms**.

*   **Mecanismo:** Flask-WTF genera automáticamente un **token de seguridad** (una cadena única) que se incluye en cada formulario. El servidor verifica este token antes de procesar cualquier petición **POST** (*petición de envío de datos*). Si el token falta o es inválido, la petición se rechaza.

*   **Ejemplo de uso en plantilla:**
    ```html
    <form method="POST">
        {{ form.hidden_tag() }} <!-- Esto inserta el token CSRF automáticamente -->
        ...
    </form>
    ```

### 3. Almacenamiento Seguro de Contraseñas (Hashing)

Nunca se deben almacenar contraseñas en texto plano dentro de una base de datos. Si un atacante obtuviera acceso, todas las cuentas quedarían comprometidas.

*   **Alternativas de implementación:**
    *   **Werkzeug:** Incluido como dependencia básica de Flask, ofrece funciones como `generate_password_hash` y `check_password_hash`.

    *   **Flask-Bcrypt:** Utiliza el algoritmo **bcrypt**, diseñado específicamente para ser computacionalmente costoso y resistir ataques de fuerza bruta.

*   **Ejemplo de uso:**
    ```python
    from werkzeug.security import generate_password_hash, check_password_hash

    # Al registrar al usuario
    password_hash = generate_password_hash('password_del_usuario')

    # Al verificar el inicio de sesión
    es_valida = check_password_hash(password_hash, 'password_ingresado')
    ```

### 4. Autenticación y Autorización

Es crucial distinguir entre estos dos conceptos: la **autenticación** verifica quién es el usuario, mientras que la **autorización** determina qué tiene permiso de hacer.

*   **Implementación de Autenticación:** Se utiliza la extensión **Flask-Login**. Esta gestiona el ciclo de vida de la sesión, permitiendo proteger rutas mediante el decorador `@login_required`.

*   **Implementación de Autorización (RBAC):** El **RBAC** (*Role-Based Access Control* o Control de Acceso Basado en Roles) se puede implementar mediante decoradores personalizados que verifiquen los permisos del usuario antes de permitir el acceso a una vista.

*   **Ejemplo de decorador de autorización:**
    ```python
    @app.route('/admin')
    @login_required
    @admin_required # Decorador personalizado para verificar rol de administrador
    def admin_panel():
        return "Bienvenido, Administrador"
    ```

### 5. Seguridad en APIs y Recursos Compartidos (CORS y JWT)

Cuando usted construye servicios web o **APIs** (*Application Programming Interface*), surgen desafíos adicionales:

*   **CORS:** El **CORS** (*Cross-Origin Resource Sharing* o Intercambio de Recursos de Origen Cruzado) es un mecanismo de seguridad de los navegadores que restringe las peticiones HTTP entre diferentes dominios. En Flask, se maneja con la extensión **Flask-CORS** para permitir o denegar el acceso a orígenes específicos.

*   **JWT:** El **JWT** (*JSON Web Token*) es un estándar para transmitir información de forma segura entre las partes como un objeto JSON. Se utiliza frecuentemente en aplicaciones **stateless** (sin estado) para autenticar peticiones de APIs sin usar cookies de sesión.

### 6. Seguridad en el Despliegue (SSL/TLS)

En entornos de producción, es obligatorio utilizar **HTTPS** (*Hypertext Transfer Protocol Secure*) para cifrar la comunicación entre el cliente y el servidor, protegiendo los datos (como contraseñas) de ser interceptados.

*   **Aspecto crítico:** Usted nunca debe ejecutar su aplicación en producción con el modo de depuración activo (`debug=True`), ya que esto permite la ejecución de código remoto a través del depurador interactivo, dejando su servidor vulnerable a ataques.

*   **Alternativa:** Extensiones como **Flask-SSLify** ayudan a redirigir automáticamente todo el tráfico HTTP hacia HTTPS en plataformas que lo soporten.