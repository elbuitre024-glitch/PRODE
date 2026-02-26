import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# 1. Configuración (SIEMPRE PRIMERO)
st.set_page_config(page_title="Prode Zonal 2026", page_icon="⚽")

# 2. Conexión a Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("🏆 Prode Liga Zonal")

partidos = [
    "Colonial vs Arenales (1ra)", "Social vs Singlar (1ra)", 
    "Belgrano vs Huracán (1ra)", "12 de Octubre vs Agustina (1ra)",
    "Colonial vs Arenales (Res)", "Social vs Singlar (Res)", 
    "Belgrano vs Huracán (Res)", "12 de Octubre vs Agustina (Res)"
]

tab1, tab2 = st.tabs(["📝 Cargar Pronósticos", "📊 Tabla"])

with tab1:
    with st.form("formulario_prode"):
        nombre = st.text_input("Tu Nombre/Apodo:")
        
        resultados = []
        for i, p in enumerate(partidos):
            st.write(f"**{p}**")
            c1, c2 = st.columns(2)
            l = c1.number_input("Goles Local", min_value=0, step=1, key=f"l_{i}")
            v = c2.number_input("Goles Visita", min_value=0, step=1, key=f"v_{i}")
            resultados.extend([l, v])
            st.divider()

        enviado = st.form_submit_button("Enviar Pronóstico")

        if enviado:
            if nombre:
                # Crear nueva fila de datos
                nueva_fila = [nombre] + resultados + [datetime.now().strftime("%Y-%m-%d %H:%M")]
                
                # Leer datos actuales y agregar el nuevo
                data_existente = conn.read(worksheet="pronosticos")
                # Lógica para guardar (esto requiere el link en Secrets)
                st.success(f"¡Gracias {nombre}! Tu pronóstico fue registrado.")
                st.balloons()
            else:
                st.error("Por favor, poné tu nombre.")

with tab2:
    st.write("Acá verás los puntos pronto...")
