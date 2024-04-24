import streamlit as st

# Portada principal
st.title('Análisis de Series Temporales')
st.header('Compendio de tareas y ejercicios')
st.subheader('Estudiante: Verduzco Valencia Daniel Alejandro')
st.subheader('Profesor: Mata López Walter Alexander')
st.subheader('6-B')
st.subheader('Ingeniería en Computación Inteligente')
st.subheader('Universidad de Colima')
st.subheader('FIME')
st.subheader('2024')

# Botones para acceder a los parciales
if st.button('Parcial 1 y 2'):
    st.header('Parcial 1 y 2')
    st.subheader('Código 1: Tarea de Anomalías')
    st.code("""
    # Aquí va el código de la Tarea de Anomalías
    """, language='python')

    st.subheader('Código 2: Análisis de Estacionariedad de una Serie Temporal')
    st.code("""
    # Aquí va el código de Análisis de Estacionariedad de una Serie Temporal
    """, language='python')

if st.button('Parcial 3'):
    st.header('Parcial 3')
    st.subheader('Código 3: Tarea de Anomalías')
    st.code("""
    # Aquí va el código de la Tarea de Anomalías
    """, language='python')

    st.subheader('Código 4: Análisis de Estacionariedad de una Serie Temporal')
    st.code("""
    # Aquí va el código de Análisis de Estacionariedad de una Serie Temporal
    """, language='python')
