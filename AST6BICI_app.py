# %% [markdown]
# <div align="center">
# 
# # **Analisis de series temporales**
# 
# ## **Actividad: Análisis de Estacionariedad de una Serie Temporal**
# 
# **Estudiante: Verduzco Valencia Daniel Alejandro**
# 
# **Profeso: Mata Lopez Walter Alexander**
# 
# **6.-B**
# 
# **Ingenieria en Computacion Inteligente**  
# **Universidad de Colima**  
# **FIME**
# 
# **22/04/2024**
# 
# ![Logo de la Universidad de Colima](https://www.ucol.mx/content/cms/41/image/escudos.png)
# </div>

# %% [markdown]
# ### Análisis de Estacionariedad de una Serie Temporal
# 
# Se tiene un conjunto de datos que representa la temperatura media mensual de una ciudad a lo largo de varios años. La serie de tiempo ha mostrado fluctuaciones que podrían ser tanto estacionales como tendenciales.
# 
# Datos:
# 
# Los datos se van a generar mediante el siguiente código en Python, que simula la temperatura media mensual en grados Celsius a lo largo de 10 años con una tendencia y estacionalidad anual:

# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
t = np.arange(120)
data = 20 + 0.05 * t + 10 * np.sin(2 * np.pi * t / 12) + np.random.normal(size=120)
serie_temporal = pd.Series(data, index=pd.date_range(start='2010-01-01', periods=120, freq='M'))


# %% [markdown]
# Actividades:
# 
# 1. Visualización de la Serie Temporal: Grafica la serie temporal completa y determina visualmente si muestra estacionalidad, tendencia o ambas. Escribe tus observaciones
# 
# 2. Transformaciones: Aplica una transformación de diferenciación a la serie para intentar hacerla estacionaria. Grafica la serie original y la serie transformada en el mismo gráfico para compararlas.
# 
# 3. Pruebas de Estacionariedad: Realiza la prueba de Dickey-Fuller aumentada (ADF) para la serie original y la serie transformada. Interpreta los resultados de las pruebas. Explica si alguna de las series (original o transformada) puede considerarse estacionaria según los resultados de las pruebas.
# 
# Entrega:
# Deberás entregar un informe que incluya:
# - Código utilizado para las transformaciones y pruebas.
# - Gráficos generados.
# - Análisis y explicaciones de cada paso.
# - Conclusiones sobre la estacionariedad de la serie y la efectividad de las transformaciones aplicadas.

# %% [markdown]
# #### Paso 1:
# 
# 1. Visualización de la Serie Temporal: Grafica la serie temporal completa y determina visualmente si muestra estacionalidad, tendencia o ambas. Escribe tus observaciones

# %%
# Graficar la serie temporal
plt.figure(figsize=(10, 6))
serie_temporal.plot()
plt.title('Serie Temporal de Temperatura Mensual')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.show()

# %%
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


# %% [markdown]
# ##### Interpretación de la gráfica
# 
# Analizando visualmente la gráfica, podemos observar claramente que existe una estacionalidad y tendencia. Esto se debe a que se aprecia un patrón oscilante repetitivo a lo largo de la serie de tiempo. Asimismo, podemos observar que esta misma oscilación sigue una tendencia, que inicia en el año 2010 con valores aproximados que van desde 12°C a 32.5°C, y aumenta hasta valores aproximados de 16°C a 36°C para finales de 2018 e inicios de 2019. Esto indica que la tendencia de la temperatura a través de esta serie de tiempo es ascendente.
# 

# %% [markdown]
# #### Paso 2:
# 
# 2. Transformaciones: Aplica una transformación de diferenciación a la serie para intentar hacerla estacionaria. Grafica la serie original y la serie transformada en el mismo gráfico para compararlas.

# %%
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


# %% [markdown]
# #### Interpretación de la gráfica:
# 
# Podemos observar cómo la gráfica ha sido transformada a una serie temporal estacionaria, lo que muestra valores medios estables y no crecientes o decrecientes en comparación con la gráfica original. Esta última muestra valores de temperatura crecientes a lo largo de la serie de tiempo.
# 

# %% [markdown]
# #### Paso 3:
# 3. Pruebas de Estacionariedad: Realiza la prueba de Dickey-Fuller aumentada (ADF) para la serie original y la serie transformada. Interpreta los resultados de las pruebas. Explica si alguna de las series (original o transformada) puede considerarse estacionaria según los resultados de las pruebas.

# %%
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





# %% [markdown]
# ##### Interpretación de las gráficas y conclusiones
# 
# Podemos observar cómo en la primera gráfica, que es la original, no puede ser categorizada como estacionaria debido a las características que presentan los datos en ella al seguir una estacionalidad y tendencia a lo largo de la serie temporal.
# 
# Por otro lado, podemos observar la segunda gráfica en la que se ha transformado la serie de tiempo a estacionaria, eliminando así las tendencias y ciclos estacionales para poder mantener valores constantes a lo largo de la serie de tiempo.
# 
# Esto es importante, ya que gracias a que se ha transformado la serie temporal inicialmente no estacionaria a estacionaria, las predicciones en dicha serie de tiempo ahora pueden ser menos sesgadas y más exactas.
# 


