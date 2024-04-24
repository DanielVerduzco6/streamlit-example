import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from statsmodels.tsa.stattools import adfuller

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
    
    # Generar datos
    np.random.seed(0)
    data = np.random.normal(0, 1, 1000)
    df = pd.DataFrame(data, columns=['Valores'])
    
    # Descripción de los datos
    st.write('**Descripción de los datos:**')
    st.write(df.describe())
    
    # Histograma
    st.write('**Histograma:**')
    fig, ax = plt.subplots()
    ax.hist(df['Valores'], bins=30, color='blue', alpha=0.7)
    ax.set_xlabel('Valor')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)
    
    st.write('### Código 2: Tarea de patrones')
    # Código 2: Tarea de patrones
    
    # Generar datos
    np.random.seed(0)
    tiempo = np.linspace(0, 10, 100)
    seno = np.sin(tiempo)
    coseno = np.cos(tiempo)
    
    # Gráfica de los patrones
    st.write('**Gráfica de los patrones:**')
    fig, ax = plt.subplots()
    ax.plot(tiempo, seno, label='Seno')
    ax.plot(tiempo, coseno, label='Coseno')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Valor')
    ax.legend()
    st.pyplot(fig)
    
elif st.button('Parcial 3'):
    st.write('### Código 3: Tarea de Anomalías')
    # Código 3: Tarea de Anomalías
    
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
    st.write('**Gráfica de temperaturas y anomalías:**')
    plt.figure(figsize=(15, 6))
    plt.plot(df_temperaturas['Fecha'], df_temperaturas['Temperaturas'], label='Temperaturas')
    plt.scatter(df_temperaturas.loc[df_temperaturas['Anomaly'], 'Fecha'], df_temperaturas.loc[df_temperaturas['Anomaly'], 'Temperaturas'], color='red', label='Anomalía', marker='x', s=100) # Marcar anomalías con una X roja
    plt.xlabel('Fecha')
    plt.ylabel('Temperatura')
    plt.title('Lecturas de Temperatura con Anomalía Detectada')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    
    st.write('### Código 4: Análisis de Estacionariedad de una Serie Temporal')
    # Código 4: Análisis de Estacionariedad de una Serie Temporal
    
    # Generar datos
    np.random.seed(0)
    t = np.arange(120)
    data = 20 + 0.05 * t + 10 * np.sin(2 * np.pi * t / 12) + np.random.normal(size=120)
    serie_temporal = pd.Series(data, index=pd.date_range(start='2010-01-01', periods=120, freq='M'))
    
    # Visualización de la Serie Temporal
    st.write('**Visualización de la Serie Temporal:**')
    plt.figure(figsize=(10, 6))
    serie_temporal.plot()
    plt.title('Serie Temporal de Temperatura Mensual')
    plt.xlabel('Fecha')
    plt.ylabel('Temperatura (°C)')
    plt.grid(True)
    st.pyplot(plt)
    
    # Transformaciones
    st.write('**Transformaciones:**')
    st.write('Aplica una transformación de diferenciación a la serie para intentar hacerla estacionaria.')
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
    st.pyplot(plt)
    
    # Pruebas de Estacionariedad
    st.write('**Pruebas de Estacionariedad:**')
    st.write('Realiza la prueba de Dickey-Fuller aumentada (ADF) para la serie original y la serie transformada.')
    
    # Aplicar prueba ADF a la serie temporal
    resultado = adfuller(serie_temporal)
    st.write('Serie Temporal')
    st.write('Estadístico ADF:', resultado[0])
    st.write('Valor p:', resultado[1])
    if resultado[1] < 0.05:
        st.write('La serie temporal es estacionaria.')
    else:
        st.write('La serie temporal no es estacionaria.')
    
    # Aplicar prueba ADF a la serie transformada
    resultado = adfuller(serie_transformada)
    st.write('Serie Transformada')
    st.write('Estadístico ADF:', resultado[0])
    st.write('Valor p:', resultado[1])
    if resultado[1] < 0.05:
        st.write('La serie transformada es estacionaria.')
    else:
        st.write('La serie transformada no es estacionaria.')

