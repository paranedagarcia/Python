# Pseudocódigo

Es la forma de escribir pasos lógicos usando un lenguaje sencillo parecido al español para planear un programa antes de escribir código real.

El pseudocódigo es una descripción informal y de alto nivel del algoritmo o de los pasos lógicos que seguirá un programa de ordenador. No está diseñado para ser ejecutado directamente por una máquina, sino para ser leído y comprendido por seres humanos.

### **Palabras reservadas**

Son términos con un significado predefinido que estructuran el algoritmo. Aunque no existe un estándar universal, las palabras reservadas más habituales en pseudocódigo en español son:

| Categoría | Palabras reservadas | Función |
| :---- | :---- | :---- |
| Inicio/Fin | INICIO, FIN | Delimitan el cuerpo principal del algoritmo. |
| Selección | SI, ENTONCES, SI NO, FIN SI | Estructuras condicionales (toma de decisiones). |
| Iteración | MIENTRAS, HACER, FIN MIENTRAS, PARA, FIN PARA | Estructuras repetitivas (bucles). |
| Entrada/Salida | LEER, ESCRIBIR | Interacción con el usuario (input/output). |
| Lógica | Y, O, NO | Operadores lógicos para combinar condiciones. |

### **Identificadores**

Los identificadores son los nombres que el programador asigna a las variables, constantes y subprogramas. En pseudocódigo se recomienda usar nombres descriptivos que indiquen claramente su propósito. Por ejemplo, `edad_alumno` es preferible a `x`, y `suma_total` es más claro que `st`.

### **Comentarios**

Los comentarios son anotaciones que el programador incluye para explicar partes del algoritmo. No forman parte de la lógica ejecutable y se escriben habitualmente precedidos de `//` o encerrados entre `/* */`. Su uso es fundamental para hacer el pseudocódigo comprensible a terceros.

### **Tipos de datos básicos**

Aunque el pseudocódigo es flexible, los tipos de datos que se manejan habitualmente son los mismos que encontramos en la mayoría de lenguajes de programación:

| Tipo | Descripción | Ejemplos | Equivalente en Java |
| :---- | :---- | :---- | :---- |
| **ENTERO** | Números sin decimales | 0, \-5, 42, 1000 | int, long |
| **REAL** | Números con decimales | 3.14, \-0.5, 99.99 | float, double |
| **CADENA** | Secuencias de caracteres | "Hola", "Java", "123" | String |
| **CARÁCTER** | Un solo carácter | 'A', 'z', '9' | char |
| **LÓGICO** | Verdadero o falso | VERDADERO, FALSO | boolean |

### **Asignación de valores**

La operación de asignación almacena un valor en una variable. En pseudocódigo se usa el símbolo `←` (flecha hacia la izquierda) para distinguir la asignación de la comparación de igualdad. Esto es una convención muy extendida que evita la confusión entre `=` (asignación) y `==` (comparación) que existe en lenguajes como Java o C:

## **Operadores en pseudocódigo**

Los operadores son símbolos que permiten realizar operaciones sobre los datos. En pseudocódigo se utilizan los mismos tipos de operadores que en los lenguajes de programación, con una notación que prioriza la legibilidad.

### **Operadores aritméticos**

| Operador | Significado | Ejemplo | Resultado |
| :---- | :---- | :---- | :---- |
| \+ | Suma | 7 \+ 3 | 10 |
| \- | Resta | 7 \- 3 | 4 |
| \* | Multiplicación | 7 \* 3 | 21 |
| / | División | 7 / 2 | 3.5 |
| MOD | Módulo (resto) | 7 MOD 3 | 1 |
| ^ | Potencia | 2 ^ 3 | 8 |

### **Operadores relacionales (de comparación)**

| Operador | Significado | Ejemplo | Resultado |
| :---- | :---- | :---- | :---- |
| \= | Igual a | 5 \= 5 | VERDADERO |
| ≠ o \<\> | Distinto de | 5 ≠ 3 | VERDADERO |
| \< | Menor que | 3 \< 5 | VERDADERO |
| \> | Mayor que | 5 \> 3 | VERDADERO |
| \<= | Menor o igual | 5 \<= 5 | VERDADERO |
| \>= | Mayor o igual | 6 \>= 5 | VERDADERO |

### **Operadores lógicos**

| Operador | Significado | Ejemplo | Resultado |
| :---- | :---- | :---- | :---- |
| Y (AND) | Ambas condiciones verdaderas | (5 \> 3\) Y (2 \< 4\) | VERDADERO |
| O (OR) | Al menos una condición verdadera | (5 \> 3\) O (2 \> 4\) | VERDADERO |
| NO (NOT) | Invierte el valor lógico |  |  |


---
## **Secuencias de Control**


