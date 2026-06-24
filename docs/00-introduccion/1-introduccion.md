---
id: introduccion
title: "Fundamentos de Python"
sidebar_label: "Fundamentos"
sidebar_position: 1
description: "Fundamentos del lenguaje"
---


Python es un lenguaje de programación de **muy alto nivel, multiparadigma y de propósito general**, creado por Guido van Rossum a principios de los años 90. Se distingue por una **sintaxis limpia, clara y sencilla** que favorece la legibilidad, haciendo que sus programas a menudo parezcan "pseudocódigo ejecutable".

A continuación se describen sus características principales y cómo se diferencia de otros lenguajes populares:

### 1. Sintaxis y Estructura del Código
*   **Indentación obligatoria:** A diferencia de lenguajes como **Java, C# o C++**, que utilizan llaves `{}` para delimitar bloques de código, Python utiliza el **espacio en blanco (sangrado)** para estructurar el programa. Esto obliga a los programadores a escribir código con un formato visual claro.
*   **Concisión:** Un programa en Python suele tener entre **un tercio y un quinto del tamaño** de su equivalente en Java o C++, lo que aumenta significativamente la productividad del desarrollador.
*   **Simplicidad:** Python evita la verbosidad de otros lenguajes; por ejemplo, no requiere terminar las sentencias con punto y coma (aunque lo permite para separar varias en una línea).

### 2. Tipado y Manejo de Datos
*   **Tipado dinámico y fuerte:** En Python no es necesario declarar el tipo de una variable antes de usarla (dinámico), pero no se permiten conversiones implícitas incompatibles, como sumar un número a una cadena de texto (fuerte). Lenguajes como **Perl o C++** permiten un tipado más débil en ciertas operaciones, mientras que **Java y C#** emplean tipado estático, donde el tipo debe conocerse al escribir el programa.
*   **Nombres vs. Variables:** A diferencia de **C**, donde una variable es una ubicación de memoria con un tipo fijo, en Python los nombres son simplemente **etiquetas que se vinculan a objetos** en memoria.
*   **Duck Typing:** Python sigue la filosofía de que "si camina como un pato y grazna como un pato, entonces es un pato". Esto significa que lo importante es **qué puede hacer un objeto** (sus métodos y atributos) y no qué tipo de objeto es estrictamente.

### 3. Ejecución y Rendimiento
*   **Lenguaje interpretado:** Python utiliza un intérprete que traduce el código fuente a un formato intermedio llamado **bytecode**, el cual se ejecuta en una máquina virtual. Esto lo hace más portátil que lenguajes compilados como **C o C++**, pero también generalmente **más lento** en ejecución pura.
*   **Gestión de memoria:** Python cuenta con administración automática de memoria mediante un **recolector de basura** y conteo de referencias, liberando al programador de la gestión manual necesaria en lenguajes como C.

### 4. Paradigmas y Filosofía
*   **Multiparadigma:** Mientras que lenguajes como **Java o C#** fuerzan un estilo orientado a objetos, Python permite programar de forma estructurada, funcional o procedimental según la necesidad.
*   **Filosofía "Zen":** Python se rige por principios como "lo bello es mejor que lo feo" y "debería haber una, y preferiblemente solo una, manera obvia de hacerlo".
*   **Baterías incluidas:** Python posee una **biblioteca estándar sumamente extensa**, lo que significa que muchas tareas complejas pueden realizarse sin instalar paquetes externos, a diferencia de otros lenguajes con bibliotecas base más limitadas.

### 5. Comparación en Ámbitos Específicos
*   **Ciencia de datos:** Comparado con lenguajes especializados como **R, Matlab o SAS**, Python es una herramienta más generalista que permite integrar la investigación y los prototipos directamente en sistemas de producción robustos.
*   **Desarrollo Web:** Python destaca por frameworks populares como **Django y Flask**, compitiendo con **Ruby (Rails)** o **Javascript (Node.js)** por su facilidad para construir aplicaciones web interactivas.


Tipado dinamico

En los proyectos de ciencia de datos, el **tipado dinámico** de Python ofrece una serie de ventajas estratégicas que facilitan el manejo de la incertidumbre y la rapidez necesarias en la investigación científica. A continuación, se detallan los beneficios principales según las fuentes:

