import streamlit as st
import pandas as pd
import os

# 1. CONFIGURACIÓN DE PÁGINA
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

# 2. DATA ACADÉMICA CON TEMARIOS EXTENDIDOS (LA CARNITA)
OFFER_ACADEMICA = {
    "Global Learning: English Mastery (24 Meses)": {
        "D": "24 Meses (100% Autodirigido)", 
        "Inv": "Matrícula ₡5,000 / Mensualidad ₡15,000",
        "Malla": {
            "AÑO 1: Nivel I - Cimentación y Fluidez Inicial": [
                "Fonética Aplicada: Los 44 sonidos del inglés",
                "Gramática en Uso: Presente, Pasado y Futuros Dinámicos",
                "Listening: Comprensión de Contextos Diarios",
                "Reading: Interpretación de Artículos y Noticias",
                "Speaking: Conversación Situacional y Supervivencia"
            ],
            "AÑO 2: Nivel II - Dominio y Bilingüismo Profesional": [
                "Business English: Correos, Reportes y Memorándums",
                "Negociación y Debate: Argumentación de Alto Nivel",
                "Inglés Técnico Sectorial (Legal, Médico, Financiero)",
                "Preparación para Entrevistas en Transnacionales",
                "Mastery Final: Comunicación con Nivel de Nativo (C1)"
            ]
        }
    },
    "Técnico en Operaciones Bancarias y Gestión de Efectivo": {
        "D": "6 Meses (Autodirigido)", 
        "Inv": "Matrícula ₡5,000 / Mensualidad ₡15,000",
        "Malla": {
            "MÓDULO I: Marco Legal y Normativo": [
                "Sistemas Bancarios de Costa Rica y Entidades Reguladoras",
                "Ley 8204: Prevención de Lavado de Dinero y Legitimación de Capitales",
                "Ética Profesional y Deontología Bancaria",
                "Secreto Bancario y Protección de Datos"
            ],
            "MÓDULO II: Operativa y Caja": [
                "Manejo Físico de Efectivo y Títulos Valores",
                "Detección de Billetaje Falso (Dólares, Euros y Colones)",
                "Arqueos, Cuadres de Caja y Gestión de Bóveda",
                "Seguridad Bancaria y Prevención de Asaltos"
            ],
            "MÓDULO III: Servicio e Inglés Técnico": [
                "Técnicas de Venta Cruzada de Productos Financieros",
                "Manejo de Objeciones y Servicio al Cliente de Excelencia",
                "Global Learning: Inglés Técnico Bancario y Financiero"
            ]
        }
    },
    "Técnico en Gestión de Operaciones e Industria Médica": {
        "D": "9 Meses (Autodirigido)", 
        "Inv": "Matrícula ₡5,000 / Mensualidad ₡15,000",
        "Malla": {
            "MÓDULO I: Calidad y Normativa": [
                "Normativa Internacional ISO 13485:2016",
                "GDP: Buenas Prácticas de Documentación",
                "FDA y Regulaciones Globales para Dispositivos Médicos",
                "Sistemas de Gestión de Calidad (QMS)"
            ],
            "MÓDULO II: Operaciones y Control": [
                "Protocolos de Cuarto Limpio (Gowning y Control de Partículas)",
                "Metrología Avanzada (Uso de Vernier, Micrómetro y CMM)",
                "Lectura e Interpretación de Planos Técnicos",
                "Validación de Procesos (IQ/OQ/PQ)"
            ],
            "MÓDULO III: Inglés Industrial": [
                "Lectura de SOPs (Procedimientos Estándar) en Inglés",
                "Vocabulario Técnico de Manufactura y Dispositivos Médicos",
                "Global Learning: Inglés Industrial Especializado"
            ]
        }
    },
    "Asistente Contable y Gestión Administrativa": {
        "D": "9 Meses (Autodirigido)", 
        "Inv": "Matrícula ₡5,000 / Mensualidad ₡15,000",
        "Malla": {
            "MÓDULO I: El Ciclo Contable": [
                "Contabilidad General: Activos, Pasivos y Capital",
                "Asientos de Diario, Libro Mayor y Balance de Comprobación",
                "Conciliaciones Bancarias y Control de Caja Chica",
                "Cuentas por Cobrar y Gestión de Cartera"
            ],
            "MÓDULO II: Tributación y Planillas": [
                "Ley del IVA y Ley de Impuesto sobre la Renta en CR",
                "Declaraciones en plataformas ATV (Hacienda) y TICA",
                "Cálculo de Planillas: CCSS, INS, Aguinaldos y Liquidaciones",
                "Facturación Electrónica y Normativa Tributaria Vigente"
            ],
            "MÓDULO III: Herramientas y Comunicación": [
                "Excel Financiero Avanzado para Contadores",
                "Global Learning: Inglés para Negocios y Administración",
                "Redacción de Informes Gerenciales"
            ]
        }
    },
    "Preparación Examen Excelencia Académica (Abogados)": {
        "D": "Curso Intensivo Virtual", 
        "Inv": "Matrícula ₡5,000 / Mensualidad ₡15,000",
        "Malla": {
            "BLOQUE A: Derecho Privado": [
                "Derecho Civil: Obligaciones, Contratos y Sucesiones",
                "Derecho Mercantil y Derecho Notarial",
                "Derecho de Familia y Procedimientos Especiales"
            ],
            "BLOQUE B: Derecho Público y Social": [
                "Derecho Constitucional y Administrativo",
                "Derecho Penal y Procesal Penal",
                "Derecho Laboral y Seguridad Social"
            ],
            "BLOQUE C: Estrategia de Examen": [
                "Análisis de Votos Clave de la Sala Cuarta y Casación",
                "Ética y Deontología Jurídica (Ley Orgánica del Poder Judicial)",
                "Simulacros Reales del Examen de Excelencia Académica"
            ]
        }
    }
}

