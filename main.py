import streamlit as st
import pandas as pd

# Configuración profesional de alto nivel
st.set_page_config(page_title="CETEP - Centro de Estudios Técnicos", layout="wide", page_icon="🎓")

# Estilo CSS para una apariencia corporativa tipo ipeacr.com
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .titulo-principal { color: #002d5a; text-align: center; font-weight: bold; margin-bottom: 20px; }
    .card { background-color: white; padding: 20px; border-radius: 10px; border-left: 5px solid #004a99; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# Menú lateral
with st.sidebar:
    st.title("🛡️ CETEP")
    opcion = st.radio("Menú Principal", ["Inicio", "Oferta Académica", "Matrícula en Línea", "Portal Administrativo"])
    st.markdown("---")
    st.write("📍 Sede Central")

# --- SECCIÓN: INICIO ---
if opcion == "Inicio":
    st.markdown("<h1 class='titulo-principal'>Centro de Estudios Técnicos y Especialidades Profesionales</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
    
    st.subheader("Formación Técnica de Excelencia")
    st.write("En CETEP transformamos el talento en capacidad profesional. Nuestros programas están alineados con la realidad laboral de Costa Rica, combinando experiencia técnica y visión práctica.")

# --- SECCIÓN: OFERTA ACADÉMICA (LOS 4 TÉCNICOS SEPARADOS) ---
elif opcion == "Oferta Académica":
    st.header("Nuestros Programas Técnicos")
    
    tabs = st.tabs(["⚖️ Asistente Legal", "🏦 Gestor Bancario", "📊 Contabilidad Técnica", "⚙️ Especialista en Procesos Industriales"])
    
    with tabs[0]: # ASISTENTE LEGAL
        st.subheader("Técnico Superior en Asistente Legal")
        st.markdown("""
        **Módulos Clave:**
        * Derecho Procesal Civil y Mercantil.
        * **Cobro Judicial y Prescripción:** Análisis profundo de plazos y gestión de expedientes.
        * Derecho Notarial y Registral.
        * Gestión de Plataformas del Poder Judicial (SDJ).
        """)

    with tabs[1]: # GESTOR BANCARIO
        st.subheader("Técnico en Gestión Bancaria Bilingüe")
        st.markdown("""
        **Módulos Clave:**
        * Legislación Bancaria y Normativa SUGEF.
        * Operaciones de Caja y Detección de Moneda.
        * Servicio al Cliente y Venta de Productos Financieros.
        * Inglés Técnico para el Sector Financiero.
        """)

    with tabs[2]: # CONTABILIDAD
        st.subheader("Técnico en Contabilidad Técnica")
        st.markdown("""
        **Módulos Clave:**
        * Ciclo Contable Completo.
        * Legislación Tributaria (IVA, Renta, ATV).
        * Planillas y Beneficios Sociales (CCSS / INS).
        * Contabilidad de Costos y Presupuestos.
        """)

    with tabs[3]: # INGENIERÍA INDUSTRIAL / PROCESOS
        st.subheader("Especialista en Procesos Industriales")
        st.write("Este programa está diseñado para el control de calidad y optimización de la producción.")
        st.markdown("""
        **Módulos Clave:**
        * Control Estadístico de Procesos.
        * Gestión de Inventarios y Logística.
        * Seguridad Industrial e Higiene Ocupacional.
        * Introducción a Lean Manufacturing.
        """)

# --- SECCIÓN: MATRÍCULA ---
elif opcion == "Matrícula en Línea":
    st.header("📝 Inscripción Oficial")
    with st.form("form_matricula"):
        nombre = st.text_input("Nombre Completo:")
        cedula = st.text_input("Número de Cédula:")
        tecnico = st.selectbox("Técnico a matricular:", [
            "Asistente Legal", 
            "Gestor Bancario Bilingüe", 
            "Contabilidad Técnica",
            "Especialista en Procesos Industriales"
        ])
        if st.form_submit_button("Confirmar Solicitud"):
            st.success(f"✅ ¡Solicitud para {tecnico} recibida!")
            st.balloons()

# --- SECCIÓN: PORTAL ADMINISTRATIVO ---
elif opcion == "Portal Administrativo":
    st.header("🔐 Acceso Administrativo")
    password = st.text_input("Clave de acceso:", type="password")
    if password == "cetep2026":
        st.success("Acceso concedido.")
        st.write("Aquí se gestionará la base de datos de los 4 técnicos.")
