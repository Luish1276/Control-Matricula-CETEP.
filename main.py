import streamlit as st

# Configuración del Sistema CETEP
st.set_page_config(page_title="CETEP - Matrícula", page_icon="🎓")

st.title("🎓 CETEP: Control de Matrícula")
st.subheader("Heredia, Costa Rica")

with st.form("registro_cetep"):
    st.write("### Datos del Estudiante")
    nombre = st.text_input("Nombre Completo:")
    cedula = st.text_input("Número de Cédula:")
    
    # Lista de Cursos Actualizada
    tecnicos = [
        "Asistente Legal", 
        "Gestor Bancario Bilingüe", 
        "Contabilidad Técnica",
        "Especialista en Procesos Industriales" # El de Ingeniería Industrial con nombre profesional
    ]
    
    curso = st.selectbox("Seleccione el Técnico:", tecnicos)
    
    boton = st.form_submit_button("Registrar Matrícula")

    if boton:
        if nombre and cedula:
            st.success(f"✅ ¡Registro Exitoso! {nombre} matriculado en {curso}.")
            st.balloons()
        else:
            st.error("Por favor, complete nombre y cédula.")

st.sidebar.info("Gestión Administrativa - CETEP 2026")
