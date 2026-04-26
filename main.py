import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="CETEP - Matrícula", page_icon="🎓")

st.title("🎓 CETEP: Control de Matrícula")
st.info("Sede: Heredia, Costa Rica")

# Conexión con Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

with st.form("registro_cetep"):
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
            try:
                # Preparamos la nueva fila
                nueva_fila = pd.DataFrame([{
                    "Fecha": datetime.now().strftime("%d/%m/%Y"),
                    "Nombre": nombre,
                    "Cédula": cedula,
                    "Técnico": curso
                }])
                
                # Leemos datos actuales
                df_existente = conn.read()
                
                # Añadimos la nueva matrícula
                df_final = pd.concat([df_existente, nueva_fila], ignore_index=True)
                
                # Actualizamos el Excel
                conn.update(data=df_final)
                
                st.success(f"✅ ¡Registro Exitoso! {nombre} matriculado en {curso}.")
                st.balloons()
            except Exception as e:
                st.error(f"Error de conexión: {e}")
        else:
            st.warning("Por favor, complete nombre y cédula.")
