import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN ESTÉTICA (RESTAURADA)
st.set_page_config(page_title="CETEP | Campus Virtual", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    /* Fuente y Colores Corporativos */
    .main-title { 
        color: #002d5a; 
        text-align: center; 
        font-weight: 800; 
        font-size: 45px; 
        margin-bottom: 0px;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .sub-title {
        color: #004a99;
        text-align: center;
        font-size: 20px;
        margin-bottom: 30px;
    }
    .hero-container {
        background: linear-gradient(135deg, #002d5a 0%, #004a99 100%);
        color: white;
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
    }
    .card-academica { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 12px; 
        border: 1px solid #e0e0e0;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .footer-legal { text-align: center; font-size: 13px; color: #888; margin-top: 60px; border-top: 1px solid #eee; padding-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. ESTRUCTURA DE DATOS (Mantenida pero organizada)
OFFER_ACADEMICA = {
    "Técnico en Operaciones Bancarias y Gestión de Efectivo": {
        "D": "6 Meses",
        "Tag": "Especialización Bancaria",
        "Plan": ["Sistemas Financieros", "Manejo de Efectivo", "Prevención de Fraude", "Normativa SUGEF"]
    },
    "Técnico Asistente Legal": {
        "D": "9 Meses",
        "Tag": "Área Jurídica",
        "Plan": ["Investigación Jurídica", "Derecho Civil", "Legislación Laboral", "IA para Abogados"]
    },
    "Asistente Contable y Gestión Administrativa": {
        "D": "9 Meses",
        "Tag": "Administración",
        "Plan": ["Principios Contables", "Excel Avanzado", "Leyes Tributarias", "Planillas CCSS"]
    },
    "Gestión de Operaciones e Industria Médica": {
        "D": "9 Meses",
        "Tag": "Manufactura Alta Tecnología",
        "Plan": ["ISO 13485", "GDP (Documentación)", "Lean Manufacturing", "Pruebas Métricas Coyol"]
    },
    "Inglés Global Conversacional": {
        "D": "12 Meses",
        "Tag": "Idiomas",
        "Plan": ["Fonética", "Business English", "Fluidez Conversacional"]
    }
}

# 3. NAVEGACIÓN LATERAL
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
    st.title("SISTEMA CETEP")
    nav = st.radio("Navegación", ["Inicio", "Oferta Académica", "Matrícula en Línea", "Acceso Estudiantes"])
    st.write("---")
    st.caption("v2.0 - 2026 Costa Rica")

# --- LÓGICA DE PÁGINAS ---

if nav == "Inicio":
    # HERO SECTION MODERNA
    st.markdown("""
        <div class="hero-container">
            <h1 style="color: white; margin:0;">CETEP COSTA RICA</h1>
            <p style="font-size: 18px; opacity: 0.9;">Formación Técnica de Alto Impacto para el Sector Global</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align:center;'>Nuestras Áreas de Especialización</h2>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card-academica'><h3>🏦 Banca</h3><p>Cajero y Gestor Bancario con enfoque en normativa SUGEF.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card-academica'><h3>⚖️ Legal</h3><p>Asistente Legal especializado en redacción y procesos civiles.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card-academica'><h3>🏭 Industria</h3><p>Gestión de operaciones para el sector de dispositivos médicos.</p></div>", unsafe_allow_html=True)

elif nav == "Oferta Académica":
    st.markdown("<h1 class='main-title'>Programas 2026</h1>", unsafe_allow_html=True)
    sel = st.selectbox("Elija un programa para ver el detalle:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[sel]
    
    col_a, col_b = st.columns([1, 2])
    with col_a:
        st.metric("Duración", info["D"])
        st.info(f"Categoría: {info['Tag']}")
    with col_b:
        st.write("### Malla Curricular")
        for item in info["Plan"]:
            st.write(f"✅ {item}")

elif nav == "Matrícula en Línea":
    st.markdown("<h1 class='main-title'>Admisiones</h1>", unsafe_allow_html=True)
    with st.form("registro"):
        col1, col2 = st.columns(2)
        nombre = col1.text_input("Nombre Completo")
        cedula = col2.text_input("Cédula")
        programa = st.selectbox("Programa de Interés", list(OFFER_ACADEMICA.keys()))
        horario = st.select_slider("Preferencia de Horario", options=["Mañana (9-11)", "Tarde (2-4)", "Noche (6-8)"])
        
        if st.form_submit_button("Enviar Solicitud"):
            st.balloons()
            st.success(f"¡Listo {nombre}! Hemos registrado tu interés para el grupo de {horario}.")

elif nav == "Acceso Estudiantes":
    st.markdown("<h1 class='main-title'>Campus Virtual</h1>", unsafe_allow_html=True)
    user = st.text_input("Usuario (Cédula)")
    password = st.text_input("Contraseña", type="password")
    if st.button("Ingresar"):
        if user == "1-0000-0000": st.success("Bienvenido, Luis Varela (Director)")
        else: st.error("Acceso restringido: Verifique sus pagos semanales.")

st.markdown("<div class='footer-legal'>CETEP - Excelencia en Educación Técnica Virtual | Costa Rica 2026</div>", unsafe_allow_html=True)
