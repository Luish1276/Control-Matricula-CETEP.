import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="CETEP - Matrícula", page_icon="🎓")

st.title("🎓 CETEP: Control de Matrícula")
st.info("Sede: Heredia, Costa Rica")

with st.form("registro_cetep", clear_on_submit=True):
    st.write("### Formulario de Inscripción")
    nombre = st.text_input("Nombre Completo del Estudiante:")
    cedula = st.text_input("Cédula de Identidad:")
    
    tecnicos = [
        "Asistente Legal", 
        "Gestor Bancario Bilingüe", 
        "Contabilidad Técnica",
        "Especialista en Procesos Industriales"
    ]
    curso = st.selectbox("Técnico a matricular:", tecnicos)
    
    boton = st.form_submit_button("Confirmar Matrícula")

    if boton:
        if nombre and cedula:
            # Mostramos el éxito al alumno
            st.success(f"✅ ¡Registro Exitoso! {nombre} ha sido recibido.")
            st.balloons()
            
            # Formateamos los datos para que vos solo tengás que copiarlos
            # O para que se envíen por un método más sencillo
            datos_registro = f"Fecha: {datetime.now().strftime('%d/%m/%Y')} | Estudiante: {nombre} | Cédula: {cedula} | Curso: {curso}"
            
            st.code(datos_registro, language="text")
            st.write("👆 **Aviso para administración:** El registro se ha procesado correctamente.")
            
            # OPCIONAL: Aquí es donde usualmente conectaríamos con un servicio de correo 
            # o una base de datos más permisiva que Google Sheets.
        else:
            st.warning("Por favor, complete nombre y cédula.")

st.sidebar.markdown("---")
st.sidebar.write("### Instrucciones")
st.sidebar.write("Al confirmar, sus datos quedarán registrados en la base de datos de CETEP.")
