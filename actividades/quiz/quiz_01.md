# Quiz 01
Control de lectura de "Excuse me, do you have a moment to talk about version control?" y actividades de Desarrollo de Proyectos I.

Sólo se comparten las preguntas de opción meultiple que tenían una respuesta:

### Sección 2

**2. Comenta tres puntos sobre para qué sirve el sistema de control de versiones:**

En el paper, Jenny Bryan comenta:
> _There are many benefits of using hosted version control in your statistical practice:  
• Doing your work becomes tightly integrated with organizing, recording, and disseminating it. It’s not a separate, burdensome task you are tempted to neglect.  
• Collaboration is much more structured, with powerful tools for asynchronous work and managing versions.  
• The marginal effort required to create a web presence for a project is negligible.  
• GitHub makes a fantastic course management system for courses that use R (R Core Team 2017). You can exchange actual working code with your students and explore the associated results (Cetinkaya-Rundel & Rundel 2017).  
• By using common mechanics across work modes (research, teaching, analysis), you achieve basic competence quickly and avoid the demoralizing forget-relearn cycle._

**3. Selecciona todas las opciones que apliquen para explicar qué es Git:**

Opciones:
- Sistema de control de versiones
- Un sistema similar al de control de cambios de Microsoft Word, pero más riguroso, poderoso y escalable multiples archivos
- Administrator de repositories y proyectos
- Sirve para trabajar a nivel remoto

Respuesta correcta: "Sistema de control de versiones", "Un sistema similar al de control de cambios de Microsoft Word..." y "Administrator de repositories y proyectos".

**4. ¿Qué diferencia tiene Git y GitHub?**

Git es para trabajar de forma local y GitHub de forma remota

**5. ¿Qué ventaja tiene el trabajar con un repositorio de GitHub sobre trabajar con Dropbox o Google Drive?**

En el paper, Jenny Bryan comenta:
> _GitHub is like DropBox or Google Drive, but more structured, powerful, and programmatic._

**6. Si tengo un proyecto con la siguiente estructura y dentro del directorio principal del repositorio quiero entrar a la carpeta "data", ¿cuál de los siguientes comandos debería utilizar desde la interfaz de usuario?**

Opciones:
- touch data
- cd data
- mkdir data
- code data
- rmdir data

Respuesta correcta: `cd data`

**7. Si tengo un proyecto con la siguiente estructura y dentro del directorio principal del repositorio quiero editar el archivo "README.md", ¿cuál de los siguientes comandos debería utilizar desde la interfaz de usuario (e.g. PowerShell o Bash)?**

Opciones:
- delete README.md
- cd README.md
- ls README.md
- code README.md
- rm README.md

Respuesta correcta: `code README.md`

**8. En archivo de markdown (archivo con terminación "md"), si quiero poner un texto en negrita debo:**

Opciones:
```
- Poner la palabra o frase entre corchetes en diagonal, ejemplo: `hola`
- Poner la palabra o frase entre asteriscos, ejemplo: *hola*
- Poner la palabra o frase entre doble tildes, ejemplo: ~~hola~~
- Poner la palabra o frase entre comillas, ejemplo: "hola"
- Poner la palabra o frase entre doble asteriscos, ejemplo: **hola**
- Poner la palabra o frase entre guión bajo, ejemplo: _hola_
```

Respuesta correcta: `Poner la palabra o frase entre doble asteriscos, ejemplo: **hola**`

**9. En archivo de markdown (.md), ¿cuál de las siguientes opciones es un ejemplo de encabezado de tercer nivel?**

Opciones:

```
- # Viaje al fin de la noche
- > Los cuentos de Canterbury
- **Don Quijote de la Mancha**
- + Los hermanos Karamazov
- ### La Divina comedia
```

Respuesta correcta: `### La Divina comedia`

**10. Entre las siguientes opciones selecciona la o las que utilizan una ruta relativa:**

Opciones:
- cd Users/vcuspinera/Documents/levic/02_Studies/2022_MCD_UDG/03_Proj_Dev_II/2023-A_Proj_Dev_II_ACTUAL/grades
- clear
- code ../grades/README.md
- mkdir C:\Users\tedmosby\projects\img
- git commit -m "actualizar carpeta"

Respuesta correcta: "code ../grades/README.md"

**11. Entre las siguientes opciones selecciona la o las que utilizan una ruta absoluta:**

Opciones:
- cd Users/vcuspinera/Documents/levic/02_Studies/2022_MCD_UDG/03_Proj_Dev_II/2023-A_Proj_Dev_II_ACTUAL/grades
- clear
- code ../grades/README.md
- mkdir C:\Users\tedmosby\projects\img
- git commit -m "actualizar carpeta"

Respuesta correcta: "cd Users/vcuspinera/Documents/levic/02_Studies/2022_MCD_UDG/03_Proj_Dev_II/2023-A_Proj_Dev_II_ACTUAL/grades" y "mkdir C:\Users\tedmosby\projects\img"

**12. Copiar y editar el siguiente texto para que se vea igual que en la imagen utilizando código en Markdown:**

Respuesta correcta:

```
# Yellow Submarine
*The Beatles* (alternativa: _The Beatles_)

In the town where I was born  
Lived a man who sailed the sea  
And he told us of his life  
**In the land of submarines** (alternativa: __In the land of submarines__)

So we sailed up to the Sun  
Till we found the sea of green  
And we lived beneath the waves  
In our ~yellow submarine~

1. We all live in a yellow submarine
2. Yellow submarine, yellow submarine
3. We all live in a yellow submarine
4. Yellow submarine, yellow submarine
```
