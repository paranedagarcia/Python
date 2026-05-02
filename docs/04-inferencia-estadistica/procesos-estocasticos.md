---
id: procesos-estocasticos
title: Procesos Estocásticos
sidebar_label: Procesos Estocásticos
sidebar_position: 5
---

## Procesos Estocásticos

Mientras que la inferencia bayesiana se enfoca en actualizar la creencia sobre parámetros, otra rama de la estadística nos ayuda a modelar secuencias de eventos aleatorios: la teoría de **procesos estocásticos**. Un proceso estocástico es una colección de variables aleatorias ordenadas en el tiempo (o en el espacio), que describe la evolución de un sistema aleatorio. Dos conceptos clave en este campo son los modelos de **Markov** y la distribución de **Poisson**.

Los **modelos de Markov** son procesos estocásticos que cumplen con la propiedad de Markov: el futuro estado del sistema depende solo del estado presente y no de la secuencia de eventos que lo precedió. Esta propiedad "sin memoria" simplifica enormemente el modelado. Un modelo de Markov se define por un conjunto de estados y las probabilidades de transición entre ellos. Por ejemplo, podríamos modelar el clima de una ciudad como un modelo de Markov con estados "soleado", "nublado" y "lluvioso". Conociendo la probabilidad de que un día soleado sea seguido por otro soleado, o por un día lluvioso, podríamos predecir la probabilidad de un patrón climático a largo plazo. Los **cadenas de Markov** son una aplicación directa de esto y se utilizan en diversos campos, desde la biología para modelar secuencias de ADN hasta en marketing para modelar la trayectoria del usuario en un sitio web.

Como ya discutimos, la distribución de **Poisson** modela el número de eventos que ocurren en un intervalo de tiempo o espacio. El proceso de Poisson es el proceso estocástico subyacente que describe la ocurrencia de estos eventos. Una de sus características clave es que el tiempo entre eventos consecutivos sigue una distribución exponencial. Por lo tanto, si el número de clics en un anuncio web sigue una distribución de Poisson, el tiempo que transcurre entre cada clic seguirá una distribución exponencial.

En resumen, al avanzar en el razonamiento estadístico, encontramos herramientas que van más allá de los datos estáticos y fijos. La inferencia bayesiana nos brinda un marco dinámico para actualizar nuestra comprensión a medida que se acumula nueva evidencia. Por otro lado, los procesos estocásticos, como los modelos de Markov y el proceso de Poisson, nos permiten modelar sistemas que cambian con el tiempo de una manera rigurosa y probabilística. Estos principios avanzados son los que impulsan aplicaciones innovadoras en aprendizaje automático, finanzas, genómica y ciencias sociales, demostrando que la estadística es un campo vivo y en constante evolución.