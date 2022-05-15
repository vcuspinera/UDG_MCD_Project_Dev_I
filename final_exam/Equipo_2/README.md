# Reporte de resultados #

## Información del equipo

Materia: Desarrollo de Proyectos II

Número de Equipo: 2

Integrantes:  Mónica Alonso, Mario Palomino

## Descripción del problema

El problema que se resuelve es del de responder a unas preguntas de costo y duración de un proyecto de lanzamiento de un producto. La idea principal es utilizar una herramienta que genere en forma automática el diagrama de Gantt complementado con el uso de @Risk para hacer el análisis de las variables de costo total del proyecto, la duración del mismo y el impacto que se tiene al considerar una lista de riesgos con efectos negativos.  A grandes rasgos el proyecto se divide en tres fases: 1) Planeación, 2) Iniciación y preparación, y 3) Lanzamiento a fabricación en las cuales se utilizan recursos cuyo costo unitario es por día (por ejemplo, Marketing o Ventas), además de utilizar recursos de costo fijo (Servicio de campo, Director de producto).

La técnica de @Risk para arrojar estimaciones de las variables en el proyecto está basada en ejecutar un número "grande" de veces un experimento que tiene como puntos de entrada (naturalmente) a los valores del proyecto como lo es el caso de la duración y el costo, seguidas por distribuciones estadísticas que simulan el comportamiento de tales valores para terminar en un resultado a manera de gráfica en las que se pueden manipular rangos de intervalos de confianza o probabilidades de una manera sencilla para responder a las preguntas regulares de duración o costo.  En nuestro problema particular se utilizarán las distribuciones de tipo uniforme, normal y pert para analizar las tareas de las fases 1, 2, y 3, respectivamente. 

## Preguntas/Respuestas

Con base en la información y experimento ejecutado en @Risk con 10,000 simulaciones se obtuvieron las siguientes respuestas:

**1. ¿Cuál es la fecha estimada y costo de terminación para dicho lanzamiento, asumiendo que las cosas salen de acuerdo a lo planeado (sin variaciones) y laborando de lunes a viernes?  Elabore un diagrama de Gantt que muestre la planifiación de este proyecto de manera detallada.**


**2. ¿Cuál es el riesgo de no terminar al 15 de septiembre del 2022 cuando consideramos los riesgos y variaciones expuestas anteriormente?**


**3. Proporcione un intervalo del 95% para el costo de todo el proyecto.**


**4. ¿Cuáles son aquellos 3 fiestos que más impactan en la variabilidad de la fecha de terminación? Explique a detalle en función del gráfico que soporta su respuesta.**


**5. ¿Qué tan probable es que la fase 2 tarde menos de 40 días?**


**6. ¿Qué fue lo que más le gustó del curso?, ¿qúe fue lo que menos le gusto?, ¿mejoras?**


