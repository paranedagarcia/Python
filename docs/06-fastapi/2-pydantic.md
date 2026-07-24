---
id: pydantic
title: "Pydantic"
sidebar_label: "📚 Introducción a Pydantic"
sidebar_position: 1
slug: /pydantic
---


El sistema de validación de **FastAPI** se basa fundamentalmente en **Pydantic**, una librería de validación de datos y gestión de configuraciones que utiliza sugerencias de tipo (type hints) de Python. Esta integración permite que FastAPI sea extremadamente robusto al manejar cómo los datos entran y salen de tu aplicación.

## Aspectos clave

### 1. Modelos de Datos (`BaseModel`)
En el núcleo de Pydantic están los **Modelos**, que son clases que heredan de `BaseModel`. Estos modelos definen la estructura, el tipo y las restricciones de los datos. Al declarar un modelo, especificas el tipo de cada campo (string, entero, lista, etc.), y Pydantic se encarga de que los datos cumplan con esa definición en tiempo de ejecución.

### 2. Validación y Conversión Automática
Pydantic no solo valida que el tipo sea correcto, sino que también realiza **conversiones de tipos (casting)** automáticas cuando es posible. Por ejemplo, si un campo espera un entero y recibe el string `"123"`, Pydantic lo convertirá automáticamente al número `123`. Si los datos no coinciden ni pueden convertirse, FastAPI generará automáticamente un error **422 Unprocessable Entity** con detalles precisos sobre dónde y por qué falló la validación.

### 3. Restricciones Avanzadas con `Field`
Además de los tipos básicos, puedes usar la función `Field` de Pydantic para añadir reglas de validación mucho más estrictas:
*   **Cadenas:** Longitud mínima/máxima (`min_length`, `max_length`).
*   **Números:** Rangos (como `ge=1` para mayor o igual a 1).
*   **Formatos especiales:** Pydantic incluye tipos para correos electrónicos (`EmailStr`), URLs (`HttpUrl`), UUIDs y direcciones IP.

### 4. Validadores Personalizados
Para lógicas de negocio más complejas, Pydantic permite crear funciones de validación propias:
*   **`@field_validator`:** Permite validar o transformar el valor de un campo específico.
*   **`@model_validator`:** Útil cuando la validación depende de la interacción entre múltiples campos (por ejemplo, comprobar que "contraseña" y "confirmar contraseña" sean iguales).

### 5. Roles en FastAPI (Entrada y Salida)
FastAPI utiliza estos modelos en dos direcciones principales:
*   **Validación de entrada:** Cuando defines un parámetro en tu función de ruta con un modelo de Pydantic, FastAPI valida automáticamente el cuerpo de la solicitud (request body).
*   **Serialización de salida (`response_model`):** Al especificar un modelo en el decorador de la ruta, FastAPI garantiza que la respuesta solo contenga los campos definidos en ese modelo, filtrando automáticamente datos sensibles o internos que no deban devolverse al cliente.

### 6. Documentación Automática
Una de las mayores ventajas es que FastAPI utiliza estos esquemas de Pydantic para generar automáticamente la especificación **OpenAPI (JSON Schema)**. Esto es lo que alimenta las interfaces interactivas como **Swagger UI** y **ReDoc**, permitiendo que los desarrolladores vean y prueben los formatos de datos exactos que requiere la API.

### 7. Rendimiento
Es importante destacar que, a partir de **Pydantic V2**, gran parte de la lógica de validación se ha reescrito en **Rust**, lo que lo convierte en uno de los sistemas de validación más rápidos disponibles para Python.

Si usas `dataclasses` estándar de Python, FastAPI también las soporta, aunque internamente las convierte en "sabores" de Pydantic para poder aplicar todas estas funcionalidades de validación y documentación.