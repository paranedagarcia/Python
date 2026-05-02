---
id: muestra
title: Población y Muestra
sidebar_label: Población y muestra
sidebar_position: 4
---

En el marco de la informática médica y la investigación biomédica, la capacidad de generalizar hallazgos desde un grupo reducido hacia una colectividad es fundamental. Este proceso se sustenta en la relación lógica entre población y muestra, mediada por técnicas de muestreo que garantizan la validez de la inferencia estadística.

## 1. Población y Muestra: El Fundamento de la Inferencia
La **Población** (o universo) se define como el conjunto total de elementos o unidades de análisis que comparten características comunes y que constituyen el objeto de interés en un estudio. En medicina, estas poblaciones pueden ser **finitas**, como los pacientes ingresados en una unidad de cuidados intensivos en un día determinado, o **infinitas/conceptuales**, como todos los pacientes futuros que podrían padecer una patología específica bajo ciertas condiciones experimentales.

La **Muestra** es un subconjunto representativo de la población, extraído con el fin de investigar características de la totalidad sin necesidad de realizar un censo, lo cual sería logística y económicamente inviable. La relación crítica radica en que los **parámetros** (medidas descriptivas de la población, como la media $\mu$) son estimados a través de los **estadísticos** (medidas calculadas en la muestra, como la media $\overline{x}$).

## 2. Técnicas de Muestreo Poblacional
El muestreo es el procedimiento científico que asegura que la muestra sea un reflejo fiel de la variabilidad biológica de la población objetivo. Se dividen principalmente en probabilísticos y no probabilísticos, siendo los primeros los únicos que permiten cuantificar el error aleatorio y realizar inferencias válidas.

## A. Muestreo Aleatorio Simple (MAS)
Es la técnica base donde cada elemento de la población tiene exactamente la misma probabilidad de ser incluido en la muestra. Se requiere de un **marco muestral** (lista exhaustiva de la población) y la selección se realiza mediante generadores de números aleatorios o sorteos. 

Garantiza la independencia de las observaciones.

El **Muestreo Aleatorio Simple (MAS)** representa el diseño experimental base de la inferencia estadística, definiéndose como el procedimiento donde una muestra de tamaño $n$ se selecciona de una población de tamaño $N$ de tal manera que cada subconjunto posible de $n$ elementos tenga exactamente la misma probabilidad de ser elegido. En el rigor de la informática médica, este método garantiza que cada unidad experimental (paciente, registro clínico o muestra biológica) posea una probabilidad de inclusión conocida e idéntica, eliminando sesgos de selección sistemáticos.

### Fundamentación

El MAS se sustenta en la construcción de un **marco muestral** (*sampling frame*), que consiste en la lista exhaustiva y numerada de todos los elementos que componen la población objetivo. Matemáticamente, si extraemos una muestra aleatoria de una variable $X$ con media poblacional $\mu$ y varianza $\sigma^2$, los estimadores fundamentales operan bajo los siguientes principios:

1.  **Media Muestral ($\bar{X}$):** Es un estimador insesgado de $\mu$, calculado como:
    ```math
    \bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i
    ```
2.  **Varianza de la Media:** En poblaciones infinitas o con reemplazo, la varianza del estimador es:
    ```math
    V(\bar{X}) = \frac{\sigma^2}{n}
    ```
3.  **Factor de Corrección para Población Finita (FPC):** Cuando el muestreo es sin reemplazo y la fracción de muestreo ($n/N$) es significativa (generalmente $> 5\%$), se debe ajustar el error estándar mediante:
    ```math
    \sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}} \cdot \sqrt{\frac{N-n}{N-1}}
    ```

El uso del FPC es crítico en estudios de salud de comunidades pequeñas, ya que reduce la varianza estimada al reconocer que se ha capturado una proporción importante de la información total de la población.

### Aplicación Rigurosa en el Ámbito de la Salud

