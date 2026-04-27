import streamlit as st
import pandas as pd
import os

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="CETEP | Campus Virtual", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    * { font-family: 'Poppins', sans-serif; }

    /* Hero Section */
    .hero-full {
        background: linear-gradient(rgba(0,30,60,0.7), rgba(0,30,60,0.9)), 
                    url('https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&q=80&w=1920');
        background-size: cover;
        background-position: center;
        padding: 110px 20px;
        color: white;
        text-align: center;
        border-radius: 0px 0px 50px 50px;
        margin: -60px -20px 40px -20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }
    
    .hero-title { font-size: 55px; font-weight: 800; line-height: 1.1; margin-bottom: 10px; letter-spacing: -2px; }

    /* Estilo de Malla Curricular */
    .bloque-header {
        background: #002d5a;
        color: #ffcc00;
        padding: 10px 20px;
        border-radius: 10px 10px 0 0;
        font-weight: 700;
        margin-top: 20px;
        font-size: 18px;
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
        padding: 16px 45px;
        border-radius: 60px;
        text-decoration: none;
        font-weight: 700;
        font-size: 20px;
        display: inline-block;
        box-shadow: 0 10px 20px rgba(255,204,0,0.4);
    }
    
    .footer { text-align: center; padding: 40px; color: #888; border-top: 1px solid #eee; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS UNIFICADA (Todos los técnicos a 5 rojos semanales)
# Excepto Preparación Colegio de Abogados
OFFER_ACADEMICA = {
    "Técnico en Operaciones Bancarias y Gestión de Efectivo": {
        "D": "6 Meses",
        "Inversion": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "MES 1-2: Fundamentación Financiera": ["Sistemas Bancarios de Costa Rica", "Legislación Financiera Básica", "Ética Profesional y Servicio al Cliente"],
            "MES 3-4: Operativa de Caja": ["Reconocimiento de Billetaje (Dólares/Colones)", "Detección de Falsificaciones", "Prevención de Legitimación de Capitales"],
            "MES 5-6: Especialización Técnica": ["Software de Gestión Bancaria", "Arqueos y Cuadres de Caja", "Técnicas de Empleabilidad Bancaria"]
        }
    },
    "Gestión de Operaciones e Industria Médica": {
        "D": "9 Meses",
        "Inversion": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "CUATRIMESTRE I": ["Introducción a la Industria Médica", "GDP (Buenas Prácticas de Documentación)", "Metrología e Instrumentación Vernier"],
            "CUATRIMESTRE II": ["Normativa ISO 13485:2016", "Protocolos de Cuarto Limpio", "Lean Manufacturing y 5S"],
            "CUATRIMESTRE III": ["Lectura de Planos Técnicos", "Entrenamiento en Pruebas Métricas", "Simulacros de Entrevista por Competencias (STAR)"]
        }
    },
    "Técnico Asistente Legal": {
        "D": "9 Meses",
        "Inversion": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "CUATRIMESTRE I": ["Investigación Jurídica y LexisNexis", "Redacción Documental y Ortografía", "IA para Productividad Legal"],
            "CUATRIMESTRE II": ["Derecho Civil y Notarial", "Legislación Migratoria", "Procesos Administrativos"],
            "CUATRIMESTRE III": ["Derecho Laboral y Cargas Sociales", "Derecho de Familia", "Técnicas de Litigio y Apoyo Procesal"]
        }
    },
    "Asistente Contable y Gestión Administrativa": {
        "D": "9 Meses",
        "Inversion": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "BLOQUE I": ["Contabilidad General I", "Cuentas por Cobrar y Pagar", "Conciliación Bancaria"],
            "BLOQUE II": ["Excel Financiero y Tablas Dinámicas", "Legislación Tributaria (IVA)", "Contabilidad de Costos"],
            "BLOQUE III": ["Planillas (TICA/CCSS/INS)", "Impuesto sobre la Renta", "Software Contable"]
        }
    },
    "Inglés Global Conversacional": {
        "D": "12 Meses",
        "Inversion": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "Básico": ["Fonética y Estructura", "Vocabulario Cotidiano", "Comprensión Auditiva"],
            "Intermedio": ["Business English", "Redacción de Correos", "Fluidez en Conversación"],
            "Avanzado": ["Presentaciones Ejecutivas", "Inglés Técnico por Área", "Preparación para Certificación"]
        }
    },
    "Preparación Examen Excelencia Académica (Abogados)": {
        "D": "Curso Intensivo",
        "Inversion": "Inversión cerrada - Consultar fechas de inicio",
        "Malla": {
            "BLOQUE JURÍDICO": ["Contratos Civiles y Mercantiles", "Responsabilidad Civil", "Sucesiones y Derechos Reales"],
            "BLOQUE PÚBLICO": ["Derecho Constitucional", "Derecho Administrativo", "Recursos de Amparo y Hábeas Corpus"],
            "BLOQUE ÉTICO": ["Deontología Jurídica", "Código de Deberes", "Jurisprudencia Reciente de la Sala Segunda"]
        }
    }
}

