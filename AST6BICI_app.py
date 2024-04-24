import streamlit as st
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Portada principal
st.title('Análisis de series temporales')
st.header('Compendio de tareas y ejercicios')
st.write("Estudiante: Verduzco Valencia Daniel Alejandro")
st.write("Profesor: Mata López Walter Alexander")
st.write("6-B")
st.write("Ingeniería en Computación Inteligente")
st.write("Universidad de Colima")
st.write("FIME")
st.write("2024")

# Botones para acceder a los códigos
if st.button('Parcial 1 y 2'):
    st.write('### Código 1: Estadísticas descriptivas')
    # Código 1: Estadísticas descriptivas
    st.markdown("""
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
    """)
    st.markdown("## Problema")
    st.markdown("Contexto: Una empresa desea realizar un análisis estadístico de los salarios anuales de sus empleados. El propósito de este análisis es obtener una mejor comprensión de la distribución de los ingresos entre los empleados, lo que permitirá a la empresa tomar decisiones informadas respecto a la equidad salarial y la estructura de compensaciones.")
    st.markdown("Objetivo: Como parte de un proyecto de análisis de datos, se te ha asignado la tarea de calcular las estadísticas descriptivas básicas de los salarios anuales en la empresa. Específicamente, deberás calcular la media, mediana, moda, varianza y desviación estándar de los salarios. Además, deberás interpretar estas estadísticas para discutir la equidad salarial y la dispersión de los salarios.")
    st.markdown("## Instrucciones")
    st.markdown("### 1. Generar Datos")
    st.markdown("Utiliza el siguiente código en Python para generar una muestra aleatoria de salarios anuales. Esta muestra simulará los salarios anuales de los empleados de la empresa.")
    
    # Generar datos de salarios anuales (simulados)
    np.random.seed(1783)
    salarios = np.random.normal(loc=50000, scale=15000, size=250)
    salarios = np.round(salarios, -3)
    salarios = np.abs(salarios)
    
    st.markdown("### 2. Calcular Estadísticas Descriptivas")
    st.markdown("Calcula la media, mediana, moda, varianza y desviación estándar de los salarios generados. Puedes usar las librerías numpy para media, mediana, varianza y desviación estándar, y scipy.stats o statistics para la moda.")
    
    # media, mediana, moda, varianza y desviación estándar de los salarios
    media_salarios = np.mean(salarios)
    mediana_salarios = np.median(salarios)
    moda_salarios = stats.mode(salarios)
    varianza_salarios = np.var(salarios)
    desviacion_estandar_salarios = np.std(salarios)
    
    st.write("Media de los salarios:", media_salarios)
    st.write("Mediana de los salarios:", mediana_salarios)
    st.write("Moda de los salarios:", moda_salarios.mode)
    st.write("La moda aparece", moda_salarios.count, "veces")
    st.write("Varianza de los salarios:", varianza_salarios)
    st.write("Desviación estándar de los salarios:", desviacion_estandar_salarios)
    
    st.markdown("### Gráficas")
    # Histograma
    fig_hist, ax_hist = plt.subplots(figsize=(10, 6))
    ax_hist.hist(salarios, bins=15, color='g', edgecolor='black', alpha=0.7)
    ax_hist.axvline(media_salarios, color='r', linestyle='dashed', linewidth=1.5, label='Media')
    ax_hist.axvline(mediana_salarios, color='b', linestyle='dashed', linewidth=1.5, label='Mediana')
    ax_hist.set_xlabel('Salarios')
    ax_hist.set_ylabel('Frecuencia')
    ax_hist.set_title('Distribución de Salarios Anuales')
    ax_hist.legend()
    ax_hist.grid(True)
    st.pyplot(fig_hist)
    
    # Diagrama de Caja de Salarios
    fig_box, ax_box = plt.subplots(figsize=(8, 6))
    ax_box.boxplot(salarios, vert=False)
    ax_box.set_xlabel('Salarios')
    ax_box.set_title('Diagrama de Caja de Salarios')
    ax_box.grid()
    st.pyplot(fig_box)
    
    # Gráfico de Dispersión con Líneas de Media y Desviación Estándar
    media = 49604.0
    desviacion_estandar = 16683.14071150873
    fig_disp, ax_disp = plt.subplots(figsize=(10, 6))
    ax_disp.plot(salarios, 'o', label='Salarios') # Puntos de los salarios
    ax_disp.axhline(media, color='r', linestyle='-', label=f'Media: {media:.2f}') # Línea de la media
    ax_disp.axhline(media + desviacion_estandar, color='g', linestyle='--', label=f'+1 Desv. Est.: {media + desviacion_estandar:.2f}')
    ax_disp.axhline(media - desviacion_estandar, color='g', linestyle='--', label=f'-1 Desv. Est.: {media - desviacion_estandar:.2f}')
    ax_disp.set_title('Dispersión de los Salarios')
    ax_disp.set_xlabel('Índice de empleado')
    ax_disp.set_ylabel('Salarios')
    ax_disp.legend()
    ax_disp.grid(True)
    st.pyplot(fig_disp)

elif st.button('Parcial 3'):
    pass  # Agrega el código del parcial 3 aquí
