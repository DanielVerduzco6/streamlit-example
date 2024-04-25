import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.ensemble import IsolationForest
from statsmodels.tsa.stattools import adfuller

# Portada principal
st.write("# **Análisis de series temporales**")
st.write("## **Compendio de actividades y ejercicios**")
st.write("**Estudiante: Verduzco Valencia Daniel Alejandro**")
st.write("**Profesor: Mata Lopez Walter Alexander**")
st.write("**6.-B**")
st.write("**Ingeniería en Computación Inteligente**")
st.write("**Universidad de Colima**")
st.write("**FIME**")
st.write("**26/04/2024**")
st.image("https://www.ucol.mx/content/cms/41/image/escudos.png", use_column_width=True)

# Menú desplegable para acceder a las actividades
actividad = st.selectbox("Seleccione una actividad:", ["Actividad 1", "Actividad 2", "Actividad 3", "Actividad 4"])

if actividad == "Actividad 1":
    st.write('### Código 1: Estadísticas descriptivas')
    # Aquí va el código 1

    st.markdown("""
    <div align="center">
        
    # **Análisis de series temporales**
    
    ## **Actividad: Estadísticas descriptivas**
    
    **Estudiante: Verduzco Valencia Daniel Alejandro**
    
    **Profesor: Mata Lopez Walter Alexander**
    
    **6.-B**
    
    **Ingeniería en Computación Inteligente**  
    **Universidad de Colima**  
    **FIME**
    
    **12/04/2024**
    
    ![Logo de la Universidad de Colima](https://www.ucol.mx/content/cms/41/image/escudos.png)
    </div>
    """, unsafe_allow_html=True)

    # Problema
    st.write("## Problema")
    st.write("Contexto: Una empresa desea realizar un análisis estadístico de los salarios anuales de sus empleados. El propósito de este análisis es obtener una mejor comprensión de la distribución de los ingresos entre los empleados, lo que permitirá a la empresa tomar decisiones informadas respecto a la equidad salarial y la estructura de compensaciones.")
    
    st.write("Objetivo: Como parte de un proyecto de análisis de datos, se te ha asignado la tarea de calcular las estadísticas descriptivas básicas de los salarios anuales en la empresa. Específicamente, deberás calcular la media, mediana, moda, varianza y desviación estándar de los salarios. Además, deberás interpretar estas estadísticas para discutir la equidad salarial y la dispersión de los salarios.")
    
    # Instrucciones
    st.write("#### Instrucciones")
    st.write("#### 1. Generar Datos:")
    st.write("Utiliza el siguiente código en Python para generar una muestra aleatoria de salarios anuales. Esta muestra simulará los salarios anuales de los empleados de la empresa.")
    
    st.code("""
    import numpy as np
    from scipy import stats
    import matplotlib.pyplot as plt
    
    # Generar datos de salarios anuales (simulados)
    np.random.seed(1783)
    salarios = np.random.normal(loc=50000, scale=15000, size=250)
    salarios = np.round(salarios, -3)
    
    # Asegurarse de que todos los salarios sean positivos
    salarios = np.abs(salarios)
    
    print(salarios)
    """)
    
    # Generar datos de salarios anuales (simulados)
    np.random.seed(1783)
    salarios = np.random.normal(loc=50000, scale=15000, size=250)
    salarios = np.round(salarios, -3)
    
    # Asegurarse de que todos los salarios sean positivos
    salarios = np.abs(salarios)
    
    # Mostrar los salarios generados
    st.write("## Datos de salarios anuales generados:")
    st.write(list(salarios))


    st.write("### 2. Calcular Estadísticas Descriptivas:")
    st.write("- Calcula la media, mediana, moda, varianza y desviación estándar de los salarios generados.")
    st.write("- Puedes usar las librerías numpy para media, mediana, varianza y desviación estándar, y scipy.stats o statistics para la moda.")
    st.code("""
        # media, mediana, moda, varianza y desviación estándar de los salarios
        media_salarios = np.mean(salarios)
        mediana_salarios = np.median(salarios)
        moda_salarios = stats.mode(salarios)
        varianza_salarios = np.var(salarios)
        desviacion_estandar_salarios = np.std(salarios)
        
        print("Media de los salarios:", media_salarios)
        print("Mediana de los salarios:", mediana_salarios)
        print("Moda de los salarios:", moda_salarios.mode)
        print("La moda aparece", moda_salarios.count, "veces")
        print("Varianza de los salarios:", varianza_salarios)
        print("Desviación estándar de los salarios:", desviacion_estandar_salarios)
    """)
    # media, mediana, moda, varianza y desviación estándar de los salarios
    media_salarios = np.mean(salarios)
    mediana_salarios = np.median(salarios)
    moda_salarios = stats.mode(salarios)
    varianza_salarios = np.var(salarios)
    desviacion_estandar_salarios = np.std(salarios)
    
    st.write("- Media de los salarios:", media_salarios)
    st.write("- Mediana de los salarios:", mediana_salarios)
    st.write("- Moda de los salarios:", moda_salarios.mode)
    st.write(f"- La moda aparece {moda_salarios.count} veces")
    st.write("- Varianza de los salarios:", varianza_salarios)
    st.write("- Desviación estándar de los salarios:", desviacion_estandar_salarios)

    st.code("""
        # Crear la gráfica
        st.write("### 5. Gráfico de la distribución de Salarios Anuales:")
        st.pyplot(plt.figure(figsize=(15, 6)))
        # Histograma de los salarios
        plt.hist(salarios, bins=15, color='g', edgecolor='black', alpha=0.7)
        plt.axvline(media_salarios, color='r', linestyle='dashed', linewidth=1.5, label='Media')
        plt.axvline(mediana_salarios, color='b', linestyle='dashed', linewidth=1.5, label='Mediana')
        plt.xlabel('Salarios')
        plt.ylabel('Frecuencia')
        plt.title('Distribución de Salarios Anuales')
        plt.legend()
        plt.grid(True)
    """)
    # Crear la gráfica dentro de un contexto de Streamlit
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.hist(salarios, bins=15, color='g', edgecolor='black', alpha=0.7)
    ax.axvline(media_salarios, color='r', linestyle='dashed', linewidth=1.5, label='Media')
    ax.axvline(mediana_salarios, color='b', linestyle='dashed', linewidth=1.5, label='Mediana')
    ax.set_xlabel('Salarios')
    ax.set_ylabel('Frecuencia')
    ax.set_title('Distribución de Salarios Anuales')
    ax.legend()
    ax.grid(True)
    
    # Mostrar la gráfica en Streamlit
    st.pyplot(fig)