### **Secuencia**
```text  
INICIO  
    LEER radio  
    area ← 3.14159 * radio ^ 2  
    ESCRIBIR "Área: ", area  
FIN
```

### **Selectiva simple**
```text
SI edad >= 18 ENTONCES  
    ESCRIBIR "Es mayor de edad"  
FIN SI
```

### **Selectiva doble**
```text
SI nota >= 5 ENTONCES  
  ESCRIBIR "Aprobado"  
SI NO  
  ESCRIBIR "Suspenso"  
FIN SI
```
#### **Selección múltiple**
```text  
SEGÚN dia_semana HACER  
    1: ESCRIBIR "Lunes"  
    2: ESCRIBIR "Martes"  
    3: ESCRIBIR "Miércoles"  
    6, 7: ESCRIBIR "Fin de semana"  
    DE OTRO MODO: ESCRIBIR "Día no válido"  
FIN SEGÚN
```
#### **Bucle mientras**
```text  
contador ← 1  
MIENTRAS contador <= 10 HACER  
  contador ← contador + 1  
FIN MIENTRAS
```
#### **Bucle repetir-hasta**  
```text
REPETIR  
    ESCRIBIR "Introduce un número positivo: "  
    LEER numero  
HASTA QUE numero > 0
```
#### **Bucle para**
```text
PARA i ← 1 HASTA 10 HACER  
    resultado ← 7 * i  
    ESCRIBIR "7 x ", i, " = ", resultado  
FIN PARA
```

#### Sumar dos números (Estructura secuencial)


```python
Proceso SumarNumeros
    Definir num1, num2, suma Como Entero
    Escribir "Ingresa el primer número:"
    Leer num1
    Escribir "Ingresa el segundo número:"
    Leer num2
    suma <- num1 + num2
    Escribir "La suma es: ", suma
FinProceso
```

#### Determinar mayoria de edad


```python
Proceso VerificarEdad
    Definir edad Como Entero
    Escribir "Ingresa tu edad:"
    Leer edad
    Si edad >= 18 Entonces
        Escribir "Eres mayor de edad."
    Sino
        Escribir "Eres menor de edad."
    FinSi
FinProceso

```

## Desafíos

**Ejercicio 0:** Algoritmo del mayor de tres números

Escribe un algoritmo en pseudocódigo que lea tres números enteros y determine cuál de los tres es el mayor. Debe funcionar correctamente incluso si dos o los tres números son iguales.

**Ejercicio 1:** escribe una funcion "saludo" que salude por nombre.


## Trabajo en equipo:
### Lógica y Pseudocódigo

1. **Calculadora de Descuentos (Estructura Secuencial y Condicional Simple)**  
   Escribe un algoritmo en pseudocódigo que pida al usuario el precio original de un producto. Si el precio es mayor a **\$100**, aplica un descuento del **15%** y muestra el precio final a pagar. Si es menor o igual a **\$100**, muestra el precio original informando que no aplica descuento.

2. **Verificación de Número Par o Impar (Operador Módulo y Condicional)**  
   Diseña un programa en pseudocódigo que solicite un número entero al usuario e informe mediante un mensaje en pantalla si el número ingresado es **par** o **impar**.

3. **Promedio de Calificaciones (Secuencia y Condicional Doble)**  
   Crea un pseudocódigo que lea las notas de tres exámenes de un estudiante. Calcula el promedio aritmético y muestra el mensaje **"Aprobado"** si el promedio es igual o superior a **6.0**, o **"Reprobado"** en caso contrario.

4. **Clasificación de Temperatura (Condicionales Anidados / Múltiples)**  
   Diseña un pseudocódigo que reciba una temperatura en grados Celsius y muestre un mensaje según los siguientes rangos:
   * Menor a 10 °C: **"Frío"**
   * Entre 10 °C y 25 °C (inclusive): **"Templado"**
   * Mayor a 25 °C: **"Cálido"**

5. **Contador de Números Pares (Bucle Definido / `Para`)**  
   Escribe un algoritmo en pseudocódigo que genere e imprima en pantalla todos los números pares comprendidos entre el **2 y el 20** utilizando una estructura de repetición.

6. **Tabla de Multiplicar (Bucle e Interacción)**  
   Escribe un programa en pseudocódigo que pida al usuario un número entero del 1 al 10 y muestre su **tabla de multiplicar completa** (desde multiplicar por 1 hasta multiplicar por 10).

7. **Suma Acumulada hasta Cero (Bucle Indefinido / `Mientras`)**  
   Crea un algoritmo que pida números al usuario de forma continua y los vaya sumando. El programa debe detenerse y mostrar el resultado total de la suma acumulada únicamente cuando el usuario ingrese el número **`0`**.



