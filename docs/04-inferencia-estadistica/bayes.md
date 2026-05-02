---
id: bayes
title: Teorema de Bayes
sidebar_label: Teorema de Bayes
sidebar_position: 2
---

# Razonamiento Estadístico

Hasta ahora, se ha explorado los fundamentos de la estadística clásica, también conocida como estadística frecuentista. En este paradigma, los parámetros poblacionales (como la media μ) son considerados como valores fijos pero desconocidos, y los datos de la muestra se ven como realizaciones aleatorias de un proceso. Sin embargo, existe un segundo gran paradigma, la **inferencia bayesiana**, que ofrece un enfoque conceptualmente diferente y cada vez más popular en la ciencia de datos. En el enfoque bayesiano, los parámetros poblacionales no se consideran fijos, sino que se tratan como variables aleatorias con sus propias distribuciones de probabilidad. Esto permite incorporar conocimiento previo o creencias sobre los parámetros antes de ver los datos, y luego actualizar estas creencias de manera sistemática a medida que se obtienen nuevos datos.

## Teorema de Bayes

El corazón de la inferencia bayesiana es el **Teorema de Bayes**, una fórmula fundamental de la probabilidad que describe cómo calcular la probabilidad condicional de un evento. Su función principal es describir cómo una creencia inicial o probabilidad, debe ser actualizada racionalmente cuando se dispone de nueva evidencia o datos.

En el contexto del aprendizaje automático (Machine Learning), el Teorema de Bayes es la base del aprendizaje bayesiano (Bayesian learning), donde los parámetros del modelo se tratan como variables aleatorias. La tarea de aprendizaje se transforma así en un esfuerzo por inferir la distribución de probabilidad que describe los parámetros desconocidos, lo que se conoce como distribución a posteriori.

En el contexto de la inferencia, el teorema de Bayes relaciona la probabilidad condicional de dos eventos. Dada una hipótesis H y una evidencia E, el teorema se define formalmente como:
La fórmula establece cómo la probabilidad de un evento $H$ (la hipótesis) cambia cuando se observa un evento $E$ (la evidencia).

$$P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E)}$$



| Término | Nombre | Significado Conceptual |
| :--- | :--- | :--- |
| $P(H\|E)$ | **Probabilidad Posterior** | Lo que queremos saber: la probabilidad de la hipótesis *después* de ver la evidencia. Es el resultado buscado: la probabilidad de que la hipótesis H sea cierta una vez que se ha observado la evidencia D. El posterior es proporcional al producto del likelihood y el prior.|
| $P(E\|H)$ | **Verosimilitud (Likelihood)** | La probabilidad de ver la evidencia, *dada* que la hipótesis es verdadera. Este término vincula el modelo (hipótesis) con los datos observados.|
| $P(H)$ | **Probabilidad Previa (Prior)** | Nuestra creencia inicial sobre la hipótesis *antes* de ver la evidencia. Es la probabilidad inicial o creencia subjetiva de que la hipótesis H sea cierta antes de que se observe la evidencia D. La elección del prior es fundamental, ya que representa el conocimiento previo disponible. |
| $P(E)$ | **Evidencia/Probabilidad Marginal** | La probabilidad de la evidencia en general. Se calcula usando la Ley de Probabilidad Total, es una constante de normalización que asegura que la probabilidad a posteriori sume uno. |

 
Esta fórmula es igualmente válida si H y E representan variables aleatorias, donde P se convierte en la función de densidad de probabilidad (ξ o f).

P(Y∣X_1,…,X_n)∝P(Y) 




### 💡 Ejemplos Cotidianos de su Uso

El teorema de Bayes se utiliza constantemente en sistemas donde las predicciones deben adaptarse a nuevos datos.

  * **1. 📧 Filtros de Spam (Tecnología):**

      * Los filtros de correo usan Bayes para calcular $P(\text{Spam} | \text{Palabra X})$. El sistema aprende que si un correo contiene la palabra **$E$** ("farmacia"), la probabilidad de que sea spam **$H$** aumenta significativamente respecto a la probabilidad previa ($P(H)$) de cualquier correo aleatorio de la bandeja de entrada.

  * **2. 🩺 Diagnóstico Médico (Salud):**

      * Como vimos, se usa para calcular $P(\text{Enfermo} | \text{Positivo})$. El resultado depende tanto de la **precisión del test** ($P(E|H)$) como de la **prevalencia de la enfermedad** en la población ($P(H)$). Si una enfermedad es muy rara, es más probable que un positivo sea un falso positivo, incluso con un test muy bueno.

  * **3. 💰 Finanzas y Mercados:**

      * Los analistas usan modelos bayesianos para actualizar las probabilidades de un evento económico (ej. una recesión) a medida que se publican nuevos datos (ej. tasas de desempleo).

### 💉 Ejemplo Práctico en Python: El Test Médico

Retomemos el ejemplo médico para ver la fuerza de la **Probabilidad Previa ($P(H)$)**.

**Escenario:**

  * **Enfermedad Rara ($P(H)$):** 0.1% (0.001)
  * **Test Preciso ($P(E|H)$):** 99% (0.99)
  * **Falsa Alarma ($P(E|\text{No } H)$):** 5% (0.05)

