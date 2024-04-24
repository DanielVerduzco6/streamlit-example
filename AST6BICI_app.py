import streamlit as st

# Portada principal
st.write("# **Análisis de series temporales**")
st.write("## **Actividad: Estadísticas descriptivas**")
st.write("**Estudiante: Verduzco Valencia Daniel Alejandro**")
st.write("**Profesor: Mata Lopez Walter Alexander**")
st.write("**6.-B**")
st.write("**Ingeniería en Computación Inteligente**")
st.write("**Universidad de Colima**")
st.write("**FIME**")
st.write("**12/04/2024**")
st.image("https://www.ucol.mx/content/cms/41/image/escudos.png", use_column_width=True)

# Menú desplegable para acceder a las actividades
actividad = st.selectbox("Seleccione una actividad:", ["Actividad 1", "Actividad 2", "Actividad 3", "Actividad 4"])

if actividad == "Actividad 1":
    st.write('### Código 1: Estadísticas descriptivas')
    # Aquí va el código 1
elif actividad == "Actividad 2":
    st.write('### Código 2: Tarea de patrones')
    # Aquí va el código 2
elif actividad == "Actividad 3":
    st.write('### Código 3: Tarea de Anomalías')
    # Aquí va el código 3
elif actividad == "Actividad 4":
    st.write('### Código 4: Análisis de Estacionariedad de una Serie Temporal')
    # Aquí va el código 4
