---
id: teoria-probabilidad
title: Teoria de Probabilidad
sidebar_label: Teoria de probabilidad
sidebar_position: 2
---



## 🎲 1. Introducción a la Teoría de la Probabilidad

La **probabilidad** es una rama de las matemáticas que se encarga de cuantificar la **incertidumbre**. Nos permite asignar un valor numérico entre 0 (imposible) y 1 (certeza) a la posibilidad de que ocurra un evento.

### 🔑 Conceptos Clave

  * **Experimento Aleatorio:** Cualquier proceso cuyo resultado no se puede predecir con certeza (ejemplo: lanzar un dado).
  * **Espacio Muestral ($\Omega$):** El conjunto de todos los posibles resultados de un experimento aleatorio (ejemplo: al lanzar un dado, $\Omega = \{1, 2, 3, 4, 5, 6\}$).
  * **Evento (E):** Un subconjunto del espacio muestral, es decir, un resultado o un conjunto de resultados que nos interesa (ejemplo: obtener un número par, $E = \{2, 4, 6\}$).

### 🔢 Cálculo Básico de la Probabilidad

La probabilidad simple de que ocurra un evento $E$ se calcula usando la **Regla de Laplace**:

$$P(E) = \frac{\text{Número de resultados favorables}}{\text{Número total de resultados posibles}}$$

### 💻 Ejemplo en Python: Probabilidad Simple

Podemos simular un experimento simple como lanzar un dado.

```python
# Importamos la librería 'random' para simular el lanzamiento
import random

# Definimos el espacio muestral (resultados posibles)
espacio_muestral = [1, 2, 3, 4, 5, 6]

# Definimos el evento E: obtener un número par
evento_e = [2, 4, 6]

# Cálculo de la probabilidad teórica
probabilidad_teorica = len(evento_e) / len(espacio_muestral)

print(f"Espacio Muestral (Ω): {espacio_muestral}")
print(f"Evento E (número par): {evento_e}")
print(f"P(E) = {len(evento_e)} / {len(espacio_muestral)} = {probabilidad_teorica:.2f}")
```

-----

Estos fundamentos son la base. El siguiente paso lógico, y crucial para el Teorema de Bayes, es entender la **Probabilidad Condicional**.

Pero antes de seguir, a partir de la explicación anterior, ¿cómo definirías la probabilidad de obtener un número **menor o igual a 3** al lanzar ese mismo dado? 🤔

La probabilidad de obtener un número menor o igual a 3 ($\{1, 2, 3\}$) era, en efecto, $3/6 = 0.5$. 

Excelente, has pasado directamente al concepto central: la **Probabilidad Condicional**. Es un paso crucial, ya que el Teorema de Bayes se basa completamente en ella.

Antes de seguir, la probabilidad de obtener un número menor o igual a 3 ($\{1, 2, 3\}$) era, en efecto, $3/6 = 0.5$. ¡Bien hecho\!

-----

## 🔗 2. Probabilidad Condicional

La **probabilidad condicional** es la probabilidad de que ocurra un **Evento A**, sabiendo que otro **Evento B** ya ha ocurrido. En esencia, estamos **reduciendo nuestro espacio muestral** a la información que ya conocemos.

### ✍️ Notación y Fórmula

La probabilidad condicional se denota como $P(A|B)$, que se lee: "Probabilidad de A, dado B" o "Probabilidad de A, condicional a B".

Se calcula con la siguiente fórmula:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

Donde:

  * $P(A \cap B)$ es la probabilidad de que **A y B** ocurran conjuntamente (la intersección).
  * $P(B)$ es la probabilidad del evento que ya se conoce (la condición).

[Images of Venn diagram conditional probability]

### 💡 El Impacto del "Dado Que"

El factor clave es el término "**dado que**". Nos dice que ya no consideramos todos los posibles resultados ($\Omega$), sino solo aquellos resultados que cumplen con la condición $B$.