**Objetivo:** Calcular $P(\text{Enfermo} | \text{Positivo})$.


El resultado final, $P(\text{Enfermo} | \text{Positivo}) \approx 0.019$ (o 1.9%), es muy bajo.

¿Por qué la probabilidad de estar realmente enfermo es solo del **1.9%** a pesar de que el test tiene una precisión del 99%? ¿Qué factor de los datos iniciales es el más determinante en este sorprendente resultado? 🤔

El resultado sorprendentemente bajo ($1.9\%$) para $P(\text{Enfermo} | \text{Positivo})$ se debe a una de las probabilidades iniciales. 

Esa es una observación clave. La **Probabilidad Previa** $P(H)$ es, de lejos, el factor más determinante en este resultado. Acá se muestro por qué, en términos de la fórmula de Bayes: 💡

$$P(H|E) = \frac{\overbrace{P(E|H) \cdot P(H)}^{\text{Casos Verdaderos Positivos}}}{\underbrace{P(E|H) \cdot P(H) + P(E|\text{No } H) \cdot P(\text{No } H)}_{\text{Casos Positivos Totales (Evidencia, } P(E))}}$$

### 📉 El Impacto de $P(H)$

1.  **El Numerador (Casos Verdaderos Positivos):** La probabilidad de que un resultado positivo sea verdadero es directamente proporcional a $P(H)$. Dado que $P(H)$ es muy pequeña ($0.001$), el numerador es diminuto: $0.99 \times 0.001 = 0.00099$.

2.  **El Denominador (Casos Positivos Totales):** La evidencia total $P(E)$ está compuesta por dos vías para obtener un positivo:
    * **Verdaderos Positivos** ($0.00099$).
    * **Falsos Positivos** ($P(E|\text{No } H) \cdot P(\text{No } H)$). Este término es $0.05 \times 0.999 \approx 0.04995$.

El valor de la evidencia ($P(E) \approx 0.05$) está **dominado por los falsos positivos** ($0.04995$) porque la población sana ($P(\text{No } H)$) es 999 veces más grande que la población enferma.

Al dividir el numerador muy pequeño ($0.00099$) entre un denominador mucho más grande que él ($0.05$), el resultado final ($P(H|E) \approx 1.9\%$) permanece bajo. **La rareza de la enfermedad ($P(H)$) supera la precisión del test ($P(E|H)$).**




## 🌎 Aplicaciones de Bayes en Diversas Industrias

### ⛏️ 1. Geología y Exploración de Recursos

En la búsqueda de petróleo, gas o depósitos minerales, las empresas enfrentan una gran incertidumbre.

* **Hipótesis ($H$):** Existe un depósito comercialmente viable en una ubicación específica.
* **Evidencia ($E$):** Los datos sísmicos arrojaron un patrón positivo (indicando posible estructura).

Antes de la perforación, la **Probabilidad Previa ($P(H)$)** puede ser muy baja (ej. 10%). Sin embargo, si los costosos y complejos datos sísmicos ($E$) son positivos, se usa Bayes para calcular la **Probabilidad Posterior ($P(H|E)$)**. Esta probabilidad actualizada es la que se utiliza para tomar la decisión de invertir millones en la perforación.

### 🤖 2. Robótica y Navegación Autónoma

Los robots, drones y vehículos autónomos usan técnicas bayesianas, como el **Filtro de Kalman**, para estimar su ubicación en tiempo real.

* **Hipótesis ($H$):** La ubicación actual del robot en el mapa.
* **Evidencia ($E$):** Las nuevas lecturas de los sensores (ej. GPS, LiDAR).

Cada nueva lectura de un sensor ($E$) se toma como evidencia que **actualiza** la creencia previa sobre la ubicación. Si el GPS da una ubicación, esta es la *evidencia*. El sistema usa Bayes para ponderar esa evidencia con su última estimación conocida (la *Prior*) y generar una nueva y más precisa estimación (la *Posterior*). Esto permite que la navegación sea fluida y precisa, a pesar del ruido o error en los sensores.

![](https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcSby6f7hmf4dsSDRE6kSnI9HvtDunMnM4lF0xgrcVXTaGvVR4rL63YNFuZ7x0ilm7wurhzAMIREZYZKG2ELe1m5MiNqGwZBWeaLUg_YRDom2CuukoY)

### ⚖️ 3. Ciencia Forense y Legal

En los tribunales, Bayes ayuda a cuantificar el valor de la evidencia, especialmente la evidencia estadística como el ADN.

* **Hipótesis ($H$):** El acusado es el responsable.
* **Evidencia ($E$):** Se encontró una coincidencia de ADN entre el acusado y la escena del crimen.

La fórmula de Bayes ayuda a los expertos a determinar la probabilidad de que la coincidencia de ADN ocurra **dado que** el acusado es inocente ($P(E|\text{No } H)$), contra la probabilidad de que la coincidencia ocurra **dado que** el acusado es culpable ($P(E|H)$). Esto permite a los jurados concentrarse en el verdadero valor probatorio de la evidencia.