En la práctica clínica y epidemiológica, el MAS se aplica en escenarios diversos:
*   **Auditoría de Calidad en Informática Médica:** Selección de 5 expedientes clínicos electrónicos de una base de datos de 1.000 para verificar la integridad de los datos codificados.

*   **Ensayos Clínicos Controlados:** Asignación aleatoria de 50 especímenes de laboratorio o sujetos a grupos de tratamiento y control para garantizar la comparabilidad basal.

*   **Estudios de Prevalencia:** Selección de una muestra de ciudadanos para estimar la tasa de vacunación o la incidencia de enfermedades raras como la poliomielitis.

### Implementación en el Entorno R

El lenguaje R ofrece herramientas robustas para la ejecución del MAS, permitiendo la reproducibilidad científica mediante la fijación de la semilla del generador de números pseudoaleatorios.

### Ejemplo 1: Selección de una muestra desde un marco muestral
Para seleccionar 10 pacientes aleatorios de un listado de 355 registrados en un sistema hospitalario:
```r
set.seed(123) # Garantiza reproducibilidad
poblacion_id <- 1:355 # Marco muestral numerado
muestra <- sample(poblacion_id, size = 10, replace = FALSE) # MAS sin reemplazo
print(muestra)
```

### Ejemplo 2: Generación de datos sintéticos y cálculo de probabilidad
Simulación de la distribución del peso al nacer en una población normal para evaluar la media muestral:
```r
# Generación de una población hipotética de pesos (n=1000, media=3100g, sd=500g)
poblacion_pesos <- rnorm(1000, mean = 3100, sd = 500)

# Extracción de una MAS de 50 pesos
muestra_pesos <- sample(poblacion_pesos, size = 50)

# Cálculo de la media y error típico
media_obs <- mean(muestra_pesos)
error_tipico <- sd(muestra_pesos) / sqrt(50)
```

#### Diferenciación Conceptual Importante
Es imperativo distinguir entre el muestreo **con reemplazo** y **sin reemplazo**. El muestreo con reemplazo se modela mediante una distribución binomial, permitiendo que un mismo individuo sea seleccionado múltiples veces; sin embargo, en biomedicina es estándar el muestreo sin reemplazo (hipergeométrico), ya que carece de sentido clínico evaluar el mismo sujeto dos veces como si fueran entidades independientes.

***


## B. Muestreo Aleatorio Estratificado
Se utiliza cuando la población es heterogénea y puede dividirse en subgrupos homogéneos llamados **estratos** (como edad, sexo o nivel socioeconómico). Se toma una muestra aleatoria simple dentro de cada estrato para asegurar que todos los subgrupos estén representados. 
*   **Significado:** Reduce el error de muestreo al controlar la variabilidad interna de los grupos.
*   **Fórmula de asignación proporcional:** 
    ```math
    n_h = n \cdot \left(\frac{N_h}{N}\right)
    ```
    Donde $n_h$ es el tamaño de la muestra en el estrato, $n$ el tamaño de la muestra total, $N_h$ el tamaño del estrato en la población y $N$ el total de la población.

El **Muestreo Aleatorio Estratificado (MAE)** es un diseño de muestreo probabilístico complejo que busca optimizar la precisión de los estimadores y garantizar la representación de subgrupos específicos dentro de una población heterogénea. En el contexto de la informática médica y la investigación clínica, este método es superior al muestreo aleatorio simple (MAS) cuando se identifican variables (estratos) que influyen significativamente en la variable de respuesta, permitiendo reducir la varianza del error de estimación.

### 1. Fundamentación

El MAE consiste en dividir la población total de tamaño $N$ en $L$ subpoblaciones o **estratos** mutuamente excluyentes y colectivamente exhaustivos, de tamaños $N_1, N_2, \dots, N_L$, de tal manera que $\sum_{h=1}^{L} N_h = N$. Una vez definidos, se extrae una muestra aleatoria simple (MAS) de tamaño $n_h$ de cada estrato de forma independiente.

