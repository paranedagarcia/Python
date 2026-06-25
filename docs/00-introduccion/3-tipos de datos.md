---
id: datos
title: "Datos y estructuras"
sidebar_label: "Datos y estructuras"
sidebar_position: 5
---

**Codigo:**
- https://colab.research.google.com/drive/1S3lUwphZRBF6mobRPb_fym7AZ2AbNjcB?usp=sharing


```python
print('--- Python Data Types Example ---')

# 1. Numeric Types: int, float, complex
# Integer
int_var = 10
print(f"Integer: {int_var}, Type: {type(int_var)}")
```


```python
# Float
float_var = 10.5
print(f"Float: {float_var}, Type: {type(float_var)}")
```


```python
# Complex (optional, less common for beginners)
complex_var = 1 + 2j
print(f"Complex: {complex_var}, Type: {type(complex_var)}")

print('\n')
```
```python
# 2. Boolean Type: bool
bool_true = True
bool_false = False
print(f"Boolean True: {bool_true}, Type: {type(bool_true)}")
print(f"Boolean False: {bool_false}, Type: {type(bool_false)}")

print('\n')
```

```python
# 3. Sequence Types: str, list, tuple
# String
str_var = "Hello Python!"
print(f"String: '{str_var}', Type: {type(str_var)}")
```
```python
# List (mutable ordered sequence)
list_var = [1, 2, 'three', 4.0]
print(f"List: {list_var}, Type: {type(list_var)}")
```

```python
# Tuple (immutable ordered sequence)
tuple_var = (10, 20, 'thirty')
print(f"Tuple: {tuple_var}, Type: {type(tuple_var)}")

print('\n')
```
```python
# 4. Set Type: set (unordered collection of unique items)
set_var = {1, 2, 3, 2, 1}
print(f"Set: {set_var}, Type: {type(set_var)}")

print('\n')
```
```python
# 5. Mapping Type: dict (unordered collection of key-value pairs)
dict_var = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(f"Dictionary: {dict_var}, Type: {type(dict_var)}")
```

**diferencia principal entre una lista y un conjunto**

La principal diferencia entre una lista y un conjunto en Python se centra en dos aspectos clave:

**Orden:**

- Una lista es una colección ordenada de elementos. Esto significa que los elementos tienen una posición definida y mantienen el orden en que fueron insertados. Puedes acceder a los elementos por su índice (por ejemplo, mi_lista[0]).
- Un conjunto es una colección no ordenada de elementos. Los elementos no tienen una posición definida y su orden puede variar. No puedes acceder a los elementos de un conjunto por un índice.

**Elementos duplicados:**

- Una lista permite elementos duplicados. Puedes tener el mismo valor múltiples veces en una lista (por ejemplo, [1, 2, 2, 3]).
- Un conjunto no permite elementos duplicados. Solo almacena elementos únicos. Si intentas agregar un elemento que ya existe, el conjunto simplemente lo ignora (como se vio en el ejemplo anterior, set_var = {1, 2, 3, 2, 1} resultó en {1, 2, 3}).

Además, tanto las listas como los conjuntos son mutables, lo que significa que puedes añadir o eliminar elementos después de su creación.
