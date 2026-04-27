import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="CETEP - Centro de Estudios Técnicos", layout="wide", page_icon="🎓")

# Estilo CSS para una apariencia profesional
st.markdown("""
    <style>
    .titulo-ipea { color: #002d5a; text-align: center; font-weight: bold; font-family: 'Arial'; margin-bottom: 20px; }
    .stTabs [aria-selected="true"] { background-color: #004a99; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 2. MENÚ DE NAVEGACIÓN (ESTRUCTURA IPEA)
with st.sidebar:
    st.image("https://www.freeiconspng.com/uploads/graduation-cap-icon-png-1.png", width=80)
    st.title("CETEP")
    opcion = st.radio("Menú Principal", [
        "Inicio", 
        "Técnicos", 
        "Inglés", 
        "Matrícula", 
        "Información", 
        "Campus Virtual"
    ])
    st.markdown("---")
    st.subheader("📱 Soporte Inmediato")
    # ENLACE CONFIGURADO CON TU NÚMERO: 86302333
    st.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Contactar-green?style=for-the-badge&logo=whatsapp)](https://wa.me/50686302333)")
    st.markdown("---")
    st.caption("© 2026 CETEP - Heredia, Costa Rica")

# --- 3. LÓGICA DE LAS SECCIONES ---

if opcion == "Inicio":
    st.markdown("<h1 class='titulo-ipea'>Centro de Estudios Técnicos y Especialidades Profesionales</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
    st.subheader("Formación Técnica para el Empleo")
    st.write("En CETEP preparamos a los profesionales que el mercado costarricense necesita. Programas cortos, prácticos y con alta demanda.")

elif opcion == "Técnicos":
    st.header("Nuestros Técnicos")
    t1, t2, t3, t4 = st.tabs(["⚖️ Asistente Legal", "🏦 Gestor Bancario", "📊 Contabilidad", "⚙️ Procesos Industriales"])
    
    with t1:
        st.subheader("Técnico Superior en Asistente Legal")
        st.write("Especialista en Cobro Judicial, Prescripción y Derecho Notarial.")
    with t2:
        st.subheader("Técnico en Gestión Bancaria Bilingüe")
        st.write("Enfoque en normativa SUGEF, operaciones de caja y servicio bancario.")
    with t3:
        st.subheader("Técnico en Contabilidad Técnica")
        st.write("Ciclo contable, impuestos (ATV) y planillas (CCSS e INS).")
    with t4:
        st.subheader("Especialista en Procesos Industriales")
        st.write("Control de calidad, logística, seguridad industrial y optimización.")

elif opcion == "Inglés":
    st.header("Programa de Inglés")
    st.image("https://images.unsplash.com/photo-1543165796-5426273eaab3?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
    st.subheader("Inglés Técnico y Conversacional")
    st.write("Desarrolle fluidez para el mundo laboral y de negocios.")

elif opcion == "Matrícula":
    st.header("📝 Formulario de Matrícula")
    with st.form("form_mat"):
        nombre = st.text_input("Nombre Completo:")
        cedula = st.text_input("Cédula:")
        programa = st.selectbox("Programa:", ["Asistente Legal", "Bancario", "Contabilidad", "Industrial", "Inglés"])
        if st.form_submit_button("Enviar"):
            st.success("✅ Solicitud recibida. Un asesor te contactará al WhatsApp.")

elif opcion == "Información":
    st.header("Sobre Nosotros")
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("¿Quiénes somos?")
        st.write("Una institución comprometida con la excelencia académica en Heredia.")
    with col_b:
        st.subheader("🤝 Convenios")
        st.info("Alianzas con despachos legales y empresas del sector industrial.")

elif opcion == "Campus Virtual":
    st.header("🔐 Campus Virtual")
    clave = st.text_input("Contraseña:", type="password")
    if st.button("Entrar"):
        clave_l = clave.strip()
        if clave_l == "admin_cetep":
            st.session_state["user"] = "admin"
        elif clave_l == "profe_cetep":
            st.session_state["user"] = "profe"
        else:
            st.error("Clave incorrecta")

    if "user" in st.session_state:
        st.write("---")
        if st.session_state["user"] == "admin":
            st.success("Director Luis Varela - Panel de Control")
            st.metric("Ingresos Mes", "₡1,250,000")
        elif st.session_state["user"] == "profe":
            st.success("Panel Docente - Registro de Notas")
