import streamlit as st
import pandas as pd
import os

# 1. CONFIGURACIÓN DE PÁGINA (ESTILO MODERNO Y MASIVO)
st.set_page_config(page_title="CETEP | Campus Virtual", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    * { font-family: 'Poppins', sans-serif; }

    .hero-masivo {
        background: linear-gradient(rgba(0,45,90,0.85), rgba(0,45,90,0.95)), 
                    url('https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=1920');
        background-size: cover; background-position: center; padding: 100px 20px; color: white; text-align: center;
        border-radius: 0px 0px 50px 50px; margin: -60px -20px 40px -20px; box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .promo-box {
        background: #ffcc00; color: #002d5a; padding: 15px 30px;
        border-radius: 15px; font-weight: 800; font-size: 28px; display: inline-block;
        margin: 20px 0; border: 2px solid #fff;
    }

    .bloque-header {
        background: #002d5a; color: #ffcc00; padding: 12px 20px;
        border-radius: 10px 10px 0 0; font-weight: 700; margin-top: 20px;
    }
    .temario-box {
        background: #fdfdfd; padding: 20px; border: 1px solid #eee;
        border-radius: 0 0 10px 10px; margin-bottom: 10px;
    }
    .tema-line { padding: 8px 0; border-bottom: 1px solid #eef0f2; font-size: 15px; color: #333; }

    .footer { text-align: center; padding: 40px; color: #888; border-top: 1px solid #eee; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 2. DATA ACADÉMICA (₡15,000 Mensuales / Autodirigido)
OFFER_ACADEMICA = {
    "Global Learning: English Mastery (24 Meses)": {
        "D": "24 Meses (100% Autodirigido)", 
        "Inv": "Matrícula ₡5,000 (Única vez) / Mensualidad ₡15,000",
        "Malla": {
            "Año 1: Fluidez y Estructuras": ["Fonética Correcta", "Gramática Aplicada", "Conversación Inicial"],
            "Año 2: Dominio Profesional": ["Business English", "Bilingüismo para Transnacionales", "Entrevistas de Alto Perfil"]
        }
    },
    "Técnico en Operaciones Bancarias": {
        "D": "6 Meses (Video-Lecciones + Prácticas)", 
        "Inv": "Matrícula ₡5,000 (Única vez) / Mensualidad ₡15,000",
        "Malla": {
            "Módulos Técnicos": ["Legislación Bancaria CR", "Ley 8204", "Detección de Billetaje", "Arqueos de Caja"],
            "Componente Extra": ["Inglés Técnico Bancario (Learning Global)"]
        }
    },
    "Técnico en Gestión e Industria Médica": {
        "D": "9 Meses (Video-Lecciones + Prácticas)", 
        "Inv": "Matrícula ₡5,000 (Única vez) / Mensualidad ₡15,000",
        "Malla": {
            "Módulos Técnicos": ["Normativa ISO 13485", "Protocolos de Cuarto Limpio", "Metrología y Lectura de Planos"],
            "Componente Extra": ["Inglés Industrial Médico (Learning Global)"]
        }
    },
    "Preparación Examen Excelencia (Abogados)": {
        "D": "Intensivo Virtual", 
        "Inv": "Matrícula ₡5,000 (Única vez) / Pago Único o Mensual",
        "Malla": {
            "Contenido Legal": ["Derecho Civil/Mercantil", "Derecho Público/Laboral", "Deontología Jurídica"],
            "Simulacros": ["Análisis de Votos Sala IV", "Exámenes de Práctica Real"]
        }
    }
}

# 3. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>CETEP</h2>", unsafe_allow_html=True)
    st.write("---")
    nav = st.radio("NAVEGACIÓN", ["🏠 Inicio", "📚 Oferta Académica", "📝 Matrícula Abierta", "🔐 Campus Virtual"])

# 4. PÁGINAS
if nav == "🏠 Inicio":
    st.markdown("""
        <div class="hero-masivo">
            <h1 style='font-size: 50px; font-weight: 800;'>ESTUDIÁ A TU RITMO,<br>ALCANZÁ TU META</h1>
            <p style='font-size: 22px; opacity: 0.9;'>Técnicos de Alta Calidad 100% Virtuales.</p>
            <div class="promo-box">₡15,000 AL MES</div>
            <p style='margin-top:10px; font-size: 18px;'>Matrícula ₡5,000 (Paga una sola vez)</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("### ¿Por qué elegir el modelo CETEP?")
    col1, col2, col3 = st.columns(3)
    col1.success("🚀 **Autodirigido:** Estudiá a la hora que podás, 24/7.")
    col2.success("📈 **Bajo Costo:** La mensualidad más competitiva del país.")
    col3.success("🛡️ **Calidad:** Contenido diseñado por expertos activos.")

elif nav == "📚 Oferta Académica":
    st.header("Programas Disponibles 2026")
    sel = st.selectbox("Seleccione el programa de su interés:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[sel]
    
    st.subheader(f"⏱️ Duración: {info['D']}")
    st.info(f"💰 {info['Inv']}")
    
    for bloque, temas in info['Malla'].items():
        st.markdown(f"<div class='bloque-header'>{bloque}</div>", unsafe_allow_html=True)
        st.markdown("<div class='temario-box'>", unsafe_allow_html=True)
        for t in temas:
            st.markdown(f"<div class='tema-line'>✅ {t}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif nav == "📝 Matrícula Abierta":
    st.header("Iniciá tu Proceso de Matrícula")
    st.write("Completá tus datos y recibí el acceso a la plataforma.")
    with st.form("registro"):
        st.text_input("Nombre Completo")
        st.text_input("Cédula")
        st.text_input("WhatsApp")
        st.selectbox("Carrera a matricular", list(OFFER_ACADEMICA.keys()))
        if st.form_submit_button("RESERVAR MI LUGAR"):
            st.balloons()
            st.success("¡Excelente! Te contactaremos para el pago de los ₡5,000 de matrícula.")

elif nav == "🔐 Campus Virtual":
    st.subheader("Acceso a Video-Lecciones")
    st.info("Ingresá para ver tus clases grabadas y realizar tus evaluaciones.")
    u = st.text_input("Usuario (Cédula)")
    p = st.text_input("Contraseña", type="password")
    if st.button("INGRESAR"):
        if u == "admin_cetep" and p == "Luis2026":
            st.session_state.user_type = "admin"
            st.success("Bienvenido Luis. Accediendo al Panel de Control...")
        else:
            st.error("Credenciales no encontradas.")

st.markdown("<div class='footer'>© 2026 CETEP | Centro de Estudios Técnicos Profesionales | Heredia - San José</div>", unsafe_allow_html=True)
