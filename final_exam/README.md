# Examen final

## ⚙️ Generalidades
El examen final de la materia de _Desarrollo de Proyectos II_ tiene un valor del **20%** sobre la calificación final. Esta actividad se deberá subir **por equipos de trabajo** en el repositorio de GitHub de esta materia [UDG_MCD_Project_Dev_II](https://github.com/vcuspinera/UDG_MCD_Project_Dev_II), en la carpeta `final_exam` dentro de la carpeta correspondiente a cada uno de los equipos:

|No. de Equipo |Alumnos |
|:---:|:---:|
|Equipo 1 |José Raúl Castro Esparza  y  Martha Olivia Ramos Lara|
|Equipo 2 |Mónica Alonso Soria  y  Mario Palomino Hernández|
|Equipo 3 |Luis Enrique Neri González  y  Carlos Samuel Cruz Mariscal|
|Equipo 4 |Pedro Martínez Ayala  y  Afra Julieta Lomelí Ávila|
|Equipo 5 |Carol Desireé Ramírez Durán  y  César Iván Vargas López|

## 🛠 Proyecto a desarrollar

Considere el proyecto de lanzamiento de cierto producto al mercado cuyas tareas están enlistadas de la siguiente manera:

|No. de tarea|Nombre de tarea|Duración|Predecesor|Recursos|
|:---:|:---|:---:|:---:|:---|
||Lanzamiento del nuevo producto||||
|1|Fase 1: Planeación||||
|2|Identificar el equipo de lanzamiento|3||Ingeniería, Fabricación, Marketing, Ventas, Soporte Técnico, Servicio de campo|
|3|Determinar los objetivos de ventas|2||Director de producto|
|4|Determinar socios||||
|5|Identificar socios del canal|4|3|Director de producto|
|6|Identificar socios de ventas|2|3 y 5|Marketing|
|7|Establecer presupuesto de lanzamiento||||
|8|Identificar requisitos de presupuesto|2|5 y 6|Marketing|
|9|Obtener aprobación del presupuesto de lanzamiento|2|8|Marketing|
|10|Fase de planeación completada|0|9||
|11|Fase 2: iniciación y preparación||||
|12|Puesta en marcha|2|10|Director de producto|
|13|Marketing||||
|14|Definir el resumen creativo|3|12|Director de producto, Marketing, Ventas|
|15|Preparar marco de trabajo de mensajería||||
|16|Revisar información actual y planear nuevos requisitos|2|14|Director de producto|
|17|Definir información de especificaciones de producto|3|14|Marketing|
|18|Definir necesidades de comunicación internas|4|14|Servicio de campo|
|19|Coordinar las fechas de lanzamiento del producto|3|14|Ingeniería|
|20|Preparar la fabricación de acuerdo con los objetivos|3|14|Fabricación|
|21|Plantear personal del equipo para apoyar a ventas|5|14|Ventas|
|22|Fase de iniciación completada|0|16 a 21||
|23|Fase 3 : Lanzamiento a fabricación||||
|24|Certificar producto|4|22|Director de producto|
|25|Fabricar el volumen planeado del producto|10|22|Fabricación|
|26|Contratar y formar al personal de ventas|3|22, 24 y 25|Ventas|
|27|Contratar y formar al personal de soporte de productos|2|26|Soporte Técnico|
|28|Contratar y formar al personal del servicio de campo|2|26|Servicio de campo|
|29|Realizar revisión de calidad final|3|27 y 28|Director de producto, Fabricación, Ingeniería, Marketing, Servicio de campo, Soporte Técnico, Ventas|
|30|Lanzar producto|1|29|Director de producto|
|31|Fase de lanzamiento finalizada|0|30||

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

⚠️ _Nota:_ tanto el equipo de _Soporte Técnico_ como el de _Servicio de Campo_ tienen un costo fijo por uso, sin importar de cuantos días se trate, al ser contratados como outsourcing por evento. Los costos diarios por equipo se prorratean en caso de tener una duración fraccionaria por tarea.

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

En base a la información anterior y el uso de @RISK con 10,000 escenarios, conteste a las siguientes preguntas planeando iniciar el día __1 de Julio del 2022__:

1) ¿Cuál es la fecha estimada y costo de terminación para dicho lanzamiento, asumiendo que las cosas salen de acuerdo a lo planeado (sin variaciones) y laborando de lunes a viernes? Elabore un Diagrama de Gantt que muestre la planificación de este proyecto de manera detallada.  
2) ¿Cuál es el riesgo de no terminar al 15 de septiembre del 2022 cuando consideramos los riesgos y variaciones expuestas anteriormente?  
3) Proporcione un intervalo del 95% para el costo de todo el proyecto.
4) ¿Cuáles son aquellos 3 riesgos que más impactan en la variabilidad de la fecha de terminación? Explique a detalle en función del gráfico que soporta su respuesta.  
5) ¿Qué tan probable es que la Fase 2 tarde menos de 40 días?  
6) ¿Qué fue lo que más le gustó de este curso?, ¿qué fue lo que menos le gustó?, y ¿qué mejoras sugiere hacer para que este curso sea más enriquecedor en la formación de quienes cursen esta maestría?

## 📚 Entregables:
Dentro de la carpeta `final_exam` se encuentra un folder para cada equipo, donde deberán añadir los siguientes archivos:  
- **Archivo de Word**, con un reporte detallado contestando a cada pregunta con base en los resultados obtenidos con @Risk y/o Project en función de la pregunta.  
- **Archivo de Excel**.  
- **Archivo de Project**.  
- **README.md** file, a manera de portada, con el número de equipo, nombre de los integrantes, una breve explicación sobre el proyecto final, y el enlace a cada uno de los archivos.

⚠️ _Nota:_ En caso de tener algún problema para subir alguno de los archivos, favor de contactarme a la brevedad vía slack o a través de mi correo vcuspinera@gmail.com  

## 📅 Deadline
⚠️ La fecha límite para subir sus resultados es el día **miércoles, 11 de mayo de 2022** a las **23:59 hr.**  

...si suben sus resultados posterior a esa fecha, habrá una **penalidad del 50%**.


## 🔍 Forma de calificar
Esta actividad se calificará con base en los siguientes puntos:

- Seguir instrucciones
- Subir archivos entregables a GitHub
- Veracidad de sus respuestas
- Claridad y presentación