#########################################################3


    # 3. Interpretar los Resultados
    st.write("### 3. Interpretar los Resultados:")
    
    st.write("- Discute qué te indican la media y la mediana sobre la tendencia central de los salarios.")
    st.write("- Analiza la moda y qué dice sobre los salarios más comunes dentro de la empresa.")
    st.write("- Interpreta la varianza y la desviación estándar en términos de dispersión de los salarios. ¿Los salarios están agrupados cerca de la media o dispersos?")
    
    st.code("""
        # Diagrama de Caja de Salarios
        plt.figure(figsize=(8, 6))
        plt.boxplot(salarios, vert=False)
        plt.xlabel('Salarios')
        plt.title('Diagrama de Caja de Salarios')
        plt.grid()
        plt.show()
    """)

    # Crear la gráfica dentro de un contexto de Streamlit
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.boxplot(salarios, vert=False)
    ax.set_xlabel('Salarios')
    ax.set_title('Diagrama de Caja de Salarios')
    ax.grid()
    
    # Mostrar la gráfica en Streamlit
    st.pyplot(fig)


    st.code("""
        # Gráfico de Dispersión con Líneas de Media y Desviación Estándar
        media = 49604.0
        desviacion_estandar = 16683.14071150873
        
        plt.figure(figsize=(10, 6))
        plt.plot(salarios, 'o', label='Salarios') # Puntos de los salarios
        plt.axhline(media, color='r', linestyle='-', label=f'Media: {media:.2f}') # Línea de la media
        plt.axhline(media + desviacion_estandar, color='g', linestyle='--', label=f'+1 Desv. Est.: {media + desviacion_estandar:.2f}')
        plt.axhline(media - desviacion_estandar, color='g', linestyle='--', label=f'-1 Desv. Est.: {media - desviacion_estandar:.2f}')
        plt.title('Dispersión de los Salarios')
        plt.xlabel('Índice de empleado')
        plt.ylabel('Salarios')
        plt.legend()
        plt.grid(True)
        plt.show()
    """)

    # Crear la gráfica dentro de un contexto de Streamlit
    media = 49604.0
    desviacion_estandar = 16683.14071150873
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(salarios, 'o', label='Salarios') # Puntos de los salarios
    ax.axhline(media, color='r', linestyle='-', label=f'Media: {media:.2f}') # Línea de la media
    ax.axhline(media + desviacion_estandar, color='g', linestyle='--', label=f'+1 Desv. Est.: {media + desviacion_estandar:.2f}')
    ax.axhline(media - desviacion_estandar, color='g', linestyle='--', label=f'-1 Desv. Est.: {media - desviacion_estandar:.2f}')
    ax.set_title('Dispersión de los Salarios')
    ax.set_xlabel('Índice de empleado')
    ax.set_ylabel('Salarios')
    ax.legend()
    ax.grid(True)
    
    # Mostrar la gráfica en Streamlit
    st.pyplot(fig)

    # Análisis de las estadísticas descriptivas
    st.write("**Análisis de las estadísticas descriptivas:**")
    
    st.write("1. Media y Mediana:")
    st.write("- La media de los salarios es de 49,604.0, lo que nos dice el salario promedio de los empleados.")
    st.write("- La mediana de los salarios es de 50,000.0, lo que nos dice el salario central cuando los salarios se ordenan de menor a mayor.")
    st.write("- Ya que la media y la mediana son cercanas en este caso, sugiere que la distribución de los salarios es relativamente simétrica y no está sesgada hacia valores extremos. Esto nos dice que la mayoría de los salarios se encuentran al rededor de estos valores centrales.")
    
    st.write("2. Moda:")
    st.write("- La moda de los salarios es de 52,000.0 y aparece 10 veces en los datos. Esto nos dice que 52,000.0 es el salario más común entre los empleados.")
    
    st.write("3. Varianza y Desviación Estándar:")
    st.write("- La varianza de los salarios es de 278,327,184.0 y la desviación estándar es de aproximadamente 16,683.14.")
    st.write("- Una varianza alta y una desviación estándar considerable indican que los salarios están dispersos alrededor de la media. En este caso, los salarios no están agrupados cerca de la media, sino que muestran una dispersión alta. Esto nos dice que hay una variabilidad alta en los salarios de los empleados.")

    # 4. Informe
    st.write("#### 4. Informe:")
    st.write("- Escribe un informe breve que incluya los cálculos realizados, las gráficas pertinentes (como histogramas o gráficos de cajas), y una discusión sobre las implicaciones de estas estadísticas en términos de equidad salarial y política de remuneraciones de la empresa.")

    # Informe sobre Análisis de Salarios Anuales
    st.write("**Informe sobre Análisis de Salarios Anuales**")
    st.write("")
    st.write("En este informe, se presenta un análisis estadístico de los salarios anuales de los empleados. Se calcularon medidas descriptivas como la media, mediana, moda, varianza y desviación estándar para comprender la distribución de los salarios y discutir su equidad salarial.")
    st.write("")
    st.write("**Resultados y Análisis**")
    st.write("Cálculos Realizados:")
    st.write("")
    st.write("Media de los salarios: 49,604.0")
    st.write("Mediana de los salarios: 50,000.0")
    st.write("Moda de los salarios: 52,000.0")
    st.write("Varianza de los salarios: 278,327,184.0")
    st.write("Desviación estándar de los salarios: 16,683.14")
    st.write("")
    st.write("**Discusión:**")
    st.write("La media de los salarios indica el valor promedio de compensación en la empresa, mientras que la mediana representa el salario central, siendo menos sensible a valores extremos. La moda señala el salario más común entre los empleados. La varianza y la desviación estándar reflejan la dispersión de los salarios alrededor de la media, indicando si los salarios están agrupados cerca de la media o dispersos.")
    st.write("")
    st.write("**Implicaciones y Recomendaciones:**")
    st.write("En base a las estadísticas obtenidas y los graficos analizados los salarios no son muy equitativos entre el personal de la empresa, por lo que se sugiere revisar la equidad salarial dentro de la empresa para garantizar una distribución justa de compensaciones.")










