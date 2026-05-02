---
sidebar_position: 2
---

# Visualización de Datos

### Histograma

```r
# R
hist(datos, 
     main = "Distribución de los datos",
     xlab = "Valores",
     ylab = "Frecuencia",
     col = "steelblue",
     border = "white")
```

```python
# Python con matplotlib
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.hist(datos, bins=6, color='steelblue', edgecolor='white')
plt.title('Distribución de los datos')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.show()
```

### Diagrama de Caja (Boxplot)

El boxplot muestra visualmente la mediana, cuartiles y valores atípicos:

```r
# R
boxplot(datos,
        main = "Diagrama de Caja",
        ylab = "Valores",
        col = "lightblue")
```

```python
# Python
plt.figure(figsize=(6, 6))
plt.boxplot(datos)
plt.title('Diagrama de Caja')
plt.ylabel('Valores')
plt.show()
```