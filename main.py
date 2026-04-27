import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA Y ESTILO "BRANDED"
st.set_page_config(page_title="CETEP | Campus Virtual", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    * { font-family: 'Poppins', sans-serif; }

    /* Hero Section - Estilo Profesional Limpio */
    .hero-full {
        background: linear-gradient(rgba(0,30,60,0.65), rgba(0,30,60,0.85)), 
                    url('https://images.unsplash.com/photo-1524178232363-1fb2b075b655?auto=format&fit=crop&q=80&w=1920');
        background-size: cover;
        background-position: center;
        padding: 100px 20px;
        color: white;
        text-align: center;
        border-radius: 0px 0px 50px 50px;
        margin: -60px -20px 50px -20px;
    }
    
    .hero-title { font-size: 50px; font-weight: 800; line-height: 1.1; margin-bottom: 10px; }

    /* Sidebar Limpio */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #f0f0f0;
    }
    .sidebar-logo-container {
        text-align: center;
        padding: 10px 0px;
    }

    /* Tarjetas de Programas */
    .program-card {
        background: #ffffff;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #f0f0f0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.02);
        text-align: center;
        height: 100%;
        transition: all 0.3s ease;
    }
    .program-card:hover { transform: translateY(-5px); border-color: #004a99; box-shadow: 0 15px 35px rgba(0,0,0,0.06); }
    
    .category-tag {
        background: #e3f2fd;
        color: #004a99;
        padding: 5px 15px;
        border-radius: 50px;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 15px;
        display: inline-block;
    }

    .btn-action {
        background: #ffcc00;
        color: #002d5a;
        padding: 15px 40px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        display: inline-block;
        margin-top: 20px;
        box-shadow: 0 5px 15px rgba(255,204,0,0.3);
    }
    
    .footer { text-align: center; padding: 40px; color: #999; font-size: 13px; border-top: 1px solid #eee; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS MANTENIDA
OFFER_ACADEMICA = {
    "Técnico en Operaciones Bancarias y Gestión de Efectivo": {
        "D": "6 Meses", "Plan": ["Sistemas Financieros", "Manejo de Efectivo", "Prevención de Fraude", "SUGEF"]
    },
    "Técnico Asistente Legal": {
        "D": "9 Meses", "Plan": ["Investigación Jurídica", "Derecho Civil", "Redacción Documental", "Laboral"]
    },
    "Asistente Contable y Gestión Administrativa": {
        "D": "9 Meses", "Plan": ["Principios Contables", "Excel Avanzado", "IVA y Renta", "Planillas"]
    },
    "Gestión de Operaciones e Industria Médica": {
        "D": "9 Meses", "Plan": ["ISO 13485", "GDP Documentación", "Lean Manufacturing", "Pruebas Métricas"]
    },
    "Inglés Global Conversacional": {
        "D": "12 Meses", "Plan": ["Fonética", "Business English", "Fluidez Profesional"]
    }
}

# 3. SIDEBAR CON LOGO PROPIO
with st.sidebar:
    st.image("LOGO CETEP.jpg", use_container_width=True) # USANDO TU LOGO AQUÍ
    st.write("---")
    nav = st.radio("MENÚ PRINCIPAL", ["Inicio", "Oferta Académica", "Admisión", "Campus Virtual"])

# 4. PÁGINAS
if nav == "Inicio":
    st.markdown("""
        <div class="hero-full">
            <h1 class="hero-title">TU FUTURO PROFESIONAL<br>EMPIEZA AQUÍ</h1>
            <p style="font-size: 20px; opacity: 0.9;">Formación técnica especializada de alto nivel.</p>
            <a href="#" class="btn-action">VER PROGRAMAS</a>
        </div>
        """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='program-card'><div class='category-tag'>6 MESES</div><h3>Banca y Finanzas</h3><p>Gestión de efectivo y operaciones bancarias.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='program-card'><div class='category-tag'>9 MESES</div><h3>Sector Industrial</h3><p>Manufactura avanzada y dispositivos médicos.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='program-card'><div class='category-tag'>9 MESES</div><h3>Área Jurídica</h3><p>Asistencia legal y procesos administrativos.</p></div>", unsafe_allow_html=True)

elif nav == "Oferta Académica":
    st.header("Nuestros Programas")
    sel = st.selectbox("Seleccione:", list(OFFER_ACADEMICA.keys()))
    st.write(f"**Duración:** {OFFER_ACADEMICA[sel]['D']}")
    for p in OFFER_ACADEMICA[sel]['Plan']: st.write(f"✅ {p}")

elif nav == "Admisión":
    st.header("Proceso de Matrícula")
    with st.form("mat"):
        st.text_input("Nombre"), st.text_input("Cédula")
        st.selectbox("Carrera", list(OFFER_ACADEMICA.keys()))
        st.selectbox("Horario", ["Mañana", "Tarde", "Noche"])
        st.form_submit_button("SOLICITAR CUPO")

elif nav == "Campus Virtual":
    st.header("Acceso Académico")
    st.text_input("Usuario"), st.text_input("Contraseña", type="password")
    st.button("Ingresar")

st.markdown("<div class='footer'>© 2026 CETEP | Centro de Estudios Técnicos Profesionales | San José, Costa Rica.</div>", unsafe_allow_html=True)