elif actividad == "Actividad 2":
    st.write('### Código 2: Tarea de patrones')
    # Aquí va el código 2

    st.markdown("""
    <div align="center">
        
    # **Análisis de series temporales**
    
    ## **Actividad: Tarea de patrones**
    
    **Estudiante: Verduzco Valencia Daniel Alejandro**
    
    **Profesor: Mata Lopez Walter Alexander**
    
    **6.-B**
    
    **Ingeniería en Computación Inteligente**  
    **Universidad de Colima**  
    **FIME**
    
    **19/04/2024**
    
    ![Logo de la Universidad de Colima](https://www.ucol.mx/content/cms/41/image/escudos.png)
    </div>
    """, unsafe_allow_html=True)

    # Problema
    st.write("## Problema de identificación de patrones en datos de ventas mensuales")
    # Instrucciones
    st.write("#### Instrucciones")
    st.write("En una empresa de venta al por menor, se ha recopilado un conjunto de datos que registra las ventas mensuales de varios productos durante un periodo de varios años. Tu tarea es analizar estos datos para identificar posibles patrones o tendencias en las ventas mensuales.")
    st.write("#### Parte 1: Generación de Datos:")
    st.write("Utiliza un programa en Python para generar datos simulados que representen las ventas mensuales de varios productos a lo largo de un período de tiempo. Los datos deben incluir al menos 3 productos diferentes y abarcar un periodo de al menos 3 años.")
    st.write("#### Parte 2: Análisis de Datos")
    st.write("Una vez que hayas generado los datos, realiza un análisis para identificar posibles patrones en las ventas mensuales. Algunas preguntas que podrías explorar incluyen:")
    st.write("- ¿Hay algún patrón estacional en las ventas de ciertos productos?")
    st.write("- ¿Se observa alguna tendencia de crecimiento o decrecimiento en las ventas a lo largo del tiempo?")
    st.write("- ¿Existen meses específicos en los que las ventas tienden a ser más altas o más bajas?")
    st.write("#### Parte 3: Informe de Resultados")
    st.write("Escribe un informe que resuma tus hallazgos. Incluye gráficos o visualizaciones que ayuden a ilustrar los patrones identificados en los datos. Además, discute cualquier insight o conclusión que hayas obtenido del análisis de los datos.")
    st.write("Entrega tu programa de Python (o libreta de Jupyter) junto con el informe de resultados. Asegúrate de incluir comentarios en tu código para explicar cada paso del proceso de análisis y cómo se generaron los datos.")

    st.code("""
        import pandas as pd
        import numpy as np
        from statsmodels.tsa.seasonal import seasonal_decompose
        
        # Definir los productos y el rango de tiempo
        productos = ['Short deportivo p/u', 'Camisa deportiva p/u', 'Teniss deportivos p/u']
        fechas = pd.date_range(start='1/1/2021', end='31/12/2023', freq='M')
        
        # Crear un DataFrame vacío
        df = pd.DataFrame()
        
        # Generar datos para cada producto
        for producto in productos:
            ventas = np.random.randint(50, 200, size=len(fechas))  # Generar ventas aleatorias entre 50 y 200
            temp_df = pd.DataFrame({'Fecha': fechas, 'Producto': producto, 'Ventas': ventas})
            df = pd.concat([df, temp_df])
        
        # Restablecer el índice del DataFrame
        df.reset_index(drop=True, inplace=True)
        
        # Mostrar las primeras filas del DataFrame
        print(df)
    """)

    # Definir los productos y el rango de tiempo
    productos = ['Short deportivo p/u', 'Camisa deportiva p/u', 'Teniss deportivos p/u']
    fechas = pd.date_range(start='1/1/2021', end='31/12/2023', freq='M')
    
    # Crear un DataFrame vacío
    df = pd.DataFrame()
    
    # Generar datos para cada producto
    for producto in productos:
        ventas = np.random.randint(50, 200, size=len(fechas))  # Generar ventas aleatorias entre 50 y 200
        temp_df = pd.DataFrame({'Fecha': fechas, 'Producto': producto, 'Ventas': ventas})
        df = pd.concat([df, temp_df])
    
    # Restablecer el índice del DataFrame
    df.reset_index(drop=True, inplace=True)
    
    # Mostrar las primeras filas del DataFrame
    st.write("### Mostrar filas del DataFrame:")
    st.write(df)

    st.code("""
        import matplotlib.pyplot as plt
        from statsmodels.tsa.seasonal import seasonal_decompose
        
        # Convertir la columna 'Fecha' a datetime
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        
        # Reestructurar el DataFrame
        df_pivot = df.pivot(index='Fecha', columns='Producto', values='Ventas')
        
        # Limitar el DataFrame al rango de fechas especificado
        df_pivot = df_pivot.loc['2021-01-01':'2023-12-31']
        
        # Descomponer las series de tiempo para cada producto
        for producto in df_pivot.columns:
            print(f"\nDescomposición de la serie de tiempo para {producto}:")
            result = seasonal_decompose(df_pivot[producto].dropna(), model='additive')
            
            # Graficar los datos originales, la tendencia, la estacionalidad y los residuos
            plt.figure(figsize=(12,8))
            plt.subplot(411)
            plt.plot(result.observed, label='Original')
            plt.legend(loc='best')
            plt.subplot(412)
            plt.plot(result.trend, label='Trend')
            plt.legend(loc='best')
            plt.subplot(413)
            plt.plot(result.seasonal,label='Seasonality')
            plt.legend(loc='best')
            plt.subplot(414)
            plt.plot(result.resid, label='Residuals')
            plt.legend(loc='best')
            plt.tight_layout()
            plt.show()
    """)


    # Definir los productos y el rango de tiempo
    productos = ['Short deportivo p/u', 'Camisa deportiva p/u', 'Teniss deportivos p/u']
    fechas = pd.date_range(start='1/1/2021', end='31/12/2023', freq='M')
    
    # Crear un DataFrame vacío
    df = pd.DataFrame()
    
    # Generar datos para cada producto
    for producto in productos:
        ventas = np.random.randint(50, 200, size=len(fechas))  # Generar ventas aleatorias entre 50 y 200
        temp_df = pd.DataFrame({'Fecha': fechas, 'Producto': producto, 'Ventas': ventas})
        df = pd.concat([df, temp_df])
    
    # Restablecer el índice del DataFrame
    df.reset_index(drop=True, inplace=True)
    
    # Convertir la columna 'Fecha' a datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    # Reestructurar el DataFrame
    df_pivot = df.pivot(index='Fecha', columns='Producto', values='Ventas')
    
    # Limitar el DataFrame al rango de fechas especificado
    df_pivot = df_pivot.loc['2021-01-01':'2023-12-31']
    
    # Descomponer las series de tiempo para cada producto
    for producto in df_pivot.columns:
        st.write(f"\nDescomposición de la serie de tiempo para {producto}:")
        result = seasonal_decompose(df_pivot[producto].dropna(), model='additive')
        
        # Graficar los datos originales, la tendencia, la estacionalidad y los residuos
        fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(12,8))
        
        axes[0].plot(result.observed, label='Original')
        axes[0].legend(loc='best')
        axes[1].plot(result.trend, label='Trend')
        axes[1].legend(loc='best')
        axes[2].plot(result.seasonal,label='Seasonality')
        axes[2].legend(loc='best')
        axes[3].plot(result.resid, label='Residuals')
        axes[3].legend(loc='best')
        
        fig.tight_layout()
        st.pyplot(fig)

    st.write("""
        #### Parte 2 y 3
        
        Parte 2: Análisis de Datos
        
        Una vez que hayas generado los datos, realiza un análisis para identificar posibles patrones en las ventas mensuales. Algunas preguntas que podrías explorar incluyen:
        
        - ¿Hay algún patrón estacional en las ventas de ciertos productos? Sí (se argumenta en el análisis de patrones de ventas mensuales)
        - ¿Se observa alguna tendencia de crecimiento o decrecimiento en las ventas a lo largo del tiempo? Sí (se argumenta en el análisis de patrones de ventas mensuales)
        - ¿Existen meses específicos en los que las ventas tienden a ser más altas o más bajas? Sí (se argumenta en el análisis de patrones de ventas mensuales)
        
        
        Parte 3: Informe de Resultados
        
        Escribe un informe que resuma tus hallazgos. Incluye gráficos o visualizaciones que ayuden a ilustrar los patrones identificados en los datos. Además, discute cualquier insight o conclusión que hayas obtenido del análisis de los datos.
        
        
        ##### Análisis de patrones en las ventas mensuales y resumen de hallazgos.
        
        1. Camisa deportiva:
        
            Para las camisas deportivas, podemos observar que tenemos 4 gráficas diferentes. La primera es la gráfica Original, que muestra la cantidad de unidades de camisas deportivas registradas como vendidas al final de cada mes a lo largo de 3 años, que comprenden las fechas del 2021-01-01 al 2023-12-31.
        
            La segunda gráfica es Trend o tendencia, que plasma el aumento o decremento en las ventas a lo largo del tiempo. Podemos observar en este caso que a lo largo del año 2021 hubo una disminución importante en la venta de este producto entre los meses de septiembre y octubre, para después volver a tener una pequeña alza en las ventas y cerrar este año con un número de ventas cercano al de inicios de año. De igual manera, podemos observar un importante aumento en las ventas que comprenden de enero a diciembre del año 2022, teniendo una muy pequeña caída entre los meses de octubre y noviembre, pero logró en diciembre volver a repuntar y cerrar el año con mayores ventas que el año anterior. Mientras que en el año 2023 parece haber iniciado con una pequeña caída para después tener un alza en las ventas y alrededor de los meses de septiembre y octubre tener un decremento en ventas para que al finalizar el año vuelva a tener un alza en ventas.
        
            La tercera gráfica, que es la estacional, podemos observar claramente cómo hay patrones en las ventas de este producto, siendo los meses de febrero a julio los meses en que más se vende este producto, mientras que en los meses de agosto a noviembre e inicios de año con enero son los meses en los que menos se vende este producto.
        
            La cuarta gráfica, que es la residual, podemos observar que no hay patrón aparente y la naturaleza de la gráfica parece ser aleatoria. Esto nos dice que la descomposición de la serie temporal ha capturado adecuadamente la tendencia y la estacionalidad en los datos, y que los residuos representan la variación aleatoria en las ventas de camisas deportivas.
        
        
        2. Short deportivo:
        
            Para los shorts deportivos, podemos observar que tenemos 4 gráficas diferentes. La primera es la gráfica Original, que muestra la cantidad de unidades de shorts deportivos registrados como vendidos al final de cada mes a lo largo de 3 años, que comprenden las fechas del 2021-01-01 al 2023-12-31.
        
            La segunda gráfica, Trend o tendencia, que plasma el aumento o decremento de las ventas a lo largo del tiempo, podemos observar en este caso que alrededor de julio a diciembre del 2021 hubo una importante disminución en las ventas de este producto. El año 2022 no fue diferente en este aspecto, ya que de igual manera tuvo una importante disminución en las ventas, siendo los meses de octubre a noviembre los que tuvieron registradas menores ventas. De igual manera, el año 2023 empezó una pequeña alza para después volver a caer en ventas en el mes de mayo para así volver a repuntar en ventas.
        
            En la tercera gráfica, que es la estacional, podemos observar claramente cómo hay patrones en las ventas de este producto, siendo los meses de marzo y abril los que registran un muy pequeño alza en las ventas para después caer en mayo y volver a tener un pequeño alza en los meses de junio y julio para nuevamente volver a caer en el mes de agosto y tener un repunte en los meses de septiembre a diciembre, empezando cada año con una pequeña caída.
        
            La cuarta gráfica, que es la residual, podemos observar que no hay patrón aparente y la naturaleza de la gráfica parece ser aleatoria. Esto nos dice que la descomposición de la serie temporal ha capturado adecuadamente la tendencia y la estacionalidad en los datos, y que los residuos representan la variación aleatoria en las ventas de shorts deportivos.
        
        
        3. Tennis deportivos:
        
            Para los tenis deportivos, podemos observar que igualmente tenemos 4 gráficas diferentes. La primera es la gráfica Original, que muestra la cantidad de unidades de tenis deportivos registrados como vendidos al final de cada mes a lo largo de 3 años, que comprenden las fechas del 2021-01-01 al 2023-12-31.
        
            La segunda gráfica, Trend o tendencia, que plasma el aumento o decremento de las ventas a lo largo del tiempo, nos muestra a lo largo del mes de julio a diciembre del 2021 un pequeño aumento en las ventas de este producto, para después tener un aumento bastante exponencial en los meses de enero a octubre del 2022 para después tener un pequeño descenso en las ventas del producto entre los meses de noviembre a julio del 2023.
        
            En la tercera gráfica, que es la estacional, podemos observar claramente cierto patrón en el mes de mayo, que según la gráfica es el mes en el cual más ventas registra este producto, mientras que los meses de junio a octubre son los que parecen presentar menos ventas.
        
            La cuarta gráfica, que es la residual, podemos observar que no hay patrón aparente y la naturaleza de la gráfica parece ser aleatoria. Esto nos dice que la descomposición de la serie temporal ha capturado adecuadamente la tendencia y la estacionalidad en los datos, y que los residuos representan la variación aleatoria en las ventas de tenis deportivos.
            
    """)
            
     