### Componentes del Estimador Estratificado
Para estimar la media poblacional estratificada ($\bar{x}_{st}$), se utiliza una media ponderada de las medias muestrales de cada estrato ($\bar{x}_h$):

```math
\bar{x}_{st} = \sum_{h=1}^{L} W_h \bar{x}_h = \frac{1}{N} \sum_{h=1}^{L} N_h \bar{x}_h
```

Donde:
*   **$W_h = \frac{N_h}{N}$**: Representa el peso relativo del estrato $h$ en la población total.
*   **$\bar{x}_h$**: Es la media calculada en la muestra del estrato $h$.

### Tipos de Afijación (Distribución de la Muestra)
La determinación del tamaño de muestra por estrato ($n_h$) puede seguir tres criterios principales:
1.  **Afijación Igual:** Se asigna el mismo número de unidades a cada estrato ($n_h = n/L$), útil si los estratos son de tamaños similares.

2.  **Afijación Proporcional:** El tamaño $n_h$ es proporcional al peso del estrato en la población ($n_h = n \cdot W_h$). Es el método más común pues mantiene la estructura poblacional en la muestra.

3.  **Afijación Óptima (Neyman):** Considera tanto el tamaño del estrato como su variabilidad interna ($\sigma_h$). Se asigna una muestra mayor a estratos más grandes o con mayor dispersión.

### 2. Importancia en el Ámbito de la Salud

En medicina, la estratificación es crítica para controlar **variables confusoras**. Por ejemplo, en un estudio sobre la eficacia de un nuevo fármaco antihipertensivo, la "edad" o el "sexo" pueden ser factores que modifiquen el efecto. Si se utilizara un MAS, se correría el riesgo de que, por azar, un grupo de tratamiento tuviera significativamente más adultos mayores que el grupo control, sesgando los resultados. El MAE asegura que cada grupo etario esté representado proporcionalmente, aumentando la **validez interna** del estudio.

### 3. Ejemplo e Implementación en R

**Escenario Clínico:** Se desea estudiar el nivel promedio de hemoglobina en una población hospitalaria de 1,000 pacientes, estratificada por "Severidad de la Enfermedad" (Leve, Moderada, Grave), dado que se sabe que la variabilidad biológica es distinta en cada grupo.

*   $N_{Leve} = 500$
*   $N_{Mod} = 300$
*   $N_{Grave} = 200$
*   Tamaño de muestra total deseado: $n = 100$.

### Código en R (Afijación Proporcional):
```r
# Definición de la población (Marco Muestral)
set.seed(42) # Reproducibilidad
poblacion <- data.frame(
  id = 1:1000,
  estrato = c(rep("Leve", 500), rep("Moderado", 300), rep("Grave", 200)),
  hemoglobina = c(rnorm(500, 14, 1), rnorm(300, 12, 1.5), rnorm(200, 10, 2))
)

# Cálculo de tamaños de muestra por estrato (Afijación Proporcional)
n_total <- 100
N <- nrow(poblacion)
pesos <- table(poblacion$estrato) / N
nh <- round(n_total * pesos)

# Extracción de la muestra estratificada usando split y lapply
estratos_lista <- split(poblacion, poblacion$estrato)
muestra_lista <- lapply(names(estratos_lista), function(nombre) {
  df_estrato <- estratos_lista[[nombre]]
  tamano <- nh[nombre]
  df_estrato[sample(1:nrow(df_estrato), tamano), ] # MAS dentro de cada estrato
})

muestra_estratificada <- do.call(rbind, muestra_lista)

# Estimación de la media estratificada
media_st <- sum(pesos * sapply(split(muestra_estratificada$hemoglobina, 
                                     muestra_estratificada$estrato), mean))
print(media_st)
```

### 4. Ventajas Metodológicas
*   **Reducción del Error Estándar:** Si los estratos son internamente homogéneos, el error típico de la media estratificada será menor que el de una media obtenida por MAS.

