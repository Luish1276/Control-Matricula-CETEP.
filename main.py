import streamlit as st
import pandas as pd
import os

# 1. CONFIGURACIÓN DE PÁGINA (ESTILO MODERNO IPEA)
st.set_page_config(page_title="CETEP | Campus Virtual", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    * { font-family: 'Poppins', sans-serif; }

    /* Hero Section Impactante */
    .hero-full {
        background: linear-gradient(rgba(0,30,60,0.65), rgba(0,30,60,0.85)), 
                    url('https://images.unsplash.com/photo-1524178232363-1fb2b075b655?auto=format&fit=crop&q=80&w=1920');
        background-size: cover;
        background-position: center;
        padding: 120px 20px;
        color: white;
        text-align: center;
        border-radius: 0px 0px 50px 50px;
        margin: -60px -20px 50px -20px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    }
    
    .hero-title { font-size: 55px; font-weight: 800; line-height: 1.1; margin-bottom: 10px; letter-spacing: -2px; }
    .hero-sub { font-size: 22px; font-weight: 300; margin-bottom: 35px; opacity: 0.9; }

    /* Sidebar Profesional */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #f0f0f0;
    }
    .sidebar-brand-text {
        font-size: 30px;
        font-weight: 800;
        color: #002d5a;
        text-align: center;
        padding: 20px 0;
    }

    /* Tarjetas de Áreas */
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
    .program-card:hover { transform: translateY(-8px); border-color: #004a99; box-shadow: 0 15px 35px rgba(0,0,0,0.06); }
    
    .category-tag {
        background: #e3f2fd;
        color: #004a99;
        padding: 5px 15px;
        border-radius: 50px;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 15px;
    }

    .btn-action {
        background: #ffcc00;
        color: #002d5a;
        padding: 16px 40px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        display: inline-block;
        box-shadow: 0 8px 20px rgba(255,204,0,0.3);
    }
    
    .footer { text-align: center; padding: 40px; color: #888; font-size: 14px; border-top: 1px solid #eee; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS ACADÉMICA (RESTABLECIDA)
OFFER_ACADEMICA = {
    "Técnico en Operaciones Bancarias y Gestión de Efectivo": {
        "D": "6 Meses",
        "Tag": "Finanzas",
        "Inversion": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Plan": ["Sistemas Financieros", "Manejo de Efectivo", "Prevención de Fraude", "Normativa SUGEF", "Arqueos"]
    },
    "Técnico Asistente Legal": {
        "D": "9 Meses",
        "Tag": "Área Jurídica",
        "Plan": ["Investigación Jurídica", "Derecho Civil", "Redacción Documental", "Legislación Laboral"]
    },
    "Asistente Contable y Gestión Administrativa": {
        "D": "9 Meses",
        "Tag": "Administración",
        "Plan": ["Principios Contables", "Excel Avanzado", "IVA y Renta", "Planillas y CCSS"]
    },
    "Gestión de Operaciones e Industria Médica": {
        "D": "9 Meses",
        "Tag": "Manufactura Avanzada",
        "Plan": ["ISO 13485", "GDP (Documentación)", "Lean Manufacturing", "Pruebas Métricas y STAR"]
    },
    "Inglés Global Conversacional": {
        "D": "12 Meses",
        "Tag": "Idiomas",
        "Plan": ["Fonética", "Business English", "Fluidez Conversacional"]
    }
}

# 3. SIDEBAR CON LOGO Y NAVEGACIÓN
with st.sidebar:
    # Manejo del archivo del logo
    logo_file = "LOGO CETEP.jpg"
    if os.path.exists(logo_file):
        st.image(logo_file, use_container_width=True)
    else:
        # Si el archivo no se encuentra, mostramos el nombre con estilo para evitar el error MediaFileStorage
        st.markdown('<div class="sidebar-brand-text">CETEP</div>', unsafe_allow_html=True)
    
    st.write("---")
    nav = st.radio("MENÚ PRINCIPAL", ["Inicio", "Oferta Académica", "Matrícula", "Campus Virtual"])

# 4. LÓGICA DE PÁGINAS
if nav == "Inicio":
    st.markdown("""
        <div class="hero-full">
            <h1 class="hero-title">TU FUTURO PROFESIONAL<br>COMIENZA HOY</h1>
            <p class="hero-sub">Especialización técnica diseñada para la empleabilidad inmediata.</p>
            <a href="#" class="btn-action">DESCUBRIR PROGRAMAS</a>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class="program-card">
                <span style="font-size:40px;">🏦</span><br><br>
                <div class="category-tag">6 Meses</div>
                <h3>Banca y Finanzas</h3>
                <p>Gestión de efectivo y operaciones en el sistema financiero.</p>
            </div>
            """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="program-card">
                <span style="font-size:40px;">🏭</span><br><br>
                <div class="category-tag">9 Meses</div>
                <h3>Procesos Industriales</h3>
                <p>Capacitación técnica para el sector de dispositivos médicos.</p>
            </div>
            """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="program-card">
                <span style="font-size:40px;">⚖️</span><br><br>
                <div class="category-tag">9 Meses</div>
                <h3>Área Legal</h3>
                <p>Asistente para procesos jurídicos y notariales de alto nivel.</p>
            </div>
            """, unsafe_allow_html=True)

elif nav == "Oferta Académica":
    st.header("Programas Disponibles 2026")
    cat = st.selectbox("Seleccione el técnico:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[cat]
    st.metric("Duración", info["D"])
    st.write(f"**Inversión:** {info.get('Inversion', 'Consultar')}")
    st.write("### Ejes de formación:")
    for t in info["Plan"]: st.write(f"✅ {t}")

elif nav == "Matrícula":
    st.header("Formulario de Admisión")
    with st.form("registro"):
        st.text_input("Nombre Completo"), st.text_input("Cédula")
        st.selectbox("Carrera de Interés", list(OFFER_ACADEMICA.keys()))
        st.selectbox("Horario Preferencial", ["Mañana (9-11 am)", "Tarde (2-4 pm)", "Noche (6-8 pm)"])
        if st.form_submit_button("REGISTRAR SOLICITUD"):
            st.success("Hemos recibido tu información. El equipo de admisiones te contactará.")

elif nav == "Campus Virtual":
    st.header("Plataforma Académica")
    st.text_input("Usuario (Cédula)")
    st.text_input("Contraseña", type="password")
    st.button("Iniciar Sesión")

st.markdown("<div class='footer'>© 2026 CETEP | Centro de Estudios Técnicos Profesionales | San José, Costa Rica.</div>", unsafe_allow_html=True)
