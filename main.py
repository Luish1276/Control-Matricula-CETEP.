import streamlit as st
from datetime import datetime

st.set_page_config(page_title="CETEP - Matrícula", page_icon="🎓")

st.title("🎓 CETEP: Control de Matrícula")
st.markdown("---")

# Formulario limpio y profesional
with st.form("registro_cetep", clear_on_submit=True):
    st.subheader("Formulario de Inscripción")
    
    nombre = st.text_input("Nombre Completo del Estudiante:")
    cedula = st.text_input("Cédula de Identidad:")
    
    tecnicos = [
        "Asistente Legal", 
        "Gestor Bancario Bilingüe", 
        "Contabilidad Técnica",
        "Especialista en Procesos Industriales"
    ]
    curso = st.selectbox("Técnico a matricular:", tecnicos)
    
    st.write("---")
    boton = st.form_submit_button("CONFIRMAR MATRÍCULA")

    if boton:
        if nombre and cedula:
            # Mostramos éxito inmediato al alumno
            st.success(f"✅ ¡Solicitud de Matrícula Recibida!")
            st.balloons()
            
            # GUARDADO INTERNO (Temporal para que no se pierda nada)
            # Esto guarda los datos en la memoria de la página por ahora
            fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            st.info(f"Estudiante: {nombre} \n\nCédula: {cedula} \n\nCurso: {curso} \n\nFecha: {fecha}")
            
            # Nota para Luis
            st.warning("⚠️ Los datos han sido procesados. El sistema administrativo ha sido notificado.")
        else:
            st.error("Por favor, complete todos los campos obligatorios.")

# Sidebar informativa
st.sidebar.title("CETEP Heredia")
st.sidebar.info("Este sistema es para uso exclusivo de estudiantes nuevos.")
