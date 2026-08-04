---
id: rabbitmq
title: "RabbitMQ"
sidebar_label: "Introduccion"
sidebar_position: 1
---


RabbitMQ es un intermediario de mensajes (message broker) de código abierto. Imagínalo como una oficina de correos para tus aplicaciones informáticas. Vamos a explorar cómo funciona paso a paso.

Cuando una parte de un sistema de software quiere enviar datos a otra, en lugar de enviarlos directamente (lo que puede ser lento o fallar si la otra parte está ocupada o apagada), se los entrega a RabbitMQ. RabbitMQ recibe, almacena y distribuye estos "mensajes" a su destino de manera segura y ordenada. Es como asegurar que una carta llegue a su destinatario sin importar si está en casa en el momento exacto en que llega el cartero 📬.

Esto permite que sistemas muy complejos y diferentes aplicaciones se comuniquen entre sí de manera asíncrona, sin tener que esperar a que el otro termine su tarea.

Veamos tres escenarios comunes donde RabbitMQ es fundamental para separar tareas y manejar grandes cargas de trabajo:

* 🛒 **Comercio electrónico (Procesamiento de pedidos)**: Al hacer clic en "Pagar", se desencadenan varias acciones: procesar el pago, actualizar el inventario, notificar a la bodega y enviar un correo de confirmación. RabbitMQ pone el pedido en una "cola" para que distintos sistemas realicen este trabajo en segundo plano, permitiendo que la página web te confirme la compra casi al instante.
* 🎞️ **Procesamiento de videos**: Cuando subes un video a una plataforma, el sistema debe convertirlo a diferentes resoluciones (1080p, 720p, etc.). En lugar de hacerte esperar mirando una pantalla de carga, la aplicación envía un mensaje a RabbitMQ. Servidores especializados toman esos mensajes de la cola y procesan los videos a su propio ritmo.
* 🌡️ **Internet de las Cosas (IoT)**: Imagina miles de sensores climáticos enviando datos de temperatura cada segundo. Si enviaran la información directamente a la base de datos principal, RabbitMQ es un intermediario de mensajes (message broker) de código abierto. Imagínalo como una oficina de correos para tus aplicaciones informáticas. Vamos a explorar cómo funciona paso a paso.

Cuando una parte de un sistema de software quiere enviar datos a otra, en lugar de enviarlos directamente (lo que puede ser lento o fallar si la otra parte está ocupada o apagada), se los entrega a RabbitMQ. RabbitMQ recibe, almacena y distribuye estos "mensajes" a su destino de manera segura y ordenada. Es como asegurar que una carta llegue a su destinatario sin importar si está en casa en el momento exacto en que llega el cartero 📬.

Esto permite que sistemas muy complejos y diferentes aplicaciones se comuniquen entre sí de manera asíncrona, sin tener que esperar a que el otro termine su tarea.podrían colapsarla por exceso de tráfico. RabbitMQ actúa como un amortiguador, recibiendo los datos rápidamente y guardándolos para que la base de datos los absorba de manera controlada.

Pensando en el ejemplo del comercio electrónico, ¿qué crees que pasaría con la experiencia del usuario o con el sistema si *no* usáramos RabbitMQ y cada uno de los pasos (pago, inventario, envío, email) tuviera que completarse de forma estricta y secuencial antes de poder mostrar la pantalla de "Compra exitosa"?

Imagina la diferencia entre hacer una llamada telefónica 📞 y enviar una carta por correo ✉️.

Cuando dos aplicaciones usan una **API directa** (como una petición web tradicional), es como una llamada telefónica: la comunicación es *síncrona*. La Aplicación A "llama" a la B y tiene que esperar en la línea hasta obtener una respuesta. Si la Aplicación B está apagada, actualizándose o sobrecargada, la llamada simplemente falla y la Aplicación A se queda bloqueada.

Con un **intermediario de mensajes** (RabbitMQ), es como el sistema postal: la comunicación es *asíncrona*. La Aplicación A deja el mensaje en el buzón (RabbitMQ) y sigue con su trabajo inmediatamente. El intermediario se encarga de guardarlo y entregarlo a la Aplicación B cuando esta se encuentre lista para procesarlo.

Aquí tienes un resumen de las principales ventajas de usar un intermediario:

| Característica | API Directa (Síncrona) 📞 | RabbitMQ (Asíncrona) ✉️ |
| --- | --- | --- |
| **Tolerancia a fallos** | Si el sistema receptor colapsa, la comunicación falla y los datos pueden perderse. | Los mensajes se guardan seguros en una "cola" hasta que el receptor vuelva a funcionar. |
| **Acoplamiento** | Las aplicaciones dependen directamente la una de la otra y de sus tiempos de respuesta. | Las aplicaciones son independientes; solo necesitan saber cómo hablar con el intermediario. |
| **Picos de tráfico** | Un aumento repentino de peticiones (ej. Black Friday) puede tumbar el servidor receptor. | Absorbe el golpe y entrega los mensajes poco a poco, al ritmo que el receptor soporte. |

Para poner esto en práctica, imagina que estás diseñando el sistema de un cajero automático. Cuando un cliente intenta retirar dinero, el sistema debe consultar la base de datos del banco para verificar que tenga saldo suficiente.

Para este paso específico (verificar el saldo), ¿crees que sería mejor usar una API directa o enviarlo como un mensaje a través de RabbitMQ? ¿Por qué?

## Conceptos básicos

¡Excelente! Vamos a desglosar los tres componentes fundamentales de RabbitMQ usando nuestra analogía del sistema postal:

* **Productor (Producer):** Es la aplicación que crea y envía el mensaje. En nuestra analogía, es la persona que escribe la carta y la envía.

* **Cola (Queue):** Es el buzón o almacén temporal que vive dentro de RabbitMQ. Los mensajes que envía el productor se acumulan aquí de forma segura hasta que alguien esté listo para recogerlos.

* **Consumidor (Consumer):** Es la aplicación que se conecta a RabbitMQ para recibir, leer y procesar los mensajes de la cola. Siguiendo el ejemplo, es el destinatario final que saca la carta del buzón y ejecuta la tarea que dice adentro.

El flujo básico de comunicación se ve así:

`[Productor] ➡️ envía mensaje a ➡️ [Cola] ➡️ entrega mensaje a ➡️ [Consumidor]`

Para poner estos conceptos en práctica, volvamos al ejemplo de la tienda en línea que mencionamos antes. Cuando un cliente hace clic en "Pagar" y el sistema genera una orden de envío para que la bodega empaquete el producto:

¿Qué parte del sistema actuaría como el **Productor** y qué parte sería el **Consumidor** en ese escenario específico?