### 💻 Ejemplo en Python: Reducción del Espacio Muestral

Volvamos a nuestro dado de 6 caras. Queremos calcular:

  * **Evento A:** Obtener un número impar ($\{1, 3, 5\}$).
  * **Evento B:** Obtener un número mayor que 3 ($\{4, 5, 6\}$).

**Pregunta:** ¿Cuál es la probabilidad de obtener un número impar, *dado que* el número fue mayor que 3? $P(A|B)$.

```python
# Definimos las probabilidades de los eventos
P_A = 3/6  # P(impar)
P_B = 3/6  # P(mayor que 3)

# Calculamos la probabilidad de la intersección (A y B)
# Los resultados que son impares Y mayores que 3: solo el 5
interseccion_A_B = 1/6

# Aplicamos la fórmula de probabilidad condicional: P(A|B) = P(A ∩ B) / P(B)
P_A_dado_B = interseccion_A_B / P_B

print(f"P(A ∩ B) = {interseccion_A_B:.2f}")
print(f"P(B) = {P_B:.2f}")
print(f"P(Impar | >3) = P(A|B) = {P_A_dado_B:.3f} (o 1/3)")
```

-----

Ahora que tenemos esta base, podemos formular una nueva pregunta usando el mismo dado:

¿Cuál es la probabilidad de obtener un número **mayor que 4** (Evento A), **dado que** el resultado fue un **número par** (Evento B)?

Identificar cuáles son los resultados de la intersección ($A \cap B$) y la probabilidad de la condición ($P(B)$).

  * **A** (mayor que 4) = $\{5, 6\}$
  * **B** (par) = $\{2, 4, 6\}$
  * La intersección ($A \cap B$) es $\{6\}$ (un solo resultado).
  * $P(A|B) = P(A \cap B) / P(B) = (1/6) / (3/6) = 1/3$. 

¡Buena pregunta\! Es excelente revisar los fundamentos antes de avanzar, ya que el Teorema de Bayes utiliza estas operaciones constantemente.

-----


## 🎯 3. Eventos y Operaciones

Un **evento** ($\text{E}$) es, simplemente, un **subconjunto** del espacio muestral ($\Omega$). Es la descripción de uno o más resultados que nos interesan de un experimento.

Por ejemplo, si el experimento es la extracción de una carta de una baraja de 52 cartas:

  * $\Omega$ = Las 52 cartas.
  * Evento $A$ = Obtener un As.
  * Evento $B$ = Obtener una carta de Corazones.

### 🧮 Operaciones Básicas entre Eventos (Basadas en Teoría de Conjuntos)

Las operaciones nos permiten combinar o modificar los eventos para calcular probabilidades más complejas.

| Operación | Símbolo | Significado | Descripción de Resultados |
| :--- | :--- | :--- | :--- |
| **Unión** | $\text{A} \cup \text{B}$ | $\text{A}$ o $\text{B}$ | Ocurre si $\text{A}$ ocurre, $\text{B}$ ocurre, o ambos ocurren. |
| **Intersección** | $\text{A} \cap \text{B}$ | $\text{A}$ y $\text{B}$ | Ocurre solo si $\text{A}$ y $\text{B}$ ocurren simultáneamente. |
| **Complemento** | $\text{A}^\text{c}$ o $\text{A}'$ | No $\text{A}$ | Ocurre si $\text{A}$ no ocurre. |
| **Eventos Mutuamente Excluyentes** | $\text{A} \cap \text{B} = \emptyset$ | $\text{A}$ y $\text{B}$ son Disjuntos | No pueden ocurrir al mismo tiempo (su intersección es vacía). |

[Images of Venn diagram showing set operations union intersection complement]

### 💻 Ejemplo de Operaciones en Python (Concepto)

Podemos ver las operaciones de manera práctica usando los conjuntos de Python.

**Experimento:** Lanzar un dado ($\Omega = \{1, 2, 3, 4, 5, 6\}$).

