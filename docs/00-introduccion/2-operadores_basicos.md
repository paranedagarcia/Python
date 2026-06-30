---
id: operadores
title: "Operadores básicos"
sidebar_label: "💻 Operadores básicos"
description: "Operaciones básicos"
sidebar_position: 4
---
# Operadores básicos
:::info[Codigo:]
- https://colab.research.google.com/drive/1PBjQ5QWjprbD8ruNbMt2Z_TufHtEViZ7
:::

```python title="Operaciones aritméticas"
print("--- Ejemplos de Operaciones Aritméticas ---")

# Definimos dos números para las operaciones
numero1 = 20
numero2 = 7
```


```python
# Suma
resultado_suma = numero1 + numero2
print(f"Suma de {numero1} y {numero2}: {resultado_suma}") 
```


```python
# Resta
resultado_resta = numero1 - numero2
print(f"Resta de {numero1} y {numero2}: {resultado_resta}") 
```


```python
# Multiplicación
resultado_multiplicacion = numero1 * numero2
print(f"Multiplicación de {numero1} y {numero2}: {resultado_multiplicacion}") 
```


```python
# División (siempre devuelve un flotante)
resultado_division = numero1 / numero2
print(f"División de {numero1} y {numero2}: {resultado_division}") 
```
```python
# División Entera (descarta la parte decimal)
resultado_division_entera = numero1 // numero2
print(f"División Entera de {numero1} y {numero2}: {resultado_division_entera}") 
```
```python
# Módulo (resto de la división)
resultado_modulo = numero1 % numero2
print(f"Módulo de {numero1} y {numero2}: {resultado_modulo}") 
```
```python
# Potencia (numero1 elevado a la potencia de numero2)
resultado_potencia = numero1 ** 2 # 20 elevado a la 2
print(f"Potencia de {numero1} al cuadrado: {resultado_potencia}") 

```
### Jerarquia de operaciones
```python
# Jerarquía PEMDAS
# P: Parentesis
# E: exponenciacion
# M: multiplicacion
# D: division
# A: Adicion
# S: Sustracción
(2 + 3) * (5 + 5)
```
Operaciones Lógicas

```python
print("--- Ejemplos de Operaciones Lógicas ---")

# Variables booleanas para demostración
es_soleado = True
es_fin_de_semana = False
hay_oferta = True
edad = 25

# Operador 'and' (Y lógico)
# Devuelve True si ambas condiciones son True
print(f"¿Es soleado Y es fin de semana? {es_soleado and es_fin_de_semana}") 
```


```python

# Operador 'or' (O lógico)
# Devuelve True si al menos una de las condiciones es True
print(f"¿Es soleado O hay oferta? {es_soleado or hay_oferta}") 

print(f"¿Es fin de semana O hay oferta? {es_fin_de_semana or hay_oferta}") 

```


```python
# Operador 'not' (Negación lógica)
# Invierte el valor booleano (True se vuelve False, False se vuelve True)
print(f"¿NO es soleado? {not es_soleado}") 
print(f"¿NO es fin de semana? {not es_fin_de_semana}") 

```


```python
# Combinación de operadores lógicos y de comparación
# Una persona es apta si tiene más de 18 Y hay oferta
es_apto = (edad > 18) and hay_oferta
print(f"¿Es apto (mayor de 18 y hay oferta)? {es_apto}") 

```


```python

# Una persona puede ir a la playa si es soleado O si hay oferta (para comprar algo)
puede_ir_playa = es_soleado or hay_oferta
print(f"¿Puede ir a la playa (es soleado o hay oferta)? {puede_ir_playa}") 
```


```python
print("--- Combinación de Operaciones Aritméticas y Lógicas en una Función ---")

def analizar_numero(numero):
    # Operación aritmética: duplicar el número
    numero_duplicado = numero * 2
    print(f"  Número original: {numero}")
    print(f"  Número duplicado: {numero_duplicado}")

    # Operaciones lógicas y aritméticas para determinar propiedades
    es_par = (numero % 2 == 0) # Comprueba si el número es par usando el módulo y comparación
    es_mayor_que_diez = (numero > 10) # Comprueba si es mayor que 10 usando comparación
    es_duplicado_interesante = (numero_duplicado > 20) and (not es_par) # Lógica con el duplicado

    # Usamos operaciones lógicas para decidir el mensaje de retorno
    if es_par and es_mayor_que_diez:
        return f"El número {numero} es PAR y MAYOR que 10. Su duplicado es {numero_duplicado}."
    elif not es_par and es_duplicado_interesante:
        return f"El número {numero} es IMPAR y su duplicado ({numero_duplicado}) es INTERESANTE (mayor que 20)."
    elif es_par:
        return f"El número {numero} es PAR pero no mayor que 10. Su duplicado es {numero_duplicado}."
    else: # Si es impar y su duplicado no es interesante
        return f"El número {numero} es IMPAR, y su duplicado ({numero_duplicado}) no es mayor que 20."


# Demostración de la función con varios números
print("\n--- Ejemplos de uso de la función ---")
print(analizar_numero(12)) # Par y mayor que 10
print(analizar_numero(7))  # Impar, duplicado 14 (no > 20)
print(analizar_numero(15)) # Impar, duplicado 30 ( > 20)
print(analizar_numero(6))  # Par y no mayor que 10

```
