import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA Y ESTILO "HIGH-END EDUCATIONAL"
st.set_page_config(page_title="CETEP | Campus Virtual", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    
    * { font-family: 'Poppins', sans-serif; }

    /* Hero Section Principal - Estilo IPEA Moderno y Limpio */
    .hero-full {
        background: linear-gradient(rgba(0,30,60,0.7), rgba(0,30,60,0.9)), 
                    url('https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&q=80&w=1920');
        background-size: cover;
        background-position: center;
        padding: 120px 20px;
        color: white;
        text-align: center;
        border-radius: 0px 0px 50px 50px;
        margin: -60px -20px 40px -20px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    }
    
    .hero-title { font-size: 55px; font-weight: 800; margin-bottom: 5px; letter-spacing: -2px; }
    .hero-sub { font-size: 22px; font-weight: 300; margin-bottom: 35px; opacity: 0.9; }

    /* Tarjetas de Áreas - Más Suaves y Educativas */
    .program-card {
        background: #ffffff;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #f0f0f0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
        text-align: center;
        height: 100%;
        transition: transform 0.3s ease;
    }
    .program-card:hover { transform: translateY(-5px); border-color: #004a99; }
    
    .area-icon { font-size: 40px; margin-bottom: 15px; display: block; }
    
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
        padding: 15px 35px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        font-size: 18px;
        display: inline-block;
        margin-top: 10px;
        box-shadow: 0 5px 15px rgba(255,204,0,0.3);
    }
    
    .footer { text-align: center; padding: 40px; color: #888; font-size: 14px; border-top: 1px solid #eee; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS MANTENIDA (Mismos nombres, duración y pagos)
OFFER_ACADEMICA = {
    "Técnico en Operaciones Bancarias y Gestión de Efectivo": {
        "D": "6 Meses",
        "Tag": "Finanzas",
        "Inversion": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Plan": ["Sistemas Financieros", "Manejo de Efectivo", "Prevención de Fraude", "SUGEF", "Arqueos"]
    },
    "Técnico Asistente Legal": {
        "D": "9 Meses",
        "Tag": "Área Jurídica",
        "Inversion": "Consultar Plan",
        "Plan": ["Investigación Jurídica", "Derecho Civil", "Redacción Documental", "Laboral y Familia"]
    },
    "Asistente Contable y Gestión Administrativa": {
        "D": "9 Meses",
        "Tag": "Administración",
        "Inversion": "Consultar Plan",
        "Plan": ["Principios Contables", "Excel Avanzado", "IVA y Renta", "Planillas y CCSS"]
    },
    "Gestión de Operaciones e Industria Médica": {
        "D": "9 Meses",
        "Tag": "Manufactura Avanzada",
        "Inversion": "Consultar Plan",
        "Plan": ["ISO 13485", "GDP (Documentación)", "Lean Manufacturing", "Pruebas Métricas Coyol"]
    },
    "Inglés Global Conversacional": {
        "D": "12 Meses",
        "Tag": "Idiomas",
        "Inversion": "Consultar Plan",
        "Plan": ["Fonética", "Business English", "Fluidez Profesional"]
    },
    "Prep. Colegio de Abogados": {
        "D": "Intensivo",
        "Tag": "Área Jurídica",
        "Inversion": "Consultar Plan",
        "Plan": ["Ejes Temáticos del Examen", "Deontología Jurídica"]
    }
}

# 3. INTERFAZ
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=70)
    st.title("🛡️ CETEP ADMIN")
    nav = st.radio("Menú Principal", ["⭐ Inicio", "📚 Oferta", "📝 Matrícula", "🔐 Campus Virtual"])
    st.write("---")
    st.caption("v2.1 - Conectando Talento e Industria")

if nav == "⭐ Inicio":
    # HERO SECTION (Estilo IPEA, Moderno y Enfocado al Estudiante)
    st.markdown("""
        <div class="hero-full">
            <h1 class="hero-title">TU CARRERA EMPIEZA AQUÍ</h1>
            <p class="hero-sub">Formación técnica especializada para los sectores de mayor crecimiento.</p>
            <a href="#nuestras-carreras" class="btn-action">EXPLORAR PROGRAMAS</a>
        </div>
        """, unsafe_allow_html=True)
    
    # SECCIÓN DE ÁREAS (Más Suaves)
    st.markdown("<h2 style='text-align:center; margin-bottom:40px;'>Especializate en las áreas del futuro</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class="program-card">
                <span class="area-icon">🏦</span>
                <div class="category-tag">6 Meses</div>
                <h3>Banca y Finanzas</h3>
                <p>Capacitación práctica para el sector bancario y gestión de efectivo.</p>
            </div>
            """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="program-card">
                <span class="area-icon">🏭</span>
                <div class="category-tag">9 Meses</div>
                <h3>Procesos Industriales</h3>
                <p>Especialización para la industria de dispositivos médicos y manufactura avanzada.</p>
            </div>
            """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="program-card">
                <span class="area-icon">⚖️</span>
                <div class="category-tag">9 Meses</div>
                <h3>Área Jurídica</h3>
                <p>Formación intensiva para asistentes legales y gestión de procesos.</p>
            </div>
            """, unsafe_allow_html=True)

elif nav == "📚 Oferta":
    st.markdown("<h2 style='text-align:center;'>Nuestra Oferta Académica 2026</h2>", unsafe_allow_html=True)
    cat = st.selectbox("Elija un programa:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[cat]
    st.metric("Duración", info["D"])
    st.write(f"**Categoría:** {info['Tag']} | **Inversión:** {info['Inversion']}")
    st.write("### Contenidos Clave")
    for t in info["Plan"]: st.write(f"✅ {t}")

elif nav == "📝 Matrícula":
    st.markdown("## Proceso de Admisión Virtual")
    with st.form("form_matricula"):
        st.text_input("Nombre Completo")
        st.text_input("Cédula")
        st.selectbox("Programa de Interés", list(OFFER_ACADEMICA.keys()))
        st.selectbox("Horario deseado", ["Mañana (9-11 am)", "Tarde (2-4 pm)", "Noche (6-8 pm)"])
        submitted = st.form_submit_button("SOLICITAR INFORMACIÓN")
        if submitted:
            st.success("Hemos recibido tu solicitud. Te contactaremos pronto.")

elif nav == "🔐 Campus Virtual":
    st.markdown("## Acceso a la Plataforma Virtual")
    user = st.text_input("Cédula")
    password = st.text_input("Contraseña", type="password")
    if st.button("Ingresar"):
        if user == "1-0000-0000": st.success("Bienvenido, Luis Varela (Director)")
        else: st.error("Usuario o contraseña incorrectos.")

st.markdown("<div class='footer'>© 2026 CETEP | Centro de Estudios Técnicos Profesionales | Sede San José.</div>", unsafe_allow_html=True)
