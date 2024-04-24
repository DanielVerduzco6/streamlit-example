import streamlit as st
import streamlit as st
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

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
    
    st.write("## Código para generar los datos de salarios anuales:")
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
    
    st.write("### 3. Resultados de las estadísticas descriptivas:")
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

    # Diagrama de Caja de Salarios
    plt.figure(figsize=(8, 6))
    plt.boxplot(salarios, vert=False)
    plt.xlabel('Salarios')
    plt.title('Diagrama de Caja de Salarios')
    plt.grid()
    plt.show()

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

    # Análisis de las estadísticas descriptivas
    st.write("**Análisis de las estadísticas descriptivas:**")
    
    st.write("1. Media y Mediana:")
    st.write("- La media de los salarios es de 49,604.0, lo que nos dice el salario promedio de los empleados.")
    st.write("- La mediana de los salarios es de 50,000.0, lo que nos dice el salario central cuando los salarios se ordenan de menor a mayor.")
    st.write("Ya que la media y la mediana son cercanas en este caso, sugiere que la distribución de los salarios es relativamente simétrica y no está sesgada hacia valores extremos. Esto nos dice que la mayoría de los salarios se encuentran al rededor de estos valores centrales.")
    
    st.write("2. Moda:")
    st.write("- La moda de los salarios es de 52,000.0 y aparece 10 veces en los datos. Esto nos dice que 52,000.0 es el salario más común entre los empleados.")
    
    st.write("3. Varianza y Desviación Estándar:")
    st.write("- La varianza de los salarios es de 278,327,184.0 y la desviación estándar es de aproximadamente 16,683.14.")
    st.write("Una varianza alta y una desviación estándar considerable indican que los salarios están dispersos alrededor de la media. En este caso, los salarios no están agrupados cerca de la media, sino que muestran una dispersión alta. Esto nos dice que hay una variabilidad alta en los salarios de los empleados.")

    # 4. Informe
    st.write("#### Informe:")
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
elif actividad == "Actividad 3":
    st.write('### Código 3: Tarea de Anomalías')
    # Aquí va el código 3
elif actividad == "Actividad 4":
    st.write('### Código 4: Análisis de Estacionariedad de una Serie Temporal')
    # Aquí va el código 4
