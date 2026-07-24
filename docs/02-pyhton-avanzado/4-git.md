---
id: git
title: "Git control de versiones"
sidebar_label: "​📊 Git & GitHub"
sidebar_position: 3
description: "Control de versiones con git"
---

Un **control de versiones** es un sistema técnico que **registra de manera detallada cada cambio realizado en el código fuente de un proyecto**, permitiendo mantener un histórico completo de las modificaciones, identificar quién las realizó y cuándo ocurrieron. En términos prácticos, funciona como una serie de "fotografías" o instantáneas del estado de los archivos en momentos específicos, lo que permite navegar por la evolución del proyecto como si fuera una línea del tiempo.

### Origen del sistema moderno Git

Aunque los sistemas de control de versiones existen desde hace décadas, el estándar actual, **Git**, fue **diseñado originalmente por Linus Torvalds en 2005**. Su creación surgió de una necesidad crítica durante el desarrollo del kernel de Linux: tras una disputa con la empresa propietaria de BitKeeper (el software que usaban antes), la comunidad perdió el acceso a dicha herramienta. Torvalds decidió entonces crear un sistema propio que fuera **rápido, eficiente y, sobre todo, distribuido**, superando las limitaciones de alternativas centralizadas de la época como Subversion.

### Características técnicas principales

*   **Arquitectura Distribuida:** A diferencia de los sistemas antiguos, un control de versiones distribuido aloja una **copia completa del repositorio en cada máquina local** que trabaja en el código. Esto permite trabajar sin conexión a internet y asegura que, si el servidor central falla, cualquier colaborador pueda restaurar el proyecto completo.

*   **Ramificación (Branching):** Es la capacidad de crear **líneas de desarrollo independientes** o bifurcaciones. Esto permite que un equipo trabaje en una nueva funcionalidad en una rama mientras otro corrige un error en una rama distinta, sin que sus cambios se interfieran hasta que decidan integrarlos.

*   **Confirmaciones (Commits):** Cada unidad de guardado es un **commit**, que registra los cambios exactos y les asigna un identificador único (hash). Cada commit incluye metadatos como el autor, la fecha y un mensaje descriptivo.

*   **Fusión e Integración (Merge/Rebase):** Proporciona mecanismos técnicos para **unir diferentes líneas de trabajo**, detectando automáticamente si hay conflictos cuando dos personas modifican la misma línea de un archivo y solicitando una resolución manual para garantizar la integridad del código.

### Importancia del control de versiones

El uso de estos sistemas es vital en el desarrollo de software profesional por las siguientes razones:
1.  **Seguridad y Recuperación:** Actúa como una red de seguridad. Si se introduce un error crítico, el sistema permite **revertir el proyecto a una versión anterior que funcione correctamente** de manera casi instantánea.

2.  **Colaboración Masiva:** Permite que cientos de desarrolladores trabajen en el mismo código base de forma simultánea y organizada, facilitando la sincronización de sus avances sin pérdida de información.

3.  **Trazabilidad y Auditoría:** Ofrece transparencia total. Es posible utilizar comandos técnicos (como `git blame`) para **saber exactamente quién modificó cada línea de código**, lo que ayuda a entender el contexto de decisiones pasadas y a solucionar errores con mayor rapidez.

4.  **Experimentación sin Riesgos:** Gracias a las ramas, los desarrolladores pueden probar ideas radicales o refactorizaciones complejas de forma aislada. Si el experimento falla, simplemente se descarta la rama sin haber afectado nunca la estabilidad del producto principal.



## Características principales de Git
1. **Distribuido**: Cada desarrollador tiene una copia completa del repositorio, lo que permite trabajar de manera independiente y sin conexión.
2. **Rendimiento**: Git está diseñado para ser rápido y eficiente, incluso con proyectos grandes.
3. **Ramas y fusiones**: Git facilita la creación y gestión de ramas, lo que permite a los desarrolladores trabajar en características o correcciones de errores de manera aislada antes de fusionarlas con la rama principal.
4. **Integridad de datos**: Git utiliza un sistema de hash SHA-1 para asegurar la integridad de los datos y rastrear los cambios en el código.
5. **Historial completo**: Git mantiene un historial completo de todos los cambios realizados en el código, lo que permite a los desarrolladores revertir a versiones anteriores si es necesario.



