import numpy as np
import streamlit as st

# Definición de los estados
de_de_estados = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
    'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
    'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19
}

# Definición del diccionario de estados inverso
estados = {v: k for k, v in de_de_estados.items()}

# Inicialización de las recompensas
R = np.array([
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
])

# Configuración de los parámetros gamma y alfa para el Q-Learning
gamma = 0.75
alpha = 0.9

# Definimos la función del ambiente
def environment(estado_actual):
    accion_realizable = [j for j in range(20) if R[estado_actual, j] > 0]
    return accion_realizable

# Definimos la función de las recompensas
def recompensas(estado_final, estado_intermedio, num):
    cont = 0
    for i in range(len(R)):
        for j in range(len(R[i])):
            if j == estado_final and R[i][j] == 1:
                R[i][j] = 20
            if len(estado_intermedio) > 0 and cont <= num:
                for k in estado_intermedio:
                    if j == k and R[i][j] == 1:
                        R[i][j] = 10
                        estado_intermedio.remove(k)
                        cont += 1
                        break

# Definimos la función de la ruta
def ruta(estado_inicio, estado_final, estados):
    st.write("\nLa ruta empieza en el estado:", estados[estado_inicio])
    estado_actual = estado_inicio
    while True:
        estado_siguiente = np.argmax(Q[estado_actual, :])
        st.write("Continua por el estado:", estados[estado_siguiente])
        estado_actual = estado_siguiente
        if estado_final == estado_actual:
            st.write("La ruta finaliza en el estado:", estados[estado_final])
            break

# Función principal de la aplicación
def main():
    st.title("Aplicación de Q-Learning con Streamlit")

    # Captura de puntos de inicio, final e intermedios
    estado_inicio_letra = st.text_input("Ingrese el Punto de Inicio", "A").upper()
    estado_final_letra = st.text_input("Ingrese el Punto Final", "M").upper()
    num_intermedios = st.number_input("Ingrese la cantidad de puntos intermedios", min_value=0, value=0)

    estado_inicio = de_de_estados.get(estado_inicio_letra, None)
    estado_final = de_de_estados.get(estado_final_letra, None)

    if estado_inicio is None or estado_final is None:
        st.error("Por favor, ingrese puntos de inicio y final válidos.")
        return

    estado_intermedio = []
    for _ in range(num_intermedios):
        estado_intermedio_letra = st.text_input("Ingrese el Punto intermedio", "").upper()
        estado_intermedio.append(de_de_estados.get(estado_intermedio_letra, None))

    # Actualización de las recompensas
    recompensas(estado_final, estado_intermedio, num_intermedios)

    # Implementación del proceso de Q-Learning
    for _ in range(1000):
        estado_actual = np.random.randint(0, 20)
        accion_realizable = environment(estado_actual)
        estado_siguiente = np.random.choice(accion_realizable)
        TD = R[estado_actual, estado_siguiente] + gamma * Q[estado_siguiente, np.argmax(Q[estado_siguiente, :])] - Q[estado_actual, estado_siguiente]
        Q[estado_actual, estado_siguiente] = Q[estado_actual, estado_siguiente] + alpha * TD

    # Mostrar los valores de Q
    st.write("Q-Values:")
    st.write(Q.astype(int))

    # Mostrar la ruta
    ruta(estado_inicio, estado_final, estados)

# Ejecutar la aplicación
if __name__ == "__main__":
    main()
