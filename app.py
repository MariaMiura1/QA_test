import streamlit as st
from datetime import datetime

# Import del SUT (como paquete instalado con pip install -e .)
from src.voice_commands import process_command


st.set_page_config(page_title="Voice Command QA Demo", page_icon="🎙️", layout="centered")

st.title("🎙️ Voice Command QA Demo")
st.caption("Demo simple para validar comandos de voz en español (SUT: process_command).")

with st.expander("Comandos soportados", expanded=True):
    st.markdown(
        """
- **encender** → Dispositivo encendido  
- **apagar** → Dispositivo apagado  
- **subir volumen** → Volumen aumentado  
- **bajar volumen** → Volumen reducido  
- **silencio** → Modo silencio activado  
- **ayuda** → Listado de comandos  
        """
    )

# Estado para guardar historial
if "history" not in st.session_state:
    st.session_state.history = []

command = st.text_input("Escribe un comando (simulando transcripción):", placeholder="Ej: ENCENDER")

col1, col2 = st.columns(2)
with col1:
    run = st.button("Procesar", type="primary")
with col2:
    clear = st.button("Limpiar historial")

if clear:
    st.session_state.history = []
    st.success("Historial limpiado.")

if run:
    response = process_command(command)
    st.success(f"Respuesta: **{response}**")

    st.session_state.history.insert(0, {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "command": command,
        "response": response,
    })

st.divider()
st.subheader("🧾 Historial (sesión actual)")
if st.session_state.history:
    st.dataframe(st.session_state.history, use_container_width=True)
else:
    st.info("Aún no hay ejecuciones. Prueba con un comando.")
