import streamlit as st
import pandas as pd
import os

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="CETEP | Campus Virtual", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    * { font-family: 'Poppins', sans-serif; }

    .hero-full {
        background: linear-gradient(rgba(0,30,60,0.7), rgba(0,30,60,0.9)), 
                    url('https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=1920');
        background-size: cover; background-position: center; padding: 100px 20px; color: white; text-align: center;
        border-radius: 0px 0px 50px 50px; margin: -60px -20px 40px -20px; box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }
    
    .hero-title { font-size: 50px; font-weight: 800; line-height: 1.1; margin-bottom: 10px; }
    
    .bloque-header {
        background: #002d5a; color: #ffcc00; padding: 12px 20px;
        border-radius: 10px 10px 0 0; font-weight: 700; margin-top: 20px;
    }
    .temario-box {
        background: #f8f9fa; padding: 20px; border: 1px solid #eee;
        border-radius: 0 0 10px 10px; margin-bottom: 10px;
    }
    .tema-line { padding: 8px 0; border-bottom: 1px solid #eef0f2; font-size: 15px; color: #333; }

    .footer { text-align: center; padding: 40px; color: #888; border-top: 1px solid #eee; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 2. DATA ACADÉMICA (Estructura de 12 + 12 meses)
OFFER_ACADEMICA = {
    "Global Learning: English Mastery - Nivel I (Primeros 12 meses)": {
        "D": "12 Meses (Fundamentos y Fluidez Inicial)", "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "ETAPA DE CIMENTACIÓN": ["Estructura Gramatical Sólida", "Fonética y Pronunciación", "Listening Comprensivo"],
            "ETAPA DE FLUIDEZ": ["Conversación Situacional", "Vocabulario Expandido", "Lectura y Comprensión de Textos"]
        }
    },
    "Global Learning: English Mastery - Nivel II (Segundos 12 meses)": {
        "D": "12 Meses (Perfeccionamiento y Bilingüismo)", "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "ETAPA AVANZADA": ["Inglés de Negocios y Corporativo", "Debate y Argumentación en Vivo", "Redacción Profesional"],
            "DOMINIO TOTAL": ["Bilingüismo para Alta Gerencia", "Simulación de Entrevistas Internacionales", "Comprensión Nativa"]
        }
    },
    "Técnico en Operaciones Bancarias y Gestión de Efectivo": {
        "D": "6 Meses", "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "MÓDULOS TÉCNICOS": ["Sistemas Bancarios CR", "Legislación Financiera", "Manejo de Efectivo"],
            "MÓDULO INTEGRADO": ["Global Learning: English Mastery (Módulos Base)"]
        }
    },
    "Gestión de Operaciones e Industria Médica": {
        "D": "9 Meses", "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "MÓDULOS TÉCNICOS": ["ISO 13485:2016", "Protocolos de Cuarto Limpio", "Metrología"],
            "MÓDULO INTEGRADO": ["Global Learning: English Mastery (Módulos Base)"]
        }
    },
    "Preparación Examen Excelencia Académica (Abogados)": {
        "D": "Curso Intensivo", "Inv": "Consultar Plan de Pagos",
        "Malla": {
            "ÁREA LEGAL": ["Derecho Civil y Mercantil", "Derecho Público", "Deontología Jurídica"],
            "REFORZAMIENTO": ["Simulacros de Examen", "Análisis de Fallos Recientes"]
        }
    }
}

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("LOGO CETEP.jpg"):
        st.image("LOGO CETEP.jpg", use_container_width=True)
    else:
        st.markdown("<h2 style='text-align:center; color:#002d5a;'>CETEP</h2>", unsafe_allow_html=True)
    st.write("---")
    nav = st.radio("MENÚ", ["🏠 Inicio", "📚 Oferta Académica", "📝 Matrícula", "🔐 Campus Virtual"])

# 4. PÁGINAS
if nav == "🏠 Inicio":
    st.markdown("""
        <div class="hero-full">
            <h1 class="hero-title">HABLA INGLÉS<br>CON TOTAL DOMINIO</h1>
            <p style="font-size: 20px; opacity: 0.9;">Global Learning: El programa de 24 meses para salir bilingüe. ₡5,000 por semana.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("### Capacidad de Apertura 2026")
    col1, col2 = st.columns([3, 1])
    col1.progress(65)
    col2.write("40/60 Estudiantes")
    
    st.write("---")
    c1, c2, c3 = st.columns(3)
    c1.info("🏦 **Banca:** ₡5,000 semanales")
    c2.info("🌍 **Inglés:** Global Mastery (24m)")
    c3.info("⚖️ **Legal:** Preparación Excelencia")

elif nav == "📚 Oferta Académica":
    st.header("Programas CETEP")
    sel = st.selectbox("Seleccione el técnico o curso:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[sel]
    st.subheader(f"⏱️ {info['D']} | 💰 {info['Inv']}")
    
    for bloque, temas in info['Malla'].items():
        st.markdown(f"<div class='bloque-header'>{bloque}</div>", unsafe_allow_html=True)
        st.markdown("<div class='temario-box'>", unsafe_allow_html=True)
        for t in temas:
            st.markdown(f"<div class='tema-line'>✅ {t}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif nav == "📝 Matrícula":
    st.header("Formulario de Inscripción")
    with st.form("reg"):
        st.text_input("Nombre Completo"), st.text_input("WhatsApp")
        st.selectbox("Programa de Interés", list(OFFER_ACADEMICA.keys()))
        if st.form_submit_button("SOLICITAR CUPO"):
            st.balloons()
            st.success("¡Excelente decisión! Nos comunicaremos con vos pronto.")

elif nav == "🔐 Campus Virtual":
    if 'user_type' not in st.session_state: st.session_state.user_type = None

    if st.session_state.user_type is None:
        st.header("Ingreso al Campus")
        u = st.text_input("Usuario")
        p = st.text_input("Contraseña", type="password")
        if st.button("ACCEDER"):
            if u == "admin_cetep" and p == "Luis2026":
                st.session_state.user_type = "admin"
                st.rerun()
            elif u == "estudiante" and p == "123":
                st.session_state.user_type = "estudiante"
                st.rerun()
            else: st.error("Acceso denegado")
    
    elif st.session_state.user_type == "admin":
        st.subheader("👨‍💼 Panel Luis (admin_cetep)")
        t1, t2, t3 = st.tabs(["💰 Financiero", "📋 Matrícula", "📊 Notas"])
        
        with t1:
            st.metric("Ingresos Proyectados", "₡1,200,000")
            st.write("Control de pagos de ₡5,000 semanales.")
            
        with t2:
            st.write("### Estudiantes Inscritos")
            st.table(pd.DataFrame({"Estudiante": ["Juan P.", "María R."], "Curso": ["English Mastery", "Banca"]}))

        if st.button("Cerrar Sesión"):
            st.session_state.user_type = None
            st.rerun()

st.markdown("<div class='footer'>© 2026 CETEP | Costa Rica</div>", unsafe_allow_html=True)
