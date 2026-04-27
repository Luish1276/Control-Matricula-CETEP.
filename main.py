import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="CETEP - Matrícula", page_icon="🎓")

# Título principal corregido
st.title("🎓 CETEP: Control de Matrícula")
st.markdown("### Centro de Estudios Técnicos y Especialidades Profesionales")
st.write("---")

# Formulario de Registro
with st.form("registro_cetep", clear_on_submit=True):
    st.subheader("Formulario de Inscripción Oficial")
    
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
            st.success(f"✅ ¡Registro Recibido Exitosamente!")
            st.balloons()
            
            # Resumen para el estudiante
            fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            st.info(f"**Comprobante de Ingreso:**\n\n**Estudiante:** {nombre}\n\n**Identificación:** {cedula}\n\n**Programa:** {curso}\n\n**Fecha/Hora:** {fecha}")
        else:
            st.error("Por favor, complete todos los campos obligatorios para procesar la matrícula.")

# Barra lateral corregida (Sidebar)
st.sidebar.title("Administración CETEP")
st.sidebar.write("Sistema de Gestión Académica v1.0")
st.sidebar.markdown("---")
st.sidebar.info("Este formulario es para uso exclusivo de trámites de inscripción técnica.")