### 1. Flexibilidad y reducción de la carga mental
El tipado dinámico significa que no es necesario declarar el tipo de dato de una variable antes de usarla; el tipo se determina automáticamente en tiempo de ejecución. Esto permite a los científicos de datos:
*   **Usar nombres con poco esfuerzo mental:** El programador puede enfocarse en la lógica del problema en lugar de en la gestión técnica de las variables.
*   **Reutilizar nombres de variables:** Un mismo nombre puede referenciar distintos tipos de objetos (como una función y luego un número) a lo largo del programa, lo que en contextos específicos hace que el código sea más fácil de leer y entender al usar términos conceptuales coherentes.

### 2. Agilidad en el prototipado y la exploración
La naturaleza dinámica de Python es fundamental para el flujo de trabajo experimental de la ciencia de datos:
*   **Ciclo de "ejecución-exploración" rápido:** No se requieren pasos de compilación o vinculación, lo que permite ver los resultados del trabajo de manera inmediata.
*   **Inspección paso a paso:** En entornos como **Jupyter Notebook**, el tipado dinámico facilita ejecutar bloques de código de forma independiente, verificar resultados intermedios y ajustar el enfoque sin reiniciar todo el proceso.
*   **Adaptabilidad:** Los programas parecen "pseudocódigo ejecutable", lo que simplifica la traducción de ideas matemáticas complejas a código funcional.

### 3. Concisión y legibilidad del código
El tipado dinámico contribuye a que el código sea significativamente más corto:
*   Un programa en Python suele tener entre **un tercio y un quinto** del tamaño de su equivalente en Java o C++.
*   Muchos argumentan que el **código corto es más fiable y fácil de mantener** que el código largo y repetitivo, lo cual es vital cuando los proyectos crecen en complejidad.

### 4. Integración como "Lenguaje de Unión"
Aunque el tipado dinámico puede ser más lento en ejecución pura, permite que Python actúe como un **"pegamento"** ideal:
*   Permite que la lógica de alto nivel permanezca flexible y dinámica mientras se delegan las tareas de cálculo pesado a bibliotecas optimizadas escritas en lenguajes de bajo nivel como C, C++ o FORTRAN (como **NumPy** o **pandas**).
*   Esto resuelve el "problema de los dos lenguajes", permitiendo usar la misma herramienta tanto para la investigación y el prototipado como para los sistemas de producción finales.

### 5. Duck Typing (Tipado de Pato)
Esta filosofía, intrínsecamente ligada al tipado dinámico, establece que lo importante es **qué puede hacer un objeto** y no qué tipo de objeto es. En ciencia de datos, esto permite:
*   Crear funciones que operen sobre cualquier objeto que cumpla con un protocolo (por ejemplo, que sea iterable), lo que aumenta enormemente la **reutilización de código**.
*   Extender diseños existentes con nuevos comportamientos sin necesidad de jerarquías de herencia rígidas y complejas.

En resumen, el tipado dinámico transforma al programador de un "constructor de catedrales" (en lenguajes compilados) en un **explorador ágil**, donde cada línea de código es un paso ligero hacia el descubrimiento científico.

IPython

**IPython** ayuda a agilizar el flujo de trabajo exploratorio al transformar el proceso de programación en un ciclo interactivo de **"ejecución-exploración"**, en lugar del flujo tradicional de "editar-compilar-ejecutar". Actúa como un intérprete de Python mejorado que permite a los desarrolladores probar fragmentos de código, examinar datos y depurar errores de manera inmediata.

A continuación se detallan las funcionalidades clave de IPython que aceleran este flujo de trabajo:

### 1. Ejecución e interacción con scripts
*   **Comando `run`:** Permite ejecutar programas de Python completos directamente desde el intérprete. Una vez finalizada la ejecución, todas las variables y funciones definidas en el script permanecen accesibles en la sesión, lo que permite examinar el estado final y realizar pruebas adicionales sin reiniciar el proceso.
*   **Recuperación de resultados:** IPython almacena automáticamente los resultados de las expresiones evaluadas en variables especiales como `_` (para el último resultado), `__` (para el penúltimo) o `_X` (donde X es el número de la línea de salida), facilitando su reutilización inmediata en cálculos posteriores.

