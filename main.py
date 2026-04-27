import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="CETEP - Campus Virtual", layout="wide", page_icon="🎓")

# Estilo profesional tipo IPEA
st.markdown("""
    <style>
    .titulo-ipea { color: #002d5a; text-align: center; font-weight: bold; font-family: 'Arial'; }
    .stTabs [aria-selected="true"] { background-color: #004a99; color: white; }
    .nota-card { background-color: #f8f9fa; padding: 15px; border-left: 5px solid #004a99; border-radius: 5px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. MENÚ DE NAVEGACIÓN
with st.sidebar:
    st.title("🛡️ CETEP")
    opcion = st.radio("Menú Principal", ["Inicio", "Técnicos", "Inglés", "Matrícula", "Información", "Campus Virtual"])
    st.markdown("---")
    st.subheader("📱 Soporte")
    st.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Contactar-green?style=for-the-badge&logo=whatsapp)](https://wa.me/50686302333)")

# Base de datos simulada para la consulta de estudiantes
notas_ejemplo = {
    "1-1111-1111": {"Nombre": "Juan Pérez", "Carrera": "Asistente Legal", "Notas": {"Cobro Judicial": 90, "Derecho Notarial": 85}},
    "2-2222-2222": {"Nombre": "Ana Mora", "Carrera": "Gestión Bancaria", "Notas": {"Legislación": 88, "Caja": 95}}
}

# --- 3. LÓGICA DE SECCIONES ---

if opcion == "Inicio":
    st.markdown("<h1 class='titulo-ipea'>Centro de Estudios Técnicos y Especialidades Profesionales</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=1200", use_container_width=True)

elif opcion == "Técnicos":
    st.header("Programas Técnicos")
    st.write("Especializaciones de alta demanda laboral en Costa Rica.")

elif opcion == "Matrícula":
    st.header("📝 Formulario de Matrícula Oficial")
    st.write("Por favor, complete todos los campos para formalizar su inscripción.")
    
    with st.form("registro_completo"):
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Nombre Completo:")
            cedula = st.text_input("Número de Cédula:")
        with col2:
            telefono = st.text_input("Número de Teléfono:")
            programa = st.selectbox("Programa de Interés:", ["Asistente Legal", "Gestor Bancario", "Contabilidad", "Procesos Industriales", "Inglés"])
        
        direccion = st.text_area("Dirección Exacta de Residencia:")
        
        enviar = st.form_submit_button("CONFIRMAR MATRÍCULA")
        
        if enviar:
            if nombre and cedula and telefono and direccion:
                st.success(f"✅ ¡Registro Exitoso! Bienvenido al CETEP, {nombre}. Nos comunicaremos al {telefono}.")
                st.balloons()
            else:
                st.error("⚠️ Todos los campos son obligatorios para el registro legal.")

elif opcion == "Información":
    st.header("Sobre Nosotros")
    st.info("Ubicados en Heredia, enfocados en el éxito profesional de nuestros estudiantes.")

elif opcion == "Campus Virtual":
    st.markdown("<h2 style='text-align: center;'>🔐 Acceso al Campus</h2>", unsafe_allow_html=True)
    
    tipo_acceso = st.selectbox("Tipo de Usuario:", ["Estudiante", "Profesor", "Director"])
    
    if tipo_acceso == "Estudiante":
        cedula_log = st.text_input("Ingrese su Cédula (con guiones):", placeholder="1-1111-1111")
        if st.button("Ver Mis Notas y Temario"):
            if cedula_log in notas_ejemplo:
                datos = notas_ejemplo[cedula_log]
                st.success(f"Bienvenido(a), {datos['Nombre']}")
                t_est1, t_est2 = st.tabs(["📊 Mi Progreso", "📚 Temario"])
                with t_est1:
                    for materia, nota in datos['Notas'].items():
                        st.markdown(f"<div class='nota-card'><strong>{materia}:</strong> {nota}</div>", unsafe_allow_html=True)
                with t_est2:
                    st.write(f"Plan de estudios oficial para {datos['Carrera']}.")
            else:
                st.error("Cédula no registrada en el sistema.")

    elif tipo_acceso == "Profesor":
        clave_p = st.text_input("Contraseña Docente:", type="password")
        if st.button("Ingresar Panel Docente"):
            if clave_p == "profe_cetep":
                st.success("Acceso concedido.")

    elif tipo_acceso == "Director":
        clave_d = st.text_input("Contraseña Director:", type="password")
        if st.button("Ingresar Panel Dirección"):
            if clave_d == "admin_cetep":
                st.success(f"Bienvenido, Luis Varela")
                st.metric("Ingresos Mes", "₡1,250,000")
