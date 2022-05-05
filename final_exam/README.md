# Examen final

## ⚙️ Generalidades
El examen final de la materia de _Desarrollo de Proyectos II_ tiene un valor del **20%** sobre la calificación final, el cuál se desarrollará **por equipos de trabajo** de acuerdo a la siguiente tabla:

|No. de Equipo |Alumnos |
|:---:|:---:|
|Equipo 1 |Martha Olivia Ramos Lara + José Raúl Castro Esparza|
|Equipo 2 |Mónica Alonso Soria + Mario Palomino Hernández|
|Equipo 3 |Carlos Samuel Cruz Mariscal + Luis Enrique Neri González|
|Equipo 4 |Afra Julieta Lomelí Ávila + Pedro Martínez Ayala|
|Equipo 5 |Carol Desireé Ramírez Durán + César Iván Vargas López|

## 🛠 Actividad a desarrollar

### Descripción

Considere el proyecto de lanzamiento de cierto producto al mercado cuyas tareas están enlistadas de la siguiente manera:

|No. de tarea|Nombre de tarea|Duración|Predecesor|Recursos|
|:---:|:---|:---:|:---:|:---|
||Lanzamiento del nuevo producto||||
|1|**Fase 1: Planeación**||||
|2| &emsp; Identificar el equipo de lanzamiento|3||Ingeniería, Fabricación, Marketing, Ventas, Soporte Técnico, Servicio de campo|
|3| &emsp; Determinar los objetivos de ventas|2||Director de producto|
|4| &emsp; **Determinar socios**||||
|5| &emsp; Identificar socios del canal|4|3|Director de producto|
|6| &emsp; Identificar socios de ventas|2|3 y 5|Marketing|
|7| &emsp; **Establecer presupuesto de lanzamiento**||||
|8| &emsp; Identificar requisitos de presupuesto|2|5 y 6|Marketing|
|9| &emsp; Obtener aprobación del presupuesto de lanzamiento|2|8|Marketing|
|10| &emsp; Fase de planeación completada|0|9||
|11|**Fase 2: iniciación y preparación**||||
|12|&emsp; Puesta en marcha|2|10|Director de producto|
|13|&emsp; **Marketing**||||
|14|&emsp; Definir el resumen creativo|3|12|Director de producto, Marketing, Ventas|
|15|&emsp; **Preparar marco de trabajo de mensajería**||||
|16|&emsp; Revisar información actual y planear nuevos requisitos|2|14|Director de producto|
|17|&emsp; Definir información de especificaciones de producto|3|14|Marketing|
|18|&emsp; Definir necesidades de comunicación internas|4|14|Servicio de campo|
|19|&emsp; Coordinar las fechas de lanzamiento del producto|3|14|Ingeniería|
|20|&emsp; Preparar la fabricación de acuerdo con los objetivos|3|14|Fabricación|
|21|&emsp; Plantear personal del equipo para apoyar a ventas|5|14|Ventas|
|22|&emsp; Fase de iniciación completada|0|16 a 21||
|23|**Fase 3 : Lanzamiento a fabricación**||||
|24|&emsp; Certificar producto|4|22|Director de producto|
|25|&emsp; Fabricar el volumen planeado del producto|10|22|Fabricación|
|26|&emsp; Contratar y formar al personal de ventas|3|22, 24 y 25|Ventas|
|27|&emsp; Contratar y formar al personal de soporte de productos|2|26|Soporte Técnico|
|28|&emsp; Contratar y formar al personal del servicio de campo|2|26|Servicio de campo|
|29|&emsp; Realizar revisión de calidad final|3|27 y 28|Director de producto, Fabricación, Ingeniería, Marketing, Servicio de campo, Soporte Técnico, Ventas|
|30|&emsp; Lanzar producto|1|29|Director de producto|
|31|&emsp; Fase de lanzamiento finalizada|0|30||

En dicha tabla, se describe la duración de cada tarea, así como la relación de sus predecesoras y los recursos (equipos de trabajo) que utiliza, para los cuales se tienen los siguientes costos:

|Equipo|Costo por uso|Costo diario|
|:---|:---:|:---:|
|Ingeniería|-|$300|
|Fabricación|-|$500|
|Marketing|-|$450|
|Ventas|-|$600|
|Soporte Técnico|$2,000|-|
|Servicio de campo|$1,350|-|
|Director de producto|-|$3,000|

⚠️ _Nota: tanto el equipo de **Soporte Técnico** como el de **Servicio de Campo** tienen un costo fijo por uso, sin importar de cuantos días se trate, al ser contratados como "outsourcing" por evento. Los costos diarios por equipo se prorratean en caso de tener una duración fraccionaria por tarea._