```python
espacio_muestral = {1, 2, 3, 4, 5, 6}
A = {1, 2, 3}  # Evento A: Obtener 3 o menos
B = {2, 4, 6}  # Evento B: Obtener un número par

# 1. Unión (A o B)
# Usamos el operador '|' o el método union()
union_A_B = A.union(B)
print(f"Unión (A U B): {union_A_B}") # Debe ser {1, 2, 3, 4, 6}

# 2. Intersección (A y B)
# Usamos el operador '&' o el método intersection()
interseccion_A_B = A.intersection(B)
print(f"Intersección (A ∩ B): {interseccion_A_B}") # Debe ser {2}
```

-----

Ahora es tu turno de practicar una operación fundamental. Usando los mismos conjuntos:

**Evento A** = $\{1, 2, 3\}$

¿Cuál es el **Complemento de A** ($A^c$)? ¿Qué resultados incluye y cuál es su probabilidad $P(A^c)$? 🤔

Para el evento **A** (Obtener 3 o menos) = $\{1, 2, 3\}$, el **Complemento de A** ($A^c$) es $\{4, 5, 6\}$, que son los resultados de "obtener más de 3". Su probabilidad es $P(A^c) = 3/6 = 0.5$.



## 📊 4. Probabilidad Marginal

La **probabilidad marginal** de un evento es la probabilidad de que ese evento ocurra, calculada **sin tener en cuenta ninguna otra variable** (o "marginando" la información sobre otras variables).

Imagina que tienes una tabla de datos (una tabla de contingencia) que muestra la cantidad de hombres y mujeres que votaron 'Sí' o 'No'. La probabilidad marginal sería la probabilidad de "votar Sí" (sin importar si fue hombre o mujer) o la probabilidad de "ser mujer" (sin importar si votó Sí o No).

### 🆚 Contraste con Otros Tipos

* **Probabilidad Marginal ($P(A)$):** La probabilidad de un solo evento. *Ejemplo: ¿Cuál es la probabilidad de que llueva?*
* **Probabilidad Conjunta ($P(A \cap B)$):** La probabilidad de que dos eventos ocurran juntos. *Ejemplo: ¿Cuál es la probabilidad de que llueva **y** sea fin de semana?*
* **Probabilidad Condicional ($P(A|B)$):** La probabilidad de A dado que B ya ocurrió. *Ejemplo: ¿Cuál es la probabilidad de que llueva, **dado que** hay nubes negras?*

### ➕ La Ley de la Probabilidad Total (Cálculo Marginal)

En el contexto del Teorema de Bayes, a menudo no conocemos la probabilidad marginal $P(A)$ directamente. En cambio, usamos la **Ley de la Probabilidad Total (LPT)**, que nos permite calcular $P(A)$ sumando las probabilidades conjuntas de $A$ con todos los posibles escenarios ($B_i$) que pueden causar $A$.

$$P(A) = \sum_{i} P(A \mid B_i) P(B_i)$$

Donde $B_i$ son eventos mutuamente excluyentes y exhaustivos (cubren todo el espacio muestral).

En el mundo real, esta ley nos permite encontrar la probabilidad general de un resultado (por ejemplo, "que una persona dé positivo en un test médico") considerando todas las formas en que ese resultado puede ocurrir (dado que está enferma **O** dado que no está enferma).

---

Ahora que hemos cubierto la Probabilidad Condicional y la Marginal, estamos listos para unir estos conceptos en el teorema más poderoso de la probabilidad.

El **Teorema de Bayes** es esencialmente una herramienta para **actualizar nuestras creencias** basadas en nueva evidencia.

$$\text{P(Hipótesis | Evidencia)} = \frac{\text{P(Evidencia | Hipótesis)} \cdot \text{P(Hipótesis)}}{\text{P(Evidencia)}}$$

En esta fórmula, el término $P(\text{Evidencia})$ en el denominador es precisamente una **Probabilidad Marginal** (calculada con la Ley de la Probabilidad Total).
