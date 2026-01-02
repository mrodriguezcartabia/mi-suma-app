import streamlit as st

# Configuración del título de la página
st.title("🔢 Mi Primera Calculadora Web")
st.write("Introduce dos números para obtener su suma instantáneamente.")

# Crear dos columnas para que los inputs se vean mejor
col1, col2 = st.columns(2)

with col1:
    numero1 = st.number_input("Primer valor:", value=0.0)

with col2:
    numero2 = st.number_input("Segundo valor:", value=0.0)

# Realizar el cálculo
resultado = numero1 + numero2

# Mostrar el resultado con un diseño destacado
st.divider()
st.subheader(f"El resultado de la suma es: :green[{resultado}]")

# Botón opcional para celebrar
if st.button("¡Celebrar!"):
    st.balloons()
