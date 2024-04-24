import streamlit as st
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Generar datos de salarios anuales simulados
np.random.seed(1783)
salarios = np.random.normal(loc=50000, scale=15000, size=250)
salarios = np.round(salarios, -3)
salarios = np.abs(salarios)

# Calcular estadísticas descriptivas
media_salarios = np.mean(salarios)
mediana_salarios = np.median(salarios)
moda_salarios = stats.mode(salarios)
varianza_salarios = np.var(salarios)
desviacion_estandar_salarios = np.std(salarios)

# Crear gráficos
fig_hist = plt.figure(figsize=(15, 6))
plt.hist(salarios, bins=15, color='g', edgecolor='black', alpha=0.7)
plt.axvline(media_salarios, color='r', linestyle='dashed', linewidth=1.5, label='Media')
plt.axvline(mediana_salarios, color='b', linestyle='dashed', linewidth=1.5, label='Mediana')
plt.xlabel('Salarios')
plt.ylabel('Frecuencia')
plt.title('Distribución de Salarios Anuales')
plt.legend()
plt.grid(True)

fig_box = plt.figure(figsize=(8, 6))
plt.boxplot(salarios, vert=False)
plt.xlabel('Salarios')
plt.title('Diagrama de Caja de Salarios')
plt.grid(True)

fig_scatter = plt.figure(figsize=(10, 6))
plt.plot(salarios, 'o', label='Salarios') 
plt.axhline(media_salarios, color='r', linestyle='-', label=f'Media: {media_salarios:.2f}')
plt.axhline(media_salarios + desviacion_estandar_salarios, color='g', linestyle='--', label=f'+1 Desv. Est.: {media_salarios + desviacion_estandar_salarios:.2f}')
plt.axhline(media_salarios - desviacion_estandar_salarios, color='g', linestyle='--', label=f'-1 Desv. Est.: {media_salarios - desviacion_estandar_salarios:.2f}')
plt.title('Dispersión de los Salarios')
plt.xlabel('Índice de empleado')
plt.ylabel('Salarios')
plt.legend()
plt.grid(True)

# Mostrar gráficos
st.title('Informe sobre Análisis de Salarios Anuales')
st.write('En este informe, se presenta un análisis estadístico de los salarios anuales de los empleados.')

st.header('Resultados y Análisis')
st.write('**Media de los salarios:**', media_salarios)
st.write('**Mediana de los salarios:**', mediana_salarios)
st.write('**Moda de los salarios:**', moda_salarios.mode[0])
st.write('La moda aparece', moda_salarios.count[0], 'veces')
st.write('**Varianza de los salarios:**', varianza_salarios)
st.write('**Desviación estándar de los salarios:**', desviacion_estandar_salarios)

st.header('Gráficos')
st.pyplot(fig_hist)
st.pyplot(fig_box)
st.pyplot(fig_scatter)

st.header('Discusión')
st.write('La media de los salarios indica el valor promedio de compensación en la empresa, mientras que la mediana representa el salario central, siendo menos sensible a valores extremos. La moda señala el salario más común entre los empleados. La varianza y la desviación estándar reflejan la dispersión de los salarios alrededor de la media, indicando si los salarios están agrupados cerca de la media o dispersos.')

st.header('Implicaciones y Recomendaciones')
st.write('En base a las estadísticas obtenidas y los gráficos analizados, los salarios no son muy equitativos entre el personal de la empresa, por lo que se sugiere revisar la equidad salarial dentro de la empresa para garantizar una distribución justa de compensaciones.')
