---
id: r-controles
title: Control de flujo
sidebar_label: Controles
sidebar_position: 2
---

# Sentencias de control en R

## if, else if, else

Ejecuta código condicionalmente según una expresión lógica.

```r
x <- 10

if (x > 5) {
    print("x es mayor que 5")
} else if (x == 5) {
    print("x es igual a 5")
} else {
    print("x es menor que 5")
}
```

## for

Itera sobre una secuencia de valores.

```r
for (i in 1:5) {
    print(i)
}

# Iterar sobre un vector
frutas <- c("manzana", "plátano", "naranja")
for (fruta in frutas) {
    print(fruta)
}
```

## while

Ejecuta código mientras una condición sea verdadera.

```r
contador <- 1
while (contador <= 5) {
    print(contador)
    contador <- contador + 1
}
```

## repeat

Ejecuta código indefinidamente hasta encontrar `break`.

```r
numero <- 1
repeat {
    print(numero)
    numero <- numero + 1
    if (numero > 5) break
}
```

## break y next

- `break`: Detiene el bucle.
- `next`: Salta a la siguiente iteración.

```r
for (i in 1:10) {
    if (i == 3) next      # Salta cuando i es 3
    if (i == 8) break     # Detiene cuando i es 8
    print(i)
}
```

## ifelse()

Versión vectorizada de `if/else` para operaciones sobre vectores.

```r
numeros <- c(1, 5, 10, 15, 20)
resultado <- ifelse(numeros > 10, "grande", "pequeño")
print(resultado)
```
