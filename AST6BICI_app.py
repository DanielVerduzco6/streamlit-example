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

# Calcular estadísticas descriptivas
media_salarios = np.mean(salarios)
mediana_salarios = np.median(salarios)
moda_salarios = stats.mode(salarios)
varianza_salarios = np.var(salarios)
desviacion_estandar_salarios = np.std(salarios)

# Crear la aplicación Streamlit
st.title("Análisis de Series Temporales: Estadísticas Descriptivas")
st.markdown("---")
st.write("### Problema")
st.markdown("Una empresa desea realizar un análisis estadístico de los salarios anuales de sus empleados. "
            "El propósito de este análisis es obtener una mejor comprensión de la distribución de los ingresos "
            "entre los empleados, lo que permitirá a la empresa tomar decisiones informadas respecto a la equidad "
            "salarial y la estructura de compensaciones.")
st.markdown("---")

# Mostrar estadísticas descriptivas
st.write("### Estadísticas Descriptivas")
st.write(f"Media de los salarios: {media_salarios}")
st.write(f"Mediana de los salarios: {mediana_salarios}")
st.write(f"Moda de los salarios: {moda_salarios.mode}, aparece {moda_salarios.count} veces")
st.write(f"Varianza de los salarios: {varianza_salarios}")
st.write(f"Desviación estándar de los salarios: {desviacion_estandar_salarios}")

# Crear y mostrar histograma
st.write("### Histograma de Salarios Anuales")
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

# Mostrar gráfico de dispersión con líneas de media y desviación estándar
st.write("### Gráfico de Dispersión con Líneas de Media y Desviación Estándar")
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

# Mostrar diagrama de caja
st.write("### Diagrama de Caja de Salarios")
plt.figure(figsize=(8, 6))
plt.boxplot(salarios, vert=False)
plt.xlabel('Salarios')
plt.title('Diagrama de Caja de Salarios')
plt.grid()
st.pyplot(plt)

# Mostrar análisis de las estadísticas descriptivas
st.write("### Análisis de las Estadísticas Descriptivas")
st.markdown("1. **Media y Mediana:**\n"
            "    - La media y la mediana son cercanas, lo que sugiere una distribución relativamente simétrica de los salarios.\n"
            "2. **Moda:**\n"
            "    - La moda indica el salario más común entre los empleados.\n"
            "3. **Varianza y Desviación Estándar:**\n"
            "    - La alta varianza y desviación estándar sugieren una dispersión considerable de los salarios alrededor de la media.")

# Mostrar informe y recomendaciones
st.write("### Informe y Recomendaciones")
st.markdown("En base a las estadísticas obtenidas y los gráficos analizados, los salarios en la empresa no son muy equitativos. "
            "Se recomienda revisar la equidad salarial dentro de la empresa para garantizar una distribución justa de compensaciones.")
