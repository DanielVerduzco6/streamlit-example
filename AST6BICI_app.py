import streamlit as st
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Configurar la semilla del generador aleatorio para reproducibilidad
np.random.seed(1783)

# Generar datos de salarios anuales (simulados)
salarios = np.random.normal(loc=50000, scale=15000, size=250)
salarios = np.round(salarios, -3)

# Asegurarse de que todos los salarios sean positivos
salarios = np.abs(salarios)

# Título y descripción
st.title('Análisis de Series Temporales: Estadísticas Descriptivas')
st.write('**Estudiante:** Verduzco Valencia Daniel Alejandro')
st.write('**Profesor:** Mata Lopez Walter Alexander')
st.write('**6.-B**')
st.write('**Ingeniería en Computación Inteligente**')
st.write('**Universidad de Colima**')
st.write('**FIME**')
st.write('**12/04/2024**')

# Problema
st.header('Problema')
st.write("Una empresa desea realizar un análisis estadístico de los salarios anuales de sus empleados. El propósito de este análisis es obtener una mejor comprensión de la distribución de los ingresos entre los empleados, lo que permitirá a la empresa tomar decisiones informadas respecto a la equidad salarial y la estructura de compensaciones.")

# Generar Datos
st.header('Generar Datos')
st.code("""
import numpy as np

# Configurar la semilla del generador aleatorio para reproducibilidad
np.random.seed(1783)

# Generar datos de salarios anuales (simulados)
salarios = np.random.normal(loc=50000, scale=15000, size=250)
salarios = np.round(salarios, -3)

# Asegurarse de que todos los salarios sean positivos
salarios = np.abs(salarios)
""", language='python')

# Mostrar los salarios generados
st.write("Salarios generados:")
st.write(salarios)

# Calcular Estadísticas Descriptivas
st.header('Calcular Estadísticas Descriptivas')
media_salarios = np.mean(salarios)
mediana_salarios = np.median(salarios)
moda_salarios = stats.mode(salarios)
varianza_salarios = np.var(salarios)
desviacion_estandar_salarios = np.std(salarios)

st.write("Media de los salarios:", media_salarios)
st.write("Mediana de los salarios:", mediana_salarios)
st.write("Moda de los salarios:", moda_salarios.mode[0]) 
st.write("La moda aparece", moda_salarios.count[0], "veces")
st.write("Varianza de los salarios:", varianza_salarios)
st.write("Desviación estándar de los salarios:", desviacion_estandar_salarios)

# Gráfica de Histograma
st.header('Histograma de Salarios')
plt.figure(figsize=(10, 6))
plt.hist(salarios, bins=15, color='g', edgecolor='black', alpha=0.7)
plt.axvline(media_salarios, color='r', linestyle='dashed', linewidth=1.5, label='Media')
plt.axvline(mediana_salarios, color='b', linestyle='dashed', linewidth=1.5, label='Mediana')
plt.xlabel('Salarios')
plt.ylabel('Frecuencia')
plt.title('Distribución de Salarios Anuales')
plt.legend()
plt.grid(True)

st.pyplot(plt)

# Interpretar los Resultados
st.header('Interpretar los Resultados')

# Diagrama de Caja
st.subheader('Diagrama de Caja de Salarios')
plt.figure(figsize=(8, 6))
plt.boxplot(salarios, vert=False)
plt.xlabel('Salarios')
plt.title('Diagrama de Caja de Salarios')
plt.grid()
st.pyplot(plt)

# Gráfico de Dispersión
st.subheader('Gráfico de Dispersión con Líneas de Media y Desviación Estándar')
plt.figure(figsize=(10, 6))
plt.plot(salarios, 'o', label='Salarios') # Puntos de los salarios
plt.axhline(media_salarios, color='r', linestyle='-', label=f'Media: {media_salarios:.2f}') # Línea de la media
plt.axhline(media_salarios + desviacion_estandar_salarios, color='g', linestyle='--', label=f'+1 Desv. Est.: {media_salarios + desviacion_estandar_salarios:.2f}')
plt.axhline(media_salarios - desviacion_estandar_salarios, color='g', linestyle='--', label=f'-1 Desv. Est.: {media_salarios - desviacion_estandar_salarios:.2f}')
plt.title('Dispersión de los Salarios')
plt.xlabel('Índice de empleado')
plt.ylabel('Salarios')
plt.legend()
plt.grid(True)

st.pyplot(plt)

# Informe
st.header('Informe')
st.write("""
**Informe sobre Análisis de Salarios Anuales**

En este informe, se presenta un análisis estadístico de los salarios anuales de los empleados. Se calcularon medidas descriptivas como la media, mediana, moda, varianza y desviación estándar para comprender la distribución de los salarios y discutir su equidad salarial.

**Resultados y Análisis**

**Cálculos Realizados:**

- Media de los salarios: 49,604.0
- Mediana de los salarios: 50,000.0
- Moda de los salarios: 52,000.0
- Varianza de los salarios: 278,327,184.0
- Desviación estándar de los salarios: 16,683.14

**Discusión:**

La media de los salarios indica el valor promedio de compensación en la empresa, mientras que la mediana representa el salario central, siendo menos sensible a valores extremos. La moda señala el salario más común entre los empleados. La varianza y la desviación estándar reflejan la dispersión de los salarios alrededor de la media, indicando si los salarios están agrupados cerca de la media o dispersos.

**Implicaciones y Recomendaciones:**

En base a las estadísticas obtenidas y los gráficos analizados, los salarios no son muy equitativos entre el personal de la empresa, por lo que se sugiere revisar la equidad salarial dentro de la empresa para garantizar una distribución justa de compensaciones.
""")