elif actividad == "Actividad 3":
    st.write('### Código 3: Tarea de Anomalías')
    # Aquí va el código 3
    st.markdown("""
    <div align="center">
        
    # **Análisis de series temporales**
    
    ## **Actividad: Tarea de anomalias**
    
    **Estudiante: Verduzco Valencia Daniel Alejandro**
    
    **Profesor: Mata Lopez Walter Alexander**
    
    **6.-B**
    
    **Ingeniería en Computación Inteligente**  
    **Universidad de Colima**  
    **FIME**
    
    **19/04/2024**
    
    ![Logo de la Universidad de Colima](https://www.ucol.mx/content/cms/41/image/escudos.png)
    </div>
    """, unsafe_allow_html=True)

    # Problema
    st.write("## Problema para la detección de anomalías en sensores de temperatura en una planta de manufactura")
    # Instrucciones
    st.write("#### Instrucciones")
    st.write("En una planta de manufactura, se utilizan sensores para monitorear la temperatura en diferentes partes de la línea de producción. Estos sensores registran lecturas de temperatura cada hora durante un periodo de varios meses. Tu tarea es analizar estos datos para identificar posibles anomalías en las lecturas de temperatura que puedan indicar problemas en el proceso de fabricación o fallos en los equipos.")
    st.write("#### Parte 1: Generación de Datos:")
    st.write("Utiliza un programa en Python para generar datos simulados que representen las lecturas de temperatura de los sensores durante varios meses. Los datos deben incluir una variedad de lecturas normales, así como algunas lecturas anómalas que simulen problemas en el proceso de fabricación o fallos en los equipos.")
    st.write("#### Parte 2: Análisis de Datos")
    st.write("Una vez que hayas generado los datos, realiza un análisis para identificar posibles anomalías en las lecturas de temperatura. Algunas preguntas que podrías explorar incluyen:")
    st.write("- ¿Existen lecturas de temperatura que se desvíen significativamente del rango esperado para esa área de la planta?")
    st.write("- ¿Hay algún patrón o tendencia en las lecturas anómalas?")
    st.write("- ¿Qué características tienen las lecturas anómalas en comparación con las lecturas normales?")
    st.write("#### Parte 3: Informe de Resultados")
    st.write("Escribe un informe que resuma tus hallazgos. Incluye gráficos o visualizaciones que ayuden a identificar las anomalías en los datos de temperatura. Además, discute cualquier insight o conclusión que hayas obtenido del análisis de los datos y cómo podrían utilizarse para mejorar el mantenimiento preventivo o la eficiencia en la planta de manufactura.")

    st.code("""
            import pandas as pd
            import numpy as np
            import matplotlib.pyplot as plt
            from sklearn.ensemble import IsolationForest
            
            # Generar datos
            np.random.seed(0)
            horas = pd.date_range(start='2024-01-01', end='2024-04-01', freq='H')
            temperaturas = np.random.normal(loc=20, scale=2, size=len(horas)) # Lecturas de temperatura normales
            
            # Introducir anomalías
            indices_anomalos = np.random.choice(range(len(horas)), size=50, replace=False)
            temperaturas[indices_anomalos] += np.random.normal(loc=10, scale=2, size=len(indices_anomalos)) # Hacer las anomalías significativamente más grandes
            
            # Crear DataFrame
            df_temperaturas = pd.DataFrame({'Fecha': horas, 'Temperaturas': temperaturas})
            
            # Utilizar Isolation Forest para detectar anomalías
            iso_forest = IsolationForest(contamination=0.02) # Suponemos que aproximadamente el 2% de los datos son anomalías
            anomalies = iso_forest.fit_predict(df_temperaturas[['Temperaturas']])
            df_temperaturas['Anomaly'] = anomalies == -1
            
            # Gráfica de temperaturas y anomalías
            plt.figure(figsize=(15, 6))
            plt.plot(df_temperaturas['Fecha'], df_temperaturas['Temperaturas'], label='Temperaturas')
            plt.scatter(df_temperaturas.loc[df_temperaturas['Anomaly'], 'Fecha'], df_temperaturas.loc[df_temperaturas['Anomaly'], 'Temperaturas'], color='red', label='Anomalía', marker='x', s=100) # Marcar anomalías con una X roja
            plt.xlabel('Fecha')
            plt.ylabel('Temperatura')
            plt.title('Lecturas de Temperatura con Anomalía Detectada')
            plt.legend()
            
            plt.grid(True)
            plt.show()
    """)
    # Generar datos
    np.random.seed(0)
    horas = pd.date_range(start='2024-01-01', end='2024-04-01', freq='H')
    temperaturas = np.random.normal(loc=20, scale=2, size=len(horas))  # Lecturas de temperatura normales
    
    # Introducir anomalías
    indices_anomalos = np.random.choice(range(len(horas)), size=50, replace=False)
    temperaturas[indices_anomalos] += np.random.normal(loc=10, scale=2, size=len(indices_anomalos))  # Hacer las anomalías significativamente más grandes
    
    # Crear DataFrame
    df_temperaturas = pd.DataFrame({'Fecha': horas, 'Temperaturas': temperaturas})
    
    # Utilizar Isolation Forest para detectar anomalías
    iso_forest = IsolationForest(contamination=0.02)  # Suponemos que aproximadamente el 2% de los datos son anomalías
    anomalies = iso_forest.fit_predict(df_temperaturas[['Temperaturas']])
    df_temperaturas['Anomaly'] = anomalies == -1
    
    # Configuración de Streamlit
    st.write("### Lecturas de Temperatura con Anomalía Detectada")
    
    # Gráfico interactivo de temperaturas y anomalías
    st.line_chart(df_temperaturas.set_index('Fecha'))

    st.code("""
        #Valores de temperatura noramales
        q1 = df_temperaturas['Temperaturas'].quantile(0.25)
        q3 = df_temperaturas['Temperaturas'].quantile(0.75)
        iqr = q3 - q1
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
        
        print("El rango normal de temperaturas es de", limite_inferior, "a", limite_superior)
    """)
    # Valores de temperatura normales
    q1 = df_temperaturas['Temperaturas'].quantile(0.25)
    q3 = df_temperaturas['Temperaturas'].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    
    st.write("### Rango normal de temperaturas:")
    st.write(f"El rango normal de temperaturas es de {limite_inferior} a {limite_superior}")

    st.code("""
        #Total de anomalías
        print("\nEl total de anómalas encontradas son: ", df_temperaturas['Anomaly'].sum())
    """)

    # Total de anomalías
    total_anomalias = df_temperaturas['Anomaly'].sum()
    
    st.write("### Total de anomalías encontradas:")
    st.write(f"El total de anomalías encontradas es: {total_anomalias}")

    st.code("""
        # Agregar columna de 'Mes'
        df_temperaturas['Mes'] = df_temperaturas['Fecha'].dt.month
        
        
        # Agrupar por 'Mes' y sumar 'Anomaly'
        anomalias_por_mes = df_temperaturas.groupby('Mes')['Anomaly'].sum()
        anomalias_por_mes = anomalias_por_mes.drop(4) # No hay datos para el mes 4
        
        # Gráfica de anomalías por mes
        plt.figure(figsize=(10, 6))
        anomalias_por_mes.plot(kind='bar')
        plt.xlabel('Mes')
        plt.ylabel('Cantidad de Anomalías')
        plt.title('Cantidad de Anomalías por Mes')
        plt.grid(True)
        plt.show()
    """)

    # Agregar columna de 'Mes'
    df_temperaturas['Mes'] = df_temperaturas['Fecha'].dt.month
    
    # Agrupar por 'Mes' y sumar 'Anomaly'
    anomalias_por_mes = df_temperaturas.groupby('Mes')['Anomaly'].sum()
    anomalias_por_mes = anomalias_por_mes.drop(4)  # No hay datos para el mes 4
    
    # Gráfica de anomalías por mes
    st.write("### Cantidad de Anomalías por Mes")
    plt.figure(figsize=(10, 6))
    anomalias_por_mes.plot(kind='bar')
    plt.xlabel('Mes')
    plt.ylabel('Cantidad de Anomalías')
    plt.title('Cantidad de Anomalías por Mes')
    plt.grid(True)
    st.pyplot(plt)


    st.write("""
        #### Parte 2 y 3
        
        Parte 2: Análisis de Datos
        
        Una vez que hayas generado los datos, realiza un análisis para identificar posibles anomalías en las lecturas de temperatura. Algunas preguntas que podrías explorar incluyen:
        - ¿Existen lecturas de temperatura que se desvíen significativamente del rango esperado para esa área de la planta? **Sí**, podemos observar una superior a 40.
        - ¿Hay algún patrón o tendencia en las lecturas anómalas? **No**.
        - ¿Qué características tienen las lecturas anómalas en comparación con las lecturas normales? Las lecturas anómalas tienen muchos menos datos en comparación con las lecturas normales y suelen ser valores extremadamente altos o bajos.
        
        Parte 3: Informe de Resultados
        
        Escribe un informe que resuma tus hallazgos. Incluye gráficos o visualizaciones que ayuden a identificar las anomalías en los datos de temperatura. Además, discute cualquier insight o conclusión que hayas obtenido del análisis de los datos y cómo podrían utilizarse para mejorar el mantenimiento preventivo o la eficiencia en la planta de manufactura.
        
        ##### Análisis de los resultados
        
        Como podemos observar, los datos de temperatura generados a lo largo de la serie de tiempo corresponden a los primeros 3 meses del año 2024, donde consideramos los valores 14.55 a 25.47 como valores de temperatura normales para el área correspondiente en la planta de manufactura. Por mes, podemos observar la cantidad de ocurrencias de temperaturas anómalas. En el primer mes, que corresponde a Enero, tenemos 16 temperaturas anómalas; para Febrero, tenemos 17 temperaturas anómalas contabilizadas; y para Marzo, 11.
        
        Al graficar los datos, podemos observar que hay ciertos valores que corresponden a valores de temperatura que, según el área en el que están, se clasifican como anómalos. De estos valores anómalos, tenemos 44, los cuales no parecen seguir un patrón o tendencia, salvo que por mes superan mas de los 10 casos.
            
    """)






