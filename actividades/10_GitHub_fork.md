# 10 • GitHub fork
*Para trabajar repositorios previamente existentes de otros usuarios*

Git es una herramienta utilizada para trabajar de forma local (en equipo propio) el sistema de control de versiones, y GitHub de forma remota (web). En esta sección trabajaremos con el uso de Fork y otras acciones en GitHub.

## Contenido
1. Forking
2. Clonar el repositorio en Git local
3. Correr archivo en Jupyter
4. Añadir archivo
5. Subir información a repositorio remoto
6. Comentarios finales
7. Referencias

## 1. Forking
En esta sección realizaremos una actividad:
1. abrir la siguiente página: https://github.com/vcuspinera/practice_actions,
2. dar click en el botón `Fork` ubicado del lado superior-derecho del repositorio,

Esta acción creará una copia del repositorio original en su cuenta de GitHub la cual tendrá el mismo nombre que el original.

## 2. Clonar el repositorio en Git local
Desde su nuevo repositorio *forkeado* con nombre **practice_actions**, deberán clonar este repositorio a su Git local, es decir:
1. dar click en `code`, seleccionar la opción `HTTPS` y copiar el URL,
2. desde su interfaz de usuario, ubicarse en su carpeta de `Mis Documentos` o en el repositorio de actividades del curso que hayan creado en actividades previas,
3. clonar el repositorio remoto GitHub en su repositorio local Git, corriendo el siguiente comando:

    ```
    git clone pegar_URL_repositorio
    ```

## 3. Correr archivo en Jupyter
Posteriormente habrá que abrir el archivo **“Harry_Potter.ipynb”** ubicado en la carpeta ‘src’, usando *Jupyter Lab*, *Jupyter Notebook* o *Visual Studio Code*, y correr el archivo.

## 4. Añadir archivo
Dentro de la carpeta `src` se deberán realizar las siguientes acciones:
1. crear un archivo de nombre `README.md`, en el que se deberá...
2. añadir un título, 
3. una breve descripción del archivo **“Harry_Potter.ipynb”**,
4. añadir una imagen relacionada con Harry Potter. **Hint:**

    4.1 Entrar a la página de [GIPHY](https://giphy.com):

         A. identificar un GIF que les guste de Harry Potter,   
         B. dar click sobre el GIF,  
         C. dar click sobre **Share**,  
         D. dar click sobre **Copy GIF Link** de menor peso.  
        
    4.2 Usar el código para añadir imágenes que vimos en las actividades [05_Markdown_basics.md](https://github.com/vcuspinera/UDG_MCD_Project_Dev_II/blob/main/actividades/05_Markdown_basics.md) y [06_GitHub_practice.md](https://github.com/vcuspinera/UDG_MCD_Project_Dev_II/blob/main/actividades/06_GitHub_practice.md))

        ```
        ![](pegar_link_aquí)  
        
        *Source: [GIPHY](pegar_link_aquí)*
        ```

## 5. Subir información a repositorio remoto

Posteriormente habrá que subir la información del repositorio local Git al repositorio remoto GitHub, usando los comandos `git add`, `git commit` y `git push`.

**Hint:** Revisar *sección 5* de la actividad [08_Git_and_GitHub.md](https://github.com/vcuspinera/UDG_MCD_Project_Dev_II/blob/main/actividades/08_Git_and_GitHub.md) para ver cómo usar los tres comandos mencionados de `git`.

## 6. Comentarios Finales
Una vez realizado lo anterior podremos identificar que estos cambios se ven reflejados en la carpeta remota ubicada en GitHub, la cual fue *forkeada* y posteriormente modificada. En resumen, cuando hacemos `Fork` de un repositorio de otro usuario, realizamos una copia en nuestros repositorios remotos en GitHub, el cual lo usamos como una **base** para realizar modificaciones, desarrollar ideas propias, y generar / actualizar / utilizar el código para nuestros nuevos proyectos.

## 7. Referencias
- Material público del curso [Plataformas para ciencia de datos](https://github.com/UBC-MDS/DSCI_521_platforms-dsci) de UBC MDS.