# 3. SIDEBAR Y NAVEGACIÓN
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>CETEP</h2>", unsafe_allow_html=True)
    st.write("---")
    nav = st.radio("MENÚ", ["🏠 Inicio", "📚 Oferta Académica", "📝 Matrícula", "🔐 Campus Virtual"])

# 4. PÁGINAS
if nav == "🏠 Inicio":
    st.markdown("""
        <div class="hero-masivo">
            <h1>LA MEJOR FORMACIÓN TÉCNICA</h1>
            <div class="promo-box">₡15,000 AL MES</div>
            <p>Matrícula ₡5,000 (Única vez) | Estudiá a tu propio ritmo 24/7</p>
        </div>
        """, unsafe_allow_html=True)
    st.info("🎯 **Objetivo 2026:** 500 Estudiantes | **Progreso:** 40 Cupos Confirmados")

elif nav == "📚 Oferta Académica":
    sel = st.selectbox("Seleccione un programa para ver el temario completo:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[sel]
    st.subheader(f"⏱️ Duración: {info['D']} | 💰 Inversión: {info['Inv']}")
    for bloque, temas in info['Malla'].items():
        st.markdown(f"<div class='bloque-header'>{bloque}</div>", unsafe_allow_html=True)
        st.markdown("<div class='temario-box'>", unsafe_allow_html=True)
        for t in temas: st.markdown(f"<div class='tema-line'>✅ {t}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif nav == "📝 Matrícula":
    st.header("Formulario de Admisión")
    with st.form("reg"):
        st.text_input("Nombre Completo"), st.text_input("Cédula"), st.text_input("WhatsApp")
        st.selectbox("Carrera de Interés", list(OFFER_ACADEMICA.keys()))
        if st.form_submit_button("RESERVAR MI LUGAR"):
            st.success("¡Información enviada! Pronto te contactaremos para el pago de matrícula.")

elif nav == "🔐 Campus Virtual":
    if 'user_type' not in st.session_state: st.session_state.user_type = None

    if st.session_state.user_type is None:
        st.subheader("Ingreso Seguro")
        u = st.text_input("Usuario")
        p = st.text_input("Contraseña", type="password")
        if st.button("INGRESAR"):
            if u == "admin_cetep" and p == "Luis2026":
                st.session_state.user_type = "admin"
                st.rerun()
            else: st.error("Acceso denegado")
    
    elif st.session_state.user_type == "admin":
        st.subheader("👨‍💼 PANEL DE CONTROL LUIS (admin_cetep)")
        if st.button("Cerrar Sesión"):
            st.session_state.user_type = None
            st.rerun()
            
        t1, t2, t3, t4 = st.tabs(["💰 Financiero", "📋 Matrícula Reciente", "📈 Notas y Rendimiento", "🎥 Analítica de Videos"])
        
        with t1:
            st.metric("Recaudación Mensual (Meta 500 alumnos)", "₡7,500,000")
            st.write("### Control de Mensualidades ₡15,000")
            st.table(pd.DataFrame({"Mes": ["Abril", "Mayo"], "Estado": ["40 pagos recibidos", "Proyectando 100+"]}))

        with t2:
            st.write("### Lista de Nuevos Ingresos")
            df_mat = pd.DataFrame({"Nombre": ["Juan Pérez", "Ana Rojas"], "Técnico": ["Banca", "Contabilidad"], "Pagó Matrícula": ["Sí", "Sí"]})
            st.dataframe(df_mat, use_container_width=True)

        with t3:
            st.write("### Promedio de Notas por Curso")
            df_notas = pd.DataFrame({"Curso": ["Inglés", "Banca", "Médica", "Contabilidad"], "Nota": [85, 90, 88, 92]})
            st.bar_chart(df_notas.set_index("Curso"))

        with t4:
            st.info("Seguimiento de consumo de video-lecciones por los estudiantes.")
            st.write("📊 Video más visto: 'Detección de Billetaje Falso' (150 reproducciones)")

st.markdown("<div class='footer'>© 2026 CETEP | Costa Rica</div>", unsafe_allow_html=True)