## Instalación de Git
#### instalar en Mac OS
```bash
brew install git
```
#### instalar en Windows
```bash
choco install git
```
#### instalar en Linux (Debian/Ubuntu)
```bash
sudo apt-get install git
```
#### instalar en Linux (Fedora)
```bash
sudo dnf install git
```
#### instalar en Linux (Fedora)
```bash
sudo dnf install git
```
#### instalar en Linux (Arch)
```bash
sudo pacman -S git
```

#### Verificar instalación de Git
Independientemente del sistema operativo, para verificar que Git se haya instalado correctamente, puedes ejecutar el siguiente comando en la terminal:

```bash
git --version
```

## Comandos básicos de Git
- `git init`: Inicializa un nuevo repositorio Git en el directorio actual.
- `git add .`: Agrega todos los archivos nuevos y modificados al área de preparación (staging area).
- `git commit -m "Mensaje del commit"`: Crea un commit con los cambios en el área de preparación y un mensaje descriptivo.
- `git branch -M main`: Cambia el nombre de la rama actual a "main".
- `git remote add   origin <REMOTE_REPOSITORY_URL>`: Agrega un repositorio remoto llamado "origin".
- `git push -u origin main`: Sube los cambios a la rama "main" del repositorio remoto "origin".
- `git pull`: Descarga y fusiona los cambios desde el repositorio remoto a tu rama local.
- `git status`: Muestra el estado de los archivos en el repositorio.
- `git log`: Muestra el historial de commits del repositorio.

## Flujo de trabajo típico
1. Clona el repositorio remoto (si es necesario).
2. Realiza cambios en los archivos del proyecto.
3. Usa `git add .` para agregar los cambios al área de preparación.
4. Usa `git commit -m "Mensaje del commit"` para crear un commit con los cambios.
5. Usa `git push` para subir los cambios al repositorio remoto.

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <REMOTE_REPOSITORY_URL>
git push -u origin main

