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

# 2. DATA ACADÉMICA EXTENDIDA (LA CARNITA)
OFFER_ACADEMICA = {
    "Global Learning: English Mastery - Nivel I (12 Meses)": {
        "D": "12 Meses (A1-B1)", "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "TRIMESTRE 1: Cimentación": ["Fonética y Sonidos del Inglés", "Estructuras Gramaticales Básicas", "Listening: Comprensión de Contexto"],
            "TRIMESTRE 2: Comunicación Activa": ["Vocabulario de Vida Cotidiana", "Técnicas de Conversación Inicial", "Lectura de Textos Simples"],
            "TRIMESTRE 3: Fluidez Intermedia": ["Pretéritos y Futuros Complejos", "Debates de Temas Generales", "Listening Avanzado"],
            "TRIMESTRE 4: Consolidación": ["Redacción de Ensayos Cortos", "Inglés para Viajes y Socialización", "Examen de Progreso B1"]
        }
    },
    "Global Learning: English Mastery - Nivel II (12 Meses)": {
        "D": "12 Meses (B2-C1)", "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "TRIMESTRE 5: Inglés Corporativo": ["Business English: Correos y Reportes", "Liderazgo en Inglés", "Presentaciones Ejecutivas"],
            "TRIMESTRE 6: Dominio Técnico": ["Terminología Industrial y Legal", "Interpretación de Documentos Complejos", "Listening con Acentos Globales"],
            "TRIMESTRE 7: Alta Fluidez": ["Argumentación y Negociación", "Pensamiento Crítico en Inglés", "Inglés Académico"],
            "TRIMESTRE 8: Mastery Final": ["Simulación de Entrevistas de Alto Perfil", "Dominio de Idioms y Phrasal Verbs", "Proyecto Final: Bilingüismo Total"]
        }
    },
    "Técnico en Operaciones Bancarias y Gestión de Efectivo": {
        "D": "6 Meses", "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "MÓDULO I: El Sistema Financiero": ["Legislación Bancaria CR", "Ley 8204: Prevención de Lavado", "Ética y Deontología Bancaria"],
            "MÓDULO II: Operativa de Caja": ["Manejo de Efectivo y Títulos Valores", "Detección de Billetaje Falso (Dólar, Euro, Colones)", "Arqueos y Cuadres de Caja"],
            "MÓDULO III: Servicio al Cliente": ["Técnicas de Venta Cruzada", "Manejo de Objeciones", "Seguridad Bancaria y Protocolos"],
            "GLOBAL LEARNING": ["Inglés Técnico Bancario", "Vocabulario Financiero Bilingüe"]
        }
    },
    "Gestión de Operaciones e Industria Médica": {
        "D": "9 Meses", "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "BLOQUE I: Normativa": ["ISO 13485:2016 Deep Dive", "GDP: Buenas Prácticas de Documentación", "Validación de Procesos"],
            "BLOQUE II: Control de Calidad": ["Metrología Avanzada (Uso de Vernier y Micrómetro)", "Lectura de Planos Técnicos", "Pruebas de Esfuerzo y Tensión"],
            "BLOQUE III: Ambiente Controlado": ["Protocolos de Cuarto Limpio (Gowning)", "Control de Contaminación", "Seguridad Industrial (OSHA)"],
            "GLOBAL LEARNING": ["Inglés para Manufactura Médica", "Lectura de Procedimientos (SOPs) en Inglés"]
        }
    },
    "Asistente Contable y Gestión Administrativa": {
        "D": "9 Meses", "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "BLOQUE I: Ciclo Contable": ["Contabilidad General", "Cuentas por Cobrar y Pagar", "Conciliaciones Bancarias"],
            "BLOQUE II: Tributación": ["IVA y Renta en Costa Rica", "Manejo de TICA y ATV", "Facturación Electrónica"],
            "BLOQUE III: Gestión Laboral": ["Planillas CCSS e INS", "Cálculo de Prestaciones y Aguinaldos", "Excel Financiero Avanzado"],
            "GLOBAL LEARNING": ["Inglés para Negocios", "Comunicación Administrativa Bilingüe"]
        }
    },
    "Preparación Examen Excelencia Académica (Abogados)": {
        "D": "Curso Intensivo", "Inv": "Inversión Especial",
        "Malla": {
            "ÁREA PRIVADA": ["Derecho Civil y Mercantil", "Derecho Notarial", "Derecho de Familia"],
            "ÁREA PÚBLICA": ["Constitucional y Administrativo", "Derecho Laboral", "Derecho Penal"],
            "REFORZAMIENTO": ["Análisis de Votos de la Sala IV", "Simulacros de Examen de Excelencia", "Deontología Jurídica"]
        }
    }
}

# 3. SIDEBAR Y NAVEGACIÓN
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#002d5a;'>CETEP</h2>", unsafe_allow_html=True)
    st.write("---")
    nav = st.radio("MENÚ PRINCIPAL", ["🏠 Inicio", "📚 Oferta Académica", "📝 Matrícula", "🔐 Campus Virtual"])

# 4. PÁGINAS
if nav == "🏠 Inicio":
    st.markdown("""
        <div class="hero-full">
            <h1 class="hero-title">FORMACIÓN TÉCNICA<br>DE ALTO NIVEL</h1>
            <p style="font-size: 20px; opacity: 0.9;">Global Learning: 24 meses para el dominio total del inglés.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("### Capacidad de Apertura 2026")
    col1, col2 = st.columns([3, 1])
    col1.progress(65)
    col2.write("40/60 Estudiantes")
    
    st.write("---")
    c1, c2, c3 = st.columns(3)
    c1.info("🏦 **Banca:** ₡5,000 semanales")
    c2.info("🌍 **Inglés:** English Mastery (24m)")
    c3.info("⚖️ **Legal:** Preparación Excelencia")

elif nav == "📚 Oferta Académica":
    st.header("Detalle de Programas Académicos")
    sel = st.selectbox("Seleccione el programa para ver el temario extendido:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[sel]
    st.subheader(f"⏱️ Duración: {info['D']} | 💰 Inversión: {info['Inv']}")
    
    for bloque, temas in info['Malla'].items():
        st.markdown(f"<div class='bloque-header'>{bloque}</div>", unsafe_allow_html=True)
        st.markdown("<div class='temario-box'>", unsafe_allow_html=True)
        for t in temas:
            st.markdown(f"<div class='tema-line'>🔹 {t}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif nav == "🔐 Campus Virtual":
    if 'user_type' not in st.session_state: st.session_state.user_type = None

    if st.session_state.user_type is None:
        st.header("Ingreso al Sistema")
        u = st.text_input("Usuario")
        p = st.text_input("Contraseña", type="password")
        if st.button("ACCEDER"):
            if u == "admin_cetep" and p == "Luis2026":
                st.session_state.user_type = "admin"
                st.rerun()
            else: st.error("Acceso denegado")
    
    elif st.session_state.user_type == "admin":
        st.subheader("👨‍💼 Panel de Control (admin_cetep)")
        t1, t2 = st.tabs(["💰 Financiero", "📋 Estudiantes"])
        with t1:
            st.metric("Recaudación Semanal Proyectada", "₡300,000")
            st.info("Ingresos netos por cuotas semanales de ₡5,000.")
        if st.button("Cerrar Sesión"):
            st.session_state.user_type = None
            st.rerun()

st.markdown("<div class='footer'>© 2026 CETEP | Costa Rica</div>", unsafe_allow_html=True)
