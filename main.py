import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN
st.set_page_config(page_title="CETEP - Centro de Estudios Técnicos", layout="wide", page_icon="🎓")

# Estilo Profesional
st.markdown("""
    <style>
    .titulo-ipea { color: #002d5a; text-align: center; font-weight: bold; font-family: 'Arial'; }
    .stTabs [aria-selected="true"] { background-color: #004a99; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 2. NAVEGACIÓN
with st.sidebar:
    st.title("🛡️ CETEP")
    opcion = st.radio("Menú Principal", ["Inicio", "Técnicos", "Inglés", "Matrícula", "Información", "Campus Virtual"])
    st.markdown("---")
    st.subheader("📱 Soporte")
    st.markdown("[![WhatsApp](https://img.shields.io/badge/WhatsApp-Contactar-green?style=for-the-badge&logo=whatsapp)](https://wa.me/50686302333)")

# --- 3. LÓGICA DE SECCIONES ---

if opcion == "Inicio":
    st.markdown("<h1 class='titulo-ipea'>CETEP: Formación Técnica Profesional</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
    st.write("Excelencia académica y práctica en Heredia, Costa Rica.")

elif opcion == "Técnicos":
    st.header("Programas Técnicos")
    t1, t2, t3, t4 = st.tabs(["Asistente Legal", "Gestión Bancaria", "Contabilidad", "Procesos Industriales"])
    # (Contenido resumido para no alargar el código)
    with t1: st.write("Especialista en Cobro Judicial y Derecho Notarial.")
    with t2: st.write("Enfoque en normativa SUGEF y banca.")
    with t3: st.write("Ciclo contable e impuestos ATV.")
    with t4: st.write("Optimización y Control de Calidad.")

elif opcion == "Inglés":
    st.header("Inglés Técnico y Conversacional")
    st.image("https://images.unsplash.com/photo-1543165796-5426273eaab3?auto=format&fit=crop&q=80&w=1200", use_container_width=True)

elif opcion == "Matrícula":
    st.header("📝 Matrícula Abierta")
    with st.form("f_mat"):
        st.text_input("Nombre:")
        st.selectbox("Programa:", ["Asistente Legal", "Bancario", "Contabilidad", "Industrial", "Inglés"])
        st.form_submit_button("Enviar Solicitud")

elif opcion == "Información":
    st.header("Sobre CETEP")
    st.info("Convenios activos con despachos y sector industrial.")

elif opcion == "Campus Virtual":
    st.header("🔐 Acceso al Campus")
    clave = st.text_input("Contraseña:", type="password")
    
    if st.button("Entrar"):
        clave_l = clave.strip()
        if clave_l == "admin_cetep": st.session_state["user"] = "admin"
        elif clave_l == "profe_cetep": st.session_state["user"] = "profe"
        else: st.error("Clave incorrecta")

    if "user" in st.session_state:
        st.write("---")
        if st.session_state["user"] == "admin":
            st.success("Panel de Dirección - Luis Varela")
            tab_adm = st.tabs(["📊 Finanzas", "📁 Repositorio de Clases"])
            with tab_adm[0]:
                st.metric("Ingresos", "₡1,250,000")
            with tab_adm[1]:
                st.subheader("Gestión de Clases Grabadas")
                st.write("Pegue aquí los enlaces de las sesiones grabadas para que los alumnos las vean.")
                st.text_input("URL de la clase (YouTube/Drive):", key="url_adm")
        
        elif st.session_state["user"] == "profe":
            st.success("Panel Docente")
            tab_pro = st.tabs(["📝 Notas", "🎥 Videoteca"])
            with tab_pro[1]:
                st.subheader("Lecciones Guardadas")
                # Ejemplo de cómo se vería una clase embebida
                st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Video de ejemplo
                st.caption("Lección: Introducción al Módulo Legal")
