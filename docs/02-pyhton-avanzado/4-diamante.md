---
id: diamante
title: "​Problema del diamante"
sidebar_label: "​El problema del diamante"
description: "El problema del diamante y su ejecución"
---

El **Problema del Diamante** (o *Diamond Problem*) es una complicación clásica de la herencia múltiple en la programación orientada a objetos que ocurre cuando una subclase hereda de dos clases que, a su vez, derivan de una misma clase base común, formando una estructura con forma de rombo o diamante.


### El Problema

1. **Doble inicialización y duplicación de llamadas:**  
   Si una subclase intenta inicializar a sus padres haciendo llamadas explícitas y directas al nombre de la clase (por ejemplo, `Contacto.__init__(self)` y `Direccion.__init__(self)`), el método inicializador de la clase base común superior termina ejecutándose **dos veces**. En sistemas reales, esta inicialización doble puede reiniciar estados de forma indebida, provocar bugs de datos o malgastar recursos críticos (como intentar conectarse dos veces a una base de datos).

2. **Ambigüedad en la resolución de métodos:**  
   En esquemas de herencia tradicionales basados en una simple búsqueda en profundidad de izquierda a derecha (*depth-first*), el intérprete podía ascender hasta la clase base superior antes de haber revisado las clases derivadas intermedias de la derecha, generando comportamientos contraintuitivos.



### Resolución

Python aborda y resuelve este problema mediante la combinación de dos mecanismos esenciales:

1. **El algoritmo [MRO (*Method Resolution Order*) de linealización C3](/docs/POO/mro):**  
   Desde Python 2.3, el lenguaje utiliza el algoritmo **C3** para calcular el orden de resolución de métodos (`__mro__`). Este algoritmo aplana la estructura en forma de diamante y la transforma en una secuencia lineal e inequívoca de clases. En un diamante, el MRO garantiza que la clase base común se busque **después** de haber recorrido todas sus subclases derivadas.

2. **Despacho cooperativo mediante `super()`:**  
   En lugar de invocar a las clases padre directamente por su nombre, las subclases utilizan **`super()`**. En herencia múltiple, `super()` no llama necesariamente al padre directo en la definición de la clase, sino que delega la ejecución a la **siguiente clase presente en la secuencia MRO** del objeto.

Gracias al encadenamiento cooperativo con `super()`, la llamada fluye a través de la lista linealizada del MRO, garantizando que **cada clase e inicializador dentro del diamante se ejecute exactamente una vez** y en el orden lógico correcto.


<br />
<Tabs>
<TabItem value="abs1" label="Ejemplo" default>
<div class="alert alert--primary">
**Ejemplo:**

En este se muestra en la primera parte **por qué ocurre el Problema del Diamante** al usar llamadas directas por nombre de clase, y en la segunda parte **cómo lo resuelve Python de forma elegante usando `super()` y el MRO (Method Resolution Order)**.

**Explicación**

1. **En la Parte 1 (El Problema):**  
   Al llamar explícitamente a `B_Problema.__init__()` y `C_Problema.__init__()`, ambos métodos ejecutan de forma independiente `A_Problema.__init__()`. Esto hace que el constructor del ancestro común `A` se ejecute **dos veces**, lo que en un sistema real podría duplicar transacciones, reabrir conexiones o sobreescribir datos.

2. **En la Parte 2 (La Solución):**  
   Al sustituir las llamadas directas por **`super()`**, Python consulta el **MRO (Method Resolution Order)** calculado con el algoritmo C3.  
   El orden de ejecución resultante para la clase `D` es exactamente:  
   ```math
   \text{D} \longrightarrow \text{B} \longrightarrow \text{C} \longrightarrow \text{A} \longrightarrow \text{object}  
   ```
   Gracias a este encadenamiento cooperativo, **`A` se inicializa exactamente una sola vez**, resolviendo el conflicto del diamante por completo.

</div>
</TabItem>
<TabItem value="abs1-python" label="🖥️ Código" >

```python showLineNumbers

# =====================================================================
# PARTE 1: EL PROBLEMA (Llamadas explícitas por nombre de clase)
# Estructura del Diamante:
#       A (Base)
#      / \
#     B   C
#      \ /
#       D
# =====================================================================

print("--- ❌ PARTE 1: EL PROBLEMA DEL DIAMANTE ---")

class A_Problema:
    def __init__(self):
        print("  [A] Inicializando A (Base común)")

class B_Problema(A_Problema):
    def __init__(self):
        print("  [B] Inicializando B")
        A_Problema.__init__(self)  # Llamada explícita al padre

class C_Problema(A_Problema):
    def __init__(self):
        print("  [C] Inicializando C")
        A_Problema.__init__(self)  # Llamada explícita al padre

class D_Problema(B_Problema, C_Problema):
    def __init__(self):
        print("  [D] Inicializando D")
        B_Problema.__init__(self)
        C_Problema.__init__(self)

# Ejecución del problema
objeto_problema = D_Problema()

# Salida obtenida:
# [D] Inicializando D
# [B] Inicializando B
# [A] Inicializando A (Base común)  <-- ¡Primera ejecución de A!
# [C] Inicializando C
# [A] Inicializando A (Base común)  <-- 🚨 ¡SEGUNDA EJECUCIÓN INNECESARIA DE A!


print("\n" + "="*50 + "\n")


# =====================================================================
# PARTE 2: LA SOLUCIÓN (Uso cooperativo de super())
# =====================================================================

print("--- ✅ PARTE 2: LA SOLUCIÓN CON super() Y MRO ---")

class A_Solucion:
    def __init__(self):
        print("  [A] Inicializando A (Base común)")
        super().__init__()

class B_Solucion(A_Solucion):
    def __init__(self):
        print("  [B] Inicializando B")
        super().__init__()  # Delega la llamada al siguiente en el MRO (C)

class C_Solucion(A_Solucion):
    def __init__(self):
        print("  [C] Inicializando C")
        super().__init__()  # Delega la llamada al siguiente en el MRO (A)

class D_Solucion(B_Solucion, C_Solucion):
    def __init__(self):
        print("  [D] Inicializando D")
        super().__init__()  # Inicia la cadena del MRO

# Ejecución de la solución
objeto_solucion = D_Solucion()

print("\n🔍 Orden MRO calculado por Python para D_Solucion:")
for i, clase in enumerate(D_Solucion.__mro__, 1):
    print(f"  {i}. {clase.__name__}")
```
</TabItem>
</Tabs>



