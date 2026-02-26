import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Prode Zonal 2026", icon="⚽")
st.title("🏆 Prode Liga Zonal")

# --- LISTA DE PARTIDOS (FECHA 1) ---
partidos = [
    "Colonial vs Arenales (1ra)", "Social vs Singlar (1ra)", 
    "Belgrano vs Huracán (1ra)", "12 de Octubre vs Agustina (1ra)",
    "Colonial vs Arenales (Res)", "Social vs Singlar (Res)", 
    "Belgrano vs Huracán (Res)", "12 de Octubre vs Agustina (Res)"
]

# --- PESTAÑAS ---
tab1, tab2 = st.tabs(["📝 Cargar Pronósticos", "📊 Tabla de Posiciones"])

with tab1:
    st.header("Cargá tus resultados")
    nombre = st.selectbox("Elegí tu nombre", ["Juan", "Pedro", "Gringo", "Cacho"]) # Aquí van tus amigos
    
    # Creamos 8 filas de predicción
    preds = []
    for p in partidos:
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1: st.write(p)
        with col2: l = st.number_input("Local", min_value=0, step=1, key=f"{p}_l")
        with col3: v = st.number_input("Visita", min_value=0, step=1, key=f"{p}_v")
        preds.append((l, v))
    
    if st.button("Enviar Pronóstico"):
        # AQUÍ IRÍA LA CONEXIÓN A GOOGLE SHEETS PARA GUARDAR
        st.success(f"¡Listo {nombre}! Pronóstico guardado.")
        st.balloons()

with tab2:
    st.header("Ranking General")
    # Ejemplo de cómo calcularías los puntos
    st.info("Aquí aparecerá la tabla cuando cargues los resultados reales.")
    # data = pd.DataFrame({"Jugador": ["Gringo", "Cacho"], "Puntos": [15, 12]})
    # st.table(data.sort_values(by="Puntos", ascending=False))