elif actividad == "Actividad 4":
    st.write('### Código 4: Análisis de Estacionariedad de una Serie Temporal')
    # Aquí va el código 4

    st.markdown("""
    <div align="center">
        
    # **Análisis de series temporales**
    
    ## **Actividad: Análisis de Estacionariedad de una Serie Temporal**
    
    **Estudiante: Verduzco Valencia Daniel Alejandro**
    
    **Profesor: Mata Lopez Walter Alexander**
    
    **6.-B**
    
    **Ingeniería en Computación Inteligente**  
    **Universidad de Colima**  
    **FIME**
    
    **22/04/2024**
    
    ![Logo de la Universidad de Colima](https://www.ucol.mx/content/cms/41/image/escudos.png)
    </div>
    """, unsafe_allow_html=True)

    # Problema
    st.write("### Análisis de Estacionariedad de una Serie Temporal")
    st.write("Se tiene un conjunto de datos que representa la temperatura media mensual de una ciudad a lo largo de varios años. La serie de tiempo ha mostrado fluctuaciones que podrían ser tanto estacionales como tendenciales.")
    st.write("#### Datos:")
    st.write("Los datos se van a generar mediante el siguiente código en Python, que simula la temperatura media mensual en grados Celsius a lo largo de 10 años con una tendencia y estacionalidad anual:")
    st.code("""
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        
        np.random.seed(0)
        t = np.arange(120)
        data = 20 + 0.05 * t + 10 * np.sin(2 * np.pi * t / 12) + np.random.normal(size=120)
        serie_temporal = pd.Series(data, index=pd.date_range(start='2010-01-01', periods=120, freq='M'))
            
    """)

    # Generar datos
    np.random.seed(0)
    t = np.arange(120)
    data = 20 + 0.05 * t + 10 * np.sin(2 * np.pi * t / 12) + np.random.normal(size=120)
    serie_temporal = pd.Series(data, index=pd.date_range(start='2010-01-01', periods=120, freq='M'))

    st.write("""
        Actividades:
        
        1. Visualización de la Serie Temporal: Grafica la serie temporal completa y determina visualmente si muestra estacionalidad, tendencia o ambas. Escribe tus observaciones
        
        2. Transformaciones: Aplica una transformación de diferenciación a la serie para intentar hacerla estacionaria. Grafica la serie original y la serie transformada en el mismo gráfico para compararlas.
        
        3. Pruebas de Estacionariedad: Realiza la prueba de Dickey-Fuller aumentada (ADF) para la serie original y la serie transformada. Interpreta los resultados de las pruebas. Explica si alguna de las series (original o transformada) puede considerarse estacionaria según los resultados de las pruebas.
        
        Entrega:
        Deberás entregar un informe que incluya:
        - Código utilizado para las transformaciones y pruebas.
        - Gráficos generados.
        - Análisis y explicaciones de cada paso.
        - Conclusiones sobre la estacionariedad de la serie y la efectividad de las transformaciones aplicadas.
    
    """)

    st.write("#### Paso 1:")
    st.write("1. Visualización de la Serie Temporal: Grafica la serie temporal completa y determina visualmente si muestra estacionalidad, tendencia o ambas. Escribe tus observaciones")
    st.code("""
        # Graficar la serie temporal
        plt.figure(figsize=(10, 6))
        serie_temporal.plot()
        plt.title('Serie Temporal de Temperatura Mensual')
        plt.xlabel('Fecha')
        plt.ylabel('Temperatura (°C)')
        plt.grid(True)
        plt.show()
    """)

    # Gráfico de la serie temporal con Matplotlib
    plt.figure(figsize=(10, 6))
    serie_temporal.plot()
    plt.title('Serie Temporal de Temperatura Mensual')
    plt.xlabel('Fecha')
    plt.ylabel('Temperatura (°C)')
    plt.grid(True)
    st.pyplot(plt)  # Mostrar el gráfico en Streamlit

    st.code("""
        #Factor de suavizado
        alfa = 0.2
        serie_suavizada = serie_temporal.ewm(alpha=alfa).mean()
        
        #Vizualizar
        plt.figure(figsize=(10, 6))
        plt.plot(serie_temporal, label='Serie Temporal')
        plt.plot(serie_suavizada, label='Serie Suavizada', color='red')
        plt.title('Serie Temporal de Temperatura Mensual Suavizada')
        plt.xlabel('Fecha')
        plt.ylabel('Temperatura (°C)')
        plt.legend()
        plt.grid(True)
        plt.show()
    """)

    # Factor de suavizado
    alfa = 0.2
    serie_suavizada = serie_temporal.ewm(alpha=alfa).mean()
    
    # Gráfico de la serie temporal y suavizada con Matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(serie_temporal, label='Serie Temporal')
    plt.plot(serie_suavizada, label='Serie Suavizada', color='red')
    plt.title('Serie Temporal de Temperatura Mensual Suavizada')
    plt.xlabel('Fecha')
    plt.ylabel('Temperatura (°C)')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)  # Mostrar el gráfico en Streamlit

    st.write("##### Interpretación de la gráfica")
    st.write("Analizando visualmente la gráfica, podemos observar claramente que existe una estacionalidad y tendencia. Esto se debe a que se aprecia un patrón oscilante repetitivo a lo largo de la serie de tiempo. Asimismo, podemos observar que esta misma oscilación sigue una tendencia, que inicia en el año 2010 con valores aproximados que van desde 12°C a 32.5°C, y aumenta hasta valores aproximados de 16°C a 36°C para finales de 2018 e inicios de 2019. Esto indica que la tendencia de la temperatura a través de esta serie de tiempo es ascendente.")

    st.write("#### Paso 2:")
    st.write("2. Transformaciones: Aplica una transformación de diferenciación a la serie para intentar hacerla estacionaria. Grafica la serie original y la serie transformada en el mismo gráfico para compararlas.")
    st.code("""
        # Aplicar diferenciación primera a la serie temporal
        serie_transformada = serie_temporal.diff().dropna()
        
        # Graficar ambas series en el mismo gráfico
        plt.figure(figsize=(10, 6))
        serie_temporal.plot(label='Serie Original')
        serie_transformada.plot(label='Serie Transformada (Diferenciada)')
        plt.title('Comparación entre Serie Original y Serie Transformada')
        plt.xlabel('Fecha')
        plt.ylabel('Temperatura (°C)')
        plt.legend()
        plt.grid(True)
        plt.show()
    """)
    
    # Aplicar diferenciación primera a la serie temporal
    serie_transformada = serie_temporal.diff().dropna()
    
    # Gráfico de ambas series en el mismo gráfico
    plt.figure(figsize=(10, 6))
    serie_temporal.plot(label='Serie Original')
    serie_transformada.plot(label='Serie Transformada (Diferenciada)')
    plt.title('Comparación entre Serie Original y Serie Transformada')
    plt.xlabel('Fecha')
    plt.ylabel('Temperatura (°C)')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)  # Mostrar el gráfico en Streamlit

    st.write("#### Interpretación de la gráfica:")
    st.write("Podemos observar cómo la gráfica ha sido transformada a una serie temporal estacionaria, lo que muestra valores medios estables y no crecientes o decrecientes en comparación con la gráfica original. Esta última muestra valores de temperatura crecientes a lo largo de la serie de tiempo.")

    st.write("#### Paso 3:")
    st.write("3. Pruebas de Estacionariedad: Realiza la prueba de Dickey-Fuller aumentada (ADF) para la serie original y la serie transformada. Interpreta los resultados de las pruebas. Explica si alguna de las series (original o transformada) puede considerarse estacionaria según los resultados de las pruebas.")
    st.code("""
        from statsmodels.tsa.stattools import adfuller
        
        #Aplicar prueba ADF a la serie temporal
        resultado = adfuller(serie_temporal)
        print('Serie Temporal')
        print('Estadístico ADF:', resultado[0])
        print('Valor p:', resultado[1])
        
        #Interpretar el resultado basado en el valor p
        if resultado[1] < 0.05:
            print('La serie temporal es estacionaria.')
        else:
            print('La serie temporal no es estacionaria.')
        
        
        #Vizualizar la serie temporal
        plt.figure(figsize=(10, 6))
        plt.plot(serie_temporal, label='Serie Temporal')
        plt.title('Serie Temporal de Temperatura Mensual')
        plt.xlabel('Fecha')
        plt.ylabel('Temperatura (°C)')
        plt.legend()
        plt.grid(True)
        plt.show()
        
        
        #Aplicar prueba ADF a la serie transformada
        resultado = adfuller(serie_transformada)
        print('\n\nSerie Transformada')
        print('Estadístico ADF:', resultado[0])
        print('Valor p:', resultado[1])
        
        #Interpretar el resultado basado en el valor p
        if resultado[1] < 0.05:
            print('La serie transformada es estacionaria.')
        else:
            print('La serie transformada no es estacionaria.')
        
        
        #Vizualizar la serie transformada
        plt.figure(figsize=(10, 6))
        plt.plot(serie_transformada, label='Serie Transformada')
        plt.title('Serie Transformada de Temperatura Mensual')
        plt.xlabel('Fecha')
        plt.ylabel('Temperatura (°C)')
        plt.legend()
        plt.grid(True)
        plt.show()
    """)

    
    # Aplicar prueba ADF a la serie temporal
    resultado = adfuller(serie_temporal)
    st.write('### Serie Temporal')
    st.write('Estadístico ADF:', resultado[0])
    st.write('Valor p:', resultado[1])
    
    # Interpretar el resultado basado en el valor p
    if resultado[1] < 0.05:
        st.write('La serie temporal es estacionaria.')
    else:
        st.write('La serie temporal no es estacionaria.')
    
    # Visualizar la serie temporal
    plt.figure(figsize=(10, 6))
    plt.plot(serie_temporal, label='Serie Temporal')
    plt.title('Serie Temporal de Temperatura Mensual')
    plt.xlabel('Fecha')
    plt.ylabel('Temperatura (°C)')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)  # Mostrar el gráfico en Streamlit
    
    # Aplicar prueba ADF a la serie transformada
    resultado = adfuller(serie_transformada)
    st.write('\n\n### Serie Transformada')
    st.write('Estadístico ADF:', resultado[0])
    st.write('Valor p:', resultado[1])
    
    # Interpretar el resultado basado en el valor p
    if resultado[1] < 0.05:
        st.write('La serie transformada es estacionaria.')
    else:
        st.write('La serie transformada no es estacionaria.')
    
    # Visualizar la serie transformada
    plt.figure(figsize=(10, 6))
    plt.plot(serie_transformada, label='Serie Transformada')
    plt.title('Serie Transformada de Temperatura Mensual')
    plt.xlabel('Fecha')
    plt.ylabel('Temperatura (°C)')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)  # Mostrar el gráfico en Streamlit

    st.write("""
        ##### Interpretación de las gráficas y conclusiones
        
        Podemos observar cómo en la primera gráfica, que es la original, no puede ser categorizada como estacionaria debido a las características que presentan los datos en ella al seguir una estacionalidad y tendencia a lo largo de la serie temporal.
        
        Por otro lado, podemos observar la segunda gráfica en la que se ha transformado la serie de tiempo a estacionaria, eliminando así las tendencias y ciclos estacionales para poder mantener valores constantes a lo largo de la serie de tiempo.
        
        Esto es importante, ya que gracias a que se ha transformado la serie temporal inicialmente no estacionaria a estacionaria, las predicciones en dicha serie de tiempo ahora pueden ser menos sesgadas y más exactas.
        
    """)


