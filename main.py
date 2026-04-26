import streamlit as st

st.set_page_config(page_title="CETEP - Matrícula", page_icon="🎓")
st.title("🎓 CETEP: Control de Matrícula")
st.subheader("Heredia, Costa Rica")

with st.form("registro_cetep"):
    nombre = st.text_input("Nombre del Estudiante:")
    cedula = st.text_input("Cédula:")
    curso = st.selectbox("Técnico:", ["Asistente Legal", "Banca", "Contabilidad"])
    if st.form_submit_button("Registrar"):
        if nombre and cedula:
            st.success(f"✅ Registrado: {nombre} en {curso}")
            st.balloons()
        else:
            st.error("Faltan datos.")
