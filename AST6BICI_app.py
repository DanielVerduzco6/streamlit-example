import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from statsmodels.tsa.stattools import adfuller

def parte_1_tarea_anomalias():
    # Código 3: Tarea de Anomalías
    
    # Inserta aquí el código de la Tarea de Anomalías
    
    pass

def parte_2_analisis_estacionariedad():
    # Código 4: Análisis de Estacionariedad de una Serie Temporal
    
    # Inserta aquí el código del Análisis de Estacionariedad
    
    pass

def portada_principal():
    # Portada principal
    
    st.title("Análisis de series temporales")
    st.header("Compendio de tareas y ejercicios")
    st.write("Estudiante: Verduzco Valencia Daniel Alejandro")
    st.write("Profesor: Mata López Walter Alexander")
    st.write("6-B")
    st.write("Ingeniería en Computación Inteligente")
    st.write("Universidad de Colima - FIME")
    st.write("2024")
    
    # Botones para acceder a cada parte del análisis
    if st.button("Parcial 1 y 2"):
        st.write("## Parcial 1 y 2")
        st.write("### Tarea de Anomalías")
        parte_1_tarea_anomalias()
        st.write("### Análisis de Estacionariedad de una Serie Temporal")
        parte_2_analisis_estacionariedad()
    if st.button("Parcial 3"):
        st.write("## Parcial 3")
        # Agrega aquí el código para el Parcial 3, si lo hay

if __name__ == "__main__":
    portada_principal()

