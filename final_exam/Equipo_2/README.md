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

La duración de las tareas y la dependencia entre ellas arroja que el proyecto tarda 40 días en completarse con un costo de $104,300 en el entendido que no existen variaciones para este caso. Los cálculos detallados se encuentran en la hoja “Project tasks”.  
* Inicio de proyecto	Julio 1, 2022   
* Fin de proyecto		Agosto 25, 2022   
* Días entre semana	40   
* Costo			$104,900   


**2. ¿Cuál es el riesgo de no terminar al 15 de septiembre del 2022 cuando consideramos los riesgos y variaciones expuestas anteriormente?**  
Parámetros del experimento   
•	10k simulaciones con 100 iteraciones cada una    
•	Distribuciones por tarea    
•	Riesgos     
Utilizar la celda de duración total para visualizar su distribución y manualmente definir un intervalo 55 días (tomar en cuenta que la duración sin variación son 40 días y que de la fecha de terminación es Agosto 25) al poner los extremos en la duración mínima y el día 55.  Esto arroja que la probabilidad de extenderse más allá del Septiembre 15 es del 8%.   

*Figura utilizada para obtención de resultado*    

   ![image](https://user-images.githubusercontent.com/58093652/168514247-eafca6bc-2574-4b01-8ab7-a320ebdb45b9.png)

**3. Proporcione un intervalo del 95% para el costo de todo el proyecto.**   
Parámetros del experimento:   
•	10k simulaciones con 100 iteraciones cada una   
•	Distribuciones por tarea   
•	Riesgos      

Utilizar la celda de costo total para visualizar su distribución y manualmente definir un intervalo del 95% al poner los extremos a una probabilidad de 2.5% cada uno.  Esto arroja límites de costo de 102 y 129 mil para el intervalo pedido del 95%.        

*Figura utilizada para obtención de resultado*

![image](https://user-images.githubusercontent.com/58093652/168514348-666b2232-4cdc-4e37-a82f-07b2ac4cb1cd.png)


**4. ¿Cuáles son aquellos 3 riesgos que más impactan en la variabilidad de la fecha de terminación? Explique a detalle en función del gráfico que soporta su respuesta.**   
Parámetros del experimento     
•	10k simulaciones con 100 iteraciones cada una    
•	Distribuciones por tarea    
•	Riesgos     

Utilizar la celda del total de total de impacto por riesgos para visualizar su distribución y seleccionar el análisis de como el impacto contribuye a la varianza teniendo como resultado que los tres riesgos que más contribuyen a la varianza total son Personal inadecuada, Disponibilidad de materiales, Permiso de registro con porcentajes de 49%, 35% y 11% aproximadamente.            
 
*Figura utilizada para obtención de resultado*   

![image](https://user-images.githubusercontent.com/58093652/168514414-0d8487f7-2e97-4214-82c3-d3206c15b758.png)


**5. ¿Qué tan probable es que la fase 2 tarde menos de 40 días?**   
Una solución es definir el total de días con riesgos y variaciones para la fase 2 y visualizar su distribución, pero revisando las tareas de tal fase se tiene que durante 10 días con solo 3 tareas que contribuyen a la ruta crítica (marcadas en rojo en la hoja de Excel) que pueden variar +/- 2 días y que no se ven afectadas por los riesgos de tal forma que con estos números siempre cae en una duración de menos de 40 días.     


**6. ¿Qué fue lo que más le gustó del curso?, ¿qúe fue lo que menos le gusto?, ¿mejoras?**     
*lo que más*  
- Github , el contenido fue muy didáctico
- Omdena, se podría llevar un proyecto a la par con la materia en lugar de quizes y controles de lectura 

*Lo que menos*
- Demasiada memorización de términos del PMBOK que si bien son importantes, el reforzamiento es tedioso y abrumador
- Mucho enfoque téorico y poco práctico, tal vez alguna dinámica con metodologías ágiles ayudaría
- El sistema de administración de información, es más fácil utilizar algo centralizado como classroom que dropbox + slack + github




