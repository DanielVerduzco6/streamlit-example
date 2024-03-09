import streamlit as st
import numpy as np

# Definir diccionarios de estados
de_de_estados = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
    'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
    'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19
}

estados = {v: k for k, v in de_de_estados.items()}

# Matriz de recompensas
R = np.array([[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
              [0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
              [0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
              [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
              [0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]])

# Configuración de los parámetros gamma y alfa para el Q-Learning
gamma = 0.75
alpha = 0.9

# Inicialización de los valores Q
Q = np.array(np.zeros([20,20]))

# Definimos la función del ambiente
def environment(estado_actual):
    accion_realizable = []
    for j in range(20):
        if R[estado_actual, j] > 0:
            accion_realizable.append(j)
    return accion_realizable

# Definimos la función de las recompensas
def recompensas(estado_final, estado_intermedio, num):
    cont = 0
    for i in range(len(R)):
        for j in range(len(R[i])):
            if j == estado_final:
                if R[i][j] == 1:
                    R[i][j] = 20
            if (len(estado_intermedio) > 0) and (cont <= num):
                for k in estado_intermedio:
                    if j == k:
                        if R[i][j] == 1:
                            R[i][j] = 10
                            estado_intermedio.remove(k)
                            cont = cont + 1
                            break

# Elección del punto inicial, final e intermedios
st.title('Ruta Óptima con Q-Learning')

st.subheader('Grafo')
url_imagen = st.text_input('https://github.com/DanielVerduzco6/streamlit-example/blob/master/grafoCut.png?raw=true')
if url_imagen:
    st.image(url_imagen, caption='Imagen cargada desde URL', use_column_width=True)

estado_inicio_letra = st.sidebar.selectbox("Punto de Inicio", list(de_de_estados.keys()))
estado_final_letra = st.sidebar.selectbox("Punto Final", list(de_de_estados.keys()))

estado_intermedio = []
num = 0  # Inicializar num con 0
if st.sidebar.checkbox("Agregar Punto Intermedio"):
    num = st.sidebar.number_input("Cantidad de Puntos Intermedios", min_value=1, max_value=10)
    for i in range(num):
        estado_intermedio_letra = st.sidebar.selectbox(f"Punto Intermedio #{i+1}", list(de_de_estados.keys()))
        estado_intermedio.append(de_de_estados[estado_intermedio_letra])

estado_inicio = de_de_estados[estado_inicio_letra]
estado_final = de_de_estados[estado_final_letra]

recompensas(estado_final, estado_intermedio, num)

# Implementación del proceso de Q-Learning
for i in range(1000):
    estado_actual = np.random.randint(0, 20)
    accion_realizable = environment(estado_actual)
    estado_siguiente = np.random.choice(accion_realizable)
    TD = R[estado_actual, estado_siguiente] + gamma * Q[estado_siguiente, np.argmax(Q[estado_siguiente,])] - Q[estado_actual, estado_siguiente]
    Q[estado_actual, estado_siguiente] = Q[estado_actual, estado_siguiente] + alpha * TD

# Función Ruta
def ruta(estado_inicio, estado_final):
    st.subheader('Ruta Calculada')
    st.write(f"La ruta empieza en el estado: **{estados[estado_inicio]}**")
    estado_actual = estado_inicio
    while True:
        estado_actual = np.argmax(Q[estado_actual, :])
        st.write(f"Continua por el estado: **{estados[estado_actual]}**")
        if estado_final == estado_actual:
            st.write(f"La ruta finaliza en el estado: **{estados[estado_final]}**")
            break

# Mostrar la Ruta
ruta(estado_inicio, estado_final)