*   **Garantía de Análisis de Subgrupos:** Permite obtener conclusiones válidas para cada estrato por separado, lo cual es vital en epidemiología para identificar grupos de riesgo.

*   **Eficiencia en Costos:** En poblaciones muy dispersas, estratificar geográficamente puede reducir los gastos de recolección de datos.

***


## C. Muestreo Sistemático
Consiste en seleccionar elementos de una lista ordenada a intervalos regulares. Se elige un punto de arranque aleatorio entre el primer elemento y el valor del intervalo $k$.
*   **Intervalo de muestreo ($k$):** 
    $$k = \frac{N}{n}$$
*   **Relación:** Es más eficiente que el MAS cuando la lista está ordenada de forma que no existan periodicidades ocultas que sesguen la muestra.
*   **Ejemplo:** Seleccionar cada 10º paciente que ingresa a urgencias, empezando por un número al azar entre 1 y 10.

El **Muestreo Sistemático** es un procedimiento de selección probabilística que se fundamenta en la extracción de elementos de una población organizada en una lista o secuencia, mediante la aplicación de un intervalo constante tras un arranque aleatorio inicial. En la informática médica y la investigación clínica, se valora por su eficiencia operativa y por garantizar una distribución uniforme de la muestra a lo largo del marco muestral, lo que en poblaciones con tendencias ordenadas puede aumentar la precisión de los estimadores.

### 1. Fundamentación

El rigor del muestreo sistemático reside en la determinación precisa de dos componentes críticos: el intervalo de muestreo ($k$) y el punto de arranque aleatorio ($A$).

#### Cálculo del Intervalo ($k$)
Representa la distancia fija entre cada unidad seleccionada. Se define matemáticamente como la razón entre el tamaño de la población ($N$) y el tamaño de la muestra deseado ($n$):
$$k = \frac{N}{n}$$
Si el cociente no es un número entero, se suele redondear al entero más cercano o superior para asegurar la cobertura.

#### El Punto de Arranque ($A$)
Para mantener el carácter probabilístico, el primer elemento debe seleccionarse mediante un proceso aleatorio simple entre la primera y la $k$-ésima unidad del listado:
$$1 \le A \le k$$

#### Secuencia de Selección
Una vez definidos $A$ y $k$, los elementos que conformarán la muestra son aquellos que ocupan las posiciones:
$$\{e_A, e_{A+k}, e_{A+2k}, \dots, e_{A+(n-1)k}\}$$

### 2. Variación: Muestreo Sistemático Circular
Cuando el intervalo $k$ no es exacto, existe el riesgo de que los últimos elementos de la lista tengan una probabilidad nula de ser elegidos, introduciendo un sesgo de selección. Para mitigar esto, se utiliza el **muestreo circular**, donde se considera que el elemento $N+1$ coincide con el primero, permitiendo recorrer la lista completamente partiendo de cualquier número aleatorio entre $1$ y $N$.

### 3. Aplicación y Ejemplos en el Ámbito de la Salud

Este método es esencial en escenarios donde los pacientes o registros fluyen de manera secuencial o están organizados jerárquicamente:

*   **Auditoría de Calidad Hospitalaria:** Si un hospital atiende a 1,200 pacientes al mes y se desea auditar 120 historias clínicas electrónicas ($k=10$), se selecciona un número al azar entre 1 y 10 (p. ej., el 4) y se analizan las fichas 4, 14, 24, etc..

*   **Ensayos Clínicos en Emergencias:** Selección de pacientes que ingresan a una unidad de cuidados críticos. Al no existir un marco muestral previo, se puede preestablecer estudiar a cada $k$-ésimo paciente que ingrese durante una semana.

*   **Control de Procesos de Laboratorio:** Extracción de una muestra de suero cada 15 tubos procesados por un analizador automático para verificar la calibración.

### 4. Implementación en R

El entorno R permite ejecutar el muestreo sistemático de forma robusta. A continuación, se presenta un script para seleccionar una muestra de pacientes en una base de datos hospitalaria.

