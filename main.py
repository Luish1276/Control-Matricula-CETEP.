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
    
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #f0f0f0; }
    
    .sidebar-brand-text {
        font-size: 30px; font-weight: 800; color: #002d5a; text-align: center; padding: 20px 0;
    }

    .cuatri-header {
        background-color: #002d5a; color: white; padding: 8px 15px;
        border-radius: 8px; margin-top: 15px; font-weight: 600;
    }

    .temario-item {
        padding: 5px 0 5px 25px; border-bottom: 1px solid #eee; color: #444; font-size: 14px;
    }

    .btn-action {
        background: #ffcc00; color: #002d5a; padding: 16px 40px;
        border-radius: 50px; text-decoration: none; font-weight: 700;
        display: inline-block; box-shadow: 0 8px 20px rgba(255,204,0,0.3);
    }
    
    .footer { text-align: center; padding: 40px; color: #888; font-size: 14px; border-top: 1px solid #eee; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS ACADÉMICA CON "CARNITA" (Temarios Completos)
OFFER_ACADEMICA = {
    "Técnico en Operaciones Bancarias y Gestión de Efectivo": {
        "D": "6 Meses",
        "Inversion": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Plan": {
            "Mes 1-2: Fundamentos": ["Sistemas Financieros Nacionales", "Ética y Servicio al Cliente", "Matemática Financiera Básica"],
            "Mes 3-4: Operativa": ["Manejo y Reconocimiento de Efectivo", "Prevención de Fraude y Lavado", "Billetaje y Falsificación"],
            "Mes 5-6: Especialización": ["Normativa SUGEF", "Simulación de Arqueos de Caja", "Técnicas de Empleabilidad Bancaria"]
        }
    },
    "Técnico Asistente Legal": {
        "D": "9 Meses",
        "Inversion": "Consultar Plan",
        "Plan": {
            "Trimestre I": ["Investigación Jurídica Digital", "Informática Legal y Redacción", "IA Aplicada al Derecho"],
            "Trimestre II": ["Derecho Civil y Mercantil", "Legislación Migratoria", "Ética y Deontología Jurídica"],
            "Trimestre III": ["Derecho Laboral Aplicado", "Derecho Inmobiliario y Familia", "Procedimientos Penales"]
        }
    },
    "Asistente Contable y Gestión Administrativa": {
        "D": "9 Meses",
        "Inversion": "Consultar Plan",
        "Plan": {
            "Trimestre I": ["Principios de Contabilidad", "Legislación Comercial", "Gestión Documental"],
            "Trimestre II": ["Contabilidad de Costos", "Excel Avanzado para Finanzas", "Legislación Tributaria (IVA/Renta)"],
            "Trimestre III": ["Planillas y Cargas Sociales (CCSS)", "Análisis de Estados Financieros", "Auditoría Básica"]
        }
    },
    "Gestión de Operaciones e Industria Médica": {
        "D": "9 Meses",
        "Inversion": "Consultar Plan",
        "Plan": {
            "Trimestre I": ["Introducción a Dispositivos Médicos", "GDP: Buenas Prácticas de Documentación", "Metrología e Instrumentación (Vernier)"],
            "Trimestre II": ["Protocolos de Cuarto Limpio", "Lean Manufacturing (5S/Kaizen)", "ISO 13485: Calidad Médica"],
            "Trimestre III": ["Entrenamiento en Pruebas Métricas", "Lectura de Planos e Instrucciones", "Simulacro de Entrevista STAR"]
        }
    },
    "Inglés Global Conversacional": {
        "D": "12 Meses",
        "Plan": {
            "Básico": ["Fonética y Estructura", "Vocabulario Cotidiano", "Comprensión Auditiva"],
            "Intermedio": ["Business English", "Redacción de Correos", "Fluidez en Conversación"],
            "Avanzado": ["Presentaciones Ejecutivas", "Inglés Técnico por Área", "Preparación para Certificación"]
        }
    },
    "Preparación Examen Excelencia Académica (Abogados)": {
        "D": "Curso Intensivo",
        "Inversion": "Consultar Fechas",
        "Plan": {
            "Módulo Civil": ["Contratos", "Derechos Reales", "Sucesiones", "Responsabilidad Civil"],
            "Módulo Laboral/Familia": ["Derecho del Trabajo", "Procesos de Familia", "Código de Niñez"],
            "Módulo Penal/Constitucional": ["Teoría del Delito", "Recursos de Amparo", "Garantías Individuales"],
            "Módulo Deontología": ["Estatutos del Colegio", "Ética Profesional", "Jurisprudencia Reciente"]
        }
    }
}

# 3. SIDEBAR
with st.sidebar:
    logo_file = "LOGO CETEP.jpg"
    if os.path.exists(logo_file):
        st.image(logo_file, use_container_width=True)
    else:
        st.markdown('<div class="sidebar-brand-text">CETEP</div>', unsafe_allow_html=True)
    
    st.write("---")
    nav = st.radio("MENÚ PRINCIPAL", ["Inicio", "Oferta Académica", "Matrícula", "Campus Virtual"])

# 4. PÁGINAS
if nav == "Inicio":
    st.markdown("""
        <div class="hero-full">
            <h1 class="hero-title">TU FUTURO PROFESIONAL<br>COMIENZA HOY</h1>
            <p style="font-size: 20px; opacity: 0.9;">Formación técnica especializada con alta demanda laboral.</p>
            <a href="#" class="btn-action">DESCUBRIR PROGRAMAS</a>
        </div>
        """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1: st.info("🏦 **Banca:** 6 Meses / ₡5,000 semanales")
    with c2: st.info("🏭 **Industria:** Especialización Médica")
    with c3: st.info("⚖️ **Legal:** Asistencia y Excelencia")

elif nav == "Oferta Académica":
    st.header("Detalle de Programas")
    sel = st.selectbox("Seleccione el técnico o curso:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[sel]
    
    st.subheader(f"⏱️ Duración: {info['D']}")
    if 'Inversion' in info: st.write(f"💰 **Inversión:** {info['Inversion']}")
    
    st.write("### Malla Curricular Detallada:")
    for bloque, temas in info['Plan'].items():
        st.markdown(f"<div class='cuatri-header'>{bloque}</div>", unsafe_allow_html=True)
        for t in temas:
            st.markdown(f"<div class='temario-item'>• {t}</div>", unsafe_allow_html=True)

elif nav == "Matrícula":
    st.header("Registro de Admisión")
    with st.form("mat"):
        st.text_input("Nombre Completo"), st.text_input("Cédula")
        st.selectbox("Programa", list(OFFER_ACADEMICA.keys()))
        st.selectbox("Horario", ["Mañana (9-11 am)", "Tarde (2-4 pm)", "Noche (6-8 pm)"])
        st.form_submit_button("REGISTRAR")

elif nav == "Campus Virtual":
    st.header("Aula Virtual")
    st.text_input("Usuario"), st.text_input("Contraseña", type="password")
    st.button("Ingresar")

st.markdown("<div class='footer'>© 2026 CETEP | Centro de Estudios Técnicos Profesionales | Costa Rica</div>", unsafe_allow_html=True)