### 2. Navegación y asistencia al programador
*   **Autocompletado con TAB:** Al presionar la tecla TAB, el sistema completa nombres de variables, funciones, módulos y atributos de objetos, lo que ahorra tiempo y reduce errores tipográficos. También funciona para completar rutas de archivos en el sistema.
*   **Introspección de objetos:** El uso del signo de interrogación (`?`) antes o después de un objeto muestra información general, como su tipo, firma y cadenas de documentación (*docstrings*), permitiendo entender rápidamente cómo funciona una biblioteca sin consultar manuales externos.
*   **Historial de comandos:** Permite navegar por comandos introducidos previamente con las flechas del teclado o buscar fragmentos específicos con `Ctrl-r`, lo que facilita repetir o editar acciones complejas.

### 3. Integración con el sistema y herramientas avanzadas
*   **Comandos de Shell:** Es posible ejecutar tareas del sistema operativo (como `ls`, `mkdir` o `date`) directamente desde el prompt de IPython, eliminando la necesidad de cambiar constantemente entre la terminal y el intérprete de Python.
*   **Comandos "mágicos" (`%`):** Ofrece funciones especiales para optimizar el desarrollo, como `%timeit` para medir con precisión el tiempo de ejecución de una sentencia, o `%logstart` para grabar toda la sesión en un archivo y poder reproducirla más tarde.
*   **Depuración interactiva:** Tras una excepción, el comando `%debug` permite entrar en un depurador interactivo en el punto exacto donde ocurrió el error para examinar variables y el estado de la pila.

### 4. Base para el entorno Jupyter
IPython es el motor subyacente (kernel) de los **Jupyter Notebooks**, una aplicación web que permite combinar bloques de código ejecutable con texto enriquecido, ecuaciones matemáticas y visualizaciones de datos en un solo documento. Esta integración es fundamental en la ciencia de datos moderna, ya que permite la inspección paso a paso de los resultados y facilita el prototipado rápido.

Jupyter

Los notebooks de Jupyter juegan un papel fundamental en el **flujo de trabajo exploratorio**, ya que transforman la programación en un ciclo interactivo de **"ejecución-exploración"**, en lugar del flujo tradicional de "editar-compilar-ejecutar". Actúan como un entorno de computación interactiva donde el pensamiento y la acción se funden en un mismo flujo, permitiendo al científico o analista actuar como un explorador.

A continuación se detallan sus funciones principales en este flujo:

### 1. Inspección y verificación paso a paso
La característica más distintiva de los notebooks es su estructura basada en **celdas**, que permite:
*   **Ejecutar código en fragmentos**: Se puede realizar una tarea pequeña (como cargar datos), verificar el resultado inmediatamente y luego proceder a la siguiente etapa sin reiniciar todo el proceso.
*   **Inspección de estados intermedios**: Permite ver cómo cambian los datos tras cada transformación, lo cual es vital para el "sanity-check" o comprobación de cordura de la información.
*   **Análisis iterativo**: Si un cálculo falla o no produce el resultado esperado, se puede modificar solo la celda afectada y volver a probar de forma ágil.

### 2. Documentación narrativa y reproducción
Jupyter permite combinar en un solo documento:
*   **Código ejecutable**: Generalmente Python, aunque soporta otros lenguajes como Julia o R.
*   **Texto enriquecido (Markdown)**: Permite incluir explicaciones, encabezados, listas y enlaces que contextualizan el análisis.
*   **Ecuaciones y visualizaciones**: Los resultados, ya sean gráficos de Matplotlib o tablas de datos, se muestran directamente debajo de la celda que los generó.

### 3. Facilidad de visualización y prototipado
*   **Renderizado de datos**: Los objetos de pandas, como los `DataFrames`, se muestran automáticamente como tablas HTML legibles, facilitando la exploración visual de grandes conjuntos de datos.
*   **Prototipado rápido**: Es la herramienta ideal para probar metodologías y depurar lógica antes de formalizar el código en scripts de Python (`.py`) destinados a producción.
*   **Depuración interactiva**: Permite utilizar comandos mágicos como `%debug` inmediatamente después de una excepción para examinar el estado de las variables en el punto exacto del error.

### Limitaciones en el flujo de trabajo
Aunque son excelentes para la exploración, las fuentes advierten que los notebooks **no se recomiendan para entornos de producción**. Su infraestructura es pesada en términos de memoria y procesamiento, lo que los hace lentos y "clunky" (torpes) para ser desplegados como parte final de una tubería de datos (ETL) o aplicaciones operativas. Por ello, se consideran el paso previo para refinar el código antes de moverlo a entornos de desarrollo más robustos como PyCharm.