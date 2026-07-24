---
id: fastapi-introduccion
title: "Introducción a Fastapi"
sidebar_label: "📚 Introducción a Fastapi"
sidebar_position: 1
slug: /fastapi-intro
---



## Inicios y Origen
FastAPI es un marco de trabajo (framework) web moderno, de **alto rendimiento** y de código abierto, diseñado para construir APIs con Python 3.6+ basándose en las sugerencias de tipo (type hints) estándar de Python. Fue creado por **Sebastián Ramírez Montaño** y tuvo su lanzamiento inicial en **diciembre de 2018**. Su arquitectura fue diseñada tras un análisis de diversas alternativas, decidiendo construirse sobre dos pilares tecnológicos: **Starlette** para el manejo de la maquinaria web y **Pydantic** para la definición y validación de datos.

## Características Principales
*   **Rendimiento Superior:** Se sitúa como uno de los frameworks de Python más veloces, compitiendo en rendimiento con entornos como Node.js y Go. Esto es posible gracias a que implementa el estándar **ASGI (Asynchronous Server Gateway Interface)**, lo que le permite gestionar múltiples solicitudes mediante concurrencia sin bloquear el proceso principal.

*   **Documentación Automática e Interactiva:** Una de sus funciones más valoradas es la generación automática de documentación técnica siguiendo los estándares OpenAPI y JSON Schema. Al ejecutar la aplicación, el desarrollador dispone de interfaces como **Swagger UI** y **ReDoc**, que permiten explorar y probar los puntos de conexión (endpoints) de forma visual.

*   **Validación de Datos y Tipado Seguro:** Al utilizar las sugerencias de tipo de Python y la potencia de Pydantic, FastAPI realiza la **validación, serialización y conversión de datos** de forma automática. Esto garantiza que los datos que entran y salen de la API cumplan estrictamente con los esquemas definidos, reduciendo significativamente los errores en producción.

*   **Programación Asíncrona Nativa:** Soporta plenamente las funciones `async` y `await`, facilitando la creación de aplicaciones altamente escalables que no se detienen mientras esperan respuestas de bases de datos o servicios externos.

*   **Sistema de Inyección de Dependencias:** Posee un sistema modular de dependencias que permite reutilizar lógica, gestionar la seguridad (como autenticación OAuth2 y JWT) y optimizar las conexiones a bases de datos de manera limpia y organizada.

## Usos y Aplicaciones Comunes
*   **Desarrollo de Servicios de IA Generativa:** Es el framework de referencia para productivizar modelos de inteligencia artificial, permitiendo exponer modelos de lenguaje (LLMs), visión o audio como servicios escalables e integrados con sistemas externos.

*   **Arquitectura de Microservicios:** Su diseño ligero y eficiente lo hace ideal para el patrón de microservicios, donde cada componente cumple una función pequeña y específica de manera autónoma.

*   **Ciencia de Datos y Machine Learning:** Los científicos de datos lo utilizan para desplegar modelos de inferencia en tiempo real, crear APIs de acceso a datos para análisis y automatizar pipelines de procesamiento.

*   **Aplicaciones en Tiempo Real:** Gracias a su soporte para **WebSockets** y Eventos Enviados por el Servidor (SSE), se emplea en la creación de chats, tableros de control con datos en vivo y sistemas de notificaciones.

*   **Backend para Aplicaciones Modernas:** Sirve como el motor de backend para aplicaciones de página única (SPAs) y aplicaciones móviles, facilitando una comunicación rápida y estructurada mediante JSON.

FastAPI continúa evolucionando rápidamente, habiéndose convertido en uno de los frameworks web de Python de mayor crecimiento gracias a su excelente **experiencia de desarrollador** y su robustez técnica.