# 3. SIDEBAR CON LOGO
with st.sidebar:
    if os.path.exists("LOGO CETEP.jpg"):
        st.image("LOGO CETEP.jpg", use_container_width=True)
    else:
        st.markdown("<h1 style='text-align:center; color:#002d5a;'>CETEP</h1>", unsafe_allow_html=True)
    
    st.write("---")
    nav = st.radio("MENÚ PRINCIPAL", ["Inicio", "Oferta Académica", "Matrícula en Línea", "Campus Virtual"])

# 4. PÁGINAS
if nav == "Inicio":
    st.markdown("""
        <div class="hero-full">
            <h1 class="hero-title">TU FUTURO PROFESIONAL<br>COMIENZA HOY</h1>
            <p style="font-size: 22px; opacity: 0.95;">Capacitación técnica de alto impacto para la industria actual.</p>
            <a href="#" class="btn-action">EXPLORAR CARRERAS</a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align:center; margin: 40px 0;'>Educación Accesible y de Calidad</h2>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.success("💰 **Mensualidad Única:** ₡5,000 semanales en todos nuestros técnicos.")
    with c2:
        st.info("🕒 **Horarios Flexibles:** Mañana, Tarde (2-4 pm) y Noche.")
    with c3:
        st.warning("🚀 **Matrícula:** Solo ₡10,000 para iniciar tu carrera.")

elif nav == "Oferta Académica":
    st.header("Programas Académicos 2026")
    sel = st.selectbox("Seleccione un programa para ver el temario:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[sel]
    
    st.markdown(f"### ⏱️ Duración: {info['D']}")
    st.write(f"💵 **Inversión:** {info['Inversion']}")
    
    st.write("---")
    st.write("### Estructura Curricular Detallada:")
    for bloque, temas in info['Malla'].items():
        st.markdown(f"<div class='bloque-header'>{bloque}</div>", unsafe_allow_html=True)
        st.markdown("<div class='temario-box'>", unsafe_allow_html=True)
        for t in temas:
            st.markdown(f"<div class='tema-line'>✅ {t}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif nav == "Matrícula en Línea":
    st.header("Formulario de Admisión")
    with st.form("registro"):
        col1, col2 = st.columns(2)
        n = col1.text_input("Nombre Completo")
        c = col2.text_input("Cédula")
        prog = st.selectbox("Programa de Interés", list(OFFER_ACADEMICA.keys()))
        hor = st.selectbox("Horario de Preferencia", ["Mañana (9-11 am)", "Tarde (2-4 pm)", "Noche (6-8 pm)"])
        if st.form_submit_button("SOLICITAR INGRESO"):
            st.balloons()
            st.success(f"¡Excelente {n}! Hemos recibido tu solicitud para {prog}. Te contactaremos pronto.")

elif nav == "Campus Virtual":
    st.header("Acceso Estudiantes")
    st.text_input("Usuario (Cédula)")
    st.text_input("Contraseña", type="password")
    st.button("Entrar")

st.markdown("<div class='footer'>© 2026 CETEP | Centro de Estudios Técnicos Profesionales | Sede San José - Heredia</div>", unsafe_allow_html=True)
