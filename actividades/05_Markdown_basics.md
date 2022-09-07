# 05 • Markdown
*Referencia rápida a comandos para usar en Markdown*

Este archivo es un una referencia rápida a manera de *cheatsheet* para dar formato a Markdowns, lo cual aplica para archivos terminación `.md`, R-markdown y Jupyter notebooks. En este documento se presenta el código usado, así como el resultado.

## Contenido
1. Header
2. Énfasis
3. Listas
4. Links
5. Imágenes
6. Código
7. Tablas
8. Citas
9. HTML
10. Líneas horizontales
11. Youtube
12. Referencias

## 1. Header
Existen varios niveles de encabezados de acuerdo a lo siguiente:

```
# H1 encabezado para título
## H2 encabezado para subtítulo
### H3 encabezados de tercer nivel
#### H4 encabezados de cuarto nivel
##### H5 encabezados de quinto nivel
###### H6 encabezados de sexto nivel
```

# H1 encabezado para título
## H2 encabezado para subtítulo
### H3 encabezados de tercer nivel
#### H4 encabezados de cuarto nivel
##### H5 encabezados de quinto nivel
###### H6 encabezados de sexto nivel

Alternativa usando líneas:

```
H1 alternativo para encabezado para título
====

H2 alterantivo para encabezado para subtítulo
---
```

H1 alternativo para encabezado para título
====

H2 alterantivo para encabezado para subtítulo
---

<center>— ⭕️ —</center>

## 2. Énfasis
Existen distintos tipos de énfasis:
```
Para énfasis use cursiva utilizando *asteriscos* o _guión bajo_.

Para un mayor énfasis puedes utilizar negritas usando  **dos asteriscos** o __dos guiones bajos__.

Para tener ambos énfasos usa **doble asterisco y _guión bajo sencillo_**.

Para tachar texto utiliza ~~dos tildes~~
```

... y aquí se ejemplifica:

Para énfasis use cursiva utilizando *asteriscos* o _guión bajo_.

Para un mayor énfasis puedes utilizar negritas usando  **dos asteriscos** o __dos guiones bajos__.

Para tener ambos énfasos usa **doble asterisco + _guión bajo sencillo_**.

Para tachar texto utiliza ~~dos tildes~~.

## 3. Listas
Para hacer una lista con números basta con incluir la numeración al inicio del texto seguida de un punto. Para una lista co viñetas se puede utilizar `-`, `*` o `+`. Se puede identar con espacios para considerar puntos adicionales

```
Lista numérica. Al despertar:
1. Apago el reloj
2. Me lavo los dientes
3. Me visto para ir a trabajar

Lista con viñetas. Compras del super:
- Leche
* Pan
+ Huevo 

Lista combinada e identada. Cocinar una sincronizada:
1. Comprar:
   - tortillas
   - queso
   - jamón
2. Calentar un sartén
3. Poner una tortilla a calentar, añadir jamón y queso
4. Se recomienda acompañar con salsa al gusto

```

Lista numérica. Al despertar:
1. Apago el reloj
2. Me lavo los dientes
3. Me visto para ir a trabajar

Lista con viñetas. Compras del super:
- Leche
* Pan
+ Huevo 

Lista combinada e identada. Cocinar una sincronizada:
1. Comprar:
   - tortillas
   - queso
   - jamón
2. Calentar un sartén
3. Poner una tortilla a calentar, añadir jamón y queso
4. Se recomienda acompañar con salsa al gusto

# 4. Links

Hay dos maneras de incuir links:

La primera es escribiendo la liga directamente o entre corchetes:


```
- link directo: https://mcd.cucea.udg.mx

- link con corchetes: <https://mcd.cucea.udg.mx>
```

Y así se ve ven estos ejemplos: 

- link directo: https://mcd.cucea.udg.mx

- link con corchetes: <https://mcd.cucea.udg.mx>

La forma alternativa es escribiendo entre corchetes el texto que queremos que se muestre seguido de paréntesis con la liga de la página:

```
- link en texto: [Página de la MCD de la UDG](https://mcd.cucea.udg.mx)
```

Y así se ve el link con hipervínculo en el texto:

- link en texto: [Página de la MCD de la UDG](https://mcd.cucea.udg.mx)

## 5. Imágenes
Para incluir una imagen se utiliza el siguiente texto:

```
![](https://media.giphy.com/media/l2Sq1RpduQRs3IPf2/giphy.gif "Flash!!!")
```

Esto es lo que se ve con el código previo:

![](https://media.giphy.com/media/l2Sq1RpduQRs3IPf2/giphy.gif "Flash!!!")

## 6. Código

Existen dos maneras de añadir código dentro de un Markdown:

La primera es añadir código en la línea de texto para lo cual se añade un corchete antes y uno después de la palabra. Ejemplo:

```
`código`
```

Y así se ve el texto anterior: `código`

La segunda forma es incluir una ventana de código para lo cual se utilizan tres corchetes ` ``` ` seguido del lenguaje, en los renglones posteriores añadir el código (cuándo ésto aplique) y en un renglón posterior se cierra con tres corchetes. Ejemplo:

````
Código en Python:
```python
x = 2
y = 3
x + y
```

Código en R:
```r
x <- 2
y <- 3
x + y
```

Código sin lenguaje:
```
Ejemplo de código 
sin añadir lenguaje
específico, en
varias líneas.
```
````

Así se ven als ventanas de códigos anteriores...

Código en Python:
```python
x = 2
y = 3
x + y
```

Código en R:
```r
x <- 2
y <- 3
x + y
```

Código sin lenguaje:
```
Ejemplo de código 
sin añadir lenguaje
específico, en
varias líneas.
```

## 7. Tablas
Para hacer tablas se utiliza el siguiente formato:
```
|No.| Nombre   | Edad|
|---|:--------:|----:|
| 1 | Armando  |   28|
| 2 | Leopoldo |   33|
| 3 | Víctor   |   39|
```

Así se ve la tabla anterior:

|No.| Nombre   | Edad|
|---|:--------:|----:|
| 1 | Armando  |   28|
| 2 | Leopoldo |   33|
| 3 | Víctor   |   39|


## 8. Citas
Para poner una cita, al inicio de la frase se añade `>`

```
> "Somos lo que hacemos para cambiar lo que somos." -Eduardo Galeano
```

Y así se ve el texto anterior:
> "Somos lo que hacemos para cambiar lo que somos." -Eduardo Galeano

## 9. HTML

Este es el código en HTML completo:
```
<html>
<body>
<p>Ejemplo de texto con HTML, extracto de poema "The Raven" de Allan Poe:</p>
<p>
<center>
But the Raven, sitting lonely on the placid bust, spoke only<br>
That one word, as if his soul in that one word he did outpour.<br>
Nothing farther then he uttered—not a feather then he fluttered—<br>
Till I scarcely more than muttered “Other friends have flown before—<br>
On the morrow he will leave me, as my Hopes have flown before.”<br>
Then the bird said: <p style="color:red">“Nevermore.”</p>
</center>
</p>
</body>
</html>
```

...Y así es como se ve el texto anterior:

<html>
<body>
<p>Ejemplo de texto con HTML, extracto de poema "The Raven" de Allan Poe:</p>
<p>
<center>
But the Raven, sitting lonely on the placid bust, spoke only<br>
That one word, as if his soul in that one word he did outpour.<br>
Nothing farther then he uttered—not a feather then he fluttered—<br>
Till I scarcely more than muttered “Other friends have flown before—<br>
On the morrow he will leave me, as my Hopes have flown before.”<br>
Then the bird said: <p style="color:red">“Nevermore.”</p>
</center>
</p>
</body>
</html>

## 10. Líneas horizontales
Hay distintas maneras de incluir una línea en el texto de markdown, apra lo cual se deben de poner tres o más de las siguientes opciones:

```
---
(1) Usando guiones

***
(2) Con asteriscos

___
(3) Usando guiones bajos
```

Y así se ve el código anterior:

---
(1) Usando guiones

***
(2) Con asteriscos

___
(3) Usando guiones bajos

## 11. Youtube
No se pueden añadir videos de Youtube directo del Markdown, pero se puede añadir una imagen que te lleve a la página de Youtube utilizando el siguiente formato:

```
[![TEXTO DE LA IMAGEN](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)
```

Aquí hay un ejemplo del código:

```
[![UBC Intro to Python by Mike Gelbart](https://img.youtube.com/vi/yBAYduexjuA/0.jpg)](https://www.youtube.com/watch?v=yBAYduexjuA)
```

...y así es como se ve el código anterior:

[![UBC Intro to Python by Mike Gelbart](https://img.youtube.com/vi/yBAYduexjuA/0.jpg)](https://www.youtube.com/watch?v=yBAYduexjuA)

Por cierto, les recomiendo las clases que comparte este profesor de la University of British Columbia: Mike Gelbart.

## 12. Referencias
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet), por Adam Pritchard (Mar 27, 2022), material en GitHub [`adam-p/markdown-here`](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).
- Material público del curso [Plataformas para ciencia de datos](https://github.com/UBC-MDS/DSCI_521_platforms-dsci) de UBC MDS.