import streamlit as st
import pandas as pd
import os

# 1. CONFIGURACIÓN DE PÁGINA (ESTILO ELITE RESTAURADO)
st.set_page_config(page_title="CETEP | Campus Virtual", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    * { font-family: 'Poppins', sans-serif; }

    /* Hero Section con Impacto Visual Original */
    .hero-full {
        background: linear-gradient(rgba(0,30,60,0.7), rgba(0,30,60,0.9)), 
                    url('https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&q=80&w=1920');
        background-size: cover;
        background-position: center;
        padding: 100px 20px;
        color: white;
        text-align: center;
        border-radius: 0px 0px 50px 50px;
        margin: -60px -20px 40px -20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }
    
    .hero-title { font-size: 50px; font-weight: 800; line-height: 1.1; margin-bottom: 10px; }
    .hero-sub { font-size: 20px; opacity: 0.9; margin-bottom: 30px; }

    /* Estilo de Malla Curricular (LA CARNITA) */
    .bloque-header {
        background: #002d5a;
        color: #ffcc00;
        padding: 10px 20px;
        border-radius: 10px 10px 0 0;
        font-weight: 700;
        margin-top: 20px;
    }
    .temario-box {
        background: #f8f9fa;
        padding: 20px;
        border: 1px solid #eee;
        border-radius: 0 0 10px 10px;
        margin-bottom: 10px;
    }
    .tema-line {
        padding: 8px 0;
        border-bottom: 1px solid #eef0f2;
        font-size: 15px;
        color: #333;
    }

    .btn-action {
        background: #ffcc00;
        color: #002d5a;
        padding: 16px 40px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        display: inline-block;
        box-shadow: 0 10px 20px rgba(255,204,0,0.3);
    }
    
    .footer { text-align: center; padding: 40px; color: #888; border-top: 1px solid #eee; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS (Mallas completas y precios unificados)
OFFER_ACADEMICA = {
    "Técnico en Operaciones Bancarias y Gestión de Efectivo": {
        "D": "6 Meses",
        "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "MES 1-2: Fundamentos Financieros": ["Sistemas Bancarios de CR", "Legislación Financiera Básica", "Ética Profesional y Servicio"],
            "MES 3-4: Operativa de Caja": ["Manejo de Efectivo", "Detección de Billetaje Falso", "Prevención de Legitimación de Capitales"],
            "MES 5-6: Especialización Técnica": ["Software de Gestión Bancaria", "Arqueos y Cuadres de Caja", "Técnicas de Empleabilidad"]
        }
    },
    "Gestión de Operaciones e Industria Médica": {
        "D": "9 Meses",
        "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "CUATRIMESTRE I": ["Intro Industria Médica", "GDP (Buenas Prácticas de Documentación)", "Metrología e Instrumentación"],
            "CUATRIMESTRE II": ["Normativa ISO 13485:2016", "Protocolos de Cuarto Limpio", "Lean Manufacturing y 5S"],
            "CUATRIMESTRE III": ["Lectura de Planos Técnicos", "Entrenamiento en Pruebas Métricas", "Simulacros de Entrevista STAR"]
        }
    },
    "Asistente Contable y Gestión Administrativa": {
        "D": "9 Meses",
        "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "BLOQUE I": ["Contabilidad General", "Cuentas por Cobrar y Pagar", "Conciliaciones Bancarias"],
            "BLOQUE II": ["Excel Financiero", "Legislación Tributaria (IVA/Renta)", "Contabilidad de Costos"],
            "BLOQUE III": ["Planillas CCSS/INS", "TICA y ATV", "Análisis de Estados Financieros"]
        }
    },
    "Técnico Asistente Legal": {
        "D": "9 Meses",
        "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "CUATRIMESTRE I": ["Investigación Jurídica Digital", "Redacción Documental", "IA para Productividad Legal"],
            "CUATRIMESTRE II": ["Derecho Civil y Notarial", "Legislación Migratoria", "Procesos Administrativos"],
            "CUATRIMESTRE III": ["Derecho Laboral y Cargas Sociales", "Derecho de Familia", "Técnicas de Litigio"]
        }
    },
    "Preparación Examen Excelencia Académica (Abogados)": {
        "D": "Curso Intensivo",
        "Inv": "Inversión Cerrada - Consultar Fechas",
        "Malla": {
            "Ejes de Estudio": ["Derecho Civil y Mercantil", "Derecho Público", "Ética y Deontología Jurídica", "Jurisprudencia Reciente"]
        }
    }
}

# 3. SIDEBAR CON LOGO
with st.sidebar:
    if os.path.exists("LOGO CETEP.jpg"):
        st.image("LOGO CETEP.jpg", use_container_width=True)
    else:
        st.markdown("<h2 style='text-align:center; color:#002d5a;'>CETEP</h2>", unsafe_allow_html=True)
    st.write("---")
    nav = st.radio("MENÚ PRINCIPAL", ["🏠 Inicio", "📚 Oferta Académica", "📝 Matrícula", "🔐 Campus Virtual"])

# 4. LÓGICA DE PÁGINAS
if nav == "🏠 Inicio":
    st.markdown("""
        <div class="hero-full">
            <h1 class="hero-title">TU FUTURO PROFESIONAL<br>COMIENZA HOY</h1>
            <p class="hero-sub">Técnicos especializados con mensualidad única de ₡20,000.</p>
            <a href="#" class="btn-action">VER PROGRAMAS</a>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("### Meta de Apertura de Grupos (Ciclo 2026)")
    col_st1, col_st2 = st.columns([3, 1])
    col_stat = 65  # Simulación de avance hacia los 60 estudiantes
    col_st1.progress(col_stat) 
    col_st2.write("40/60 Cupos")

    st.write("---")
    c1, c2, c3 = st.columns(3)
    with c1: st.info("🏦 **Banca:** Ideal para plataforma y cajas.")
    with c2: st.info("🏭 **Médica:** Especialización para Zonas Francas.")
    with c3: st.info("⚖️ **Legal:** Asistencia y Excelencia Académica.")

elif nav == "📚 Oferta Académica":
    st.header("Nuestra Oferta Académica")
    sel = st.selectbox("Seleccione el programa para ver el temario:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[sel]
    st.subheader(f"⏱️ Duración: {info['D']} | 💰 {info['Inv']}")
    for bloque, temas in info['Malla'].items():
        st.markdown(f"<div class='bloque-header'>{bloque}</div>", unsafe_allow_html=True)
        st.markdown("<div class='temario-box'>", unsafe_allow_html=True)
        for t in temas: st.markdown(f"<div class='tema-line'>✅ {t}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif nav == "📝 Matrícula":
    st.header("Formulario de Admisión")
    with st.form("reg"):
        st.text_input("Nombre Completo"), st.text_input("WhatsApp")
        st.selectbox("Carrera de Interés", list(OFFER_ACADEMICA.keys()))
        st.selectbox("Horario Preferencial", ["Mañana (9-11 am)", "Tarde (2-4 pm)", "Noche (6-8 pm)"])
        if st.form_submit_button("RESERVAR MI CUPO"):
            st.balloons()
            st.success("¡Excelente! Nos comunicaremos con usted para formalizar la matrícula de ₡10,000.")

st.markdown("<div class='footer'>© 2026 CETEP | Centro de Estudios Técnicos Profesionales | Costa Rica</div>", unsafe_allow_html=True)