```R
# Simulación de un marco muestral de 1000 pacientes
# con una variable de interés (ej. Presión Arterial Sistólica)
set.seed(2024)
hospital_data <- data.frame(
  id = 1:1000,
  pas = rnorm(1000, mean = 125, sd = 15)
)

# Parámetros del muestreo
N <- nrow(hospital_data)
n <- 50
k <- floor(N / n) # Intervalo de muestreo

# 1. Selección del Punto de Arranque Aleatorio (A)
punto_arranque <- sample(1:k, 1)

# 2. Generación de los índices sistemáticos
indices_sistematicos <- seq(from = punto_arranque, 
                            by = k, 
                            length.out = n)

# 3. Extracción de la muestra
muestra_sistematica <- hospital_data[indices_sistematicos, ]

# Estimación de la media muestral y error típico
media_muestral <- mean(muestra_sistematica$pas)
error_estandar <- sd(muestra_sistematica$pas) / sqrt(n)

cat("Punto de arranque:", punto_arranque, "\n")
cat("Media estimada:", media_muestral, "\n")
```

### 5. Consideración Crítica: El Peligro de la Periodicidad
La mayor amenaza a la validez del muestreo sistemático es la **periodicidad oculta**. Si la población presenta un ciclo biológico o administrativo que coincide exactamente con el intervalo $k$, la muestra dejaría de ser representativa.
*   **Ejemplo:** Si se estudia la ocupación de camas cada 7 días ($k=7$) y la mayoría de los ingresos programados ocurren los lunes, la muestra podría sobreestimar sistemáticamente la saturación del servicio.


***

## D. Muestreo por Conglomerados
A diferencia de la estratificación (donde se busca homogeneidad interna), el muestreo por conglomerados divide la población en grupos naturales que se supone son tan heterogéneos como la población misma (p. ej., hospitales, escuelas o manzanas de una ciudad). Se seleccionan aleatoriamente algunos conglomerados y se estudian todos los individuos dentro de ellos (una etapa) o una muestra de ellos (dos etapas).

:::note
Es una técnica costo-efectiva útil cuando no existe un marco muestral de individuos, pero sí de grupos geográficos o administrativos.
:::

El **Muestreo por Conglomerados** (o por racimos) es una técnica de muestreo probabilístico en la que la unidad de selección no es el individuo, sino un grupo de individuos que forman una unidad natural o administrativa, denominada **conglomerado**. En el ámbito de la salud y la informática médica, esta técnica es esencial cuando no se dispone de un listado exhaustivo de todos los pacientes (marco muestral individual), pero sí existe un registro de las instituciones o áreas donde se agrupan.

### 1. Fundamentación

A diferencia del muestreo estratificado, donde se busca homogeneidad interna y heterogeneidad entre estratos, el muestreo por conglomerados asume que cada grupo es una **"micro-población"** que representa fielmente la diversidad de la población total. Por lo tanto, se busca que exista **heterogeneidad interna** (máxima variabilidad dentro del grupo) y **homogeneidad externa** (que los conglomerados sean similares entre sí).

#### Unidades Primarias y Secundarias
*   **Unidades Primarias de Muestreo (UPM):** Son los conglomerados seleccionados en la primera etapa (ej. hospitales, centros de salud, manzanas geográficas).
*   **Unidades Secundarias de Muestreo (USM):** Son los elementos individuales dentro de los conglomerados (ej. pacientes, expedientes clínicos).

### 2. Clasificación por Etapas

*   **Muestreo Monoetápico (una etapa):** Se seleccionan aleatoriamente los conglomerados y se estudian **todos** los individuos dentro de ellos.
*   **Muestreo Bietápico (dos etapas):** Primero se seleccionan los conglomerados (UPM) y, dentro de cada uno de ellos, se selecciona una muestra aleatoria de individuos (USM).
*   **Muestreo Multietápico:** Se añaden niveles jerárquicos (ej. Región -> Ciudad -> Hospital -> Paciente).

