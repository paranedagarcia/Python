---
id: flask-microservicios
title: "Microservicios"
sidebar_label: "Microservicios"
sidebar_position: 5
---

La arquitectura de **microservicios** representa un paradigma de diseño de software en el cual una aplicación de gran envergadura se descompone en unidades funcionales pequeñas, independientes y autónomas que se comunican entre sí a través de una red,. A diferencia de la arquitectura monolítica, donde todos los componentes residen en un único proceso, cada microservicio se enfoca en una tarea específica y es gobernado por un contrato de interfaz, generalmente bajo el estilo arquitectónico **REST** (*Representational State Transfer* o Transferencia de Estado Representacional),.

### Fundamentos de los Microservicios con Flask

Flask es considerado un **microframework** (marco de trabajo minimalista) ideal para construir microservicios debido a su ligereza y a que no impone una estructura rígida al desarrollador,. Esta flexibilidad permite crear capas delgadas de servicio de datos que actúan como "cajas negras", ocultando la complejidad interna y exponiendo solo los puntos de acceso o **endpoints** necesarios,.

Para construir microservicios robustos con Flask, debe considerar los siguientes componentes tecnológicos:

1.  **Protocolo de Comunicación:** La comunicación suele realizarse mediante solicitudes **HTTP** (*Hypertext Transfer Protocol*), utilizando formatos de intercambio de datos como **JSON** (*JavaScript Object Notation*).

2.  **Servidor WSGI:** Flask requiere una **WSGI** (*Web Server Gateway Interface* o Interfaz de Pasarela de Servidor Web), como **Gunicorn**, para manejar las solicitudes en entornos de producción, ya que el servidor de desarrollo incluido no es lo suficientemente robusto.

3.  **Contenedores:** Se utiliza **Docker** para empaquetar el código, las dependencias y el entorno de ejecución en una imagen única, garantizando que el servicio funcione de la misma forma en cualquier host.

4.  **Orquestación:** Herramientas como **Docker Compose** permiten coordinar y enlazar múltiples contenedores (servicios) de manera local para pruebas de integración.

---

### Ejemplo Completo: Sistema de Usuarios y Verificación

A continuación, se detalla la construcción de un entorno con dos servicios: un servicio de **Usuarios** y un servidor de **Proxy Inverso** utilizando **Nginx**.

#### 1. Estructura del Proyecto
Debe organizar sus archivos de la siguiente manera para separar las responsabilidades:
```text
/proyecto-microservicios
├── docker-compose-dev.yml
└── /services
    ├── /users
    │   ├── Dockerfile-dev
    │   ├── manage.py
    │   ├── requirements.txt
    │   └── /project
    │       ├── __init__.py
    │       └── config.py
    └── /nginx
        ├── Dockerfile-dev
        └── dev.conf
```

#### 2. Definición del Microservicio de Usuarios (Flask)
En el archivo `services/users/project/__init__.py`, usted inicializará la aplicación y definirá una ruta de prueba:

```python
from flask import Flask, jsonify

app = Flask(__name__)
# Se establece la configuración desde un objeto externo
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
```

#### 3. Configuración de Docker para el Microservicio
Creará un archivo `services/users/Dockerfile-dev` para definir la imagen del contenedor:

```dockerfile
FROM python:3.6.4
# Instalación de netcat para verificar la disponibilidad de otros servicios
RUN apt-get update -yqq && apt-get install -yqq netcat
WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/app
CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]
```

#### 4. Configuración del Proxy Inverso (Nginx)
Para centralizar las solicitudes, se utiliza **Nginx** como puerta de entrada. En `services/nginx/dev.conf`, se redirigirá el tráfico hacia el contenedor de Flask:

```nginx
server {
    listen 80;
    location /users {
        proxy_pass http://users:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

#### 5. Orquestación con Docker Compose
Finalmente, se integrará ambos servicios en el archivo `docker-compose-dev.yml`:

```yaml
version: '3.4'
services:
  users:
    container_name: users
    build:
      context: ./services/users
      dockerfile: Dockerfile-dev
    environment:
      - APP_SETTINGS=project.config.DevelopmentConfig
    expose:
      - '5000'

  nginx:
    container_name: nginx
    build:
      context: ./services/nginx
      dockerfile: Dockerfile-dev
    ports:
        - 80:80
    depends_on:
      - users
```

### Ejecución del Sistema
Para poner en marcha estos microservicios, debe ejecutar los siguientes comandos en su terminal:
1. `docker-compose -f docker-compose-dev.yml build` (para construir las imágenes).
2. `docker-compose -f docker-compose-dev.yml up -d` (para iniciar los contenedores en segundo plano).

Una vez activos, podrá acceder a su microservicio a través de `http://localhost/users/ping`, donde Nginx recibirá la petición en el puerto 80 y la delegará internamente al servicio de Flask.