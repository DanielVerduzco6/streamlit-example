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

    # Generar datos de salarios anuales (simulados)
    np.random.seed(1783)
    salarios = np.random.normal(loc=50000, scale=15000, size=250)
    salarios = np.round(salarios, -3)
    
    # Asegurarse de que todos los salarios sean positivos
    salarios = np.abs(salarios)
    
    # Mostrar los salarios generados
    st.write("## Datos de salarios anuales generados:")
    st.write(salarios)



















elif actividad == "Actividad 2":
    st.write('### Código 2: Tarea de patrones')
    # Aquí va el código 2
elif actividad == "Actividad 3":
    st.write('### Código 3: Tarea de Anomalías')
    # Aquí va el código 3
elif actividad == "Actividad 4":
    st.write('### Código 4: Análisis de Estacionariedad de una Serie Temporal')
    # Aquí va el código 4
