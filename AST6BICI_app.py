import streamlit as st
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(1783)
salaries = np.random.normal(loc=50000, scale=15000, size=250)
salaries = np.round(salaries, -3)
salaries = np.abs(salaries)

# Calculate descriptive statistics
mean_salaries = np.mean(salaries)
median_salaries = np.median(salaries)
mode_salaries = stats.mode(salaries)
variance_salaries = np.var(salaries)
standard_deviation_salaries = np.std(salaries)

# Display descriptive statistics
st.title("Análisis de Salarios Anuales")
st.write("Media de los salarios:", mean_salaries)
st.write("Mediana de los salarios:", median_salaries)
st.write("Moda de los salarios:", mode_salaries.mode)
st.write("Varianza de los salarios:", variance_salaries)
st.write("Desviación estándar de los salarios:", standard_deviation_salaries)

# Histogram
st.figure(figsize=(15, 6))
plt.hist(salaries, bins=15, color='g', edgecolor='black', alpha=0.7)
plt.axvline(mean_salaries, color='r', linestyle='dashed', linewidth=1.5, label='Media')
plt.axvline(median_salaries, color='b', linestyle='dashed', linewidth=1.5, label='Mediana')
plt.xlabel('Salarios')
plt.ylabel('Frecuencia')
plt.title('Distribución de Salarios Anuales')
plt.legend()
plt.grid(True)
st.pyplot()

# Box plot
st.figure(figsize=(8, 6))
plt.boxplot(salaries, vert=False)
plt.xlabel('Salarios')
plt.title('Diagrama de Caja de Salarios')
plt.grid()
st.pyplot()

# Scatter plot with mean and standard deviation lines
mean = mean_salaries
standard_deviation = standard_deviation_salaries

st.figure(figsize=(10, 6))
plt.plot(salaries, 'o', label='Salarios')
plt.axhline(mean, color='r', linestyle='-', label=f'Media: {mean:.2f}')
plt.axhline(mean + standard_deviation, color='g', linestyle='--', label=f'+1 Desv. Est.: {mean + standard_deviation:.2f}')
plt.axhline(mean - standard_deviation, color='g', linestyle='--', label=f'-1 Desv. Est.: {mean - standard_deviation:.2f}')
plt.title('Dispersión de los Salarios')
plt.xlabel('Índice de empleado')
plt.ylabel('Salarios')
plt.legend()
plt.grid(True)
st.pyplot()

# Discussion
st.markdown("## Discusión")

# Interpretation of mean and median
st.markdown("La media de los salarios es de **49,604.0**, lo que nos dice el salario promedio de los empleados.")
st.markdown("La mediana de los salarios es de **50,000.0**, lo que nos dice el salario central cuando los salarios se ordenan de menor a mayor.")
st.markdown("Ya que la media y la mediana son cercanas en este caso, sugiere que la distribución de los salarios es relativamente **simétrica** y no está sesgada hacia valores extremos.")
st.markdown("Esto nos dice que la mayoría de los salarios se encuentran al rededor de estos valores centrales.")

# Interpretation of mode
st.markdown("La moda de los salarios es de **52,000.0** y aparece **10** veces en los datos.")
st.markdown("Esto nos dice que **52,000.0** es el salario más común entre los empleados.")

# Interpretation of variance and standard deviation
st.markdown("La varianza de los salarios es de **278,327,184.0** y la desviación estándar es de aproximadamente **16,683.14**. Una varianza alta y una desviación estándar considerable indican que
