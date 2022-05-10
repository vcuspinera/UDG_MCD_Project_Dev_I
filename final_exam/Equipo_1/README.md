# Reporte de resultados
En este documento se comparte el detalle de los resultados del examen final para la materia de Desarrollo de Proyectos II de la Maestría en Ciencia de los Datos (MCD) de la Universidad de Guadalajara (UDG).


## Información del equipo
Materia: Desarrollo de Proyectos II

Número de Equipo: 1

Integrantes:
- Martha Olivia Ramos Lara
- José Raúl Castro Esparza


## Descripción del problema
En este examen se considera un proyecto de lanzamiento de cierto producto al mercado en donde se enlistan las tareas inivolucradas, su orden de precedencia, las variaciones a que están expuestas en sus duraciones y los riesgos adicionales que se pueden experimentar. Asimismo, se incliuyen los costo asociados a los recursos que se utilizan para dicho fin.


## Respuestas
Con base en la información anterior y mediante el uso de @RISK con 10,000 escenarios, se contestan a las siguientes preguntas planeando iniciar el día __1 de Julio del 2022__:

1. **¿Cuál es la fecha estimada y costo de terminación para dicho lanzamiento, asumiendo que las cosas salen de acuerdo a lo planeado (sin variaciones) y laborando de lunes a viernes? Elabore un Diagrama de Gantt que muestre la planificación de este proyecto de manera detallada.**  

El modelo desarrollado en @RISK se puede apreciar en las siguientes imágenes (donde las celdas de color azul representan variables aleatorias de entrada, y las rojas son variables de salida):

<img src="https://raw.githubusercontent.com/vcuspinera/UDG_MCD_Project_Dev_II/main/final_exam/Equipo_1/Grafico_1.png">

Por tal motivo, la fecha de terminación sería establecida para el 26/Agosto/2022

2. **¿Cuál es el riesgo de no terminar al 15 de septiembre del 2022 cuando consideramos los riesgos y variaciones expuestas anteriormente?**  

De acuerdo al histograma de frecuencias en @RISK obtenido para este proyecto en su fecha de terminación tenemos:

<img src="https://raw.githubusercontent.com/vcuspinera/UDG_MCD_Project_Dev_II/main/final_exam/Equipo_1/Grafico_2.png">

Así, la probabilidad de no terminar al 15/Sep/2022 es del 9.8%

3. **Proporcione un intervalo del 95% para el costo de todo el proyecto.**

Con una confianza del 95% podemos decir que el costo del proyecto estará entre $102,231 y $129,459, de acuerdo al histograma obtenido para el costo total del proyecto siguiente:

<img src="https://raw.githubusercontent.com/vcuspinera/UDG_MCD_Project_Dev_II/main/final_exam/Equipo_1/Grafico_3.png">

4. **¿Cuáles son aquellos 3 riesgos que más impactan en la variabilidad de la fecha de terminación? Explique a detalle en función del gráfico que soporta su respuesta.**  

Al obtener el diagrama de tornado correspondiente tenemos:

<img src="https://raw.githubusercontent.com/vcuspinera/UDG_MCD_Project_Dev_II/main/final_exam/Equipo_1/Grafico_4.png">

Por consiguiente, los tres componentes de riesgo que impactan más en la variabilidad de la fecha de entrega son:
1)	Tener personal inadecuado
2)	Disponibilidad de materiales
3)	Permiso de registro

Entre todos ellos, suman un total del 79.7% de la variabilidad (lo cual de acuerdo a la regla de Pareto representa el 80% que se captura en casi el 20% del total desplegado en la lista).


5. **¿Qué tan probable es que la Fase 2 tarde menos de 40 días?**  

La probabilidad de que la fase 2 tarde menos de 40 días es del 88.5%, de acuerdo al histograma de frecuencias de la salida asociada a esta variable, como se puede ver a continuación:

<img src="https://raw.githubusercontent.com/vcuspinera/UDG_MCD_Project_Dev_II/main/final_exam/Equipo_1/Grafico_5.png">

6. **¿Qué fue lo que más le gustó de este curso?, ¿qué fue lo que menos le gustó?, y ¿qué mejoras sugiere hacer para que este curso sea más enriquecedor en la formación de quienes cursen esta maestría?**

Lo que más nos gustó del curso fue la flexibilidad por parte del profesor para responder dudas y compartir su conocimiento en diversas áreas. Siempre hubo una actitud positiva al trabajo en equipo, lo cual favoreció el aprendizaje. Asimismo, la opción de puntos extras fue una idea excelente, que desafortunadamente muy pocos supieron aprovechar.

En lo referente a lo que menos nos gustó podemos mencionar las prórrogas de último minuto y cambios en fechas de entrega, derivadas del poco trabajo que algunos tuvieron a lo largo del curso. No es culpa del profesor que en muchos casos no se asistía a clase o se hacía caso omiso a las indicaciones sobre @RISK para estar a la par con lo que se estaba explicando. 

Recomendacion: Creemos que debería existir mayor exigencia en ese sentido.