# para actualizar cambios
git add .
git commit -m "Update files"
git push
```

## Ramas en Git

Una **rama (branch)** en Git es, fundamentalmente, una **línea de desarrollo independiente** que permite trabajar en diferentes partes de un proyecto al mismo tiempo sin interferir con el trabajo de los demás. Desde un punto de vista técnico, una rama no es más que un **puntero móvil** que apunta a un commit específico dentro del historial del repositorio.

Las ramas en Git permiten a los desarrolladores trabajar en diferentes características o correcciones de errores de manera aislada. Cada rama es una línea independiente de desarrollo que puede fusionarse con otras ramas cuando sea necesario.

A continuación, se detalla por qué Git las considera **"baratas"**:

*   **No hay duplicación de archivos:** A diferencia de otros sistemas de control de versiones antiguos que copiaban todos los archivos del proyecto a una nueva carpeta, en Git crear una rama no implica copiar ni clonar datos pesados.

*   **Es solo un archivo de texto:** Técnicamente, una rama es simplemente un pequeño archivo almacenado en el directorio oculto `.git/refs/heads/` que contiene únicamente el código hash (identificador único) del commit al que apunta.

*   **Operación casi instantánea:** Debido a que solo se requiere crear un archivo con una referencia de 40 caracteres, la creación de una rama es una operación extremadamente rápida y consume un espacio en disco insignificante.

*   **Actualización eficiente:** Cuando se realiza un nuevo commit en una rama, Git simplemente actualiza ese puntero para que apunte al nuevo hash del commit recién creado, lo cual sigue siendo un proceso muy ligero.

En resumen, las ramas son herramientas poderosas para **aislar el trabajo** (como probar nuevas funcionalidades o arreglar errores) de forma segura, permitiendo que el historial del proyecto diverja y luego, si es necesario, se vuelva a integrar mediante una fusión (merge).

![](https://git-scm.com/book/en/v2/images/two-branches.png)


### Puntero HEAD

El puntero **HEAD** es una de las referencias más importantes en Git, ya que funciona como un indicador de **"usted está aquí"** dentro del historial de tu repositorio. A continuación se detalla su funcionamiento y su estrecha relación con las ramas:

#### ¿Qué es el puntero HEAD?
*   **Referencia actual:** HEAD es un puntero que referencia el punto específico del historial de cambios en el que estás trabajando en ese momento. 
*   **Ubicación física:** Técnicamente, es un archivo almacenado en el directorio oculto `.git/HEAD`. Si abres este archivo, verás que normalmente contiene una referencia a una rama, por ejemplo: `ref: refs/heads/main`.
*   **Unicidad:** Solo puede haber un único HEAD en un repositorio local; representa el estado actual de tu directorio de trabajo.

#### Relación entre HEAD y las ramas
La relación entre ambos es jerárquica y dinámica:
1.  **Puntero de punteros:** Normalmente, HEAD no apunta directamente a un commit, sino que **apunta a una rama** (que a su vez es un puntero móvil que apunta a un commit).
2.  **Movimiento al cambiar de rama:** Cuando usas comandos como `git switch` o `git checkout` para cambiar de rama, Git actualiza el puntero HEAD para que apunte a la nueva rama seleccionada. Esto provoca que tu directorio de trabajo se actualice con los archivos de esa rama específica.
3.  **Actualización tras un commit:** Cuando realizas una nueva confirmación (commit), la rama en la que estás situado se mueve hacia adelante para apuntar al nuevo hash generado. Como HEAD está "enganchado" a esa rama, se mueve automáticamente junto con ella para mantenerse en la punta del historial.

#### El estado de "HEAD desprendido" (Detached HEAD)
Existe una situación especial en la que HEAD pierde su relación con las ramas:
*   Ocurre cuando haces un `checkout` directamente a un **hash de commit específico** o a una **etiqueta (tag)** en lugar de a una rama.
*   En este estado, HEAD apunta directamente a un commit y no a un nombre de rama. Aunque puedes explorar el código y hacer cambios experimentales, los nuevos commits que hagas no pertenecerán a ninguna rama y podrían ser difíciles de recuperar si cambias de lugar sin crear una rama nueva para guardarlos.

El estado de **"HEAD desprendido" (detached HEAD)** ocurre cuando el puntero HEAD de Git apunta directamente a un **commit específico** en lugar de apuntar a una rama.

Normalmente, HEAD es un puntero que indica en qué rama te encuentras (como `main` o `feature`), y esa rama, a su vez, apunta al último commit realizado en ella. Sin embargo, si decides explorar una versión antigua del proyecto o una etiqueta (tag) específica, entras en este estado especial.

#### ¿Cómo se entra en este estado?
La forma más común es utilizando el comando `git checkout` seguido de un **hash de commit** (por ejemplo: `git checkout cee84b4`) o un tag. Al hacerlo, Git te avisará con un mensaje indicando que has cambiado a un estado de 'detached HEAD'.

#### ¿Por qué se considera riesgoso?
Aunque este estado es útil para visualizar versiones anteriores o realizar experimentos rápidos, presenta riesgos importantes si decides trabajar en él:

1.  **Pérdida de commits:** Puedes realizar cambios y crear nuevos commits en este estado, pero estos **no pertenecen a ninguna rama**.

2.  **Dificultad de recuperación:** Si decides cambiar de rama (por ejemplo, con `git switch main`) sin haber guardado tu trabajo en una rama nueva, los commits que hiciste en el estado desprendido se vuelven muy difíciles de encontrar. Aunque técnicamente siguen en el historial por un tiempo, no hay una referencia (rama) que los sostenga, por lo que Git podría eliminarlos eventualmente mediante procesos internos de limpieza (garbage collection).

3.  **Historia no lineal:** Trabajar sin una rama asignada rompe el flujo de desarrollo estándar de Git, que está diseñado para funcionar mediante punteros móviles (ramas).

#### ¿Cómo salir de este estado de forma segura?
El estado de **"HEAD desprendido"** (detached HEAD) ocurre cuando el puntero HEAD apunta directamente a un identificador de commit específico (hash) en lugar de apuntar al nombre de una rama.

Para "arreglar" o salir de este estado, el procedimiento depende de si deseas conservar los cambios realizados o descartarlos:

#### 1. Si quieres guardar los cambios realizados
Si has hecho commits o modificaciones en este estado y no quieres perderlas, lo ideal es **crear una nueva rama** a partir de tu posición actual. Esto le da un nombre y una referencia estable a tu trabajo.
*   **Comando recomendado:** `git switch -c <nombre-de-la-nueva-rama>`.
*   **Alternativa:** `git checkout -b <nombre-de-la-nueva-rama>`.

Al hacer esto, HEAD dejará de estar desprendido y pasará a apuntar a la nueva rama que acabas de crear.

#### 2. Si quieres descartar los cambios y volver a una rama
Si solo estabas explorando una versión antigua y quieres regresar a tu línea de desarrollo principal (como `main` o `master`), simplemente debes **cambiar de rama**.
*   **Comando:** `git switch <nombre-de-la-rama>` o `git checkout <nombre-de-la-rama>`.

**Nota importante:** Al cambiar a otra rama sin haber guardado tu trabajo previo en una nueva, podrías perder los commits realizados en el estado desprendido, ya que no habrá ninguna rama que los referencie.

#### 3. ¿Qué pasa si ya saliste del estado y "perdiste" el trabajo?
Si regresaste a una rama y te das cuenta de que olvidaste guardar commits importantes que hiciste mientras el HEAD estaba desprendido, aún puedes recuperarlos:
*   Utiliza el comando **`git reflog`**. Este comando muestra un historial completo de todas las acciones y movimientos del puntero HEAD, permitiéndote encontrar el hash del commit "perdido" para volver a él o crear una rama a partir de él.

## Administración de ramas

### Crear una nueva rama 'testing' y trabajar en ella
```bash
git checkout -b testing
# hacer cambios en los archivos
git add .
git commit -m "Add testing feature"
git push -u origin testing
```
![](https://git-scm.com/book/en/v2/images/head-to-testing.png)

Se han realizado los cambios en la rama 'testing'
```bash
git commit -a -m 'Make a change'
```

![](https://git-scm.com/book/en/v2/images/advance-testing.png)

Se han verificado los cambios en la rama 'testing' y ahora esta rama 'testing' se encuentra más actualizada que la master y queremos por tanto que se fusione con 'master'. Para ello activamos la rama 'master'.

```bash
git checkout master
```
![](https://git-scm.com/book/en/v2/images/checkout-master.png)

Ahora el puntero HEAD está en la rama 'master' y todos los cambios que hagamos se aplicarán a esta rama 'master'. Las modificaciones de archivos que hemos hecho en la rama 'testing' no se ven reflejadas en la rama 'master' todavía.

Ahora fusionamos la rama 'testing' con la rama 'master'
```bash
git merge testing
```
![](https://git-scm.com/book/en/v2/images/merge-testing-into-master.png)

---
## Script para automatizar commits y push
```sh
#!/bin/sh
git add .
git commit -m "Update files"
git push
```


# Github
GitHub es una plataforma de alojamiento de código fuente y control de versiones que utiliza Git. Permite a los desarrolladores colaborar en proyectos, gestionar versiones de código y compartir su trabajo con la comunidad.

## Crear un repositorio en GitHub
1. Inicia sesión en tu cuenta de GitHub.
2. Haz clic en el botón "New" o "Nuevo" para crear un nuevo repositorio.
3. Proporciona un nombre para tu repositorio y una descripción opcional.
4. Elige si deseas que el repositorio sea público o privado.
5. Haz clic en "Create repository" o "Crear repositorio".

## Clonar un repositorio
```bash
git clone <REMOTE_REPOSITORY_URL>
```
