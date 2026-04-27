import streamlit as st
import pandas as pd
import os

# 1. CONFIGURACIÓN TÉCNICA (Invisible para el usuario)
st.set_page_config(page_title="CETEP | Campus Virtual", layout="wide", page_icon="🎓")

# Estilos CSS Limpios
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    * { font-family: 'Poppins', sans-serif; }
    
    .main-title { color: #002d5a; font-weight: 800; font-size: 40px; margin-bottom: 20px; }
    
    .cuatri-header {
        background: #002d5a; color: #ffcc00; padding: 10px 15px;
        border-radius: 8px; font-weight: 700; margin-top: 15px;
    }
    
    .tema-item { padding: 5px 0 5px 20px; border-bottom: 1px solid #f0f0f0; color: #333; }
    
    .footer { text-align: center; padding: 30px; color: #999; font-size: 12px; border-top: 1px solid #eee; margin-top: 40px; }
    </style>
    """, unsafe_allow_html=True)

# 2. ESTRUCTURA ACADÉMICA (La Carnita)
OFFER_ACADEMICA = {
    "Técnico en Operaciones Bancarias y Gestión de Efectivo": {
        "D": "6 Meses", "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "Mes 1-2: Fundamentación": ["Sistemas Financieros CR", "Legislación Bancaria", "Servicio al Cliente"],
            "Mes 3-4: Operativa": ["Manejo de Efectivo", "Detección de Falsos", "Prevención de Lavado"],
            "Mes 5-6: Especialización": ["Normativa SUGEF", "Arqueos de Caja", "Técnicas de Empleabilidad"]
        }
    },
    "Gestión de Operaciones e Industria Médica": {
        "D": "9 Meses", "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "Bloque I": ["Intro Industria Médica", "GDP Documentación", "Metrología"],
            "Bloque II": ["ISO 13485", "Cuarto Limpio", "Lean Manufacturing"],
            "Bloque III": ["Pruebas Métricas", "Lectura de Planos", "Entrevista STAR"]
        }
    },
    "Asistente Contable y Gestión Administrativa": {
        "D": "9 Meses", "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "Bloque I": ["Contabilidad General", "Legislación Mercantil"],
            "Bloque II": ["Excel Financiero", "IVA y Renta"],
            "Bloque III": ["Planillas CCSS/INS", "Software Contable"]
        }
    },
    "Preparación Examen Excelencia Académica (Abogados)": {
        "D": "Intensivo", "Inv": "Inversión Cerrada",
        "Malla": {"Módulos": ["Derecho Civil", "Derecho Público", "Ética Profesional"]}
    }
}

# 3. SIDEBAR (Solo lo necesario)
with st.sidebar:
    if os.path.exists("LOGO CETEP.jpg"):
        st.image("LOGO CETEP.jpg", use_container_width=True)
    else:
        st.markdown("<h2 style='text-align:center;'>CETEP</h2>", unsafe_allow_html=True)
    
    st.write("---")
    nav = st.radio("MENÚ", ["Inicio", "Carreras Técnicas", "Matrícula en Línea", "Campus Virtual"])

# 4. PÁGINAS PRINCIPALES
if nav == "Inicio":
    st.markdown("<h1 class='main-title'>CONECTANDO TU TALENTO CON LA INDUSTRIA</h1>", unsafe_allow_html=True)
    st.write("Especialización técnica diseñada para la empleabilidad inmediata en el sector bancario, industrial y legal.")
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Mensualidad", "₡20,000", "5,000/sem")
    col2.metric("Matrícula", "₡10,000")
    col3.metric("Meta Apertura", "60 Cupos")

elif nav == "Carreras Técnicas":
    st.header("Programas Académicos")
    sel = st.selectbox("Seleccione una carrera:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[sel]
    
    st.info(f"**Duración:** {info['D']}  |  **Inversión:** {info['Inv']}")
    
    for bloque, temas in info['Malla'].items():
        st.markdown(f"<div class='cuatri-header'>{bloque}</div>", unsafe_allow_html=True)
        for t in temas:
            st.markdown(f"<div class='tema-item'>• {t}</div>", unsafe_allow_html=True)

elif nav == "Matrícula en Línea":
    st.header("Formulario de Inscripción")
    with st.form("registro"):
        st.text_input("Nombre Completo")
        st.text_input("Número de WhatsApp")
        st.selectbox("Carrera de Interés", list(OFFER_ACADEMICA.keys()))
        st.selectbox("Horario Preferencial", ["Mañana", "Tarde (2-4 pm)", "Noche"])
        if st.form_submit_button("REGISTRAR MI ESPACIO"):
            st.success("Información enviada. Nos comunicaremos con usted a la brevedad.")

elif nav == "Campus Virtual":
    st.header("Aula Virtual")
    st.text_input("Usuario")
    st.text_input("Contraseña", type="password")
    st.button("Ingresar")

st.markdown("<div class='footer'>© 2026 CETEP | Centro de Estudios Técnicos Profesionales | Costa Rica</div>", unsafe_allow_html=True)
