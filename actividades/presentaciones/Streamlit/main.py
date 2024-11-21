# Definimos las librerias que vamos a utilizar
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Definimos las páginas

# Página de inicio
def pagina_inicio():

    #Definimos el nombre de la seccíon
    st.session_state.selected_page = "Inicio"

    #Definimos el titulo del inicio
    st.markdown(
        """
        <div style="display: flex; align-items: center;">
            <h1 style="margin-right: 10px;">Gracias por visitarnos en consesionaria Piolín</h1>
            <img src="https://static-00.iconduck.com/assets.00/tesla-icon-512x512-50f00505.png" width="150" alt="Tesla Logo"/>
        </div>
        """,
        unsafe_allow_html=True
    )

    #Texto de bienvenida
    st.write("Bienvenido a la sección de Inicio. Aquí puedes encontrar información sobre nosotros.")

    #Texto, quienes somos
    st.write("### ¿Quiénes somos?")

    #Texto que explica quienes somos
    st.write("En Piolin, somos una concesionaria con 20 años de experiencia, dedicada a ofrecerte las mejores opciones en vehículos en Guadalajara, jalisco.\
              Nuestro compromiso es brindarte un servicio excepcional y asesoría personalizada para que encuentres el mejor automovil Tesla que se adapte a tus necesidades.\
              Con una amplia variedad de modelos, nos esforzamos por ser tu primera elección en el mundo automotriz.\
             ¡Te invitamos a visitarnos y descubrir todo lo que tenemos para ofrecerte!")

    # Ejemplo con código Markdown, 
    # En este momento, Magic solo funciona en el archivo principal de la aplicación Python, no en los archivos importados. 
    # Consulta el problema n.° 288 de GitHub para obtener una explicación de los problemas.

    '''
    #### Ubicacción 
    * Av. Vallarta 1515, federalismo, Guadalajara Jalisco.
    * Télefono: 333154896
    * Correo: cuca@cucea.mx
    * Horario de atención: 08:00 AM a 18:00 PM
    '''

    #Mapa de nuestra ubicación en Google Maps
    st.markdown(
        """
        <div style="text-align: right;">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d67032.07174609829!2d-103.43240567053282!3d20.69299205282504!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8428ae9224d6547b%3A0xaa04cbbd316bb96!2sAv.%20Ignacio%20L%20Vallarta%2C%20Jalisco!5e0!3m2!1ses-419!2smx!4v1730361740505!5m2!1ses-419!2smx" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )

# Página del modelo de Machine Learning
def ml_model():

    #Función para cargar el dataframe
    @st.cache_data
    def get_UN_data():
        #Importamos el dataset
        df = pd.read_csv("tesla_cars.csv")
        #Eliminamos los valores nulos
        df_limpio = df.dropna()
        #Retornamos el dataframe
        return df_limpio

    #Modelo de Machine Learning
    def ml(df_carros, ano, kilometraje, cuantos_choques_a_tenido, numero_puertas):

        # Seleccionamos las variables de entrada y salida
        x = df_carros[["ano","kilometraje","cuantos_choques_a_tenido","numero_puertas"]]
        y = df_carros["precio"]

        # Dividimos el dataset en datos de entrenamiento y de prueba
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

        # Creamos una instancia del objeto PolynomialFeatures con un grado de polinomio de 2
        poly = PolynomialFeatures(degree=2)

        # Transformamos los datos de entrada a un polinomio de segundo grado
        X_train_poly = poly.fit_transform(X_train)
        X_test_poly = poly.transform(X_test)

        # Entrenamos el modelo de regresión lineal
        lr = LinearRegression()
        lr.fit(X_train_poly, y_train)

        # Hacemos las predicciones en los datos de prueba
        y_pred = lr.predict(X_test_poly)

        # Calculamos el coeficiente de determinación R^2 para evaluar el modelo
        r2 = r2_score(y_test, y_pred)

        # Hacemos una predicción con los datos del modelo
        X_new = np.array([[ano, kilometraje, cuantos_choques_a_tenido, numero_puertas]])
        X_new_poly = poly.transform(X_new)
        y_new_pred = lr.predict(X_new_poly)

        return y_new_pred[0]

    # Cargamos el dataframe a una variable para su uso en el proyecto
    df_carros = get_UN_data()

    # Definimos el nombre de la seccíon
    st.session_state.selected_page = "Te compramos tu carro"

    #Texto Cotiza tu vehiculo aquí mismo
    st.write("### Te ayudamos a pronosticar el precio de tu vehiculo Tesla")

    st.write("Nuestro algoritmo de Machine Learning realizara la valoración con base a la información proporcionada por usted.")

    #Creamos el campo para seleccionar el modelo del vehiculo
    modelo = st.selectbox("Selecciona el modelo de tu vehiculo", list(df_carros["modelo"].unique()))

    #Creamos el campo para seleccionar el año del vehiculo
    ano = st.selectbox("Seleccione el año", list(df_carros["ano"].unique()))

    #Creamos el campo para seleccionar la transmision del vehiculo
    transmision = st.selectbox("Seleccione la transmision del vehiculo ", list(df_carros["transmision"].unique()))

    #Creamos el campo para que el usuario inserte el kilometraje
    kilometraje = st.number_input("Seleccione el kilometraje", min_value=0, step=1)

    #Creamos el campo para seleccionar la verison del carro
    version = st.selectbox("Seleccione la version del carro", list(df_carros["version"].unique()))

    #Creamos el campo para que el usuario inserte el número de choques que ha tenido el vehiculo
    cuantos_choques_a_tenido = st.number_input("Número de choques", min_value=0, step=1, format="%d")

    #Creamos el campo para que el usuario inserte el número de puertas que tiene el vehiculo
    numero_puertas = st.number_input("Número de puertas", min_value=2, max_value=4, step=2, format="%d")


    #Validamos si el usuario no selecciono ningun campo
    if not modelo:

        #Error en caso de que el usuario no seleccione una mara de vehiculo
        st.error("Por favor, seleccione un fabricante.")

    else:
        
        #Precio del dolar
        dolar = 16

        #Realizamos la predicción
        precio_estimado = ml(df_carros, ano, kilometraje, cuantos_choques_a_tenido, numero_puertas)
        
        #Texto Cotiza tu vehiculo aquí mismo
        st.write(f"### Precio estimado: ${precio_estimado * dolar:,.2f} MXN")

# Página del Inventario actual
def pagina_inventario():

    # Definimos el nombre de la seccíon
    st.session_state.selected_page = "Inventario"

    # Titulo del apartado
    st.header("Inventario Actual")

    # Cargamos el dataframe del inventario
    df_inventario = pd.read_csv("tesla_cars.csv")

    # Creamos el campo para seleccionar el modelo del vehiculo
    modelo = st.multiselect("Selecciona el modelo del vehiculo", list(df_inventario["modelo"].unique()), ["Model S"])

    # Creamos el campo para seleccionar el año del vehiculo
    ano = st.multiselect("Selecciona el año del vehiculo", list(df_inventario["ano"].unique()),[2023])

    # Validamos si el usuario no seleccione ningun campo
    if not modelo:

        # Error en caso de que el usuario no seleccione un vehiculo
        st.error("Por favor, seleccione un modelo de vehiculo.")

    # En caso de que el usuario seleccione el vehiculo
    else:

        # Validamos si el usuario no selecciono el año del vehiculo
        if not ano:

            # Filtramos los datos por los modelos y años seleccionados
            data_filtrada = df_inventario[df_inventario["modelo"].isin(modelo)]

            # Mostrar los precios de los carros seleccionados
            st.write("Precios de los vehículos seleccionados:")

            # Cambiamos el nombre de las columnas
            data = data_filtrada.rename(columns={
                'ano': 'Año',
                'modelo': 'Modelo',
                'transmision': 'Transmisión',
                'kilometraje': 'Kilometraje',
                'version': 'Versión',
                'numero_puertas': 'Número de Puertas',
                'precio': 'Precio'})

            # Si el dataframe esta vacio
            if data.empty:

                # Notifica al usuario que no contamos con el vehiculo que busca
                st.error("Por el momento no tenemos el modelo con las características que desea 😔")
                if st.button("¿Quieres preguntar si podemos conseguir el modelo?"):
                    st.session_state.selected_page = "Contacto"  # Cambiar la página en el estado de sesión
                    st.rerun()  # Forzar la actualización

            # En caso de que tengamos registros
            else:
                # Mostramos el dataframe al cliente
                st.dataframe(data[["Modelo","Año","Transmisión","Kilometraje","Versión","Número de Puertas","Precio"]])


        # En caso de que el usuario seleccione el año 
        else:

            # Filtramos los datos por los modelos y años seleccionados
            data_filtrada = df_inventario[df_inventario["modelo"].isin(modelo) & df_inventario["ano"].isin(ano)]

            # Mostrar los precios de los carros seleccionados
            st.write("Precios de los vehículos seleccionados:")

            # Cambiamos el nombre de las columnas
            data = data_filtrada.rename(columns={
                'ano': 'Año',
                'modelo': 'Modelo',
                'transmision': 'Transmisión',
                'kilometraje': 'Kilometraje',
                'version': 'Versión',
                'numero_puertas': 'Número de Puertas',
                'precio': 'Precio'})

            # Si el dataframe esta vacio
            if data.empty:

                # Notifica al usuario que no contamos con el vehiculo que busca
                st.error("Por el momento no tenemos el modelo con las características que desea 😔")
                if st.button("¿Quieres preguntar si podemos conseguir el modelo?"):
                    st.session_state.selected_page = "Contacto"  # Cambiar la página en el estado de sesión
                    st.rerun()  # Forzar la actualización
                
            # En caso de que tengamos registros
            else:
                # Mostramos el dataframe al cliente
                st.dataframe(data[["Modelo","Año","Transmisión","Kilometraje","Versión","Número de Puertas","Precio"]])

# Página del grafico     
def pagina_graficos():

    #Definimos el nombre de la seccíon
    st.session_state.selected_page = "Gráficos"

    #Leemos los datos del dataframe
    data = pd.read_csv("tesla_cars.csv")

    # Título del apartado
    st.title('Análisis de Datos de Autos Tesla')

    # Gráfico 1: Relación entre Kilometraje y Precio
    st.subheader("Relación entre Kilometraje y Precio")
    scatter_chart = alt.Chart(data).mark_point().encode(
        x='kilometraje',
        y='precio',
        color='modelo',
        tooltip=['marca', 'modelo', 'kilometraje', 'precio']
    ).properties(
        title="Relación entre Kilometraje y Precio"
    )
    st.altair_chart(scatter_chart, use_container_width=True)

    # Gráfico 2: Precio Promedio por Modelo
    st.subheader("Precio Promedio por Modelo")
    bar_chart = alt.Chart(data).mark_bar().encode(
        x='modelo',
        y='mean(precio):Q',
        color='modelo',
        tooltip=['modelo', 'mean(precio):Q']
    ).properties(
        title="Precio Promedio por Modelo"
    )
    st.altair_chart(bar_chart, use_container_width=True)

    # Gráfico 3: Distribución de Versiones por Modelo
    st.subheader("Distribución de Versiones por Modelo")
    stacked_bar_chart = alt.Chart(data).mark_bar().encode(
        x='modelo',
        y='count():Q',
        color='version',
        tooltip=['modelo', 'version', 'count():Q']
    ).properties(
        title="Distribución de Versiones por Modelo"
    )
    st.altair_chart(stacked_bar_chart, use_container_width=True)

    # Gráfico 4: Número de Choques vs Precio
    st.subheader("Número de Choques vs Precio")
    choques_price_chart = alt.Chart(data).mark_point().encode(
        x='cuantos_choques_a_tenido',
        y='precio',
        color='modelo',
        shape='modelo',
        tooltip=['marca', 'modelo', 'cuantos_choques_a_tenido', 'precio']
    ).properties(
        title="Número de Choques vs Precio"
    )
    st.altair_chart(choques_price_chart, use_container_width=True)

    # Gráfico 5: Evolución del Precio Promedio por Año
    st.subheader("Evolución del Precio Promedio por Año")
    line_chart = alt.Chart(data).mark_line().encode(
        x='ano:O',
        y='mean(precio):Q',
        color='modelo',
        tooltip=['ano', 'mean(precio):Q']
    ).properties(
        title="Evolución del Precio Promedio por Año"
    )
    st.altair_chart(line_chart, use_container_width=True)

    # Gráfico 6: Distribución de Número de Puertas por Modelo
    st.subheader("Distribución de Número de Puertas por Modelo")
    horizontal_bar_chart = alt.Chart(data).mark_bar().encode(
        y='modelo',
        x='count(numero_puertas):Q',
        color='numero_puertas',
        tooltip=['modelo', 'count(numero_puertas):Q']
    ).properties(
        title="Distribución de Número de Puertas por Modelo"
    )
    st.altair_chart(horizontal_bar_chart, use_container_width=True)

# Página para agendar una cita con la consecionaria
def pagina_contacto():

    # Definimos el nombre de la seccíon
    st.session_state.selected_page = "Contacto"  

    #Titulo del apartados
    st.header("Contacto")

    # Input de tipo texto
    # Nombre del cliente
    st.text_input("¿Cuál es tu nombre completo?", "Luis Carlos Su Sotelo")

    # Input de tipo date/calendario
    # Fecha de la cita
    d = st.date_input("¿Qué día te gustaría visitarnos?", datetime.date(2024, 11, 13))

    # Input de tipo time hora
    # Establecemos los límites
    hora_minima = datetime.time(8, 0)  # 8:00 AM
    hora_maxima = datetime.time(18, 0)  # 6:00 PM

    # Entrada de tiempo con valor predeterminado
    t = st.time_input("¿En qué horario te gustaría visitarnos?", value=datetime.time(8, 45))

    # Validamos si la hora seleccionada está dentro del rango permitido
    if t < hora_minima or t > hora_maxima:
        st.warning(f"Por favor, selecciona una hora entre {hora_minima} y {hora_maxima}.")
   
    # Input de tipo Text area
    # Establecemos los detalles
    st.text_area("¿Cuál es el motivo de la cita?", "Me gustaria agendar una cita con ustedes por que deseo vender mi auto Tesla model Y ....")

    # Casilla de verificación de Politicas y condiciones
    # Mostrar un checkbox con el texto "Estoy de acuerdo" y un enlace en Markdown
    st.markdown('Para terminos de calidad en el servicio, ¿estás de acuerdo con las [políticas y condiciones](https://www.example.com) de este sitio?')

    # Crear el checkbox
    agree = st.checkbox("Acepto los términos")


    # Estilo CSS para el botón
    st.markdown(
        """
        <style>
        .custom-button {
            background-color: #28a745; /* Color verde */
            color: white; /* Texto blanco */
            border: none; /* Sin borde */
            padding: 10px 20px; /* Espaciado interno */
            text-align: center; /* Centrado */
            text-decoration: none; /* Sin subrayado */
            display: inline-block; /* Mostrar como bloque en línea */
            font-size: 16px; /* Tamaño de fuente */
            margin: 4px 2px; /* Espaciado externo */
            cursor: pointer; /* Cursor de mano */
            border-radius: 5px; /* Bordes redondeados */
        }

        .custom-button:hover {
            background-color: #218838; /* Color más oscuro al pasar el mouse */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Botón personalizado
    st.markdown('<button class="custom-button">Reset</button>', unsafe_allow_html=True)

# Diccionario de páginas
paginas = {
    "Inicio": pagina_inicio,
    "Te compramos tu carro": ml_model,
    "Inventario": pagina_inventario,
    "Gráficos": pagina_graficos,
    "Contacto": pagina_contacto,
}


# Usamos st.session_state para recordar la página seleccionada
if 'selected_page' not in st.session_state:
    
    # Definimos la página inicial predeterminada
    st.session_state.selected_page = "Inicio"  


# Barra lateral para la navegación
opcion = st.sidebar.selectbox("Selecciona una sección:", list(paginas.keys()), index=list(paginas.keys()).index(st.session_state.selected_page))

# Llamar a la función correspondiente
paginas[opcion]()