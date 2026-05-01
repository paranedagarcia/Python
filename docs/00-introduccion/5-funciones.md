---
id: funciones
title: "Funciones"
sidebar_label: "Funciones"
sidebar_position: 5
---

## Espacios de nombres y ámbito

## Devolución de valores

## Funciones como objetos

## Parámetros
### Argumentos

```python
# key.points.argument.passing.py
x = 3
def func(y):
    print(y)
func(x) # prints: 3
```

```python
# key.points.assignment.py
x = 3
def func(x):
    x = 7 # defining a local x, not changing the global one
func(x)
print(x) # prints: 3

```

### Definición de argumentos

#### Parámetros opcionales

```python
# parameters.default.py
def func(a, b=4, c=88):
    print(a, b, c)

func(1) # prints: 1 4 88
func(b=5, a=7, c=9) # prints: 7 5 9
func(42, c=9) # prints: 42 4 9
func(42, 43, 44) # prints: 42, 43, 44
```


#### Posición variable

```python
# parameters.variable.keyword.py
def func(**kwargs):
    print(kwargs)

func(a=1, b=42) # prints {'a': 1, 'b': 42}
func() # prints {}
func(a=1, b=46, c=99) # prints {'a': 1, 'b': 46, 'c': 99}
```

```python

def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
    }
    print(conn_params)
    # we then connect to the db (commented out)
    # db.connect(**conn_params)

connect()
connect(host='127.0.0.42', port=5433)
connect(port=5431, user='fab', pwd='gandalf')
```
#### Posicionales

#### keyword-only

#### Combinación de parametros

```python
def func(a, b, c=7, *args, **kwargs):
    print('a, b, c:', a, b, c)
    print('args:', args)
    print('kwargs:', kwargs)

func(1, 2, 3, 5, 7, 9, A='a', B='b')

```
```raw
a, b, c: 1 2 3
args: (5, 7, 9)
kwargs: {'A': 'a', 'B': 'b'}
```

### Valores de retorno

```python
def func():
    pass

func() # the return of this call won't be collected. It's lost.
a = func() # the return of this one instead is collected into 'a'
print(a) # prints: None
```

```python
def factorial(n):
    if n in (0, 1):
        return 1
    result = n
    for k in range(2, n):
        result *= k
    return result

f5 = factorial(5) # f5 = 120
```

```python
from functools import reduce
from operator import mul

def factorial(n):
    return reduce(mul, range(1, n + 1), 1)

f5 = factorial(5) # f5 = 120
```

#### Valores multiples

```python
def moddiv(a, b):
    return a // b, a % b
    
print(moddiv(20, 7)) # prints (2, 6)
```
## Funciones anónimas (lambda)

## Generadores

## Manejo de errores y excepciones
