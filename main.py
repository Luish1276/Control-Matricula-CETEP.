import streamlit as st
import pandas as pd
import os

# 1. CONFIGURACIÓN DE PÁGINA (ESTILO ELITE)
st.set_page_config(page_title="CETEP | Campus Virtual", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    * { font-family: 'Poppins', sans-serif; }

    .hero-full {
        background: linear-gradient(rgba(0,30,60,0.7), rgba(0,30,60,0.9)), 
                    url('https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&q=80&w=1920');
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

# 2. DATA ACADÉMICA COMPLETA (Incluye Inglés y Preparación)
OFFER_ACADEMICA = {
    "Técnico en Operaciones Bancarias y Gestión de Efectivo": {
        "D": "6 Meses", "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "MÓDULOS TÉCNICOS": ["Sistemas Bancarios CR", "Manejo de Efectivo", "SUGEF"],
            "GLOBAL LEARNING": ["Inglés Técnico para Finanzas", "Servicio al Cliente Bilingüe"]
        }
    },
    "Gestión de Operaciones e Industria Médica (Énfasis Coyol)": {
        "D": "9 Meses", "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "MÓDULOS TÉCNICOS": ["ISO 13485:2016", "Metrología", "Cuarto Limpio"],
            "GLOBAL LEARNING": ["Inglés Industrial", "Interpretación de Documentación en Inglés"]
        }
    },
    "Preparación Examen Excelencia Académica (Abogados)": {
        "D": "Intensivo", "Inv": "Inversión Cerrada",
        "Malla": {
            "ÁREA LEGAL": ["Derecho Civil y Mercantil", "Derecho Público", "Deontología Jurídica"],
            "ESTRATEGIA": ["Simulacros de Examen", "Jurisprudencia Reciente"]
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
    nav = st.radio("MENÚ PRINCIPAL", ["🏠 Inicio", "📚 Oferta Académica", "📝 Matrícula", "🔐 Campus Virtual"])

# 4. PÁGINAS
if nav == "🏠 Inicio":
    st.markdown("""
        <div class="hero-full">
            <h1 class="hero-title">CONECTANDO TU TALENTO<br>CON LA INDUSTRIA</h1>
            <p style="font-size: 20px; opacity: 0.9;">Técnicos + Inglés (Global Learning). Matrícula abierta 2026.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("### Meta de Apertura (Ciclo 2026)")
    col1, col2 = st.columns([3, 1])
    col1.progress(65)
    col2.write("40/60 Cupos")
    
    st.write("---")
    c1, c2, c3 = st.columns(3)
    c1.info("🏦 **Banca:** ₡5,000 semanales")
    c2.info("🏭 **Médica:** Énfasis Coyol")
    c3.info("⚖️ **Legal:** Asistencia y Excelencia")

elif nav == "📚 Oferta Académica":
    sel = st.selectbox("Seleccione el programa:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[sel]
    st.subheader(f"⏱️ {info['D']} | 💰 {info['Inv']}")
    for bloque, temas in info['Malla'].items():
        st.markdown(f"<div class='bloque-header'>{bloque}</div>", unsafe_allow_html=True)
        st.markdown("<div class='temario-box'>", unsafe_allow_html=True)
        for t in temas: st.markdown(f"<div class='tema-line'>✅ {t}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif nav == "📝 Matrícula":
    st.header("Formulario de Admisión")
    with st.form("reg"):
        st.text_input("Nombre Completo"), st.text_input("WhatsApp")
        st.selectbox("Carrera", list(OFFER_ACADEMICA.keys()))
        if st.form_submit_button("RESERVAR MI CUPO"):
            st.balloons()
            st.success("¡Recibido! Te contactaremos para formalizar.")

elif nav == "🔐 Campus Virtual":
    if 'user_type' not in st.session_state: st.session_state.user_type = None

    if st.session_state.user_type is None:
        st.header("Ingreso al Sistema")
        u = st.text_input("Usuario")
        p = st.text_input("Contraseña", type="password")
        if st.button("INGRESAR"):
            if u == "admin_cetep" and p == "Luis2026":
                st.session_state.user_type = "admin"
                st.rerun()
            elif u == "estudiante" and p == "123":
                st.session_state.user_type = "estudiante"
                st.rerun()
            else: st.error("Credenciales incorrectas")
    
    elif st.session_state.user_type == "admin":
        st.subheader("👨‍💼 Panel Administrativo (admin_cetep)")
        t1, t2, t3 = st.tabs(["📊 Financiero", "📝 Estudiantes", "📈 Notas"])
        
        with t1:
            st.metric("Total Recaudado", "₡300,000", "5,000/alumno")
            st.write("Control de pagos semanales activo.")
            
        with t2:
            st.write("### Matrícula Activa (Meta 60)")
            st.dataframe(pd.DataFrame({"Nombre": ["Juan", "Ana"], "Técnico": ["Banca", "Médica"]}), use_container_width=True)

        if st.button("Cerrar Sesión Admin"):
            st.session_state.user_type = None
            st.rerun()

st.markdown("<div class='footer'>© 2026 CETEP | Costa Rica</div>", unsafe_allow_html=True)