En relación a la variabilidad de este proyecto se tiene identificado lo siguiente:  

1) Las tareas de la “Fase de Planeación” pueden desviarse del valor en la tabla en +/- 1 día con la misma probabilidad de ocurrencia.  
2) Las tareas de la “Fase de iniciación y preparación” varían de acuerdo a la distribución Normal donde su valor esperado es el valor de referencia en la tabla y el rango histórico de desviación es de +/- 2 días bajo un criterio Seis Sigma.  
3) Las tareas de la “Fase de lanzamiento a fabricación” varían entre el valor de referencia de la tabla y hasta 3 días más, donde el valor más probable es el de referencia y la probabilidad de alcanzar valores altos es muy baja.  

De manera adicional a lo comentado anterior, existen riesgos complementarios que podrían alargar algunos tiempos de ejecución de diversas tareas. La tabla siguiente describe dichos riesgos, sus probabilidades de ocurrencia, así como las tareas que podrían ser afectadas (en función de los días adicionales que habría que sumar a su duración):

|Riesgo|Prob. de ocurrencia|Tareas afectadas|Días adicionales|
|:---|:---:|:---|:---:|
|Permiso de registro|0.35|Identificar requisitos de presupuesto|3|
|Disponibilidad de materiales|0.45|Fabricar el volumen planeado del producto|5|
|Calidad inadecuada|0.15|Realizar revisión de calidad final|2|
|Personal inadecuado|0.1|Contratar y formar al personal de ventas|10|

### Preguntas
Con base en la información anterior y mediante el uso de @RISK con 10,000 escenarios, conteste a las siguientes preguntas planeando iniciar el día __1 de Julio del 2022__:

1) ¿Cuál es la fecha estimada y costo de terminación para dicho lanzamiento, asumiendo que las cosas salen de acuerdo a lo planeado (sin variaciones) y laborando de lunes a viernes? Elabore un Diagrama de Gantt que muestre la planificación de este proyecto de manera detallada.  

2) ¿Cuál es el riesgo de no terminar al 15 de septiembre del 2022 cuando consideramos los riesgos y variaciones expuestas anteriormente?  

3) Proporcione un intervalo del 95% para el costo de todo el proyecto.

4) ¿Cuáles son aquellos 3 riesgos que más impactan en la variabilidad de la fecha de terminación? Explique a detalle en función del gráfico que soporta su respuesta.  

5) ¿Qué tan probable es que la Fase 2 tarde menos de 40 días?  

6) ¿Qué fue lo que más le gustó de este curso?, ¿qué fue lo que menos le gustó?, y ¿qué mejoras sugiere hacer para que este curso sea más enriquecedor en la formación de quienes cursen esta maestría?

## 📚 Entregables:
### Correo Electrónico
Enviar un correo electrónico a **vcuspinera@gmail.com** con nombre del Asunto: "MCD Examen final equipo #", el cual deberá contener:  
- **Reporte detallado en Word**, en el cual se compartirán las respuestas a cada pregunta con base en los resultados obtenidos con @Risk y Project.  
- **Archivo de Excel**.  
- **Archivo de Project**.  

### GitHub
En el repositorio de GitHub de [UDG_MCD_Project_Dev_II](https://github.com/vcuspinera/UDG_MCD_Project_Dev_II), dentro de la carpeta `final_exam`, encontrarán una carpeta correspondiente a su equipo, en la cual deberán compartir:  
- **Reporte de resultados**. El archivo `README.md` deberá contener el número de equipo, nombre de los integrantes, breve descripción sobre la problemática y las respuestas compartidas en el "Reporte detallado en Word" enviado por email. Como referencia pueden revisar el [`Ejemplo` de entrega de resultados](https://github.com/vcuspinera/UDG_MCD_Project_Dev_II/tree/main/final_exam/Ejemplo).

⚠️ _Nota: En caso de tener algún problema para enviar los archivos favor de contactarme a la brevedad vía slack o a través de mi correo vcuspinera@gmail.com_

## 📅 Deadline
La fecha límite para enviar los entregables y subir sus resultados a GitHub es el día **domingo, 15 de mayo de 2022** a las **23:59 hr.**  

...en caso de compartir sus archivos o resultados posterior a esa fecha habrá una **penalización del 50%** sobre la calificación del examen final.  


## 🔍 Forma de calificar
Esta actividad se calificará con base en los siguientes puntos:

- Seguir instrucciones
- Envío de archivos entregables
- Subir reporte de resultados a GitHub
- Veracidad de sus respuestas
- Claridad de los resultados