### 3. Estimación Matemática de la Media

En un diseño de conglomerados, si se desea estimar la media de una variable de salud (ej. niveles de glucosa), el estimador de la media por unidad ($\overline{x}_{clu}$) se calcula como la razón entre la suma total de los valores observados y el total de individuos muestreados:

```math
\overline{x}_{clu} = \frac{\sum_{i=1}^{n} \sum_{j=1}^{m_i} x_{ij}}{\sum_{i=1}^{n} m_i}
```

Donde:
*   $n$: Número de conglomerados seleccionados.
*   $m_i$: Número de individuos en el conglomerado $i$.
*   $x_{ij}$: Valor de la variable para el individuo $j$ en el conglomerado $i$.

:::note
**Nota sobre el Error:** El error de muestreo suele ser mayor que en el muestreo aleatorio simple (MAS) si existe correlación intraclase (ej. pacientes en un mismo hospital tienden a recibir tratamientos similares), por lo que a veces se requiere aumentar el tamaño de la muestra para compensar este "efecto de diseño".
:::

### 4. Ejemplo Práctico e Implementación en R

**Escenario Clínico:** Se desea evaluar la calidad de la atención (escala 0-100) en los centros de atención primaria de una provincia. No hay un listado nacional de pacientes, pero sí de los 50 centros de salud (conglomerados). Se decide realizar un muestreo bietápico: seleccionar 5 centros y, dentro de cada uno, auditar 10 historias clínicas.

#### Código en R (Uso de `sample` y lógica jerárquica):
El lenguaje R permite gestionar estas estructuras mediante la selección de niveles jerárquicos.

```r
# 1. Simulación del Marco Muestral (50 centros con n pacientes cada uno)
set.seed(123)
poblacion_centros <- data.frame(
  centro_id = rep(1:50, each = 100),
  calidad_atencion = rnorm(5000, mean = 75, sd = 10)
)

# 2. Etapa 1: Selección Aleatoria de Conglomerados (UPM)
n_clusters <- 5
clusters_seleccionados <- sample(unique(poblacion_centros$centro_id), size = n_clusters)

# 3. Etapa 2: Selección Aleatoria de Individuos dentro de los clusters (USM)
# Filtramos la población por los centros seleccionados
muestra_upm <- poblacion_centros[poblacion_centros$centro_id %in% clusters_seleccionados, ]

# Seleccionamos 10 pacientes por cada centro usando split y lapply
muestra_final_lista <- lapply(split(muestra_upm, muestra_upm$centro_id), function(df_centro) {
  df_centro[sample(1:nrow(df_centro), 10), ]
})

muestra_final <- do.call(rbind, muestra_final_lista)

# 4. Cálculo del Estimador de la Media de Conglomerados
media_est <- mean(muestra_final$calidad_atencion)
print(paste("Estimación de la calidad media:", round(media_est, 2)))
```

### 5. Ventajas en Informática Médica
*   **Eficiencia de Costos:** Reduce drásticamente los desplazamientos de los investigadores al concentrar la recolección en puntos específicos.

*   **Viabilidad Logística:** Es la única opción cuando los pacientes están dispersos geográficamente y no existe una base de datos centralizada.

*   **Análisis Multinivel:** Permite capturar variaciones debidas a la gestión institucional (efecto hospital) frente a la variación individual del paciente.





### Resumen de los tipos muestrales
| Técnica | Unidad | Objetivo Principal | Relación con la Población |
| :--- | :--- | :--- | :--- |
| **MAS** | Individuo | Simplicidad y equiprobabilidad | Representación directa. |
| **Estratificado** | Estrato | Representatividad de subgrupos | Control de varianza interna. |
| **Sistemático** | Intervalo $k$ | Facilidad operativa | Distribución uniforme en la lista. |
| **Conglomerados** | Grupo natural | Eficiencia en recursos | Útil ante dispersión geográfica. |

