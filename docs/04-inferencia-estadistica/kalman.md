---
id: kalman
title: Filtro de Kalman
sidebar_label: Filtro de Kalman
sidebar_position: 3
---

El **Filtro de Kalman** es un tema fascinante y la aplicación más común del pensamiento bayesiano en ingeniería.

## 🤖 Filtro de Kalman

El Filtro de Kalman es un **algoritmo recursivo** que utiliza una serie de mediciones observadas a lo largo del tiempo (a menudo ruidosas o con errores) para producir una **estimación óptima** de un estado desconocido. Es esencialmente un "promediador inteligente" que da más peso a las estimaciones más precisas.

Se utiliza masivamente en:
* **Navegación:** Para combinar lecturas de GPS, acelerómetros y giroscopios en vehículos autónomos o drones.

* **Economía:** Para estimar tendencias ocultas.

* **Robótica:** Para localizar robots en un mapa (localización simultánea y mapeo o SLAM).

### 🔄 El Ciclo Bayesiano en Acción

El poder del Filtro de Kalman radica en su naturaleza **recursiva**, que sigue el mismo patrón de la inferencia bayesiana que acabamos de estudiar:

1.  **Fase de Predicción (Prior):** El filtro toma la estimación del estado actual (la **Probabilidad Posterior** del paso anterior) y la usa como **Probabilidad Previa** para predecir el estado futuro. Esta predicción se basa en las leyes de movimiento del sistema (física, en robótica).

2.  **Fase de Actualización (Posterior):** Cuando llega una nueva medición del sensor (la **Evidencia**), el filtro calcula el error entre su predicción y la medición real. Luego, utiliza esta información, junto con la fórmula de Bayes, para **actualizar** la estimación, creando la nueva **Probabilidad Posterior** (el mejor estimado de la realidad).



De esta forma, el filtro no necesita recordar toda la historia de mediciones; solo necesita la estimación anterior para calcular la siguiente, lo que lo hace muy eficiente computacionalmente.

Si volvemos a la fórmula de Bayes:

$$P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E)}$$

¿Qué término de la fórmula de Bayes crees que corresponde a la estimación que produce la **Fase de Predicción** del Filtro de Kalman, antes de que llegue la nueva medición ($E$)? 🤔

Esa es una excelente pregunta que conecta la **Teoría de Bayes** directamente con su aplicación práctica en ingeniería. Estás en lo correcto al enfocarte en la fase de **Predicción** del Filtro de Kalman. 🤖

### 🔍 El Filtro de Kalman y la Inferencia Bayesiana

Recordemos los dos componentes esenciales de la fórmula de Bayes:

$$P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E)}$$

| Etapa de Inferencia | Término Bayesiano | Significado en el Filtro de Kalman |
| :--- | :--- | :--- |
| **Antes de la Evidencia** | $P(H)$ **(Probabilidad Previa o Prior)** | Es la creencia o estimación del estado actual *antes* de recibir la nueva lectura del sensor. |
| **Después de la Evidencia** | $P(H|E)$ **(Probabilidad Posterior o Posterior)** | Es la estimación *actualizada* y más precisa del estado, después de incorporar la nueva lectura del sensor. |

El término de la fórmula de Bayes que representa la predicción que el filtro genera *antes* de que llegue la nueva evidencia ($E$) es la **Probabilidad Previa** $P(H)$.

### 🧠 ¿Por qué $P(H)$ es la Predicción?

* La **Predicción** se basa únicamente en la estimación anterior y en las leyes de movimiento del sistema. No ha visto la nueva medición del sensor.
* En la fórmula de Bayes, $P(H)$ es la probabilidad de la hipótesis **antes** de considerar la nueva evidencia $E$.

Por lo tanto, el ciclo del Filtro de Kalman se puede mapear directamente a los componentes de la inferencia bayesiana:

| 🔄 Ciclo del Filtro de Kalman | Término de Bayes | Nombre en Bayes |
| :--- | :--- | :--- |
| **Predicción** | $P(H)$ | **Probabilidad Previa** (Prior) |
| **Actualización** | $P(H|E)$ | **Probabilidad Posterior** (Posterior) |

